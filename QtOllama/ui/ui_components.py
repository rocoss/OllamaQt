# ui_components.py
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QComboBox, QTextEdit, QLineEdit, QPushButton, QStatusBar, QProgressBar
)
from QtOllama.utility.logger_setup import create_logger
logger = create_logger(__name__)

class UIComponents:
    """
    A class to initialize and manage the UI components of the main window.
    Attributes:
    -----------
    main_window : QMainWindow
        The main window of the application.
    Methods:
    --------
    __init__(main_window):
        Initializes the UIComponents with the main window.
    init_ui():
        Initializes and sets up the UI components and layout for the main window.
    """
    def __init__(self, main_window):
        """
        Initializes the UI components with the given main window.

        Args:
            main_window: The main window instance to which the UI components belong.
        """
        try:
            self.main_window = main_window
            logger.info("UIComponents initialized successfully.")
        except Exception as e:
            logger.error(f"Error initializing UIComponents in ui_component.py: {e}", exc_info=True)

    def init_ui(self):
        """
        Initializes the user interface components for the main window.
        This method sets up the main layout and various UI elements including:
        - A combo box for model selection.
        - A text edit area for chat display.
        - An input field and send button for user input.
        - Multiple buttons for various functionalities such as:
            - Saving chat
            - Viewing saved chats
            - Downloading chat
            - Showing analytics
            - Stopping chat
            - Restarting chat
            - Viewing statistics
            - Generating word cloud
            - Viewing historical stats
        - A status bar with a status message, progress bar, and additional info label.
        The layout is organized using QVBoxLayout and QHBoxLayout to structure the widgets.
        """
        try:
            main_widget = QWidget()
            main_layout = QVBoxLayout()
            top_layout = QHBoxLayout()
            model_label = QLabel("Select Model:")
            self.main_window.model_combo = QComboBox()
            top_layout.addWidget(model_label)
            top_layout.addWidget(self.main_window.model_combo)

            self.main_window.chat_display = QTextEdit()

            input_layout = QHBoxLayout()
            self.main_window.input_field = QLineEdit()
            self.main_window.send_button = QPushButton("Send")
            input_layout.addWidget(self.main_window.input_field)
            input_layout.addWidget(self.main_window.send_button)

            button_layout = QHBoxLayout()
            self.main_window.historical_stats_button = QPushButton("Stats History")
            self.main_window.word_cloud_btn = QPushButton("Word Cloud")
            self.main_window.download_button = QPushButton("Download Chat")
            self.main_window.analytics_button = QPushButton("Show Analytics")
            self.main_window.stop_button = QPushButton("Stop Chat")
            self.main_window.restart_button = QPushButton("Restart Chat")
            self.main_window.stats_button = QPushButton("Statistics")
            self.main_window.save_chat_button = QPushButton("Save Chat")
            self.main_window.view_saved_chats_button = QPushButton("View Chats")
            self.main_window.simulation_btn = QPushButton("Simulation")
            
            button_layout.addWidget(self.main_window.save_chat_button)
            button_layout.addWidget(self.main_window.view_saved_chats_button)
            button_layout.addWidget(self.main_window.analytics_button)
            button_layout.addWidget(self.main_window.historical_stats_button)
            button_layout.addWidget(self.main_window.stats_button)
            button_layout.addWidget(self.main_window.word_cloud_btn)
            button_layout.addWidget(self.main_window.simulation_btn)
            button_layout.addWidget(self.main_window.restart_button)
            button_layout.addWidget(self.main_window.stop_button)
            button_layout.addWidget(self.main_window.download_button)

            main_layout.addLayout(top_layout)
            main_layout.addWidget(self.main_window.chat_display)
            main_layout.addLayout(input_layout)
            main_layout.addLayout(button_layout)

            main_widget.setLayout(main_layout)
            self.main_window.setCentralWidget(main_widget)

            self.main_window.status_bar = QStatusBar(self.main_window)
            self.main_window.status_message = QLabel(self.main_window)
            self.main_window.progress_bar = QProgressBar(self.main_window)
            self.main_window.progress_bar.setMaximumHeight(self.main_window.status_bar.fontMetrics().height())
            self.main_window.progress_bar.setVisible(False)
            self.main_window.status_widget = QWidget(self.main_window)
            self.main_window.status_layout = QHBoxLayout(self.main_window.status_widget)
            self.main_window.status_layout.addWidget(self.main_window.status_message)
            self.main_window.status_layout.addWidget(self.main_window.progress_bar)
            self.main_window.status_bar.addPermanentWidget(self.main_window.status_widget)
            self.main_window.info_label = QLabel(self.main_window)
            self.main_window.status_bar.addPermanentWidget(self.main_window.info_label)
            self.main_window.setStatusBar(self.main_window.status_bar)

            logger.info("UI initialized successfully.")
        except Exception as e:
            logger.error(f"Error initializing UI in ui_component.py: {e}", exc_info=True)


# for later...

        # self.create_toolbars()

        # self.stats_dialog = None
        # self.toolbar = self.addToolBar("Interaction")

        # undo_action.triggered.connect(self.text_editor.undo)
        # self.new_button.triggered.connect(self.new_file)
        # self.open_button.triggered.connect(self.open_file)
        # self.save_button.triggered.connect(self.save_file)
        # redo_action.triggered.connect(self.text_editor.redo)
        # self.stats_button.triggered.connect(self.show_statistics)
        # self.settings_button.triggered.connect(self.open_settings)
        # self.help_button.triggered.connect(self.open_help)

        # self.toolbar.addAction(self.new_button)
        # self.toolbar.addAction(self.open_button)
        # self.toolbar.addAction(self.save_button)
        # self.toolbar.addAction(undo_action)
        # self.toolbar.addAction(redo_action)
        # self.toolbar.addAction(self.stats_button)
        # self.toolbar.addAction(self.settings_button)
        # self.toolbar.addAction(self.help_button)
        
        # redo_action = QAction("Redo", self)
        # self.settings_button = QAction("Settings", self)
        # self.new_button = QAction("New", self)
        # self.open_button = QAction("Open", self)
        # self.save_button = QAction("Save", self)
        # self.stats_button = QAction("Statistics", self)
        # self.help_button = QAction("Help", self)
        # undo_action = QAction("Undo", self)
        

        

