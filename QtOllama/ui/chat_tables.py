from PyQt6.QtWidgets import QDialog, QVBoxLayout, QTableWidget, QTableWidgetItem, QLabel
import json
import os
from datetime import datetime
from QtOllama.utility.logger_setup import create_logger

logger = create_logger(__name__)


class SavedChatsDialog(QDialog):
    """
    A dialog window that displays saved chat histories in a table format.
    Attributes:
        label (QLabel): A label displaying instructions.
        table (QTableWidget): A table widget to display the saved chats.
    Methods:
        __init__(parent=None):
            Initializes the SavedChatsDialog with a title, size, layout, and loads the saved chats.
        load_chats():
            Loads the saved chats from a JSON file and populates the table with the chat data.
    """
    
    def __init__(self, parent=None):
        """
        Initializes the chat table window.
        Args:
            parent (QWidget, optional): The parent widget. Defaults to None.
        Attributes:
            label (QLabel): A label displaying instructions.
            table (QTableWidget): A table widget to display saved chats with two columns: "Timestamp" and "Chat".
        Methods:
            load_chats(): Loads and displays the saved chats in the table.
        """
        super().__init__(parent)
        self.setWindowTitle("Saved Chats")
        self.resize(600, 400)
        layout = QVBoxLayout()
        
        # Label for instructions
        self.label = QLabel("Showing Saved Chats over time:", self)
        layout.addWidget(self.label)
        
        # Table to display the chats
        self.table = QTableWidget(0, 2)
        self.table.setHorizontalHeaderLabels(["Timestamp", "Chat"])
        self.table.horizontalHeader().setStretchLastSection(True)
        layout.addWidget(self.table)
        
        self.setLayout(layout)
        
        # Load and display chats
        try:
            self.load_chats()
        except Exception as e:
            logger.error(f"Failed to load chats in __init__: {e}")
            self.label.setText("Failed to load chats. Please check the logs for more details.")
    
    def load_chats(self):
        """
        Load chat history from a JSON file and populate the table with the saved chats.
        This method attempts to read chat history from a file named "chat_history.json".
        If the file does not exist, it updates the label to indicate that no chats are available.
        If the file exists, it reads the chat data and populates the table with the chat entries.
        Each chat entry includes a timestamp and the chat content, which is formatted and displayed
        in the table.
        Raises:
            Exception: If there is an error loading the chat history, it logs the error message.
        """
        try:
            chats_file = "chat_history.json"
            if not os.path.exists(chats_file):
                self.label.setText("No chats available yet.")
                logger.info("No chat history file found.")
                return
            
            with open(chats_file, "r") as f:
                saved_chats = json.load(f)
                logger.info(f"Loaded {len(saved_chats)} chat entries from {chats_file}.")
            
            # Populate the table with the saved chats
            for entry in saved_chats:
                timestamp = entry.get("timestamp", "Unknown Time")
                chat = entry.get("chat", [])
                chat_content = ""
                for msg in chat:
                    role = msg.get("role", "")
                    content = msg.get("content", "")
                    chat_content += f"{role.capitalize()}: {content}\n"
                row = self.table.rowCount()
                self.table.insertRow(row)
                self.table.setItem(row, 0, QTableWidgetItem(timestamp))
                self.table.setItem(row, 1, QTableWidgetItem(chat_content))
            logger.info("Successfully populated the table with chat entries.")
        except json.JSONDecodeError as e:
            logger.error(f"JSON decode error while loading chats: {e}")
            self.label.setText("Failed to load chats due to JSON format error.")
        except FileNotFoundError as e:
            logger.error(f"Chat history file not found: {e}")
            self.label.setText("Chat history file not found.")
        except Exception as e:
            logger.error(f"Unexpected error loading chats: {e}")
            self.label.setText("Failed to load chats. Please check the logs for more details.")
