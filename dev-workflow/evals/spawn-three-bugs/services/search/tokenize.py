import re

WORD = re.compile(r"[a-z0-9]+")


def tokens(text):
    return WORD.findall(text)
