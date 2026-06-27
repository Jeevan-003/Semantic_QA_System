import re
class TextPreprocessor:
    @staticmethod
    def clean(text: str) -> str:
        # Remove multiple spaces
        text = re.sub(r"\s+", " ", text)

        # Remove extra newlines
        text = re.sub(r"\n+", "\n", text)

        return text.strip()