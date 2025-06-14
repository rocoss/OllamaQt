import sys

from PyQt6.QtWidgets import QApplication, QStyleFactory

from QtOllama.quilLlama import MainWindow
from QtOllama.ui.wrap_style import stylesheet
from QtOllama.utility.simulation import SimulationDialog


from QtOllama.utility.logger_setup import create_logger
logger = create_logger(__name__)


def run_app():
    try:
        app = QApplication(sys.argv)
        app.setStyleSheet(stylesheet)
        window = MainWindow()
        try:
            window.setStyle(QStyleFactory.create("Fusion"))
        except Exception as style_error:
            logger.error(f"{style_error}")
        window.show()
        sys.exit(app.exec())
    except Exception as main_error:
        logger.error(f"Critical error: {str(main_error)}")
        print(f"An error occurred: {str(main_error)}")


if __name__ == '__main__':
    run_app()
