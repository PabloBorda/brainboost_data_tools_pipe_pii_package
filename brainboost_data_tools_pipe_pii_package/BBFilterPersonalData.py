# brainboost_data_tools_pipe_pii_package/BBFilterPersonalData.py

from brainboost_data_source_logger_package.BBLogger import BBLogger
from presidio_anonymizer import AnonymizerEngine
from presidio_anonymizer.entities import AnonymizerConfig
from presidio_analyzer import AnalyzerEngine, PatternRecognizer, Pattern
import re

class BBFilterPersonalData:
    def __init__(self):
        BBLogger.log("Initializing BBFilterPersonalData...")
        # Initialize Presidio Analyzer and Anonymizer engines
        self.analyzer = AnalyzerEngine()
        self.anonymizer = AnonymizerEngine()

        # Define default anonymization behavior
        self.anonymization_config = {
            "DEFAULT": AnonymizerConfig("replace", {"new_value": "[FILTERED]"})
        }

        # Define specific entities to detect
        self.entities_to_detect = ["PERSON", "EMAIL_ADDRESS", "PHONE_NUMBER", "API_KEY", "ID_NUMBER"]

        # Add custom recognizers for IDs, API keys, and short phone numbers
        self._add_custom_recognizers()
        BBLogger.log("BBFilterPersonalData initialized successfully.")

    def _add_custom_recognizers(self):
        BBLogger.log("Adding custom recognizers...")

        # Custom Recognizer for API_KEY
        api_key_regex = r"\b[a-zA-Z0-9]{32}\b"
        api_key_pattern = Pattern(name="api_key_pattern", regex=api_key_regex, score=0.85)
        api_key_recognizer = PatternRecognizer(
            supported_entity="API_KEY",
            patterns=[api_key_pattern],
            supported_language="en"  # Correct parameter name and type
        )
        self.analyzer.registry.add_recognizer(api_key_recognizer)
        BBLogger.log("API_KEY recognizer added.")

        # Custom Recognizer for ID_NUMBER
        id_number_regex = r"\b\d{3}-\d{2}-\d{4}\b"
        id_number_pattern = Pattern(name="id_number_pattern", regex=id_number_regex, score=0.85)
        id_number_recognizer = PatternRecognizer(
            supported_entity="ID_NUMBER",
            patterns=[id_number_pattern],
            supported_language="en"  # Correct parameter name and type
        )
        self.analyzer.registry.add_recognizer(id_number_recognizer)
        BBLogger.log("ID_NUMBER recognizer added.")

        # **Custom Recognizer for 7-Digit Phone Numbers (e.g., 555-1234)**
        phone_number_7_digit_regex = r"\b\d{3}-\d{4}\b"  # Matches formats like 555-1234
        phone_number_7_digit_pattern = Pattern(name="phone_number_7_digit_pattern", regex=phone_number_7_digit_regex, score=0.85)
        phone_number_7_digit_recognizer = PatternRecognizer(
            supported_entity="PHONE_NUMBER",
            patterns=[phone_number_7_digit_pattern],
            supported_language="en"  # Correct parameter name and type
        )
        self.analyzer.registry.add_recognizer(phone_number_7_digit_recognizer)
        BBLogger.log("Custom PHONE_NUMBER recognizer for 7-digit phone numbers added.")

    def filter(self, text: str) -> str:
        BBLogger.log("Starting PII filtering process.")
        
        if not isinstance(text, str):
            BBLogger.log("Input text is not a string.", level="error")
            raise ValueError("Input text must be a string.")
        
        if not text.strip():
            BBLogger.log("Input text is empty or whitespace, returning as is.")
            return text
        
        try:
            BBLogger.log(f"Analyzing text: {text}")
            # Analyze the text to detect specified PII entities
            analysis_results = self.analyzer.analyze(text=text, entities=self.entities_to_detect, language="en")
            BBLogger.log(f"Built-in analysis completed. Detected entities: {analysis_results}")

            # Detect custom PII entities using regex
            # (Already handled by custom recognizers)

            # Combine built-in and custom analysis results
            # (Presidio automatically combines all recognizers)
            BBLogger.log(f"Total analysis results: {analysis_results}")

            # Anonymize the detected PII entities
            anonymized_result = self.anonymizer.anonymize(
                text=text,
                analyzer_results=analysis_results,
                anonymizers_config=self.anonymization_config
            )
            BBLogger.log("Anonymization process completed.")

            # Extract the resulting anonymized text
            anonymized_text = anonymized_result  # Direct assignment since it's a string
            BBLogger.log(f"Anonymized text: {anonymized_text}")
            BBLogger.log("PII filtering process finished successfully.")

            return anonymized_text

        except Exception as e:
            BBLogger.log(f"Error during PII filtering: {e}", level="error")
            raise
