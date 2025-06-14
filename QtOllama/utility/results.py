
import os

import openai
from PyQt6.QtCore import QThread, pyqtSignal
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QDialog, QVBoxLayout, QTextEdit, QScrollArea, QToolBar, QApplication, \
    QFileDialog, QMessageBox, QInputDialog, QPushButton, QHBoxLayout, \
    QStatusBar

# from conversation import AIDialog
from settings import load_settings
from QtOllama.utility.logger_setup import create_logger
logger = create_logger(__name__)


class Worker(QThread):
    """
    Worker class for performing textual analysis using the OpenAI API.

    Attributes:
        completed (pyqtSignal): Signal emitted upon completion of the analysis with the analysis type, 

    Methods:
        __init__(analysis_type: str, text: str):
            Initializes the Worker with the specified analysis type and text.
        
        run():
    """

    completed = pyqtSignal(str, str, str, dict)

    def __init__(self, analysis_type: str, text: str):
        try:
            QThread.__init__(self)
            self.analysis_type = analysis_type
            self.text = text
        except Exception as e:
            logger.error(f"error initializing Worker thread in results.py {e}", exc_info=True)

    def run(self):
        """
        Executes the analysis by interacting with the OpenAI API.

        This method performs the following steps:
        1. Loads the settings which include the OpenAI API key and model.
        2. Constructs the system and user messages for the API request.
        3. Sends a request to the OpenAI API to perform the specified analysis.
        4. Emits the result of the analysis or an error if one occurs.

        Emits:
            self.completed (str, str, str, dict): Signal emitted with the analysis type,
            result, error message (if any), and settings.

        Raises:
            Exception: If any error occurs during the API request or processing.
        """
        try:
            settings = load_settings()
            openai.api_key = settings["api_key"]
            system_message = (
                "You are an AI developed by OpenAI with advanced textual analysis capabilities. "
                "Your main task is to analyze texts based on parameters set by your operators. "
                "You are expected to provide detailed and scholarly analysis. "
            )
            user_message = (
                f"Please perform a {self.analysis_type} on the following text: '{self.text}'"
            )
            messages = [
                {
                    "role": "system",
                    "content": system_message,
                },
                {
                    "role": "user",
                    "content": user_message,
                },
            ]
            response = openai.ChatCompletion.create(
                model=settings["conversation_model"], messages=messages, temperature=0.2
            )
            result = response["choices"][0]["message"]["content"]
            self.completed.emit(self.analysis_type, result, None, settings)
        except Exception as e:
            self.completed.emit(self.analysis_type, None, str(e))
            logger.error(f"error initializing Worker thread in results.py {e}")


