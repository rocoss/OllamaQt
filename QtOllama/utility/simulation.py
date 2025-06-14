# simulation.py
import logging
import time
import traceback
import json

import ollama
from PyQt6.QtCore import QThread, pyqtSignal, pyqtSlot
from PyQt6.QtGui import QTextCursor
from PyQt6.QtWidgets import (
    QDialog,
    QTextEdit,
    QLineEdit,
    QPushButton,
    QHBoxLayout,
    QStatusBar,
    QProgressBar,
    QLabel,
    QVBoxLayout,
    QCheckBox,
    QGroupBox,
    QGridLayout,
    QMessageBox,
)
from QtOllama.utility.settings import load_settings
from QtOllama.utility.logger_setup import create_logger
logger = create_logger(__name__)


def messages_to_prompt(messages):
    """
    Converts a list of message dictionaries into a formatted prompt string.

    Each message dictionary should contain the keys "role" and "content".
    The "role" key should have a value of either "system", "user", or "assistant".
    The "content" key should contain the message text.

    The function concatenates the content of each message into a single string,
    with specific formatting based on the role:
    - "system" messages are added as-is with double newlines.
    - "user" messages are prefixed with "User: " and followed by a newline.
    - "assistant" messages are prefixed with "Assistant: " and followed by a newline.

    The final prompt string ends with "Assistant: ".

    Args:
        messages (list): A list of dictionaries, each containing "role" and "content" keys.

    Returns:
        str: A formatted prompt string.

    Raises:
        Exception: If an error occurs during the processing of messages.
    """

    try:
        prompt = ""
        for message in messages:
            role = message["role"]
            content = message["content"]
            if role == "system":
                prompt += content.strip() + "\n\n"
            elif role == "user":
                prompt += "User: " + content.strip() + "\n"
            elif role == "assistant":
                prompt += "Assistant: " + content.strip() + "\n"
        prompt += "Assistant: "
        return prompt
    except Exception as e:
        logger.error(f"{e}")


class SimWorker(QThread):
    """
    SimWorker is a QThread subclass responsible for handling the simulation of message processing
    using a specified model. It emits signals for new messages, completion, and errors.
    Attributes:
        new_message (pyqtSignal): Signal emitted when a new message chunk is received.
                                  Parameters are the message content (str), a boolean indicating
                                  if it's the first chunk (bool), and the start time (float).
        complete_message (pyqtSignal): Signal emitted when the message processing is complete.
                                       Parameters are the complete message (str) and the start time (float).
        error (pyqtSignal): Signal emitted when an error occurs. Parameter is the error message (str).
    Args:
        messages (list): List of messages to be processed.
        model_name (str): Name of the model to be used for processing messages.
    Methods:
        run(): Executes the message processing simulation, emitting signals for new message chunks,
               completion, and errors.
    """
    new_message = pyqtSignal(str, bool, float)
    complete_message = pyqtSignal(str, float)
    error = pyqtSignal(str)
    
    def __init__(self,
                 messages: list,
                 model_name: str):
        super().__init__()
        self.messages = messages
        self.model_name = model_name  # Store the model name
    
    def run(self):
        """
        Executes the simulation by generating responses based on the provided messages.
        This method performs the following steps:
        1. Converts the messages to a prompt.
        2. Logs the request details.
        3. Generates responses from the model in a streaming manner.
        4. Processes each chunk of the response:
            - If the chunk is a string, attempts to parse it as JSON to extract the 'response' field.
            - If the chunk is a dictionary, extracts the 'response' field directly.
            - Logs and handles unexpected chunk types.
        5. Emits new messages as they are received.
        6. Emits a complete message once all chunks are processed.
        Emits:
            new_message (str, bool, float): Emitted for each chunk of the response.
            complete_message (str, float): Emitted after all chunks are processed.
            error (str): Emitted if an exception occurs during execution.
        Logs:
            Various debug and error messages related to the request and response processing.
        Raises:
            Exception: If any error occurs during the execution of the simulation.
        """
        start_time = time.time()
        try:
            prompt = messages_to_prompt(self.messages)
            logging.debug(f"Ollama Request: model={self.model_name}, prompt={prompt}")
            
            responses = ollama.generate(model=self.model_name, prompt=prompt, stream=True)
            
            first_chunk = True
            result = ""
            
            for chunk in responses:
                logger.debug(f"Type of chunk: {type(chunk)}")
                logger.debug(f"Chunk received: {chunk}")
                # Handle chunk
                if isinstance(chunk, str):
                    try:
                        chunk_dict = json.loads(chunk)
                        content = chunk_dict.get('response', '')
                    except json.JSONDecodeError:
                        logging.error(f"Failed to parse chunk as JSON: {chunk}")
                        content = chunk  # Use as is
                elif isinstance(chunk, dict):
                    content = chunk.get('response', '')
                else:
                    logger.error(f"Unexpected chunk type: {type(chunk)}")
                    content = ''
                result += content
                self.new_message.emit(content, first_chunk, start_time)
                first_chunk = False
            
            # After the loop, the generation is complete
            self.complete_message.emit(result, start_time)
        except Exception as e:
            self.error.emit(
                f"Error on sim worker: {e}, Trace: {traceback.format_exc()}"
            )


