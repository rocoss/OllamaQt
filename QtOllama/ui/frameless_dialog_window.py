from PyQt6.QtWidgets import QDialog
from PyQt6.QtCore import Qt, QRectF
from PyQt6.QtGui import QPainter, QPainterPath, QRegion, QMouseEvent, QResizeEvent
from QtOllama.utility.logger_setup import create_logger
logger = create_logger(__name__)


class FramelessDialog(QDialog):
    """
    A custom QDialog that provides a frameless window with rounded corners and drag functionality.

    Attributes:
        startPos (QPoint): The starting position of the mouse when dragging begins.
        pressing (bool): A flag indicating whether the left mouse button is being pressed.

    Methods:
        __init__(parent=None):
            Initializes the FramelessDialog with optional parent widget.
        
        mousePressEvent(event: QMouseEvent) -> None:
            Handles the mouse press event to initiate dragging.
        
        mouseMoveEvent(event: QMouseEvent) -> None:
            Handles the mouse move event to update the dialog's position while dragging.
        
        mouseReleaseEvent(event: QMouseEvent) -> None:
            Handles the mouse release event to stop dragging.
        
        resizeEvent(event: QResizeEvent):
            Handles the resize event to apply rounded corners to the dialog.
    """
    def __init__(self, parent=None):
        """
        Initializes the FramelessDialogWindow.

        Args:
            parent (QWidget, optional): The parent widget of this dialog window. Defaults to None.

        Attributes:
            startPos (QPoint or None): The starting position of the window when dragging.
            pressing (bool): Indicates whether the window is currently being dragged.
        """
        super().__init__(parent)
        self.startPos = None
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.Dialog)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.pressing = False

    def mousePressEvent(self, event: QMouseEvent) -> None:
        """
        Handles the mouse press event.

        This method is triggered when a mouse button is pressed within the widget.
        It checks if the left mouse button is pressed and, if so, sets the `pressing`
        attribute to True and records the starting position of the mouse press.

        Args:
            event (QMouseEvent): The mouse event containing information about the mouse press.

        Raises:
            Exception: If an error occurs during the execution of the method, it is logged.
        """
        try:
            if event.button() == Qt.MouseButton.LeftButton:
                self.pressing = True
                self.startPos = event.position().toPoint()
        except Exception as e:
            logger.error(f"Error in mousePressEvent: {e}", exc_info=True)

    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        """
        Handles the mouse move event for the frameless dialog window.

        This method is triggered when the mouse is moved. If the mouse is being pressed
        and the starting position is not None, it moves the window to follow the mouse
        cursor.

        Args:
            event (QMouseEvent): The mouse event containing information about the mouse movement.

        Raises:
            Exception: Logs any exceptions that occur during the execution of the method.
        """
        try:
            if self.pressing and self.startPos is not None:
                self.move(self.pos() + event.position().toPoint() - self.startPos)
        except Exception as e:
            logger.error(f"Error in mouseMoveEvent: {e}", exc_info=True)

    def mouseReleaseEvent(self, event: QMouseEvent) -> None:
        """
        Handles the mouse release event.

        This method is triggered when a mouse button is released. If the left mouse button
        is released, it sets the `pressing` attribute to False. If an exception occurs,
        it logs the error with detailed exception information.

        Args:
            event (QMouseEvent): The mouse event that triggered this method.

        Raises:
            Exception: If an error occurs during the execution of the method, it is caught
                       and logged.
        """
        try:
            if event.button() == Qt.MouseButton.LeftButton:
                self.pressing = False
        except Exception as e:
            logger.error(f"error occurred mouseReleaseEvent: {e}", exc_info=True)

    def resizeEvent(self, event: QResizeEvent):
        """
        Handles the resize event for the frameless dialog window.

        This method is called whenever the window is resized. It creates a rounded
        rectangle path with a corner radius of 10.0 and sets this path as the mask
        for the window, giving it rounded corners. If an error occurs during this
        process, it logs the error.

        Args:
            event (QResizeEvent): The resize event object containing information
                                  about the resize event.
        """
        try:
            path = QPainterPath()
            path.addRoundedRect(QRectF(self.rect()), 10.0, 10.0)

            region = QRegion(path.toFillPolygon().toPolygon())
            self.setMask(region)
        except Exception as e:
            logger.error(f"Error in resizeEvent: {e}", exc_info=True)
