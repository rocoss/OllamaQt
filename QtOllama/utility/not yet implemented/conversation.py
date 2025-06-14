import logging
import time

import ollama
from PyQt6.QtCore import QThread, pyqtSignal
from PyQt6.QtWidgets import QDialog, QTextEdit, QLineEdit, QPushButton, QHBoxLayout, QStatusBar, \
    QProgressBar, QLabel, \
    QVBoxLayout

from settings import load_settings
new_message = pyqtSignal(str, bool, float)
complete_message = pyqtSignal(str, float)
error = pyqtSignal(str)


class ChatWorker(QThread):
    """
    ChatWorker is a QThread subclass responsible for handling chat interactions with the OpenAI API.

    Attributes:
        new_message (pyqtSignal): A signal emitted when a HammerAI-lama-3_1-storm-latest message is received. It carries three parameters:
            - str: The content of the message.
            - bool: A flag indicating if this is the first chunk of the message.
            - float: The start time of the message processing.

    Args:
        messages (list): A list of messages to be sent to the OpenAI API.

    Methods:
        run(): Executes the thread's activity. It loads settings, sets the OpenAI API key, and sends the messages to the OpenAI API.
               It streams the responses and emits the new_message signal for each chunk of the response.
    """
    def __init__(self,
                 messages: list,
                 model_name: str):
        """
        Initializes the simulation thread with a list of messages and a model name.

        Args:
            messages (list): A list of messages to be processed by the simulation.
            model_name (str): The name of the model to use for generating responses.
        """
        QThread.__init__(self)
        self.messages = messages
        self.model_name = model_name
    
    def run(self):
        """
        Runs the Ollama chat simulation.

        This method initiates a chat with Ollama using the provided messages,
        streams the response, and emits signals for each chunk received.
        """
        start_time = time.time()
        
        try:
            logging.debug("Ollama Request: {}".format(self.messages))
            
            # Stream responses from Ollama using the selected model
            stream = ollama.chat(model=self.model_name, messages=self.messages, stream=True)
            
            first_chunk = True
            result = ""
            
            for response in stream:
                content = response.get("message", {}).get("content")
                
                if content:
                    result += content
                    self.new_message.emit(content, first_chunk, start_time)
                    if first_chunk:
                        first_chunk = False
            
            # Emit the complete message once all chunks are processed
            self.complete_message.emit(result, start_time)
        
        except Exception as e:
            self.error.emit(f"Error on Ollama worker: {e}, Trace: {traceback.format_exc()}")
            
            
