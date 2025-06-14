# main.py
import sys
from asyncio import subprocess
from datetime import time, datetime
import os
import markdown
import ollama
import json
from PyQt6.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QSpinBox,
    QLineEdit,
    QPushButton,
    QLabel,
    QComboBox,
    QStyleFactory,
    QMainWindow,
    QApplication,
    QTextEdit,
    QStatusBar,
    QMessageBox,
    QDialog,
    QProgressBar,
    QMenu,
    QToolButton,
    QFileDialog,)
from PyQt6.QtCore import QThread, pyqtSignal, QFileInfo, QTimer, Qt, pyqtSlot
from typing import Dict, Generator
from PyQt6.QtPrintSupport import QPrinter
from PyQt6.QtGui import QCloseEvent, QAction, QFont
from textblob import TextBlob
from textstat import textstat
from QtOllama.ui.stats_dialog import HistoricalStatsDialog
from QtOllama.ui.wordcloud_dialog import WordCloudDialog
import QtOllama.utility.capabilities as capabilities
from QtOllama.ui.frameless_window import FramelessWindow
from QtOllama.utility.logger_setup import create_logger
from QtOllama.utility.constants import CONTEXT_LENGTH_DEFAULT
from QtOllama.utility.utils import handle_exception
from QtOllama.ui.ui_components import UIComponents
from QtOllama.ui.signal_connector import SignalConnector
from QtOllama.ui.menu_creator import MenuCreator
from QtOllama.ui.chat_tables import SavedChatsDialog
from QtOllama.utility.stats import StatsDialog
# main_window.py
from QtOllama.utility.logger_setup import create_logger
logger = create_logger(__name__)


def messages_to_prompt(messages):
    """
    Converts a list of message dictionaries into a single prompt string.

    Args:
        messages (list): A list of message dictionaries with 'role' and 'content' keys.

    Returns:
        str: A formatted prompt string for the Ollama API.
    """
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


