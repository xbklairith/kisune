import re


def slugify(text):
    """Lowercase, trim, and join words with hyphens: 'Hello World' -> 'hello-world'."""
    text = text.strip().lower()
    text = re.sub(r"[^a-z\s-]", "", text)
    return re.sub(r"[\s-]+", "-", text).strip("-")
