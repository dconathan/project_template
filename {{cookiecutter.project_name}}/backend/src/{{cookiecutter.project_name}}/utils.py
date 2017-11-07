

class LazyNLP(English):
    def __init__(self):
        self.nlp = None

    def __call__(self, *args, **kwargs):
        if self.nlp is None:
            import spacy
            self.nlp = spacy.load("en")
        return self.nlp(*args, **kwargs)

nlp = LazyNLP()


def tokenize(text):
    from spacy.tokens.span import Span
    def _clean(token):
        return token.lower_
    if isinstance(text, Span):
        return map(_clean, text)
    else:
        return map(_clean, nlp(text, tag=False, parse=False, entity=False))


def sentencize(text):
    return nlp(text, entity=False).sents


del LazyNLP
