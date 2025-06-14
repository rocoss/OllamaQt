import json
import os

from PyQt6.QtCore import pyqtSignal
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QDialog, QVBoxLayout, QGroupBox, QLabel, QLineEdit, QHBoxLayout, QRadioButton, QPushButton, \
    QFontDialog


# settings.py
import json
import os

from QtOllama.utility.logger_setup import create_logger
logger = create_logger(__name__)


def load_settings():
    """
    Loads settings from a JSON file named 'settings.json'. If the file does not exist,
    it returns default settings.

    Returns:
        dict: A dictionary containing the settings.

    Raises:
        Exception: If there is an error loading the settings, it logs the error.
    """

    try:
        settings_file = "settings.json"
        if os.path.exists(settings_file):
            with open(settings_file, 'r') as f:
                settings = json.load(f)
        else:
            # Default settings
            settings = {
                "conversation_model": "llama2"
            }
        return settings
    except Exception as e:
        logger.error(f"Error loading settings {e}")


class SettingsDialog(QDialog):
    """
    A dialog window for updating application settings.

    Signals:
        updated: Emitted when settings are updated.

    Methods:
        __init__(parent=None):
            Initializes the settings dialog.
        
        choose_font():
            Opens a font dialog to choose a font and updates the font fields.
        
        load_settings():
            Loads the settings from a persistent storage.
    """
    updated = pyqtSignal()
    def __init__(self, parent=None):
        """
        Initializes the SettingsDialog.
        Args:
            parent (QWidget, optional): The parent widget of the dialog. Defaults to None.
        Attributes:
            layout (QVBoxLayout): The layout manager for the dialog.
        Raises:
            Exception: If an error occurs during initialization, it is logged.
        """
        try:
            super().__init__(parent)
            self.setWindowTitle("Settings")
            self.resize(500, 200)  # specify dialog size
    
            self.layout = QVBoxLayout()
            self.setLayout(self.layout)
    
    
    
            self.load_settings()
        except Exception as e:
            logger.error(f"Error constructing the SettingsDialog {e}", exc_info=True)

    def choose_font(self):
        """
        Opens a QFontDialog to allow the user to choose a font and font size.
        
        The current font and font size are retrieved from the respective input fields.
        If the user selects a valid font, the input fields are updated with the chosen font family and size.
        
        If an error occurs during the process, it is logged.

        Raises:
            Exception: If an error occurs while choosing the font.
        """
        try:
            current_font = self.font_field.text() or "Helvetica"
            current_font_size = int(self.font_size_field.text() or 14)
            current_font = QFont(current_font, current_font_size)
            font, valid = QFontDialog.getFont(current_font, self, "Choose Font")
            if valid:
                self.font_field.setText(font.family())
                self.font_size_field.setText(str(font.pointSize()))
        except Exception as e:
            logger.error(f"Error choosing font {e}", exc_info=True)

    def load_settings(self):
        """
        Loads the application settings.

        This method attempts to load the application settings using the `load_settings` function.
        If an error occurs during the loading process, it logs an error message with the exception details.

        Raises:
            Exception: If there is an error loading the settings.
        """
        try:
            settings = load_settings()
        except Exception as e:
            logger.error(f"Error loading settings {e}", exc_info=True)
