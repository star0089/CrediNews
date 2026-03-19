import re
import string

def preprocess_text(text: str) -> str:
    if not isinstance(text, str): return ""
    # Strip URLS
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
    # Strip typical news prefixes
    text = re.sub(r'^.*?-\s*', '', text)
    # Strip standard twitter handles
    text = re.sub(r'\@\w+|\#', '', text)
    
    # Lowercase
    text = text.lower()
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    # Remove extra spaces
    text = re.sub(r'\s+', ' ', text).strip()
    return text

