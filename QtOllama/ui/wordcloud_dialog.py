import sys
from PyQt6.QtWidgets import QDialog, QVBoxLayout, QPushButton, QLabel, QGraphicsView, QGraphicsScene
from PyQt6.QtGui import QPixmap
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from io import BytesIO
from .frameless_dialog_window import FramelessDialog
from .wrap_style import stylesheet



class WordCloudDialog(FramelessDialog, QDialog):
    """
    A dialog window for displaying and regenerating a word cloud based on the text from a given text editor widget.
    Attributes:
        text_edit_widget (QTextEdit): The text editor widget containing the text to generate the word cloud from.
        layout (QVBoxLayout): The main layout of the dialog.
        graphics_view (QGraphicsView): The view for displaying the word cloud.
        generate_button (QPushButton): The button to regenerate the word cloud.
    Methods:
        __init__(text_edit_widget, parent=None):
            Initializes the WordCloudDialog with the given text editor widget and optional parent widget.
        generate_word_cloud():
            Generates a word cloud from the text in the text editor widget and displays it in the graphics view.
    """
    
    def __init__(self, text_edit_widget, parent=None):
        """
        Initializes the WordCloudDialog.
        Args:
            text_edit_widget (QTextEdit): The text edit widget containing the text for the word cloud.
            parent (QWidget, optional): The parent widget. Defaults to None.
        Attributes:
            text_edit_widget (QTextEdit): Stores the reference to the text edit widget.
            layout (QVBoxLayout): The layout manager for the dialog.
            graphics_view (QGraphicsView): The view for displaying the word cloud.
            generate_button (QPushButton): The button to regenerate the word cloud.
        """
        super().__init__(parent)
        self.text_edit_widget = text_edit_widget
        self.setWindowTitle("Word Cloud")
        self.resize(600, 600)
        
        # Layout
        self.layout = QVBoxLayout(self)
        
        # Graphics view for displaying the word cloud
        self.graphics_view = QGraphicsView(self)
        self.layout.addWidget(self.graphics_view)
        
        # Button to regenerate word cloud
        self.generate_button = QPushButton("Regenerate Word Cloud", self)
        self.generate_button.clicked.connect(self.generate_word_cloud)
        self.layout.addWidget(self.generate_button)
        
        # Initial word cloud generation
        self.generate_word_cloud()
    
    def generate_word_cloud(self):
        """
        Generates a word cloud from the text in the text editor and displays it in the graphics view.
        This method performs the following steps:
        1. Retrieves text from the text editor widget.
        2. Generates a word cloud image using the retrieved text.
        3. Creates a matplotlib figure to display the word cloud.
        4. Saves the figure to a BytesIO object.
        5. Converts the saved image to a QPixmap.
        6. Updates the graphics view with the generated QPixmap.
        Note:
            This method assumes that the text editor widget is accessible via `self.text_edit_widget`
            and the graphics view is accessible via `self.graphics_view`.
        """
        try:
            # Get text from the text editor
            text = self.text_edit_widget.toPlainText()
            logger.debug("Retrieved text from text editor widget.")
            
            # Generate word cloud
            wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
            logger.debug("Generated word cloud.")
            
            # Create a matplotlib figure
            plt.figure(figsize=(8, 4))
            plt.imshow(wordcloud, interpolation='bilinear')
            plt.axis('off')
            
            # Save the figure to a BytesIO object
            buf = BytesIO()
            plt.savefig(buf, format='png')
            buf.seek(0)
            logger.debug("Saved word cloud to BytesIO object.")
            
            # Convert to QPixmap and display it
            pixmap = QPixmap()
            pixmap.loadFromData(buf.getvalue())
            buf.close()
            logger.debug("Converted word cloud to QPixmap.")
            
            # Update graphics view
            scene = QGraphicsScene(self)
            scene.addPixmap(pixmap)
            self.graphics_view.setScene(scene)
            logger.debug("Updated graphics view with new word cloud.")
            
            plt.close()
        except Exception as e:
            logger.error("Failed to generate word cloud: %s", e, exc_info=True)
