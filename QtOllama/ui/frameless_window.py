from PyQt6.QtWidgets import QMainWindow, QApplication, QGraphicsDropShadowEffect
from PyQt6.QtCore import Qt, QRectF
from PyQt6.QtGui import QPainter, QPainterPath, QRegion, QMouseEvent, QResizeEvent, QColor
from QtOllama.utility.logger_setup import create_logger
logger = create_logger(__name__)


class FramelessWindow(QMainWindow):
    """
    Initializes the FramelessWindow instance.

    This constructor sets up the initial state of the frameless window,
    including setting window flags and attributes for a translucent background.

    Attributes:
        startPos (QPoint or None): The starting position of the window drag.
        pressing (bool): A flag indicating whether the window is being dragged.
    """
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.startPos = None
        self.pressing = False

        # Adding a shadow effect
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(20)
        shadow.setColor(QColor(0, 0, 0, 180))
        shadow.setOffset(0, 0)
        self.setGraphicsEffect(shadow)

    def mousePressEvent(self, event: QMouseEvent) -> None:
        """
        Handles the mouse press event for the frameless window.

        This method is triggered when a mouse button is pressed within the window.
        It checks if the left mouse button is pressed and, if so, sets the `pressing`
        attribute to True and records the starting position of the mouse press.

        Args:
            event (QMouseEvent): The mouse event containing information about the mouse press.

        Raises:
            Exception: Logs any exceptions that occur during the execution of the method.
        """
        try:
            if event.button() == Qt.MouseButton.LeftButton:
                self.pressing = True
                self.startPos = event.position().toPoint()
        except Exception as e:
            logger.error(f"Error in mousePressEvent: {e}", exc_info=True)

    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        """
        Handles the mouse move event for a frameless window.

        This method is triggered when the mouse is moved. If the window is being 
        dragged (indicated by `self.pressing`), it updates the window's position 
        based on the current mouse position.

        Args:
            event (QMouseEvent): The mouse event containing information about the 
                                 mouse movement.

        Raises:
            Exception: Logs any exceptions that occur during the execution of the 
                       method.
        """
        try:
            if self.pressing and self.startPos is not None:
                self.move(self.pos() + event.position().toPoint() - self.startPos)
        except Exception as e:
            logger.error(f"Error in mouseMoveEvent: {e}", exc_info=True)

    def mouseReleaseEvent(self, event: QMouseEvent) -> None:
        """
        Handles the mouse release event for the frameless window.

        This method is triggered when a mouse button is released. If the left mouse button
        is released, it sets the `pressing` attribute to False.

        Args:
            event (QMouseEvent): The mouse event containing information about the button released.

        Raises:
            Exception: Logs any exception that occurs during the execution of the method.
        """
        try:
            if event.button() == Qt.MouseButton.LeftButton:
                self.pressing = False
        except Exception as e:
            logger.error(f"error occurred mouseReleaseEvent: {e}", exc_info=True)

    def resizeEvent(self, event: QResizeEvent):
        """
        Handles the resize event for the frameless window.

        This method is called whenever the window is resized. It creates a rounded rectangle
        path with a corner radius of 10.0 and sets it as the mask for the window, giving it
        rounded corners. If an error occurs during this process, it logs the error.

        Args:
            event (QResizeEvent): The resize event object containing information about the resize event.

        Raises:
            Exception: If an error occurs during the creation of the rounded rectangle path or setting the mask.
        """
        try:
            path = QPainterPath()
            path.addRoundedRect(QRectF(self.rect()), 10.0, 10.0)

            # Create a QRegion from the QPainterPath
            region = QRegion(path.toFillPolygon().toPolygon())
            self.setMask(region)
        except Exception as e:
            logger.error(f"error occurred resizeEvent: {e}", exc_info=True)


if __name__ == "__main__":
    try:
        app = QApplication([])
        window = FramelessWindow()
        window.show()
        app.exec()
    except Exception as e:
        logger.exception("Error in main: %s", str(e))