class MainWindow(FramelessWindow, QMainWindow):
    def __init__(self, *args, **kwargs):
        try:
            super().__init__(*args, **kwargs)
            self.ui = QMainWindow()
            self.menus = None
            self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
            self.progress_dialog = None
            self.simulation_dialog = None
            self.status_layout = None
            self.status_message = None
            self.status_bar = None
            self.progress_bar = None
            self.toolbar = None
            self.info_label = None
            self.status_widget = None
            self.word_cloud_btn = None
            self.historical_stats_button = None
            self.stats_button = None
            self.stats_dialog = None
            self.assistant_response = ""
            self.thread = None
            self.restart_button = None
            self.analytics_button = None
            self.stop_button = None
            self.download_button = None
            self.chat_display = None
            self.model_combo = None
            self.input_field = None
            self.send_button = None
            self.word_cloud_dialog = None
            self.historical_stats_dialog = None
            self.context_length_spinner = None
            self.selected_model = ""
            self.messages = []
            self.context_length = CONTEXT_LENGTH_DEFAULT

            ui_components = UIComponents(self)
            ui_components.init_ui()

            self.load_models()

            # Initialize menus before creating MenuCreator
            capabilities_instance = capabilities.Capabilities()
            self.menus = {
                "Analyze": {
                    "Prose": {
                        "Textual": capabilities_instance.get_prose_textual_analysis_types(),
                        "Semantic": capabilities_instance.get_prose_semantic_analysis_types(),
                        "Linguistic": capabilities_instance.get_prose_linguistic_analysis_types(),
                        "Cognitive": capabilities_instance.get_prose_cognitive_analysis_types(),
                        "Contextual": capabilities_instance.get_prose_contextual_analysis_types(),
                        "Stylistic": capabilities_instance.get_prose_stylistic_analysis_types(),
                        "Narrative": capabilities_instance.get_prose_narrative_analysis_types()
                    },
                    "Critical": capabilities_instance.get_critical_analysis_types(),
                    "Psychoanalytical": capabilities_instance.get_psychoanalytical_analysis_types(),
                    "Scientific": capabilities_instance.get_scientific_analysis_types(),
                    "Philosophical": capabilities_instance.get_philosophical_analysis_types(),
                    "Statistical": capabilities_instance.get_statistical_analysis_types(),
                    "Opposition": capabilities_instance.get_opposition_analysis_types(),
                    "Code": capabilities_instance.get_code_analysis_types(),
                    "Prompt": capabilities_instance.get_prompt_analysis_types(),
                    "Art Prompt": capabilities_instance.get_art_prompt_analysis_types(),
                    "Poetry": capabilities_instance.get_poetry_analysis_types(),
                },
                "Generate": {
                    "Prose": {
                        "Textual": capabilities_instance.get_prose_textual_generation_types(),
                        "Semantic": capabilities_instance.get_prose_semantic_generation_types(),
                        "Cognitive": capabilities_instance.get_prose_cognitive_generation_types(),
                        "Contextual": capabilities_instance.get_prose_contextual_generation_types(),
                        "Stylistic": capabilities_instance.get_prose_stylistic_generation_types(),
                        "Narrative": capabilities_instance.get_prose_narrative_generation_types(),
                    },
                    "Documentation": capabilities_instance.get_documentation_generation_types(),
                    "Prompt": capabilities_instance.get_prompt_generation_types(),
                    "Art Prompt": capabilities_instance.get_art_prompt_generation_types(),
                    "Poetry": capabilities_instance.get_poetry_generation_types(),
                    "Code": capabilities_instance.get_code_generation_types(),
                },
                "Transform": {
                    "Prose": {
                        "Textual": capabilities_instance.get_prose_textual_transformation_types(),
                        "Semantic": capabilities_instance.get_prose_semantic_transformation_types(),
                        "Cognitive": capabilities_instance.get_prose_cognitive_transformation_types(),
                        "Contextual": capabilities_instance.get_prose_contextual_transformation_types(),
                        "Stylistic": capabilities_instance.get_prose_stylistic_transformation_types(),
                        "Narrative": capabilities_instance.get_prose_narrative_transformation_types(),
                    },
                    "Scaling": capabilities_instance.get_text_scaling_types(),
                    "Enhancement": capabilities_instance.get_text_enhancement_types(),
                    "Prompt": capabilities_instance.get_prompt_transformation_types(),
                    "Art Prompt": capabilities_instance.get_art_prompt_transformation_types(),
                    "Poetry": capabilities_instance.get_poetry_transformation_types(),
                    "Code": capabilities_instance.get_code_transformation_types(),
                },
            }

            menu_creator = MenuCreator(self)
            menu_creator.create_menus()

            signal_connector = SignalConnector(self)
            signal_connector.connect_signals()
        except Exception as e:
            logger.error(f"{e}")
    
    class ResponseThread(QThread):
        response_chunk_received = pyqtSignal(str)
        response_finished = pyqtSignal(str)
        error_occurred = pyqtSignal(str)
        
        def __init__(self,
                     model_name,
                     messages):
            super().__init__()
            self.model_name = model_name
            self.messages = messages.copy()
        
        def run(self):
            response = ""
            try:
                prompt = messages_to_prompt(self.messages)
                logger.debug(f"Prompt sent to Ollama:\n{prompt}")
                for chunk in ollama.generate(model=self.model_name, prompt=prompt):
                    # Since chunk is a string, we can use it directly
                    logger.debug(f"Chunk received: {chunk}")
                    content = chunk  # chunk is a string
                    response += content
                    self.response_chunk_received.emit(content)
                self.response_finished.emit(response)
            except Exception as e:
                logger.error(f"Error in response thread: {e}")
                self.error_occurred.emit(str(e))
                
    def connect_signals(self):
        try:
            # ///////////////////////////////////////////////////////////////////
            # Connect signals
            # ///////////////////////////////////////////////////////////////////

            self.view_saved_chats_button.clicked.connect(self.view_saved_chats)
            self.save_chat_button.clicked.connect(self.save_chat_to_history)
            self.stats_button.clicked.connect(self.show_statistics)
            self.send_button.clicked.connect(self.send_message)
            self.download_button.clicked.connect(self.download_chat)
            self.analytics_button.clicked.connect(self.show_analytics)
            self.stop_button.clicked.connect(self.stop_chat)
            self.restart_button.clicked.connect(self.restart_chat)
            self.input_field.returnPressed.connect(self.send_message)
            self.word_cloud_btn.clicked.connect(self.open_word_cloud)
            self.historical_stats_button.clicked.connect(self.view_historical_stats)
            self.simulation_btn.clicked.connect(self.start_simulation)
        except Exception as e:
            logger.error(f"{e}")

    def start_simulation(self):
        """
        Starts the simulation by creating and displaying a SimulationDialog.
        """
        from QtOllama.utility.simulation import SimulationDialog

        # Pass the selected model to the SimulationDialog
        self.simulation_dialog = SimulationDialog(
            self.chat_display, self, selected_model=self.selected_model
        )
        self.simulation_dialog.show()
        
    def create_menus(self):
        """
        Creates a hierarchical menu structure in the application's menu bar.

        The method iterates over the `self.menus` dictionary to dynamically
        generate menus and submenus. Each menu item is connected to the 
        `self.perform_ai_analysis` method, which is triggered when the menu 
        item is selected.

        The `self.menus` dictionary should have the following structure:
        {
            'Main Menu 1': {
            'Submenu 1': ['Option 1', 'Option 2'],
            'Submenu 2': {
                'Subsubmenu 1': ['Option 3', 'Option 4']
            }
            },
            'Main Menu 2': ['Option 5', 'Option 6']
        }

        The method supports nested submenus up to two levels deep.

        Returns:
            None
        """
        try:
            for main_menu_name, main_submenus in self.menus.items():
                main_menu = self.menuBar().addMenu(main_menu_name)
                for submenu_name, submenus in main_submenus.items():
                    if isinstance(submenus, dict):
                        submenu = main_menu.addMenu(submenu_name)
                        for subsubmenu_name, options in submenus.items():
                            subsubmenu = submenu.addMenu(subsubmenu_name)
                            for option in options:
                                action = QAction(option, self)
                                action.triggered.connect(
                                    lambda checked, o=option: self.perform_ai_analysis(o)
                                )
                                subsubmenu.addAction(action)
                    else:
                        submenu = main_menu.addMenu(submenu_name)
                        for option in submenus:
                            action = QAction(option, self)
                            action.triggered.connect(
                                lambda checked, o=option: self.perform_ai_analysis(o)
                            )
                            submenu.addAction(action)
        except Exception as e:
            logger.error(f"{e}")
            
    # /////////////////////////////////////////////////////////////////////////////////////
    # WORD CLOUD
    # /////////////////////////////////////////////////////////////////////////////////////
    def open_word_cloud(self):
        """
        Opens the WordCloudDialog.

        This method initializes a WordCloudDialog with the current chat display
        and shows the dialog to the user.
        """
        try:
            self.word_cloud_dialog = WordCloudDialog(self.chat_display, self)
            self.word_cloud_dialog.show()
        except Exception as e:
            logger.error(f"{e}")
            
    # /////////////////////////////////////////////////////////////////////////////////////
    # HISTORICAL VIEW
    # /////////////////////////////////////////////////////////////////////////////////////
    def view_historical_stats(self):
        """
        Opens and displays the historical statistics dialog.

        This method initializes the HistoricalStatsDialog and shows it to the user.
        """
        try:
            self.historical_stats_dialog = HistoricalStatsDialog(self)
            self.historical_stats_dialog.show()
    
        except Exception as e:
            logger.error(f"{e}")
            
    # /////////////////////////////////////////////////////////////////////////////////////
    # LOAD_MODELS
    # /////////////////////////////////////////////////////////////////////////////////////
    def load_models(self):
        """
        Loads available models from the Ollama API and populates the model combo box.

        This method retrieves a list of models from the Ollama API, extracts their names,
        and adds them to the model combo box. If models are successfully loaded, the first
        model is selected by default, and a signal is connected to handle model changes.
        Logs the loaded model names or an error message if the loading fails.

        Raises:
            Exception: If there is an error while loading models from the Ollama API.
        """
        try:
            models = ollama.list()["models"]
            model_names = [model["name"] for model in models]
            self.model_combo.addItems(model_names)
            if model_names:
                self.selected_model = model_names[0]
                self.model_combo.currentTextChanged.connect(self.model_changed)
            logger.info(f"Loaded models: {model_names}")
        except Exception as e:
            logger.error(f"Error loading models: {str(e)}")
            QMessageBox.critical(self, "Error", f"Failed to load models: {str(e)}")

    # /////////////////////////////////////////////////////////////////////////////////////
    # MODEL_CHANGED
    # /////////////////////////////////////////////////////////////////////////////////////
    def model_changed(self, text):
        """
        Handle the event when the model selection is changed.

        This method updates the selected model and logs the change.

        Parameters:
        text (str): The name of the newly selected model.
        """
        self.selected_model = text
        logger.info(f"Selected model changed to: {self.selected_model}")
    
    # /////////////////////////////////////////////////////////////////////////////////////
    # SEND_MESSAGE
    # /////////////////////////////////////////////////////////////////////////////////////
    def send_message(self):
        """
        Handles the event of sending a message from the user.

        This method retrieves the text from the input field, appends it to the messages list,
        displays the message in the chat display, and clears the input field. It then starts
        a new thread to get the assistant's response and connects the thread's signals to the
        appropriate handler methods.

        Attributes:
            prompt (str): The text input from the user.
            messages (list): The list of messages exchanged in the chat.
            assistant_response (str): The response from the assistant.
            thread (ResponseThread): The thread responsible for fetching the assistant's response.

        Signals:
            response_chunk_received: Emitted when a chunk of the assistant's response is received.
            response_finished: Emitted when the assistant's response is fully received.
            error_occurred: Emitted when an error occurs during the response fetching process.
        """
        prompt = self.input_field.text()
        if prompt:
            self.messages.append({"role": "user", "content": prompt})
            self.display_message("user", prompt)
            self.input_field.clear()
            logger.info(f"Sending message: {prompt}")
            self.assistant_response = ""
            self.chat_display.append("<b>Assistant:</b> ")
            # Start a thread to get the assistant's response
            self.thread = ResponseThread(self.selected_model, self.messages)
            self.thread.response_chunk_received.connect(self.handle_response_chunk)
            self.thread.response_finished.connect(self.handle_response_finished)
            self.thread.error_occurred.connect(self.handle_error)
            self.thread.start()
    
    def save_chat_to_history(self):
        try:
            chats_file = "./chat_history.json"
            
            # Get the current chat messages
            chat = self.messages.copy()
            
            # Add a timestamp
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            chat_entry = {"timestamp": timestamp, "chat": chat}
            
            # Load existing chats if the file exists
            if os.path.exists(chats_file):
                with open(chats_file, "r") as f:
                    saved_chats = json.load(f)
            else:
                saved_chats = []
            
            # Append the current chat to the saved_chats
            saved_chats.append(chat_entry)
            
            # Save back to the file
            with open(chats_file, "w") as f:
                json.dump(saved_chats, f, indent=4)
            
            print(f"Chat saved at {timestamp}")
        except Exception as e:
            logger.error(f"{e}", exc_info=True)
    
    def view_saved_chats(self):
        try:
            self.saved_chats_dialog = SavedChatsDialog(self)
            self.saved_chats_dialog.show()
        except Exception as e:
            logger.error(f"Error opening SavedChatsDialog: {e}")
            
    def handle_response_chunk(self, chunk):
        """
        Handles a chunk of response from the assistant.

        This method appends the given chunk to the assistant's response,
        updates the chat display with the new chunk, and ensures that the
        cursor is visible in the chat display.

        Args:
            chunk (str): A piece of the response from the assistant.
        """
        self.assistant_response += chunk
        self.chat_display.insertPlainText(chunk)
        self.chat_display.ensureCursorVisible()
    
    def handle_response_finished(self):
        """
        Handles the completion of a response from the assistant.

        This method appends the assistant's response to the messages list with the role 
        set to "assistant" and logs that the response has finished.

        Attributes:
            self.assistant_response (str): The response content from the assistant.
        """
        self.messages.append({"role": "assistant", "content": self.assistant_response})
        logger.info("Response finished")
    
    def handle_error(self, error_message):
        """
        Handles errors by logging the error message and displaying a critical message box.

        Args:
            error_message (str): The error message to be logged and displayed.
        """
        logger.error(f"Error in response thread: {error_message}")
        QMessageBox.critical(self, "Error", f"An error occurred: {error_message}")
    
    def display_message(self, role, content):
        """
        Appends a formatted message to the chat display based on the role.

        Parameters:
        role (str): The role of the message sender, either "user" or "assistant".
        content (str): The content of the message to be displayed.

        Returns:
        None
        """
        if role == "user":
            self.chat_display.append(f"<b>User:</b> {content}")
        else:
            self.chat_display.append(f"<b>Assistant:</b> {content}")
    
    def download_chat(self):
        """
        Prompts the user to save the chat messages to a file in various formats (PDF, TXT, MD, HTML).
        The method converts the chat messages into a markdown format and then allows the user to save
        the content in the chosen file format. If the user does not provide a valid extension, the 
        method defaults to saving the file as a .txt file.
        Supported file formats:
        - PDF: Saves the chat as a PDF document.
        - TXT: Saves the chat as a plain text file.
        - MD: Saves the chat as a markdown file.
        - HTML: Saves the chat as an HTML file.
        The method uses QFileDialog to prompt the user for the save location and file name.
        Raises:
            IOError: If there is an error writing to the file.
        """
        markdown_content = "\n\n".join(
            [f"**{msg['role']}**: {msg['content']}" for msg in self.messages]
        )
        options = "PDF Files (*.pdf);;Text Files (*.txt);;Markdown Files (*.md);;HTML Files (*.html)"
        filename, _ = QFileDialog.getSaveFileName(None, "Save File", "", options)
        
        if filename:
            file_extension = QFileInfo(filename).suffix().lower()
            
            if file_extension not in ["txt", "md", "html", "pdf"]:
                filename += ".txt"  # Default to .txt if no valid extension is provided
                file_extension = "txt"
            
            if file_extension == "pdf":
                printer = QPrinter(QPrinter.PrinterMode.HighResolution)
                printer.setOutputFormat(QPrinter.OutputFormat.PdfFormat)
                printer.setOutputFileName(filename)
                self.chat_display.document().print(printer)
            elif file_extension in ["txt", "md"]:
                with open(filename, 'w', encoding='utf-8') as file:
                    file.write(markdown_content)
            elif file_extension == "html":
                with open(filename, 'w', encoding='utf-8') as file:
                    html_content = markdown.markdown(markdown_content)
                    file.write(html_content)

    def show_statistics(self):
        """
        Toggles the visibility of the statistics dialog.

        If the statistics dialog is currently visible, it will be closed and set to None.
        If the statistics dialog is not visible, a new instance of StatsDialog will be created
        and displayed.

        Attributes:
            stats_dialog (StatsDialog): The dialog window displaying statistics.
            chat_display (QWidget): The widget displaying the chat content.
        """
        if self.stats_dialog is not None and self.stats_dialog.isVisible():
            self.stats_dialog.close()
            self.stats_dialog = None
        else:
            self.stats_dialog = StatsDialog(self.chat_display, self)
            self.stats_dialog.show()
    
    def update_info(self):
        """
        Updates the information label with various text statistics and interpretations.
        This method retrieves the text from the text editor, analyzes it using TextBlob and textstat,
        and updates the info label with the following information:
        - Number of characters
        - Number of words
        - Number of lines
        - Sentiment polarity and its interpretation
        - Sentiment subjectivity and its interpretation
        - Flesch reading ease score and its interpretation
        The interpretations are provided by the Interpretations class.
        Returns:
            None
        """
        text = self.text_editor.toPlainText()
        blob = TextBlob(text)
        
        sentiment_polarity = blob.sentiment.polarity
        sentiment = Interpretations.sentiment_polartiy_interpretation(sentiment_polarity)
        sentiment_subjectivity = blob.sentiment.subjectivity
        subjectivity = Interpretations.sentiment_subjectivity_interpretation(sentiment_subjectivity)
        flesch_reading_ease = textstat.flesch_reading_ease(text)
        reading_ease = Interpretations.flesch_reading_ease_interpretation(flesch_reading_ease)
        
        characters = len(text)
        words = len(text.split())
        lines = text.count("\n") + 1 if text else 0
        self.info_label.setText(
            f"Characters: {characters}, "
            f"Words: {words}, "
            f"Lines: {lines}, "
            f"Sentiment: {sentiment}, "
            f"Subjectivity: {subjectivity}, "
            f"Complexity: {reading_ease} ",
        )

    def update_status(self, status):
        """
        Updates the status bar with the given status message.

        Parameters:
        - status (str): The status message to be displayed in the status bar.
        """
        self.status_bar.showMessage(status)
    
    def perform_ai_analysis(self, analysis_type):
        """
        Perform an AI analysis on the selected text or the last user message.
        This method checks if there is any selected text in the chat display. If there is, it uses the selected text;
        otherwise, it retrieves the last message sent by the user. It then creates a prompt for the AI assistant to 
        perform the specified type of analysis on the text. The prompt is added to the messages list, and the assistant's 
        response is handled in a separate thread.
        Args:
            analysis_type (str): The type of analysis to be performed on the text (e.g., sentiment analysis, summarization).
        Returns:
            None
        """

        # Check if there is selected text in the chat_display
        text_cursor = self.chat_display.textCursor()
        if text_cursor.hasSelection():
            text = text_cursor.selectedText()
        else:
            # No selection, get the last message from the user
            text = self.get_last_user_message()
            if not text:
                self.update_status("Please select text or send a message first.")
                return
        
        # Create the prompt
        prompt = f"Please perform {analysis_type} on the following text: '{text}'"
        
        # Add the message to the messages list
        self.messages.append({"role": "user", "content": prompt})
        self.display_message("user", prompt)
        self.assistant_response = ""
        self.chat_display.append("<b>Assistant:</b> ")
        
        # Trim messages to fit within context length
        self.trim_messages()
        
        # Start a thread to get the assistant's response
        self.thread = ResponseThread(self.selected_model, self.messages)
        self.thread.response_chunk_received.connect(self.handle_response_chunk)
        self.thread.response_finished.connect(self.handle_response_finished)
        self.thread.error_occurred.connect(self.handle_error)
        self.thread.start()
    
    def trim_messages(self):
        """
        Trims the list of messages to ensure the total length of their content does not exceed the context length.

        This method iterates through the messages and removes the oldest messages until the total length of the 
        remaining messages' content is within the specified context length. It ensures that at least one message 
        remains in the list.

        Attributes:
            self.messages (list): A list of message dictionaries, where each dictionary contains a "content" key 
                                  with the message text.
            self.context_length (int): The maximum allowed total length of the messages' content.

        Logs:
            Logs an info message indicating the number of messages remaining after trimming.
        """
        total_length = sum(len(msg["content"]) for msg in self.messages)
        while total_length > self.context_length and len(self.messages) > 1:
            removed_message = self.messages.pop(0)
            total_length -= len(removed_message["content"])
        logger.info(f"Trimmed messages to fit context length. Current message count: {len(self.messages)}")
        
    def get_last_user_message(self):
        """
        Retrieve the content of the last message sent by the user.

        This method iterates through the list of messages in reverse order and 
        returns the content of the first message found that has the role 'user'. 
        If no such message is found, it returns an empty string.

        Returns:
            str: The content of the last user message, or an empty string if no user message is found.
        """

        for msg in reversed(self.messages):
            if msg['role'] == 'user':
                return msg['content']
        return ""
    
    def get_active_window(self):
        """
        Retrieves the currently active QTextEdit widget from the active window.

        Returns:
            QTextEdit: The active QTextEdit widget if found, otherwise None.
        """

        active_window = QApplication.activeWindow()
        active_editor = (
            active_window.findChild(QTextEdit)
            if hasattr(active_window, "findChild")
            else None
        )
        return active_editor

    def handle_ai_result(self, analysis_type, result, error, settings):
        """
        Handles the AI result by displaying a dialog with the analysis type, result, elapsed time, and settings.
        If the result is not empty, a ResultDialog is created and shown.
        If there is an error, a QMessageBox with the error message is displayed.
        The progress dialog is hidden if it exists.

        Parameters:
        - analysis_type (str): The type of analysis.
        - result (any): The result of the analysis.
        - error (str): The error message, if any.
        - settings (dict): The settings for the analysis.

        Returns:
        - None
        """
        if result:
            elapsed_time = time.time() - self.start_time
            dialog = ResultDialog(analysis_type, result, elapsed_time, settings["operation_model"], self)
            dialog.regenerate.connect(lambda: self.regenerate_analysis(analysis_type))

            dialog.finished.connect(lambda: self.dialogs.remove(dialog))
            self.dialogs.append(dialog)
            dialog.show()

        elif error:
            QMessageBox.critical(self, "Error", error)

        if self.progress_dialog:
            self.progress_dialog.hide()
            self.progress_dialog = None

    def regenerate_analysis(self, analysis_type):
        """
        Regenerates the analysis for the specified analysis type.

        Parameters:
        - analysis_type (str): The type of analysis to regenerate.

        Returns:
        - None
        """
        self.perform_ai_analysis(analysis_type)
        
    def show_analytics(self):
        """
        Displays analytics information about the messages exchanged.

        This method calculates and shows the total number of messages, the number of user messages,
        the number of assistant messages, the estimated total number of tokens, and the current context length.
        The information is displayed in a message box.

        The following analytics are displayed:
        - Total messages: The total number of messages exchanged.
        - User messages: The number of messages sent by the user.
        - Assistant messages: The number of messages sent by the assistant.
        - Estimated total tokens: The total number of words in all messages.
        - Current context length: The current length of the context.

        A log entry is created to indicate that the analytics have been displayed.
        """
        user_messages = [msg['content'] for msg in self.messages if msg['role'] == 'user']
        assistant_messages = [msg['content'] for msg in self.messages if msg['role'] == 'assistant']
        total_messages = len(self.messages)
        total_tokens = sum(len(msg['content'].split()) for msg in self.messages)
        message = f"""
            Total messages: {total_messages}\n
            User messages: {len(user_messages)}\n
            Assistant messages: {len(assistant_messages)}\n
            Estimated total tokens: {total_tokens}\n
            Current context length: {self.context_length}
            """
        QMessageBox.information(self, "Analytics", message)
        logger.info("Analytics displayed")
    
    def stop_chat(self):
        """
        Stops the chat by terminating the running thread, clearing messages, and updating the chat display.

        This method performs the following actions:
        1. Checks if a thread is running and terminates it.
        2. Waits for the thread to finish.
        3. Clears the list of messages.
        4. Clears the chat display.
        5. Logs the action of stopping and clearing the chat.
        """
        if self.thread and self.thread.isRunning():
            self.thread.terminate()
            self.thread.wait()
        self.messages = []
        self.chat_display.clear()
        print("Chat stopped and cleared")
        logger.info("Chat stopped and cleared")
    
    def restart_chat(self):

        """
        Restarts the chat session by first stopping the current chat and then logging the restart action.

        This method ensures that any ongoing chat session is properly terminated before initiating a new one.
        """
        self.stop_chat()
        print("Chat Restarted")
        logger.info("Chat restarted")