class AIDialog(QDialog):
    """
    AIDialog is a custom QDialog class designed for interacting with a language model (LLM) in a conversational manner.

    Attributes:
        messages (list): A list to store the conversation messages.
        ai_response_edit (QTextEdit): A text edit widget to display the AI's responses.
        user_input_edit (QLineEdit): A line edit widget for user input.
        send_button (QPushButton): A button to send the user's input.
        input_layout (QHBoxLayout): A horizontal layout to arrange the user input edit and send button.
        status_bar (QStatusBar): A status bar to display the progress and status messages.
        progress_bar (QProgressBar): A progress bar to show the processing status.
        status_message (QLabel): A label to display status messages.
        layout (QVBoxLayout): A vertical layout to arrange the main components of the dialog.
        conversation_history (list): A list to store the history of the conversation.

    Methods:
        __init__(self, parent=None, initial_text="", analysis_type=""):
            Initializes the AIDialog with optional parent, initial text, and analysis type.

        initialize_discussion(self, initial_text):
            Initializes the discussion with the given initial text.

        process_chat_worker(self):
            Processes the chat by starting a ChatWorker thread to handle the conversation.

        send_user_input(self, user_text=None):
            Sends the user's input to the conversation and processes the response.

        update_ai_response(self, ai_response, first_chunk, start_time):
            Updates the AI's response in the dialog and handles the display of the response and status.
    """
    def __init__(self, parent=None, initial_text="", analysis_type=""):
        """
        Initializes the conversation window.

        Args:
            parent (QWidget, optional): The parent widget. Defaults to None.
            initial_text (str, optional): The initial text to start the conversation. Defaults to "".
            analysis_type (str, optional): The type of analysis to be discussed. Defaults to "".

        Attributes:
            messages (list): A list to store conversation messages.
            ai_response_edit (QTextEdit): A text edit widget to display AI responses.
            user_input_edit (QLineEdit): A line edit widget for user input.
            send_button (QPushButton): A button to send user input.
            input_layout (QHBoxLayout): A horizontal layout for user input and send button.
            status_bar (QStatusBar): A status bar to display status messages and progress.
            progress_bar (QProgressBar): A progress bar to indicate ongoing processes.
            status_message (QLabel): A label to display status messages.
            layout (QVBoxLayout): A vertical layout for the main window.
            conversation_history (list): A list to store the history of the conversation.
        """
        super().__init__(parent)
        self.chat_worker = None
        self.messages = []
        dialog_title = f"Conversation with LLM about {analysis_type}" if analysis_type else "Conversation with LLM"
        self.setWindowTitle(dialog_title)

        self.ai_response_edit = QTextEdit(self)
        self.ai_response_edit.setReadOnly(True)
        self.ai_response_edit.setLineWrapMode(QTextEdit.LineWrapMode.WidgetWidth)
        self.ai_response_edit.setStyleSheet(
            "QTextEdit {background-color: #003366; color: #ffffff;}"
        )

        self.user_input_edit = QLineEdit(self)
        self.user_input_edit.setStyleSheet(
            "QLineEdit {background-color: #003366; color: #ffffff;}"
        )
        self.send_button = QPushButton("Send", self)
        self.send_button.clicked.connect(self.send_user_input)
        self.input_layout = QHBoxLayout()
        self.input_layout.addWidget(self.user_input_edit)
        self.input_layout.addWidget(self.send_button)

        self.status_bar = QStatusBar(self)
        self.progress_bar = QProgressBar(self)
        self.status_bar.addPermanentWidget(self.progress_bar)
        self.progress_bar.setRange(0, 0)

        self.status_message = QLabel(self)
        self.status_bar.addPermanentWidget(self.status_message)
        self.status_bar.setSizeGripEnabled(False)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.ai_response_edit)
        self.layout.addLayout(self.input_layout)
        self.layout.addWidget(self.status_bar)

        self.setLayout(self.layout)

        self.resize(600, 400)

        self.conversation_history = [
            {
                "role": "system",
                "content": "You are a helpful assistant optimized for text analysis.",
            }
        ]

        if initial_text:
            self.initialize_discussion(initial_text)
        else:
            self.initialize_discussion("Let's have a conversation. Tell me something virtually nobody knows.")

    def initialize_discussion(self, initial_text):
        """
        Initializes a discussion with the given initial text.

        This method extends the messages list with a system message indicating the role of the assistant
        and a user message containing the initial text to discuss. It then processes the chat worker.

        Args:
            initial_text (str): The initial text to start the discussion with.
        """
        self.messages.extend(
            [
                {
                    "role": "system",
                    "content": "You are a helpful assistant that analyzes and discusses text.",
                },
                {"role": "user", "content": f"Let's discuss: {initial_text}"},
            ]
        )
        self.process_chat_worker()

    def process_chat_worker(self):
        """
        Processes the chat by initializing and starting a ChatWorker.

        This method performs the following actions:
        1. Displays a progress bar.
        2. Concatenates the conversation history with the current messages.
        3. Initializes a ChatWorker with the combined messages.
        4. Connects the ChatWorker's new_message signal to the update_ai_response method.
        5. Starts the ChatWorker.

        Returns:
            None
        """
        
        self.progress_bar.show()
        self.messages = self.conversation_history + self.messages
        self.chat_worker = ChatWorker(self.messages)
        self.chat_worker.new_message.connect(self.update_ai_response)
        self.chat_worker.start()

    def send_user_input(self, user_text=None):
        """
        Handles the user input, appends it to the conversation history, and processes the chat.

        Args:
            user_text (str, optional): The text input from the user. If not provided, it will be fetched from the user input edit field.

        Actions:
            - If user_text is not provided, fetches the text from the user input edit field.
            - Strips the user_text and checks if it is not empty.
            - Creates a HammerAI-lama-3_1-storm-latest message dictionary with the user's role and content.
            - Appends the HammerAI-lama-3_1-storm-latest message to the messages list.
            - Updates the AI response edit field with the user's input.
            - Clears the user input edit field.
            - Initiates the chat processing worker.
            - Appends the HammerAI-lama-3_1-storm-latest message to the conversation history.
        """
        user_text = user_text or self.user_input_edit.text()
        if user_text.strip():
            new_message = {"role": "user", "content": user_text}
            self.messages.append(new_message)
            self.ai_response_edit.append("\nUser: " + user_text)
            self.user_input_edit.clear()
            self.process_chat_worker()

            self.conversation_history.append(new_message)

    def update_ai_response(self, ai_response, first_chunk, start_time):
        """
        Updates the AI response in the conversation interface.

        Args:
            ai_response (str): The response generated by the AI.
            first_chunk (bool): Indicates if this is the first chunk of the response.
            start_time (float): The start time of the response generation process.

        Updates:
            - Inserts the AI response into the conversation history.
            - Appends the AI response to the conversation history.
            - Ensures the cursor is visible in the response edit area.
            - Hides the progress bar.
            - Updates the status message with the model used and processing time.
        """

        elapsed_time = time.time() - start_time
        model_used = load_settings()["conversation_model"]

        if first_chunk:
            ai_response = "\n\nLLM: " + ai_response

        self.ai_response_edit.insertPlainText(ai_response)

        self.conversation_history.append({"role": "assistant", "content": ai_response})
        self.ai_response_edit.ensureCursorVisible()

        self.progress_bar.hide()
        self.status_message.setText(
            f"LLM: {model_used} | PT: {elapsed_time:.2f}s"
        )