class ResultDialog(QDialog):
    """
    A dialog window that displays the results of an analysis and provides various actions.

    Attributes:
        regenerate (pyqtSignal): Signal emitted to trigger regeneration of results.
        main_window (QMainWindow): Reference to the main application window.
        result_text_edit (QTextEdit): Text edit widget displaying the result.
        conversation_button (QPushButton): Button to initiate a discussion about the result.
        dismiss_button (QPushButton): Button to dismiss the dialog.
        status_bar (QStatusBar): Status bar displaying processing time and model used.

    Methods:
        __init__(self, analysis_type, result, elapsed_time, operation_model, main_window):
            Initializes the ResultDialog with the given parameters.
        
        copy_to_clipboard(self):
            Copies the result text to the clipboard.
        
        save_to_file(self):
            Opens a file dialog to save the result text to a file.
        
        discuss_result(self):
            Opens a dialog to discuss the result text.
        
        transfer_text(self):
            Transfers the result text to the main text editor with options to prepend, append, or replace.
        
        emit_regenerate_signal(self):
            Emits the regenerate signal.
    """
    regenerate = pyqtSignal()

    def __init__(self, analysis_type, result, elapsed_time, operation_model, main_window):
        """
        Initializes the result window with the given parameters.

        Args:
            analysis_type (str): The type of analysis performed.
            result (str): The result text to be displayed.
            elapsed_time (float): The time taken to perform the analysis.
            operation_model (str): The model used for the operation.
            main_window (QMainWindow): The main window of the application.

        Initializes the window title, layout, toolbar with actions, result text edit,
        scroll area, conversation and dismiss buttons, and status bar displaying
        processing time and model used.
        """
        try:
            super().__init__()
            self.setWindowTitle(f"{analysis_type}")
            layout = QVBoxLayout()
            self.setLayout(layout)
            self.main_window = main_window
    
            # Create a toolbar
            toolbar = QToolBar()
            layout.addWidget(toolbar)
    
            # Create actions for the toolbar
            copy_action = QAction("Copy", self)
            save_action = QAction("Save", self)
            transfer_action = QAction("Transfer", self)
            regenerate_action = QAction("Regenerate", self)
    
            # Add actions to the toolbar
            toolbar.addAction(copy_action)
            toolbar.addAction(save_action)
            toolbar.addAction(transfer_action)
            toolbar.addAction(regenerate_action)
    
            # Connect actions to their respective slots
            copy_action.triggered.connect(self.copy_to_clipboard)
            save_action.triggered.connect(self.save_to_file)
            transfer_action.triggered.connect(self.transfer_text)
            regenerate_action.triggered.connect(self.emit_regenerate_signal)
    
            self.result_text_edit = QTextEdit()
            self.result_text_edit.setPlainText(result)
            self.result_text_edit.setReadOnly(True)
            self.result_text_edit.setLineWrapMode(QTextEdit.LineWrapMode.WidgetWidth)
    
            scroll = QScrollArea(self)
            scroll.setWidgetResizable(True)
            scroll.setWidget(self.result_text_edit)
            layout.addWidget(scroll)
    
            # Add a Conversation button and a Dismiss button side by side,
            # with the Dismiss button on the right and as the default button
            buttons_layout = QHBoxLayout()
            self.conversation_button = QPushButton("Conversation", self)
            self.conversation_button.clicked.connect(self.discuss_result)
            buttons_layout.addWidget(self.conversation_button)
    
            self.dismiss_button = QPushButton("Dismiss", self)
            self.dismiss_button.clicked.connect(self.close)
            self.dismiss_button.setDefault(True)
            buttons_layout.addWidget(self.dismiss_button)
    
            layout.addLayout(buttons_layout)
    
            elapsed_time_str = f"{elapsed_time:.2f}"
            self.status_bar = QStatusBar(self)
            layout.addWidget(self.status_bar)
            self.status_bar.showMessage("Processing time: " + elapsed_time_str + " seconds" + ", Model used: " + operation_model)
    
            self.resize(600, 800)
        except Exception as e:
            logger.error(f"error initializing ResultDialog {e}", exc_info=True)
            
    def copy_to_clipboard(self):
        """
        Copies the text from the result_text_edit widget to the system clipboard.

        This method retrieves the current text from the result_text_edit widget,
        which is expected to be a QTextEdit or similar widget, and sets this text
        to the system clipboard using QApplication's clipboard functionality.
        """
        try:
            clipboard = QApplication.clipboard()
            clipboard.setText(self.result_text_edit.toPlainText())
        except Exception as e:
            logger.error(f"error copying results to clipboard results.py {e}", exc_info=True)

    def save_to_file(self):
        """
        Opens a file dialog to save the current text from the result text edit widget to a file.

        This method uses a QFileDialog to prompt the user to select a location and name for the file.
        If a valid filename is provided, the method writes the content of the result text edit widget
        to the specified file.

        Returns:
            None
        """
        try:
            filename, _ = QFileDialog.getSaveFileName(
                self, "Save Result", os.getenv("HOME")
            )
            if filename:
                with open(filename, "w") as file:
                    file.write(self.result_text_edit.toPlainText())
        except Exception as e:
            logger.error(f"Error saving results to file, results.py {e}", exc_info=True)
            
    def discuss_result(self):
        """
        Initiates a discussion about the result text.

        This method retrieves the current window title to determine the type of analysis
        and the text content from a text edit widget. It then creates and displays an 
        AI dialog initialized with the retrieved text and analysis type.

        Attributes:
            analysis_type (str): The type of analysis derived from the window title.
            text_content (str): The text content from the result text edit widget.
            initial_text (str): The initial text to be displayed in the AI dialog.
            ai_dialog (AIDialog): The AI dialog instance initialized with the initial text and analysis type.
        """
        analysis_type = self.windowTitle()
        text_content = self.result_text_edit.toPlainText()
        initial_text = f"You wrote: '{text_content}'. Now let's discuss more about this."
        self.ai_dialog = AIDialog(
            self, initial_text=initial_text, analysis_type=analysis_type
        )
        self.ai_dialog.show()

    def transfer_text(self):
        """
        Prompts the user to transfer text from the result text editor to the main text editor.
        
        This method displays a confirmation dialog to the user. If the user confirms, it then
        allows the user to choose how to transfer the text: prepend, append, or replace the 
        existing content in the main text editor. The selected text from the result text editor 
        is transferred based on the chosen option.

        Dialogs:
            - QMessageBox: Asks for confirmation to proceed with the text transfer.
            - QInputDialog: Allows the user to choose the transfer option (Prepend, Append, Replace).

        Modifies:
            - The content of the main text editor in the main window.

        Raises:
            None
        """
        response = QMessageBox.question(
            self,
            "Transfer Text",
            "This operation will modify the content in the main text editor. Do you want to proceed?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No,
        )
        if response == QMessageBox.StandardButton.Yes:
            main_editor = self.main_window.text_editor
            text_cursor = main_editor.textCursor()

            if self.result_text_edit.textCursor().selectedText().strip() == "":
                selected_text = self.result_text_edit.toPlainText()
            else:
                selected_text = (
                    self.result_text_edit.textCursor()
                    .selectedText()
                    .replace("\u2029", "\n")
                )

            options = ["Prepend", "Append"]
            if main_editor.toPlainText() or text_cursor.selectedText():
                options.append("Replace")

            modify_text_option, is_ok = QInputDialog.getItem(
                self, "Transfer Text", "Choose an option:", options, 0, False
            )
            if is_ok:
                if modify_text_option == "Prepend":
                    main_editor.setPlainText(
                        selected_text + "\n" + main_editor.toPlainText()
                    )
                elif modify_text_option == "Append":
                    main_editor.setPlainText(
                        main_editor.toPlainText() + "\n" + selected_text
                    )
                else:
                    if text_cursor.selectedText():
                        text_cursor.insertText(selected_text)
                    else:
                        main_editor.clear()
                        text_cursor.insertText(selected_text)

    def emit_regenerate_signal(self):
        """
        Emit the regenerate signal.

        This method triggers the `regenerate` signal, notifying any connected
        slots that a regeneration event has occurred.
        """
        self.regenerate.emit()
