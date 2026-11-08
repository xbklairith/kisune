from .tokenize import tokens


class Index:
    def __init__(self):
        self.postings = {}

    def add(self, doc_id, text):
        for t in tokens(text.lower()):
            self.postings.setdefault(t, set()).add(doc_id)

    def search(self, query):
        hits = [self.postings.get(t, set()) for t in tokens(query)]
        return set.intersection(*hits) if hits else set()
