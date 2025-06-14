from QtOllama.utility.logger_setup import create_logger
logger = create_logger(__name__)


class Interpretations:
    """
    The Interpretations class provides static methods to interpret various scores and metrics related to sentiment analysis and readability.

    Methods:
        sentiment_polartiy_interpretation(sentiment_polarity: float) -> str:
            Interprets the sentiment polarity score and returns a string description of the sentiment.

        sentiment_subjectivity_interpretation(sentiment_subjectivity: float) -> str:
            Interprets the sentiment subjectivity score and returns a string description of the subjectivity.

        flesch_reading_ease_interpretation(score: float) -> str:
            Interprets the Flesch Reading Ease score and returns a string description of the readability level.

        flesch_kincaid_grade_interpretation(score: float) -> str:
            Interprets the Flesch-Kincaid Grade Level score and returns a string description of the grade level.

        gunning_fog_index_interpretation(score: float) -> str:
            Interprets the Gunning Fog Index score and returns a string description of the education level required to understand the text.

        coleman_liau_index_interpretation(score: float) -> str:
            Interprets the Coleman-Liau Index score and returns a string description of the education level required to understand the text.
    """
    @staticmethod
    def sentiment_polartiy_interpretation(sentiment_polarity):
        """
        Interpret the sentiment polarity score and return a corresponding sentiment description.

        Parameters:
        sentiment_polarity (float): A float value representing the sentiment polarity score, 
                                    ranging from -1 (very strongly negative) to 1 (very strongly positive).

        Returns:
        str: A string describing the sentiment based on the given polarity score. Possible values are:
             - "Very Strongly Negative"
             - "Strongly Negative"
             - "Moderately Negative"
             - "Slightly Negative"
             - "Barely Negative"
             - "Neutral"
             - "Barely Positive"
             - "Slightly Positive"
             - "Moderately Positive"
             - "Strongly Positive"
             - "Very Strongly Positive"
        """
        if -1 <= sentiment_polarity < -0.8:
            sentiment = "Very Strongly Negative"
        elif -0.8 <= sentiment_polarity < -0.6:
            sentiment = "Strongly Negative"
        elif -0.6 <= sentiment_polarity < -0.4:
            sentiment = "Moderately Negative"
        elif -0.4 <= sentiment_polarity < -0.2:
            sentiment = "Slightly Negative"
        elif -0.2 <= sentiment_polarity < -0.1:
            sentiment = "Barely Negative"
        elif -0.1 <= sentiment_polarity < 0.1:
            sentiment = "Neutral"
        elif 0.1 <= sentiment_polarity < 0.2:
            sentiment = "Barely Positive"
        elif 0.2 <= sentiment_polarity < 0.4:
            sentiment = "Slightly Positive"
        elif 0.4 <= sentiment_polarity < 0.6:
            sentiment = "Moderately Positive"
        elif 0.6 <= sentiment_polarity < 0.8:
            sentiment = "Strongly Positive"
        else:
            sentiment = "Very Strongly Positive"

        return sentiment

    @staticmethod
    def sentiment_subjectivity_interpretation(sentiment_subjectivity):
        """
        Interpret the sentiment subjectivity score and return a descriptive string.

        Parameters:
        sentiment_subjectivity (float): A float value between 0 and 1 representing the subjectivity of the sentiment.

        Returns:
        str: A string describing the level of subjectivity:
            - "Extremely Objective" for scores between 0 and 0.15 (inclusive of 0, exclusive of 0.15)
            - "Very Objective" for scores between 0.15 and 0.35 (inclusive of 0.15, exclusive of 0.35)
            - "Somewhat Objective" for scores between 0.35 and 0.5 (inclusive of 0.35, exclusive of 0.5)
            - "Moderately Subjective" for scores between 0.5 and 0.65 (inclusive of 0.5, exclusive of 0.65)
            - "Somewhat Subjective" for scores between 0.65 and 0.85 (inclusive of 0.65, exclusive of 0.85)
            - "Very Subjective" for scores between 0.85 and 1 (inclusive of 0.85 and 1)
            - "Invalid score" for any score outside the range of 0 to 1
        """
        if 0 <= sentiment_subjectivity < 0.15:
            subjectivity = "Extremely Objective"
        elif 0.15 <= sentiment_subjectivity < 0.35:
            subjectivity = "Very Objective"
        elif 0.35 <= sentiment_subjectivity < 0.5:
            subjectivity = "Somewhat Objective"
        elif 0.5 <= sentiment_subjectivity < 0.65:
            subjectivity = "Moderately Subjective"
        elif 0.65 <= sentiment_subjectivity < 0.85:
            subjectivity = "Somewhat Subjective"
        elif 0.85 <= sentiment_subjectivity <= 1:
            subjectivity = "Very Subjective"
        else:
            subjectivity = "Invalid score"

        return subjectivity

    @staticmethod
    def flesch_reading_ease_interpretation(score):
        """
        Interprets the Flesch Reading Ease score.

        Parameters:
        score (float): The Flesch Reading Ease score to interpret.

        Returns:
        str: A string interpretation of the Flesch Reading Ease score.
            - "Extremely Difficult" for scores less than 0
            - "Very Difficult" for scores between 0 and 9
            - "Significantly Difficult" for scores between 10 and 19
            - "Difficult" for scores between 20 and 29
            - "Moderately Difficult" for scores between 30 and 39
            - "Medium" for scores between 40 and 44
            - "Slightly Above Medium" for scores between 45 and 49
            - "Medium" for scores between 50 and 54
            - "Balanced" for scores between 55 and 59
            - "Slightly Below Medium" for scores between 60 and 64
            - "Moderately Easy" for scores between 65 and 69
            - "Easy" for scores between 70 and 74
            - "Significantly Easy" for scores between 75 and 79
            - "Very Easy" for scores between 80 and 84
            - "Close To Minimal" for scores between 85 and 89
            - "Minimal" for scores between 90 and 94
            - "Almost Negligible" for scores between 95 and 100
            - "Uniform" for scores greater than 100
        """
        if score < 0:
            return "Extremely Difficult"
        elif 0 <= score < 10:
            return "Very Difficult"
        elif 10 <= score < 20:
            return "Significantly Difficult"
        elif 20 <= score < 30:
            return "Difficult"
        elif 30 <= score < 40:
            return "Moderately Difficult"
        elif 40 <= score < 45:
            return "Medium"
        elif 45 <= score < 50:
            return "Slightly Above Medium"
        elif 50 <= score < 55:
            return "Medium"
        elif 55 <= score < 60:
            return "Balanced"
        elif 60 <= score < 65:
            return "Slightly Below Medium"
        elif 65 <= score < 70:
            return "Moderately Easy"
        elif 70 <= score < 75:
            return "Easy"
        elif 75 <= score < 80:
            return "Significantly Easy"
        elif 80 <= score < 85:
            return "Very Easy"
        elif 85 <= score < 90:
            return "Close To Minimal"
        elif 90 <= score < 95:
            return "Minimal"
        elif 95 <= score <= 100:
            return "Almost Negligible"
        else:
            return "Uniform"

    @staticmethod
    def flesch_kincaid_grade_interpretation(score):
        """
        Interpret the Flesch-Kincaid grade level score.

        This function takes a Flesch-Kincaid grade level score and returns a string
        representing the corresponding educational grade level.

        Parameters:
        score (float): The Flesch-Kincaid grade level score.

        Returns:
        str: A string representing the educational grade level corresponding to the score.
             Possible return values are:
             - "Kindergarten"
             - "First/Second Grade"
             - "Third Grade"
             - "Fourth Grade"
             - "Fifth Grade"
             - "Sixth Grade"
             - "Seventh Grade"
             - "Eighth Grade"
             - "Ninth Grade"
             - "Tenth Grade"
             - "Eleventh Grade"
             - "Twelfth Grade"
             - "College student"
             - "Professor"
        """
        if score <= 1:
            return "Kindergarten"
        elif score <= 2:
            return "First/Second Grade"
        elif score <= 3:
            return "Third Grade"
        elif score <= 4:
            return "Fourth Grade"
        elif score <= 5:
            return "Fifth Grade"
        elif score <= 6:
            return "Sixth Grade"
        elif score <= 7:
            return "Seventh Grade"
        elif score <= 8:
            return "Eighth Grade"
        elif score <= 9:
            return "Ninth Grade"
        elif score <= 10:
            return "Tenth Grade"
        elif score <= 11:
            return "Eleventh Grade"
        elif score <= 12:
            return "Twelfth Grade"
        elif score <= 13:
            return "College student"
        elif score > 13:
            return "Professor"

    @staticmethod
    def gunning_fog_index_interpretation(score):
        """
        Interpret the Gunning Fog Index score.

        The Gunning Fog Index is a readability test that estimates the years of formal education
        needed to understand a text on the first reading. This function interprets the score
        and returns the corresponding education level.

        Parameters:
        score (float): The Gunning Fog Index score.

        Returns:
        str: The education level corresponding to the given score.
            - "Elementary school" for scores <= 6
            - "Middle school" for scores <= 8
            - "High school" for scores <= 12
            - "College student" for scores <= 16
            - "College graduate" for scores > 16
        """
        if score <= 6:
            return "Elementary school"
        elif score <= 8:
            return "Middle school"
        elif score <= 12:
            return "High school"
        elif score <= 16:
            return "College student"
        elif score > 16:
            return "College graduate"

    @staticmethod
    def coleman_liau_index_interpretation(score):
        """
        Interprets the Coleman-Liau index score and returns the corresponding education level.

        Parameters:
        score (int or float): The Coleman-Liau index score.

        Returns:
        str: A string representing the education level corresponding to the given score.
             Possible return values are:
             - "Elementary school" for scores <= 6
             - "Middle school" for scores <= 8
             - "High school" for scores <= 12
             - "College student" for scores <= 16
             - "College graduate" for scores > 16
        """
        if score <= 6:
            return "Elementary school"
        elif score <= 8:
            return "Middle school"
        elif score <= 12:
            return "High school"
        elif score <= 16:
            return "College student"
        elif score > 16:
            return "College graduate"