class SimulationDialog(QDialog):
    """    
    SimulationDialog is a QDialog subclass that facilitates a turn-based, role-playing simulation
    with a language model. It provides a user interface for setting up simulation parameters and 
    interacting with the simulation.
    Attributes:
        sim_worker (SimWorker): The worker responsible for processing simulation interactions.
        character_label (QLabel): Label for the character input field.
        character_edit (QLineEdit): Input field for the character name.
        messages (list): List to store messages exchanged during the simulation.
        ai_response_edit (QTextEdit): Text edit widget to display AI responses.
        user_input_edit (QLineEdit): Input field for user messages.
        send_button (QPushButton): Button to send user input.
        input_layout (QHBoxLayout): Layout for user input field and send button.
        status_bar (QStatusBar): Status bar to display progress and status messages.
        progress_bar (QProgressBar): Progress bar to indicate ongoing processing.
        status_message (QLabel): Label to display status messages.
        layout (QVBoxLayout): Main layout of the dialog.
        conversation_history (list): List to store the conversation history.
        text_editor (QTextEdit): Reference to the text editor containing additional information.
        selected_model (str): The selected language model for the simulation.
    Methods:
        __init__(self, text_editor, parent=None, selected_model=None):
            Initializes the SimulationDialog with the given text editor, parent, and selected model.
        get_editor_contents(self):
        initialize_simulation(self):
        handle_dialog_finished(self, result):
        process_sim_worker(self):
            Processes the simulation worker with the selected model.
        handle_worker_error(self, error_message):
        send_user_input(self, user_text=None):
        update_ai_response(self, ai_response, is_first_chunk, start_time):
        update_conversation_history(self, full_response, start_time):
    """
    def __init__(self, text_editor, parent=None, selected_model=None):
        super().__init__(parent)
        self.sim_worker = None
        self.character_label = None
        self.character_edit = None
        self.messages = []
        self.setWindowTitle("Simulation with LLM")
        
        self.ai_response_edit = QTextEdit(self)
        self.ai_response_edit.setReadOnly(True)
        self.ai_response_edit.setLineWrapMode(QTextEdit.LineWrapMode.WidgetWidth)
        
        self.user_input_edit = QLineEdit(self)

        self.send_button = QPushButton("Send", self)
        self.send_button.clicked.connect(self.send_user_input)
        self.input_layout = QHBoxLayout()
        self.input_layout.addWidget(self.user_input_edit)
        self.input_layout.addWidget(self.send_button)
        
        self.status_bar = QStatusBar(self)
        self.progress_bar = QProgressBar(self)
        self.status_bar.addPermanentWidget(self.progress_bar)
        self.progress_bar.setRange(0, 0)
        self.progress_bar.hide()
        
        self.status_message = QLabel(self)
        self.status_bar.addPermanentWidget(self.status_message)
        self.status_bar.setSizeGripEnabled(False)
        
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.ai_response_edit)
        self.layout.addLayout(self.input_layout)
        self.layout.addWidget(self.status_bar)
        
        self.setLayout(self.layout)
        
        self.resize(600, 400)
        
        self.conversation_history = []
        
        self.text_editor = text_editor
        self.selected_model = selected_model  # Store the selected model
        self.initialize_simulation()

        
    def get_editor_contents(self):
        """
        Retrieves the current contents of the text editor.

        Returns:
            str: The plain text content of the text editor.

        Raises:
            Exception: If an error occurs while retrieving the text editor contents.
        """

        try:
            return self.text_editor.toPlainText()
        except Exception as e:
            logger.error(f"{e}")
            
    def initialize_simulation(self):
        """
        Initializes the simulation dialog where users can input various parameters for the simulation.
        This method creates a dialog window with fields for the user to specify:
        - Character name (required)
        - Location (optional)
        - Year (optional)
        - Activity (optional)
        - Scenario notes (optional)
        - Option to include text editor contents
        The dialog also includes a button to begin the simulation. If the required character name is not provided,
        an error message is shown and the simulation is not started. Upon successful input, the simulation parameters
        are used to set up the simulation environment and conversation history.
        Raises:
            Exception: If any error occurs during the initialization process.
        """
        try:
            dialog = QDialog(self)
            dialog.setWindowTitle("Simulation Parameters")
            
            layout = QVBoxLayout()
            dialog.setLayout(layout)
            
            groupBox = QGroupBox("Simulation Parameters")
            layout.addWidget(groupBox)
            
            grid = QGridLayout()
            groupBox.setLayout(grid)
            
            self.character_label = QLabel("Who do you want to be in the simulation?")
            self.character_edit = QLineEdit()
            self.character_edit.setPlaceholderText("Required")
            grid.addWidget(self.character_label, 0, 0)
            grid.addWidget(self.character_edit, 0, 1)
            
            location_label = QLabel("Where do you want the simulation to take place?")
            location_edit = QLineEdit()
            location_edit.setPlaceholderText("Optional")
            grid.addWidget(location_label, 1, 0)
            grid.addWidget(location_edit, 1, 1)
            
            year_label = QLabel("In what year should the simulation take place?")
            year_edit = QLineEdit()
            year_edit.setPlaceholderText("Optional")
            grid.addWidget(year_label, 2, 0)
            grid.addWidget(year_edit, 2, 1)
            
            doing_label = QLabel("What are you doing?")
            doing_edit = QLineEdit()
            doing_edit.setPlaceholderText("Optional")
            grid.addWidget(doing_label, 3, 0)
            grid.addWidget(doing_edit, 3, 1)
            
            scenario_label = QLabel("Include any scenario notes?")
            scenario_edit = QTextEdit()
            scenario_edit.setPlaceholderText("Optional")
            grid.addWidget(scenario_label, 4, 0)
            grid.addWidget(scenario_edit, 4, 1)
            
            
            include_editor_checkbox = QCheckBox("Include text editor contents")
            include_editor_checkbox.setDisabled(not self.get_editor_contents().strip())
            grid.addWidget(include_editor_checkbox, 5, 0)
            
            button = QPushButton("Begin Simulation")
            layout.addWidget(button)
            button.clicked.connect(dialog.accept)
            
            dialog.finished.connect(self.handle_dialog_finished)
        
            if dialog.exec():
                character = self.character_edit.text()
                if not character.strip():
                    msg = QMessageBox(QMessageBox.Icon.Critical,
                                      "Missing Required Field",
                                      "Please provide a character name.")
                    msg.exec()
                    self.close()
                    return
                
                location = (
                    location_edit.text()
                    if location_edit.text().strip()
                    else "undisclosed location"
                )
                year = (
                    year_edit.text().strip()
                    if year_edit.text().strip()
                    else "unspecified time"
                )
                doing = (
                    doing_edit.text().strip()
                    if doing_edit.text().strip()
                    else "unspecified doing"
                )
                
                scenario_notes = (
                    scenario_edit.toPlainText() if scenario_edit.toPlainText().strip() else None
                )
                
                include_editor_contents = include_editor_checkbox.isChecked()
                
                self.setWindowTitle(f"Simulation: {character}—{location}—{year}")
                
                system_message = """
                Function as a turn-based, role-playing simulation. Remember, this is a game of interaction,
                and after every turn, the simulation will pause allowing the user to interact. The simulation
                will never break out of the scenario."""
                
                if scenario_notes is not None:
                    system_message += (
                        f"\n\nAdditional simulation scenario notes: {scenario_notes}"
                    )
                
                if include_editor_contents:
                    editor_contents = self.get_editor_contents()
                    system_message += f"\n\nAdditional information: {editor_contents}"
                
                initial_user_message = f"""
                \n\nIn this simulation, I am {character.strip()}, currently in {location.strip()},
                and the year is {year}. And I am {doing}. Begin the simulation.
                """
                
                self.conversation_history.extend(
                    [
                        {
                            "role": "system",
                            "content": system_message,
                        },
                        {"role": "user", "content": initial_user_message},
                    ]
                )
                self.process_sim_worker()
            else:
                self.close()
        except Exception as e:
            logger.error(f"{e}")
    
    @pyqtSlot(int)
    def handle_dialog_finished(self, result):
        """
        Handles the event when a dialog is finished.

        This method is triggered when a dialog is closed. It checks the result of the dialog,
        and if the dialog was rejected, it closes the current window.

        Args:
            result (QDialog.DialogCode): The result code of the dialog, indicating whether it was accepted or rejected.
        """

        if result == QDialog.DialogCode.Rejected:
            self.close()
    
    def process_sim_worker(self):
        """
        Processes the simulation worker by initializing and starting a new SimWorker instance.
        This method performs the following steps:
        1. Determines the model to use based on the selected model or defaults to 'llama2'.
        2. Displays the progress bar.
        3. Cleans up any existing SimWorker instance by quitting, waiting for it to finish, 
           and disconnecting its signals.
        4. Creates a new SimWorker instance with the conversation history and the determined model name.
        5. Connects the new SimWorker's signals to the appropriate slots for handling new messages, 
           completed messages, and errors.
        6. Starts the new SimWorker instance.
        """
        # Use the selected model
        if self.selected_model:
            model_name = self.selected_model
        else:
            model_name = 'llama2'  # Default model
        
        self.progress_bar.show()
        
        # Clean up existing worker if it exists
        if self.sim_worker:
            self.sim_worker.quit()
            self.sim_worker.wait()
            self.sim_worker.new_message.disconnect()
            self.sim_worker.error.disconnect()
            self.sim_worker.complete_message.disconnect()
        
        # Create new SimWorker with model_name
        self.sim_worker = SimWorker(self.conversation_history, model_name)
        self.sim_worker.new_message.connect(self.update_ai_response)
        self.sim_worker.complete_message.connect(self.update_conversation_history)
        self.sim_worker.error.connect(self.handle_worker_error)
        self.sim_worker.start()
    
    @pyqtSlot(str)
    def handle_worker_error(self, error_message):
        """
        Handles errors encountered by a worker thread.

        Args:
            error_message (str): The error message to be displayed and logged.

        Side Effects:
            - Prints the error message to the console.
            - Updates the status message to indicate an error has occurred.
            - Hides the progress bar.
        """

        print(error_message)
        self.status_message.setText("An error occurred. Please view logs.")
        self.progress_bar.hide()
    
    def send_user_input(self, user_text=None):
        """
        Handles the user input, appends it to the conversation history, updates the UI, and triggers the simulation process.

        Args:
            user_text (str, optional): The text input from the user. If not provided, it will be fetched from the user input edit field.

        Returns:
            None
        """
        user_text = user_text or self.user_input_edit.text()
        if user_text.strip():
            new_message = {"role": "user", "content": user_text}
            self.conversation_history.append(new_message)
            self.ai_response_edit.append("\n👤 " + user_text)
            self.user_input_edit.clear()
            self.process_sim_worker()
    
    @pyqtSlot(str, bool, float)
    def update_ai_response(self, ai_response, is_first_chunk, start_time):
        """
        Updates the AI response in the text editor.

        Args:
            ai_response (str): The response generated by the AI.
            is_first_chunk (bool): Flag indicating if this is the first chunk of the response.
            start_time (float): The start time of the response generation.

        Returns:
            None
        """

        if ai_response.strip() != "":
            if is_first_chunk:
                ai_response = "\n\n🌐 " + ai_response
            self.ai_response_edit.insertPlainText(ai_response)
            self.ai_response_edit.moveCursor(QTextCursor.MoveOperation.End)
            self.ai_response_edit.ensureCursorVisible()
    
    @pyqtSlot(str, float)
    def update_conversation_history(self,
                                    full_response,
                                    start_time):
        """
        Updates the conversation history with the AI response.

        Args:
            full_response (str): The full response content from the assistant.
            start_time (float): The start time of the response generation.
        """
        new_message = {"role": "assistant", "content": full_response.strip()}
        self.conversation_history.append(new_message)
        self.ai_response_edit.ensureCursorVisible()
        self.progress_bar.hide()
