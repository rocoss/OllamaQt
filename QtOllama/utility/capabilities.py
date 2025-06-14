from QtOllama.utility.logger_setup import create_logger
logger = create_logger(__name__)


class Capabilities:
    
    def analyze_journal(self):
        """
        Returns a list of a variety of ways to analyze my addiction journal
        so as to help with my addiction recovery research
        """
        pass
    
    def get_wefe_reports(self):
        """
        A way to discover what the scored of my wefe exam determine by way of looking
        through texts and matching the input with a score of 1-10 in the various
        domains
        :return:
        """
        pass
    
    def get_cspr_reports(self):
        pass
    
    def get_critical_analysis_types(self):
        """
        Returns a list of critical analysis types.

        This method provides a comprehensive list of various critical analysis
        methodologies that can be applied in literary and social studies. The 
        types of analysis include:

        - Ideology Analysis
        - Representation Analysis
        - Discourse Analysis
        - Power Relation Analysis
        - Value System Analysis
        - Social Construction Analysis
        - Binary Opposition Analysis
        - Multimodality Analysis
        - Narrative and Plot Structure Analysis
        - Literature Theory Application

        Returns:
            list: A list of strings, each representing a type of critical analysis.
        """
        return [
            "Ideology Analysis",
            "Representation Analysis",
            "Discourse Analysis",
            "Power Relation Analysis",
            "Value System Analysis",
            "Social Construction Analysis",
            "Binary Opposition Analysis",
            "Multimodality Analysis",
            "Narrative and Plot Structure Analysis",
            "Literature Theory Application",
        ]

    def get_psychoanalytical_analysis_types(self):
        """
        Retrieve a list of psychoanalytical analysis types.

        Returns:
            list: A list of strings, each representing a type of psychoanalytical analysis.
        """
        return [
            "Psychoanalytical Interpretation",
            "Unconscious Motives Analysis",
            "Symbolism Analysis",
            "Repression Analysis",
            "Psychosexual Stage Analysis",
            "Transference Analysis",
            "Oedipus Complex Detection",
            "Id, Ego, Superego Analysis",
            "Unconscious Fantasy Analysis",
            "Anxiety and Defense Mechanism Analysis",
        ]

    def get_scientific_analysis_types(self):
        """
        Returns a list of scientific analysis types.

        This method provides a predefined list of various types of scientific analyses 
        that can be performed. These types include checks for scientific validity, 
        fact checking, hypothesis analysis, detection of scientific terms, identification 
        of scientific laws, validation of scientific methods, analysis of observational 
        data, analysis of experimental procedures, interpretation of data, and application 
        of scientific theories.

        Returns:
            list: A list of strings, each representing a type of scientific analysis.
        """
        return [
            "Scientific Validity Check",
            "Fact Checking",
            "Hypothesis Analysis",
            "Scientific Term Detection",
            "Scientific Law Identification",
            "Scientific Method Validation",
            "Observational Data Analysis",
            "Experimental Procedure Analysis",
            "Data Interpretation",
            "Scientific Theory Application",
        ]

    def get_philosophical_analysis_types(self):
        """
        Returns a list of different types of philosophical analyses.

        The types of analyses include:
        - Philosophical Argument Analysis
        - Logic and Fallacy Check
        - Philosophical Concept Explanation
        - Philosophy Branch Identification
        - Philosophical Theory Application
        - Morality and Ethics Analysis
        - Metaphysical Claim Analysis
        - Epistemological Consideration Analysis
        - Existential Theme Evaluation
        - Thought Experiment Analysis

        Returns:
            list: A list of strings representing various philosophical analysis types.
        """
        return [
            "Philosophical Argument Analysis",
            "Logic and Fallacy Check",
            "Philosophical Concept Explanation",
            "Philosophy Branch Identification",
            "Philosophical Theory Application",
            "Morality and Ethics Analysis",
            "Metaphysical Claim Analysis",
            "Epistemological Consideration Analysis",
            "Existential Theme Evaluation",
            "Thought Experiment Analysis",
        ]

    def get_statistical_analysis_types(self):
        """
        Returns a list of statistical analysis types.

        This method provides a comprehensive list of various statistical analysis
        techniques that can be used for data analysis. The list includes:

        - Descriptive Statistics Analysis
        - Inferential Statistics Analysis
        - Hypothesis Testing
        - Data Distribution Analysis
        - Correlation Analysis
        - Regression Analysis
        - Statistical Significance Analysis
        - Causality Analysis
        - Statistical Anomaly Detection
        - Probability Analysis

        Returns:
            list: A list of strings, each representing a type of statistical analysis.
        """
        return [
            "Descriptive Statistics Analysis",
            "Inferential Statistics Analysis",
            "Hypothesis Testing",
            "Data Distribution Analysis",
            "Correlation Analysis",
            "Regression Analysis",
            "Statistical Significance Analysis",
            "Causality Analysis",
            "Statistical Anomaly Detection",
            "Probability Analysis",
        ]

    def get_prose_textual_transformation_types(self):
        """
        Returns a list of prose textual transformation types.

        The transformations include:
        - Condense the Text to a Shorter Version
        - Increase the Difficulty Level of the Text
        - Reduce the Difficulty Level of the Text
        - Expand the Short Text into a Detailed Version
        - Enrich the Text Semantically
        - Paraphrase the Text into Different Wording
        - Translate the Text into a Different Language
        - Summarize the Text
        - Transform the Text Structure to Improve Coherence
        - Increase the Verbose Level of the Text
        - Convert the Text to a Numbered List

        Returns:
            list: A list of strings representing different types of prose textual transformations.
        """
        return [
            "Condense the Text to a Shorter Version",
            "Increase the Difficulty Level of the Text",
            "Reduce the Difficulty Level of the Text",
            "Expand the Short Text into a Detailed Version",
            "Enrich the Text Semantically",
            "Paraphrase the Text into Different Wording",
            "Translate the Text into a Different Language",
            "Summarize the Text",
            "Transform the Text Structure to Improve Coherence",
            "Increase the Verbose Level of the Text",
            "Convert the Text to a Numbered List",
        ]

    def get_prose_semantic_transformation_types(self):
        """
        Retrieve a list of prose semantic transformation types.

        Returns:
            list: A list of strings representing different types of semantic transformations 
                  that can be applied to prose. The types include:
                  - "Semantic Mapping"
                  - "Semantics Alteration"
                  - "Semantic Paraphrasing"
                  - "Text-to-Concept Transformation"
                  - "Semantic-based Text Summarization"
                  - "Text Translation into Logical Forms"
                  - "Semantic Role Labeling Transformation"
        """
        return [
            "Semantic Mapping",
            "Semantics Alteration",
            "Semantic Paraphrasing",
            "Text-to-Concept Transformation",
            "Semantic-based Text Summarization",
            "Text Translation into Logical Forms",
            "Semantic Role Labeling Transformation",
        ]

    def get_prose_cognitive_transformation_types(self):
        """
        Retrieve a list of prose cognitive transformation types.

        Returns:
            list: A list of strings representing different types of cognitive transformations 
                  that can be applied to prose, including:
                  - "Cognitive Reimplementations"
                  - "Cognitive Insights Structuring"
                  - "Cognitive Bias Removal"
                  - "Text Simplification for Cognitive Load"
                  - "Cognitive Discourse Analysis"
                  - "Ideation to Text Generation"
                  - "Mental Model Text Adaptation"
        """
        return [
            "Cognitive Reimplementations",
            "Cognitive Insights Structuring",
            "Cognitive Bias Removal",
            "Text Simplification for Cognitive Load",
            "Cognitive Discourse Analysis",
            "Ideation to Text Generation",
            "Mental Model Text Adaptation",
        ]

    def get_prose_semantic_generation_types(self):
        """
        Returns a list of prose semantic generation types.

        These types represent various methods and techniques for generating
        semantic content from different forms of data, such as mappings,
        relations, clusters, roles, logical forms, and ontologies.

        Returns:
            list: A list of strings, each representing a type of prose semantic generation.
        """
        return [
            "Generate Semantic Mapping",
            "Generate Enhanced Semantic Relations",
            "Generate Semantic Clusters",
            "Generate Text from Semantic Roles",
            "Generate Sentences from Logical forms",
            "Generate Semantic-based Summaries",
            "Natural Language Generation from Ontology",
        ]

    def get_prose_stylistic_transformation_types(self):
        """
        Returns a list of available prose stylistic transformation types.

        The transformations include various stylistic changes such as:
        - Pronoun transformations (e.g., 'she' to 'he', gender-neutral pronouns)
        - Writing style adjustments (e.g., modernizing, localizing, mimicking specific authors)
        - Tone adjustments (e.g., formal to casual, casual to formal)
        - Voice transformations (e.g., passive to active voice)
        - Speech transformations (e.g., direct to indirect speech)
        - Simplification and normalization of writing style
        - Paraphrasing while maintaining the same style
        - Converting figurative language to literal expressions

        Returns:
            list: A list of strings describing the available prose stylistic transformations.
        """
        return [
            "Transform 'she' pronouns to 'he'",
            "Transform 'he' pronouns to 'she'",
            "Transform gender-specific pronouns to they/neutral",
            "Transform the Writing Style to Another Style",
            "Enhance the Existing Writing Style",
            "Normalize the Writing Style for Consistency",
            "Modernize the Writing Style to Contemporary Usage",
            "Localize the Writing Style to a Specific Locale or Culture",
            "Mimic a Specific Author's Writing Style",
            "Paraphrase the Text While Maintaining the Same Style",
            "Simplify the Writing Style",
            "Convert Direct Speech in Text to Indirect Speech",
            "Transform Sentences from Passive Voice to Active Voice",
            "Convert Figurative Language to Literal Expressions",
            "Adjust the Tone of the Text",
            "Transform a Formal-Style Text to Casual Style",
            "Transform a Casual-Style Text to Formal Style",
        ]

    def get_prose_narrative_transformation_types(self):
        """
        Retrieves a list of prose narrative transformation types.

        Returns:
            list: A list of strings, each representing a type of narrative transformation.
        """
        return [
            "Narrative Refactoring",
            "Narrative Streamlining",
            "Narrative Expansion",
            "Narrative Compression",
            "Narrative Perspective Change",
            "Narrative Mood Adjustment",
            "Narrative Setting Modification",
            "Narrative Exposition Enhancement",
            "Narrative Conflict Modification",
            "Transform Narrative to Dialogue",
            "Transform Narrative to Script",
            "Add Foreshadowing to Narrative",
            "Reverse Narrative Order",
        ]

    def get_text_scaling_types(self):
        """
        Returns a list of text scaling types.

        These text scaling types include various methods to modify and adjust text,
        such as condensing, expanding, increasing or decreasing complexity, 
        reordering paragraphs, breaking down sentences, elaborating on concepts, 
        adding contextual details, adjusting reading levels, reducing jargon, 
        expanding abbreviations, enriching with additional information, and mixing sentences.

        Returns:
            list: A list of strings representing different text scaling types.
        """
        return [
            "Condense Text into Shorter Versions",
            "Expand Short Text into More Detailed Versions",
            "Increase the Complexity of the Text",
            "Decrease the Complexity of the Text",
            "Reorder Paragraphs to Improve Flow",
            "Break Down Complex Sentences into Simpler Ones",
            "Elaborate on Concepts Mentioned in the Text",
            "Expand the Text with Full Details",
            "Add Contextual Details to the Text",
            "Adjust the Reading Level of the Text",
            "Reduce the Use of Jargon in the Text",
            "Expand Abbreviations Used in the Text",
            "Enrich the Text with Additional Relevant Information",
            "Mix Sentences to Improve Variety and Engagement",
        ]

    def get_text_enhancement_types(self):
        """
        Returns a list of text enhancement types.

        The text enhancement types include various transformations and corrections
        that can be applied to text to improve its quality, readability, and 
        appropriateness for different contexts.

        Returns:
            list: A list of strings, each representing a type of text enhancement.
        """
        return [
            "Automatic Paraphrasing",
            "Slang to Formal Translation",
            "Passive to Active Voice Conversion",
            "Sentence Reordering for Coherence",
            "Linguistic Simplification",
            "Grammar Correction",
            "Spelling Correction",
            "Punctuation Addition/Correction",
            "Style Adaptation",
            "Tone Modification",
            "Clarity and Precision Enhancement",
            "Content Enrichment",
            "Idiom to Literal Translation",
            "Jargon Translation to Plain Language",
            "Readability Improvement",
            "Cultural Adaptation",
            "Gender-neutral Language Conversion",
            "Content Localization",
            "Subject-specific Language Adaptation",
        ]

    def get_prompt_transformation_types(self):
        """
        Returns a list of different types of prompt transformations.

        Each transformation type is a string that describes a specific way to modify or enhance a given prompt. The available transformation types include:

        - "Improve Prompt - Increase the clarity and effectiveness of the given prompt"
        - "Paraphrase Prompt - Rephrase the prompt without losing the original meaning"
        - "Prompt Difficulty Level Adjustment - Modify the complexity level of the prompt"
        - "Expand Prompt - Add more detail and context to enrich the prompt"
        - "Simplify Prompt - Reduce complexity and shorten the prompt for easier comprehension"
        - "Convert to Art Prompt - Transform the given input into an art-related prompt"
        - "Adjust Prompt Context - Alter the setting or scenario of the prompt"
        - "Clarify Prompt - Add explanations or definitions to make the prompt more understandable"
        - "Translate Prompt - Convert the prompt into a different language while keeping its original meaning"
        - "Analyze Prompt - Assess and give feedback on how well-formed the prompt is"
        - "Generate Similar Prompts - Create HammerAI-lama-3_1-storm-latest prompts that lead to similar results"
        - "Prompt Abstraction - Remove specific details from the prompt to make it more general"

        Returns:
            list: A list of strings, each describing a type of prompt transformation.
        """
        return [
            "Improve Prompt - Increase the clarity and effectiveness of the given prompt",
            "Paraphrase Prompt - Rephrase the prompt without losing the original meaning",
            "Prompt Difficulty Level Adjustment - Modify the complexity level of the prompt",
            "Expand Prompt - Add more detail and context to enrich the prompt",
            "Simplify Prompt - Reduce complexity and shorten the prompt for easier comprehension",
            "Convert to Art Prompt - Transform the given input into an art-related prompt",
            "Adjust Prompt Context - Alter the setting or scenario of the prompt",
            "Clarify Prompt - Add explanations or definitions to make the prompt more understandable",
            "Translate Prompt - Convert the prompt into a different language while keeping its original meaning",
            "Analyze Prompt - Assess and give feedback on how well-formed the prompt is",
            "Generate Similar Prompts - Create HammerAI-lama-3_1-storm-latest prompts that lead to similar results",
            "Prompt Abstraction - Remove specific details from the prompt to make it more general"
        ]

    def get_art_prompt_transformation_types(self):
        """
        Returns a list of art prompt transformation types.

        The transformation types include:
        - Improve Art Prompt
        - Paraphrase Art Prompt
        - Art Prompt Context Adjustment
        - Rephrase Art Prompt for Different Art Styles
        - Convert to Text Prompt
        - Art Prompt Difficulty Level Adjustment

        Returns:
            list: A list of strings representing different types of art prompt transformations.
        """
        return [
            "Improve Art Prompt",
            "Paraphrase Art Prompt",
            "Art Prompt Context Adjustment",
            "Rephrase Art Prompt for Different Art Styles",
            "Convert to Text Prompt",
            "Art Prompt Difficulty Level Adjustment",
        ]

    def get_poetry_transformation_types(self):
        """
        Returns a list of poetry transformation types.

        This method provides various options for transforming poetry, including:
        - Transforming regular text to poetry
        - Translating poetry to another language
        - Paraphrasing poetry while retaining its essence
        - Adjusting the use of poetic devices to enhance impact
        - Converting regular poetry to a sonnet
        - Converting regular poetry to a haiku
        - Altering the rhyme scheme of existing poetry
        - Imitating a specific poet's style in an existing poem
        - Creating a visual poem from regular poetry
        - Changing the meter or rhythm of existing poetry
        - Transforming prose into verse form
        - Adding or rewriting stanzas in existing poetry

        Returns:
            list: A list of strings, each representing a type of poetry transformation.
        """
        return [
            "Transform Regular Text to Poetry",
            "Translate Poetry to Another Language",
            "Paraphrase Poetry while Retaining its Essence",
            "Adjust the Use of Poetic Devices to Enhance Impact",
            "Convert Regular Poetry to a Sonnet",
            "Convert Regular Poetry to a Haiku",
            "Alter the Rhyme Scheme of the Existing Poetry",
            "Imitate a Specific Poet's Style in an Existing Poem",
            "Create a Visual Poem from Regular Poetry",
            "Change the Meter or Rhythm of the Existing Poetry",
            "Transform Prose into Verse form",
            "Add or Rewrite Stanzas in Existing Poetry",
        ]

    def get_prose_textual_analysis_types(self):
        """
        Returns a list of available prose textual analysis types.

        The analysis types include various methods for examining and evaluating
        textual content, such as sentiment analysis, entity extraction, and
        readability checks.

        Returns:
            list: A list of strings representing different types of textual analysis.
        """
        return [
            "Sentiment Analysis",
            "Theme/Topic Modeling",
            "Entity Extraction",
            "Logical Fallacy Check",
            "Readability Check",
            "Fact Checking",
            "Grammar and Spell Check",
            "Entity Sentiment Analysis",
            "Plagiarism Detection",
            "Text Classification",
            "Keyword Extraction",
            "Language Detection",
            "Sentiment Trend Analysis",
            "Authorship Attribution",
            "Lexical Diversity Analysis",
            "Abstraction Level Analysis",
        ]

    def get_prose_semantic_analysis_types(self):
        """
        Returns a list of prose semantic analysis types.

        The list includes various types of semantic analysis techniques that can be applied to prose text, such as:
        - Logical Reasoning
        - Structural Logic
        - Emotional Reasoning
        - POS Tagging
        - Semantic Similarity Check
        - Argument Mining
        - Paraphrase Identification
        - Syntax Tree Parsing
        - Text Clustering
        - Embedding Vectorization
        - Dependency Parsing
        - Word Sense Disambiguation
        - Text Similarity
        - Text Segmentation
        - Coreference Resolution
        - Semantic Role Labeling
        - Semantic Relation Identification
        - Semantic Field Analysis

        Returns:
            list: A list of strings representing different types of prose semantic analysis.
        """
        return [
            "Logical Reasoning",
            "Structural Logic",
            "Emotional Reasoning",
            "POS Tagging",
            "Semantic Similarity Check",
            "Argument Mining",
            "Paraphrase Identification",
            "Syntax Tree Parsing",
            "Text Clustering",
            "Embedding Vectorization",
            "Dependency Parsing",
            "Word Sense Disambiguation",
            "Text Similarity",
            "Text Segmentation",
            "Coreference Resolution",
            "Semantic Role Labeling",
            "Semantic Relation Identification",
            "Semantic Field Analysis",
        ]

    def get_prose_cognitive_analysis_types(self):
        """
        Returns a list of cognitive analysis types for prose.

        These types represent various methods and techniques used to analyze and
        evaluate written content from different cognitive perspectives.

        Returns:
            list: A list of strings, each representing a type of cognitive analysis.
        """
        return [
            "Counter-argument Generator",
            "Perspective Analysis",
            "Hypothesis Testing",
            "Assumption Identification",
            "Cognitive Bias Detection",
            "Inference Generation",
            "Conceptual Link Detection",
            "Idea Validation",
            "Logical Consistency Check",
            "Thought Structure Analysis",
            "Idea Exploration",
            "Abstract Reasoning",
            "Causal Relationship Analysis",
            "Decision Making Analysis",
            "Mind Mapping",
            "Predictive Analysis",
            "Mental Model Generation",
        ]

    def get_prose_contextual_analysis_types(self):
        """
        Returns a list of prose contextual analysis types.

        These types represent different contexts in which prose can be analyzed, 
        including cultural, historical, geographic, political, economic, societal, 
        scientific, organizational, temporal, emotional, and philosophical contexts.

        Returns:
            list: A list of strings, each representing a type of prose contextual analysis.
        """
        return [
            "Cultural Context Analysis",
            "Historical Context Analysis",
            "Geographic Context Analysis",
            "Political Context Analysis",
            "Economic Context Analysis",
            "Societal Context Analysis",
            "Scientific Context Analysis",
            "Organizational Context Analysis",
            "Temporal Context Analysis",
            "Emotional Context Analysis",
            "Philosophical Context Analysis",
        ]

    def get_prose_linguistic_analysis_types(self):
        """
        Returns a list of prose linguistic analysis types.

        The list includes various types of linguistic analyses that can be performed on prose, such as:
        - Linguistic Evolution Analysis
        - Linguistic Drift Analysis
        - Linguistic Convergence Analysis
        - Linguistic Divergence Analysis
        - Linguistic Morphological Analysis
        - Linguistic Phonetic Analysis
        - Linguistic Syntactic Analysis
        - Linguistic Pragmatic Analysis

        Returns:
            list: A list of strings representing different types of linguistic analyses.
        """
        return [
            "Linguistic Evolution Analysis",
            "Linguistic Drift Analysis",
            "Linguistic Convergence Analysis",
            "Linguistic Divergence Analysis",
            "Linguistic Morphological Analysis",
            "Linguistic Phonetic Analysis",
            "Linguistic Syntactic Analysis",
            "Linguistic Pragmatic Analysis",
        ]

    def get_prose_stylistic_analysis_types(self):
        """
        Returns a list of prose stylistic analysis types.

        The list includes various types of analyses that can be performed on prose to evaluate different stylistic elements.

        Returns:
            list: A list of strings, each representing a type of prose stylistic analysis.
                - "Rhetorical Device Detection"
                - "Writing Style Analysis"
                - "Tone Analysis"
                - "Reading Level Analysis"
                - "Genre Classification"
                - "Voice (Active/Passive) Analysis"
                - "Modality Analysis"
                - "Figurative Language Detection"
                - "Text Coherence and Cohesion Analysis"
        """
        return [
            "Rhetorical Device Detection",
            "Writing Style Analysis",
            "Tone Analysis",
            "Reading Level Analysis",
            "Genre Classification",
            "Voice (Active/Passive) Analysis",
            "Modality Analysis",
            "Figurative Language Detection",
            "Text Coherence and Cohesion Analysis",
        ]

    def get_prose_narrative_analysis_types(self):
        """
        Returns a list of prose narrative analysis types.

        This method provides various types of analyses that can be performed on prose narratives, 
        including but not limited to plot structure, character, theme, and setting analyses.

        Returns:
            list: A list of strings, each representing a type of prose narrative analysis.
        """
        return [
            "Plot Structure Analysis",
            "Character Analysis",
            "Theme Analysis",
            "Narrative Tense Analysis",
            "Point of View Analysis",
            "Story Arc Analysis",
            "Setting Analysis",
            "Symbolism and Allegory Analysis",
            "Mood and Atmosphere Analysis",
            "Author's Purpose and Message Analysis",
        ]

    def get_opposition_analysis_types(self):
        """
        Returns a list of opposition analysis types.

        The opposition analysis types include various methods and strategies for 
        detecting, analyzing, and resolving conflicts. These types cover a wide 
        range of conflict-related aspects, from detection and resolution to 
        mediation and impact analysis.

        Returns:
            list: A list of strings, each representing a type of opposition analysis.
        """
        return [
            "Conflict Detection",
            "Conflict Resolution",
            "Contradiction Identification",
            "Argument Analysis",
            "Dispute Mediation Suggestions",
            "Bias Detection",
            "Emotion Analysis in Conflict",
            "Stakeholder Identification",
            "Conflict Escalation Prediction",
            "Resolution Strategy Suggestion",
            "Conflict Impact Analysis",
            "Conflict De-escalation Techniques",
            "Implicit Conflict Detection",
            "Non-verbal Conflict Indicators",
            "Historical Conflict Pattern Analysis",
            "Diplomacy and Negotiation Strategy Suggestions",
        ]

    def get_code_analysis_types(self):
        """
        Returns a list of various code analysis types.

        This method provides a comprehensive list of different types of code analysis
        that can be performed on a codebase. These types include but are not limited to:
        - Code Analysis
        - Code Review
        - Code Metrics
        - Code Smells
        - Static Analysis
        - Dynamic Analysis
        - Functional Analysis
        - Performance Analysis
        - Security Analysis
        - Dependency Analysis
        - Duplication Detection
        - Code Coverage
        - Refactor Suggestions
        - Comment Analysis
        - Coding Standards Compliance
        - Error and Exception Detection
        - Architecture Analysis
        - Version Control Analysis
        - Documentation Analysis

        Returns:
            list: A list of strings representing different code analysis types.
        """
        return [
            "Code Analysis",
            "Code Review",
            "Code Metrics",
            "Code Smells",
            "Static Analysis",
            "Dynamic Analysis",
            "Functional Analysis",
            "Performance Analysis",
            "Security Analysis",
            "Dependency Analysis",
            "Duplication Detection",
            "Code Coverage",
            "Refactor Suggestions",
            "Comment Analysis",
            "Coding Standards Compliance",
            "Error and Exception Detection",
            "Architecture Analysis",
            "Version Control Analysis",
            "Documentation Analysis",
        ]

    def get_prompt_analysis_types(self):
        """
        Returns a list of prompt analysis types.

        The analysis types include:
        - Prompt Efficiency
        - Prompt Effectiveness
        - Prompt Clarity Analysis
        - Prompt Engagement Level
        - Prompt Bias Detection
        - Prompt Category Prediction
        - Expected Response Type Prediction
        - Prompt Difficulty Level Prediction

        Returns:
            list: A list of strings representing different types of prompt analysis.
        """
        return [
            "Prompt Efficiency",
            "Prompt Effectiveness",
            "Prompt Clarity Analysis",
            "Prompt Engagement Level",
            "Prompt Bias Detection",
            "Prompt Category Prediction",
            "Expected Response Type Prediction",
            "Prompt Difficulty Level Prediction",
        ]

    def get_art_prompt_analysis_types(self):
        """
        Returns a list of art prompt analysis types.

        The analysis types include:
        - Art Prompt Efficiency
        - Art Prompt Clarity Analysis
        - Art Prompt Engagement Level
        - Art Prompt Bias Detection
        - Art Style Prediction
        - Colour Scheme Prediction
        - Art Prompt Difficulty Level Prediction

        Returns:
            list: A list of strings representing different types of art prompt analyses.
        """
        return [
            "Art Prompt Efficiency",
            "Art Prompt Clarity Analysis",
            "Art Prompt Engagement Level",
            "Art Prompt Bias Detection",
            "Art Style Prediction",
            "Colour Scheme Prediction",
            "Art Prompt Difficulty Level Prediction",
        ]

    def get_poetry_analysis_types(self):
        """
        Returns a list of available poetry analysis types.

        The list includes various types of analyses that can be performed on poetry,
        such as rhyme scheme analysis, poetic device identification, and more.

        Returns:
            list: A list of strings, each representing a type of poetry analysis.
        """
        return [
            "Rhyme Scheme Analysis",
            "Poetry Analysis",
            "Poetic Device Identification",
            "Theme Analysis",
            "Metaphor and Simile Analysis",
            "Syllable Count Analysis",
            "Sonnet Check",
            "Haiku Check",
        ]

    def get_prose_textual_generation_types(self):
        """
        Returns a list of prose textual generation types.

        The types include:
        - Generate Text Summary
        - Generate Text Excerpt with Keyword
        - Generate Text with Specific Style
        - Generate Text with Specific Tone
        - Generate Text in Active/Passive Voice

        Returns:
            list: A list of strings representing different types of prose textual generation.
        """
        return [
            "Generate Text Summary",
            "Generate Text Excerpt with Keyword",
            "Generate Text with Specific Style",
            "Generate Text with Specific Tone",
            "Generate Text in Active/Passive Voice",
        ]

    def get_prose_cognitive_generation_types(self):
        """
        Returns a list of cognitive generation types for prose.

        These types include various methods of generating text that are designed
        to provide cognitive insights, persuasive text, easy-to-understand text,
        cognitive maps, load-leveled text, hypotheses, predictive text, and 
        counterfactual text.

        Returns:
            list: A list of strings representing different cognitive generation types.
        """
        return [
            "Generate Cognitive Insights",
            "Generate Persuasive Text",
            "Generate Easy-to-Understand Text",
            "Generate Cognitive Maps from Text",
            "Generate Cognitive Load-leveled Text",
            "Generate Hypotheses from Text",
            "Predictive Text Generation",
            "Counterfactual Text Generation",
        ]

    def get_prose_contextual_generation_types(self):
        """
        Returns a list of prose contextual generation types.

        These types represent different categories of text generation that take into account various contexts such as analysis, locale, situation, and time.

        Returns:
            list: A list of strings, each representing a type of contextual prose generation.
        """
        return [
            "Generate Contextual Analysis Report",
            "Generate Context-Aware Summaries",
            "Generate Locale-Specific Texts",
            "Generate Contextual Paraphrases",
            "Generate Historical Texts",
            "Generate Situation-Aware Texts",
            "Generate Time-Aware Texts",
        ]

    def get_prose_stylistic_generation_types(self):
        """
        Returns a list of prose stylistic generation types.

        This method provides various types of stylistic text generation options,
        including generating stylized text, text with figurative language, text in 
        different genres, tones, and voices, as well as generating poetry, text 
        following a rhythm, and text in historical styles.

        Returns:
            list: A list of strings representing different prose stylistic generation types.
        """
        return [
            "Generate Stylized Text",
            "Generate Text with Figurative Language",
            "Generate Text in Different Genres",
            "Generate Text in Different Tones",
            "Generate Text in Different Voices",
            "Generate Poetry",
            "Generate Text Following a Rhythm",
            "Generate Text in Historical Styles",
        ]

    def get_prose_narrative_generation_types(self):
        """
        Returns a list of prose narrative generation types.

        This method provides various types of narrative generation capabilities 
        that can be used to create different styles and structures of stories.

        Returns:
            list: A list of strings, each representing a type of prose narrative 
                  generation capability.
        """
        return [
            "Generate Narrative Summary",
            "Generate Linear Story Arcs",
            "Generate Interactive Stories",
            "Generate Multi-Perspective Narratives",
            "Generate Flashbacks or Foreshadowing",
            "Generate Thematic-Based Stories",
            "Generate Plots with Surprising Twists",
            "Generate Stories in Different Genres",
        ]

    def get_documentation_generation_types(self):
        """
        Returns a list of strings representing different types of documentation 
        that can be generated.

        The types of documentation include:
        - Personal Log Entry
        - Clinical Report
        - Project Progress Report
        - Outline for a Research Paper
        - Itemized Invoice
        - Customized Resume
        - Professional Cover Letter
        - Technical Documentation for a Product
        - Meeting Minutes
        - End-of-Year Financial Report
        - Employee Performance Report
        - Data Analysis Report
        - Market Research Report
        - User Guide for a Software
        - Incident Report
        - Project Proposal
        - Business Plan
        - Press Release

        Returns:
            list: A list of strings, each representing a type of documentation.
        """
        return [
            "Generate a Personal Log Entry",
            "Generate a Clinical Report",
            "Generate a Project Progress Report",
            "Generate an Outline for a Research Paper",
            "Generate an Itemized Invoice",
            "Generate a Customized Resume",
            "Generate a Professional Cover Letter",
            "Generate Technical Documentation for a Product",
            "Generate Meeting Minutes",
            "Generate an End-of-Year Financial Report",
            "Generate an Employee Performance Report",
            "Generate a Data Analysis Report",
            "Generate a Market Research Report",
            "Generate a User Guide for a Software",
            "Generate an Incident Report",
            "Generate a Project Proposal",
            "Generate a Business Plan",
            "Generate a Press Release",
        ]

    def get_prompt_generation_types(self):
        """
        Returns a list of different types of prompt generation capabilities.

        The types of prompt generation include:
        - Generate a Contextual Prompt
        - Generate an Exploratory Prompt
        - Generate an Instruction-Following Prompt
        - Generate a Conversational Prompt
        - Perform Iterative Prompt Refinement
        - Generate a Prompt for a Specific Skill Level
        - Generate a Prompt for a Specific AI Model
        - Generate a Multi-step Prompt
        - Generate a Prompt with Explicit User Intent
        - Generate a Report on Prompt Effectiveness

        Returns:
            list: A list of strings representing various prompt generation types.
        """
        return [
            "Generate a Contextual Prompt",
            "Generate an Exploratory Prompt",
            "Generate an Instruction-Following Prompt",
            "Generate a Conversational Prompt",
            "Perform Iterative Prompt Refinement",
            "Generate a Prompt for a Specific Skill Level",
            "Generate a Prompt for a Specific AI Model",
            "Generate a Multi-step Prompt",
            "Generate a Prompt with Explicit User Intent",
            "Generate a Report on Prompt Effectiveness",
        ]

    def get_art_prompt_generation_types(self):
        """
        Returns a list of different types of art prompt generation capabilities.

        The list includes:
        - Generate Art Prompts
        - Expand Art Prompts
        - Create Text Prompts from Art
        - Generate Art Prompts for Different Styles
        - Generate Sequences of Art Prompts
        - Generate Thematic Art Prompts

        Returns:
            list: A list of strings representing various art prompt generation types.
        """
        return [
            "Generate Art Prompts",
            "Expand Art Prompts",
            "Create Text Prompts from Art",
            "Generate Art Prompts for Different Styles",
            "Generate Sequences of Art Prompts",
            "Generate Thematic Art Prompts",
        ]

    def get_poetry_generation_types(self):
        """
        Returns a list of available poetry generation types.

        The list includes various styles and forms of poetry that can be generated,
        such as rhyming couplets, sonnets, haikus, and more.

        Returns:
            list: A list of strings representing different poetry generation types.
        """
        return [
            "Generate Poetry",
            "Generate Rhyming Couplets",
            "Emulate Poetic Styles",
            "Generate Sonnets",
            "Generate Haiku",
            "Generate Free Verse",
            "Generate Limericks",
            "Create Poetry from Prompts",
        ]

    def get_code_transformation_types(self):
        """
        Retrieve a list of code transformation types.

        Returns:
            list: A list of strings representing various types of code transformations, including:
                - "Module Decomposition"
                - "Increase Granularity"
                - "Decrease Granularity"
                - "Code Refactoring"
                - "Code Restructuring"
                - "Code Formatting"
                - "Code Simplification"
                - "Code Modularization"
                - "Code Optimization"
                - "Code Parallelization"
                - "Code Translation"
        """
        return [
            "Module Decomposition",
            "Increase Granularity",
            "Decrease Granularity",
            "Code Refactoring",
            "Code Restructuring",
            "Code Formatting",
            "Code Simplification",
            "Code Modularization",
            "Code Optimization",
            "Code Parallelization",
            "Code Translation",
        ]

    def get_code_generation_types(self):
        """
        Returns a list of code generation capabilities.

        This method provides various types of code generation functionalities 
        that can be utilized, including but not limited to:

        - Generate Test Cases
        - Generate Code Snippets
        - Generate API Documentation
        - Generate Code from Pseudocode
        - Automatic Code Completion
        - Generate Code from UML Diagrams
        - Code Skeleton Generation
        - Generate Build Scripts

        Returns:
            list: A list of strings representing different code generation types.
        """
        return [
            "Generate Test Cases",
            "Generate Code Snippets",
            "Generate API Documentation",
            "Generate Code from Pseudocode",
            "Automatic Code Completion",
            "Generate Code from UML Diagrams",
            "Code Skeleton Generation",
            "Generate Build Scripts",
        ]

    def get_prose_contextual_transformation_types(self):
        """
        Retrieves a list of prose contextual transformation types.

        Returns:
            list: A list of strings, each representing a type of contextual transformation 
                  that can be applied to prose. The types include:
                  - Historical Context Adaptation
                  - Cultural Context Translation
                  - Temporal Context Enhancement
                  - Geographical Context Alteration
                  - Adjust Prose to Societal Contexts
                  - Political Context Infusion
                  - Economic Context Embedding
                  - Scientific Context Integration
                  - Prose Localization with Context
                  - Philosophical Context Enrichment
        """
        return [
            "Historical Context Adaptation",
            "Cultural Context Translation",
            "Temporal Context Enhancement",
            "Geographical Context Alteration",
            "Adjust Prose to Societal Contexts",
            "Political Context Infusion",
            "Economic Context Embedding",
            "Scientific Context Integration",
            "Prose Localization with Context",
            "Philosophical Context Enrichment",
        ]