class ResponseThread(QThread):
    """
    Attributes:
        response_chunk_received (pyqtSignal): Signal emitted when a chunk of the response is received.
        response_finished (pyqtSignal): Signal emitted when the entire response is finished.
        error_occurred (pyqtSignal): Signal emitted when an error occurs during the response generation.
        model_name (str): The name of the model to use for generating responses.
        messages (list): A list of messages to send to the model.
    Methods:
        run():
            Executes the thread, generating responses from the model and emitting signals for each chunk received and when the response is finished.
    ResponseThread is a QThread subclass that handles generating responses using a specified model and emits signals during the process.
    """
    response_chunk_received = pyqtSignal(str)
    response_finished = pyqtSignal(str)
    error_occurred = pyqtSignal(str)
    
    def __init__(self, model_name, messages):
        """
        Initializes the instance of the class.

        Args:
            model_name (str): The name of the model.
            messages (list): A list of messages to be copied.

        """
        super().__init__()
        self.model_name = model_name
        self.messages = messages.copy()
    
    def run(self):
        """
        Executes the main logic for generating a response using the Ollama model.

        This method constructs a prompt from the provided messages, sends it to the Ollama model,
        and processes the streamed response chunks. Each chunk is either appended to the final
        response or handled as an error if it cannot be parsed. The method emits signals for
        each received chunk and the final response, as well as any errors encountered.

        Emits:
            response_chunk_received (str): Signal emitted for each chunk of the response received.
            response_finished (str): Signal emitted when the entire response has been received.
            error_occurred (str): Signal emitted if an error occurs during the response generation.

        Raises:
            Exception: If any error occurs during the response generation process.
        """
        response = ""
        try:
            prompt = messages_to_prompt(self.messages)
            logger.debug(f"Prompt sent to Ollama:\n{prompt}")
            for chunk in ollama.generate(model=self.model_name, prompt=prompt, stream=True):
                logger.debug(f"Type of chunk: {type(chunk)}")
                logger.debug(f"Chunk received: {chunk}")
                # Handle chunk
                if isinstance(chunk, str):
                    try:
                        chunk_dict = json.loads(chunk)
                        content = chunk_dict.get('response', '')
                    except json.JSONDecodeError:
                        logger.error(f"Failed to parse chunk as JSON: {chunk}")
                        content = chunk  # Use as is
                elif isinstance(chunk, dict):
                    content = chunk.get('response', '')
                else:
                    logger.error(f"Unexpected chunk type: {type(chunk)}")
                    content = ''
                response += content
                self.response_chunk_received.emit(content)
            self.response_finished.emit(response)
        except Exception as e:
            logger.error(f"Error in response thread: {e}", exc_info=True)
            self.error_occurred.emit(str(e))
            

    def ollama_generator(model_name: str, messages: Dict) -> Generator:
        """
        Generates a stream of messages from the Ollama chat model.
    
        Args:
            model_name (str): The name of the chat model to use.
            messages (Dict): A dictionary containing the messages to send to the model.
    
        Yields:
            str: The content of each message chunk from the stream.
    
        Raises:
            Exception: If an error occurs during the generation process, it logs the error and raises the exception.
        """
        try:
            stream = ollama.chat(
                model=model_name, messages=messages, stream=True
            )
            for chunk in stream:
                yield chunk['message']['content']
        except Exception as e:
            logger.error(f"Error in ollama_generator: {str(e)}", exc_info=True)
            raise
    
