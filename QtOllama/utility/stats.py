import os
import json
import textstat as textstat
from PyQt6.QtCore import QTimer, Qt
from PyQt6.QtWidgets import QDialog, \
    QTextEdit, \
    QVBoxLayout, \
    QTableWidget, \
    QTableWidgetItem, \
    QHeaderView
from nltk import word_tokenize
from textblob import TextBlob
from datetime import datetime
from QtOllama.utility.interpretations import Interpretations
from QtOllama.utility.logger_setup import create_logger
logger = create_logger(__name__)


class StatsDialog(QDialog):
    """
    A dialog window that displays real-time text statistics for a given QTextEdit widget.
    Attributes:
        text_edit_widget (QTextEdit): The text edit widget whose statistics are to be displayed.
        timer (QTimer): A timer to periodically update the statistics.
        table (QTableWidget): A table widget to display the statistics.
    Methods:
        __init__(text_edit_widget: QTextEdit, parent=None):
            Initializes the StatsDialog with the given QTextEdit widget and optional parent.
        update_statistics():
            Updates the statistics displayed in the table based on the current text in the text_edit_widget.
        save_stats():
            Saves the current statistics to a JSON file with a timestamp.
        closeEvent(event):
            Handles the close event by saving the current statistics before closing the dialog.
    """
    def __init__(self, text_edit_widget: QTextEdit, parent=None):
        """
        Initializes the statistics window for real-time text statistics.
        Args:
            text_edit_widget (QTextEdit): The text edit widget to monitor.
            parent (QWidget, optional): The parent widget. Defaults to None.
        Attributes:
            text_edit_widget (QTextEdit): The text edit widget to monitor.
            table (QTableWidget): The table widget to display statistics.
            timer (QTimer): Timer to update statistics every second.
        """
        super().__init__(parent)
        
        self.text_edit_widget = text_edit_widget
        
        self.setWindowTitle("Real-Time Text Statistics")
        
        # set window size
        self.resize(800, 760)
        
        # create layout
        layout = QVBoxLayout()
        
        # create tableWidget to display stats
        self.table = QTableWidget(0, 3)
        self.table.setHorizontalHeaderLabels(["Statistic", "Raw Value", "Interpretation"])
        self.table.verticalHeader().setVisible(False)
        
        # add tableWidget to the layout
        layout.addWidget(self.table)
        
        # set the layout to the layout which was the QVBoxLayout, fun right? :D
        self.setLayout(layout)
        
        # does things I need to ask about cause I didn't make this part of the app I'm modding it
        # but I assume it's an auto time to update the statistics
        # I wish the op developer would've maybe(I PROLLY DELETED THEM ACTUALLY) been more clear?
        # but I admire the fuck out of them anyways so yeah FUCK ME for derping here,
        # todo better comment here :D
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_statistics)
        self.timer.start(1000)
    
    def update_statistics(self):
        """
        Updates the statistics of the text present in the text edit widget.
        This method calculates various statistics and readability scores for the text present in the 
        text edit widget and updates a table with these values. The statistics include token counts, 
        lexical diversity, character counts, syllable counts, sentence counts, readability scores, 
        sentiment analysis, and more.
        The following statistics are calculated and displayed:
        - Characters: Total number of characters in the text.
        - Letters: Total number of letters in the text, ignoring spaces.
        - Words: Total number of words in the text.
        - Unique words: Total number of unique words in the text.
        - Difficult Words: Total number of difficult words in the text.
        - Syllables: Total number of syllables in the text.
        - Mono Syllables: Total number of monosyllabic words in the text.
        - Poly Syllables: Total number of polysyllabic words in the text.
        - Sentences: Total number of sentences in the text.
        - Lines: Total number of lines in the text.
        - Paragraphs: Total number of paragraphs in the text.
        - Total tokens: Total number of tokens in the text.
        - Unique tokens: Total number of unique tokens in the text.
        - Lexical diversity: Ratio of unique tokens to total tokens.
        - Sentiment Polarity: Sentiment polarity score of the text.
        - Sentiment Subjectivity: Sentiment subjectivity score of the text.
        - Flesch Reading Ease: Flesch Reading Ease score of the text.
        - Flesch-Kincaid Grade Level: Flesch-Kincaid Grade Level score of the text.
        - Smog Index: SMOG index of the text.
        - Gunning Fog: Gunning Fog index of the text.
        - Automated Readability Index: Automated Readability Index of the text.
        - Text Standards: Text standard score of the text.
        - Spache Readability Formula: Spache Readability Formula score of the text.
        - McAlpine EFLAW Readability Score: McAlpine EFLAW Readability Score of the text.
        - Dale-Chall Readability Score: Dale-Chall Readability Score of the text.
        - Linsear Write Formula: Linsear Write Formula score of the text.
        - Coleman-Liau Index: Coleman-Liau Index of the text.
        - Estimated Reading Time (minutes): Estimated reading time for the text.
        The method updates a table with these statistics, where each row represents a different 
        statistic, and the columns represent the statistic name, raw value, and interpretation (if 
        applicable).
        """
        
        # grabbing the text from the textWidget // chat_window so that them sexy stats can sassy on
        text = self.text_edit_widget.toPlainText()
        
        # how many tokens in the text?
        tokens = word_tokenize(text)
        total_tokens = len(tokens)
        unique_tokens = len(set(tokens))
        # todo ask coco or chatty for help with a better explanation here
        lexical_diversity = unique_tokens / total_tokens if total_tokens > 0 else 0
        # basic MS WORD stats :D
        characters = len(text)
        letters = textstat.letter_count(text, ignore_spaces=True)
        words = textstat.lexicon_count(text)
        sentences = textstat.sentence_count(text)
        syllables = textstat.syllable_count(text)
        lines = text.count("\n") + 1 if text else 0
        # Returns the Flesch-Kincaid Grade of the given text. This is a grade formula in that a
        # score of 9.3 means that a ninth grader would be able to read the document.
        # https://en.wikipedia.org/wiki/Flesch–Kincaid_readability_tests#Flesch–Kincaid_grade_level
        flesch_reading_ease = textstat.flesch_reading_ease(text)
        reading_ease_interpretation = Interpretations.flesch_reading_ease_interpretation(
            flesch_reading_ease)
        flesch_kincaid_grade = textstat.flesch_kincaid_grade(text)
        flesch_kincaid_grade_interpretation = Interpretations.flesch_kincaid_grade_interpretation(
            flesch_kincaid_grade)
        
        # Returns the SMOG index of the given text. This is a grade formula in that a score of 9.3
        # means that a ninth grader would be able to read the document.
        # Texts of fewer than 30 sentences are statistically invalid, because the SMOG formula was
        # normed on 30-sentence samples. textstat requires at least 3 sentences for a result.
        # https://en.wikipedia.org/wiki/SMOG
        smog_index = textstat.smog_index(text)
        
        # Returns the FOG index of the given text. This is a grade formula in that a score of 9.3
        # means that a ninth grader would be able to read the document.
        # https://en.wikipedia.org/wiki/Gunning_fog_index
        gunning_fog = textstat.gunning_fog(text)
        gunning_fog_interpretation = Interpretations.gunning_fog_index_interpretation(gunning_fog)
        
        # Returns the ARI (Automated Readability Index) which outputs a number that approximates
        # the grade level needed to comprehend the text.
        # For example if the ARI is 6.5, then the grade level to comprehend the text is 6th to 7th
        # grade.
        # https://en.wikipedia.org/wiki/Automated_readability_index
        automated_readability_index = textstat.automated_readability_index(text)
        
        # Different from other tests, since it uses a lookup table of the most commonly used 3000
        # English words. Thus it returns the grade level using the New Dale-Chall Formula.
        # https://en.wikipedia.org/wiki/Dale–Chall_readability_formula
        dale_chall_readability_score = textstat.dale_chall_readability_score(text)
        difficult_words = textstat.difficult_words(text)
        spache_read = textstat.spache_readability(text)
        text_standards = textstat.text_standard(text, float_output=False)
        linsear_write_formula = textstat.linsear_write_formula(text)
        coleman_liau_index = textstat.coleman_liau_index(text)
        coleman_liau_index_interpretation = Interpretations.coleman_liau_index_interpretation(
            coleman_liau_index)
        reading_time = textstat.reading_time(text, ms_per_char=2)
        blob = TextBlob(text)
        sentiment_polarity = round(blob.sentiment.polarity, 2)
        sentiment_polarity_interpretation = Interpretations.sentiment_polartiy_interpretation(
            sentiment_polarity)
        sentiment_subjectivity = round(blob.sentiment.subjectivity, 2)
        sentiment_subjectivity_interpretation = Interpretations.sentiment_subjectivity_interpretation(
            sentiment_subjectivity)
        unique_words = len(set(word_tokenize(text)))
        mono_syl = textstat.monosyllabcount(text)
        poly_syl = textstat.polysyllabcount(text)
        mcalpine = textstat.mcalpine_eflaw(text)
        
        number_of_paragraphs = text.count("\n\n")
        
        stats = [
            ("Characters", characters, ""),
            ("Letters", letters, ""),
            ("Words", words, ""),
            ("Unique words", unique_words, ""),
            ("Difficult Words", difficult_words, ""),
            ("Syllables", syllables, ""),
            ("Mono Syllables", mono_syl, ""),
            ("Poly Syllables", poly_syl, ""),
            ("Sentences", sentences, ""),
            ("Lines", lines, ""),
            ("Paragraphs", number_of_paragraphs, ""),
            ("Total tokens", total_tokens, ""),
            ("Unique tokens", unique_tokens, ""),
            ("Lexical diversity", lexical_diversity, ""),
            ("Sentiment Polarity", sentiment_polarity, sentiment_polarity_interpretation),
            ("Sentiment Subjectivity", sentiment_subjectivity,
             sentiment_subjectivity_interpretation),
            ("Flesch Reading Ease", flesch_reading_ease, reading_ease_interpretation),
            ("Flesch-Kincaid Grade Level", flesch_kincaid_grade,
             flesch_kincaid_grade_interpretation),
            ("Smog Index", smog_index, ""),
            ("Gunning Fog", gunning_fog, gunning_fog_interpretation),
            ("Automated Readability Index", automated_readability_index, ""),
            ("Text Standards", text_standards, ""),
            ("Spache Readability Formula", spache_read, ""),
            ("McAlpine EFLAW Readability Score", mcalpine, ""),
            ("Dale-Chall Readability Score", dale_chall_readability_score, ""),
            ("Linsear Write Formula", linsear_write_formula, ""),
            ("Coleman-Liau Index", coleman_liau_index, coleman_liau_index_interpretation),
            ("Estimated Reading Time (minutes)", reading_time, ""),
            
        ]
        
        self.table.setRowCount(len(stats))
        for i, (stat_name, raw_value, interpretation) in enumerate(stats):
            self.table.setItem(i, 0, QTableWidgetItem(stat_name))
            self.table.setItem(i, 1, QTableWidgetItem(str(raw_value)))
            self.table.setItem(i, 2, QTableWidgetItem(interpretation))
        
        self.table.horizontalHeader().setSectionResizeMode(0,
                                                           QHeaderView.ResizeMode.ResizeToContents)
        self.table.horizontalHeader().setSectionResizeMode(1,
                                                           QHeaderView.ResizeMode.ResizeToContents)
        self.table.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeMode.Stretch)
    
    def save_stats(self):
        """
        Saves the current statistics from the table to a JSON file with a timestamp.
        This method collects all statistics from a table, adds a timestamp, and appends
        them to a historical list of stats stored in a JSON file. If the file does not
        exist, it creates a new one.
        The JSON file is named "historical_stats.json" and is located in the current
        working directory.
        Steps:
        1. Collects statistics from the table.
        2. Adds a timestamp to the collected statistics.
        3. Loads existing statistics from the JSON file if it exists.
        4. Appends the new statistics to the historical list.
        5. Saves the updated list back to the JSON file.
        Raises:
            IOError: If there is an error reading from or writing to the JSON file.
        Prints:
            A message indicating that the stats have been saved along with the timestamp.
        """
        # Define the filename where the stats will be saved
        stats_file = "./historical_stats.json"
        
        # Gather all the stats from the table
        stats = {}
        for row in range(self.table.rowCount()):
            stat_name = self.table.item(row, 0).text()
            raw_value = self.table.item(row, 1).text()
            stats[stat_name] = raw_value
        
        # Add a timestamp to the stats
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        stats["timestamp"] = timestamp
        
        # Load existing stats if the file exists
        if os.path.exists(stats_file):
            with open(stats_file, "r") as f:
                historical_stats = json.load(f)
        else:
            historical_stats = []
        
        # Append HammerAI-lama-3_1-storm-latest stats to the historical list
        historical_stats.append(stats)
        
        # Save the updated stats back to the file
        with open(stats_file, "w") as f:
            json.dump(historical_stats, f, indent=4)
        
        print(f"Stats saved at {timestamp}")
    
    def closeEvent(self, event):
        """
        Handles the close event for the window.

        This method is called when the window is about to be closed. It ensures
        that the current statistics are saved before the window is closed.

        Args:
            event (QCloseEvent): The close event that triggered this method.
        """
        self.save_stats()
        super().closeEvent(event)
