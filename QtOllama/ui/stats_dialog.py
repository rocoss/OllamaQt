from PyQt6.QtWidgets import QDialog, QVBoxLayout, QTableWidget, QTableWidgetItem, QLabel
import json
import os
from datetime import datetime
from QtOllama.utility.logger_setup import create_logger

logger = create_logger(__name__)

class HistoricalStatsDialog(QDialog):
    """
    A dialog window that displays historical statistics in a table format.
    Attributes:
        label (QLabel): A label to display instructions.
        table (QTableWidget): A table to display the historical stats.
    Methods:
        __init__(parent=None):
            Initializes the HistoricalStatsDialog with a title, size, and layout.
        load_stats():
            Loads the historical stats from a JSON file and populates the table.
    """
    def __init__(self, parent=None):
        """
        Initializes the StatsDialog.
        Args:
            parent (QWidget, optional): The parent widget. Defaults to None.
        Sets up the dialog window with a title, size, and layout. Adds a label for instructions
        and a table to display historical statistics. Loads and displays the stats upon initialization.
        """
        try:
            super().__init__(parent)
            self.setWindowTitle("Historical Stats")
            self.resize(400, 600)
            layout = QVBoxLayout()
            
            # Label for instructions
            self.label = QLabel("Showing historical stats over time:", self)
            layout.addWidget(self.label)
            
            # Table to display the stats
            self.table = QTableWidget(0, 3)
            self.table.setHorizontalHeaderLabels(["Timestamp", "Statistic", "Value"])
            layout.addWidget(self.table)
            
            self.setLayout(layout)
            
            # Load and display stats
            self.load_stats()
        except Exception as e:
            logger.error(f"Error constructing HistoricalStatsDialog: {e}", exc_info=True)
    
    def load_stats(self):
        """
        Load and display historical statistics from a JSON file.
        This method reads historical statistics from a JSON file named 
        'historical_stats.json'. If the file does not exist, it updates 
        the label to indicate that no historical stats are available. 
        Otherwise, it populates a table with the historical stats, where 
        each entry includes a timestamp and associated key-value pairs.
        The table is updated with each entry's timestamp, key, and value.
        Raises:
            json.JSONDecodeError: If the JSON file contains invalid JSON.
            OSError: If there is an issue opening or reading the file.
        """
        stats_file = "historical_stats.json"
        if not os.path.exists(stats_file):
            self.label.setText("No historical stats available yet.")
            logger.warning(f"Stats file {stats_file} does not exist.")
            return
        
        try:
            with open(stats_file, "r") as f:
                historical_stats = json.load(f)
            
            # Populate the table with the historical stats
            for entry in historical_stats:
                timestamp = entry.get("timestamp", "Unknown Time")
                for key, value in entry.items():
                    if key != "timestamp":
                        row = self.table.rowCount()
                        self.table.insertRow(row)
                        self.table.setItem(row, 0, QTableWidgetItem(timestamp))
                        self.table.setItem(row, 1, QTableWidgetItem(key))
                        self.table.setItem(row, 2, QTableWidgetItem(str(value)))
        except json.JSONDecodeError as e:
            self.label.setText("Error loading stats: Invalid JSON format.")
            logger.error(f"JSONDecodeError while loading stats from {stats_file}: {e}", exc_info=True)
        except OSError as e:
            self.label.setText("Error loading stats: Unable to read file.")
            logger.error(f"OSError while reading stats file {stats_file}: {e}", exc_info=True)
        except Exception as e:
            self.label.setText("Error loading stats: An unexpected error occurred.")
            logger.error(f"Unexpected error while loading stats: {e}", exc_info=True)
