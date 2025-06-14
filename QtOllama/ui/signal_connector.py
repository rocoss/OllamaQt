from QtOllama.utility.logger_setup import create_logger

logger = create_logger(__name__)


class SignalConnector:
    """
    SignalConnector is a class responsible for connecting UI signals to their respective slots in the main window.
    Attributes:
        main_window (QMainWindow): The main window instance containing the UI elements.
    Methods:
        __init__(main_window):
            Initializes the SignalConnector with the given main window.
        connect_signals():
            Connects the signals from the main window's UI elements to their corresponding slots.
            - stats_button.clicked -> show_statistics
            - send_button.clicked -> send_message
            - download_button.clicked -> download_chat
            - analytics_button.clicked -> show_analytics
            - stop_button.clicked -> stop_chat
            - restart_button.clicked -> restart_chat
            - input_field.returnPressed -> send_message
            - word_cloud_btn.clicked -> open_word_cloud
            - historical_stats_button.clicked -> view_historical_stats
            - view_saved_chats_button.clicked -> view_saved_chats
            - save_chat_button.clicked -> save_chat_to_history
            - simulation_btn.clicked -> start_simulation
    """
    def __init__(self, main_window):
        """
        Initializes the SignalConnector with the given main window.

        Args:
            main_window (QMainWindow): The main window instance to which signals will be connected.
        """
        self.main_window = main_window

    def connect_signals(self):
        """
        Connects the signals (events) from the main window's UI elements to their corresponding handler methods.

        This method sets up the following connections:
        - stats_button: Connects to show_statistics method.
        - send_button: Connects to send_message method.
        - download_button: Connects to download_chat method.
        - analytics_button: Connects to show_analytics method.
        - stop_button: Connects to stop_chat method.
        - restart_button: Connects to restart_chat method.
        - input_field (on return pressed): Connects to send_message method.
        - word_cloud_btn: Connects to open_word_cloud method.
        - historical_stats_button: Connects to view_historical_stats method.
        - view_saved_chats_button: Connects to view_saved_chats method.
        - save_chat_button: Connects to save_chat_to_history method.
        - simulation_btn: Connects to start_simulation method.
        """
        try:
            self.main_window.stats_button.clicked.connect(self.main_window.show_statistics)
            logger.info("Connected stats_button to show_statistics")

            self.main_window.send_button.clicked.connect(self.main_window.send_message)
            logger.info("Connected send_button to send_message")

            self.main_window.download_button.clicked.connect(self.main_window.download_chat)
            logger.info("Connected download_button to download_chat")

            self.main_window.analytics_button.clicked.connect(self.main_window.show_analytics)
            logger.info("Connected analytics_button to show_analytics")

            self.main_window.stop_button.clicked.connect(self.main_window.stop_chat)
            logger.info("Connected stop_button to stop_chat")

            self.main_window.restart_button.clicked.connect(self.main_window.restart_chat)
            logger.info("Connected restart_button to restart_chat")

            self.main_window.input_field.returnPressed.connect(self.main_window.send_message)
            logger.info("Connected input_field returnPressed to send_message")

            self.main_window.word_cloud_btn.clicked.connect(self.main_window.open_word_cloud)
            logger.info("Connected word_cloud_btn to open_word_cloud")

            self.main_window.historical_stats_button.clicked.connect(self.main_window.view_historical_stats)
            logger.info("Connected historical_stats_button to view_historical_stats")

            self.main_window.view_saved_chats_button.clicked.connect(self.main_window.view_saved_chats)
            logger.info("Connected view_saved_chats_button to view_saved_chats")

            self.main_window.save_chat_button.clicked.connect(self.main_window.save_chat_to_history)
            logger.info("Connected save_chat_button to save_chat_to_history")

            self.main_window.simulation_btn.clicked.connect(self.main_window.start_simulation)
            logger.info("Connected simulation_btn to start_simulation")

        except AttributeError as e:
            logger.error(f"AttributeError while connecting signals: {e}")
        except Exception as e:
            logger.error(f"Unexpected error while connecting signals: {e}")
