import nltk


class Text:

    def __init__(self, text):
        tokens = nltk.word_tokenize(text)
        self.tagged_tokens = nltk.pos_tag(tokens)
        self.replacements = {}

    def get_tokens(self):
        return [Token(token, tag) for (token, tag) in self.tagged_tokens]

    def replace(self, index, word):
        self.replacements[index] = word

    def compile(self):
        tokens = self.get_tokens()
        output = ""
        for index, token in enumerate(tokens):
            if token.is_preceded_by_space():
                output += " "

            if index in self.replacements:
                output += self.replacements[index]
            else:
                output += token.token
        return output.strip()


class Token:

    def __init__(self, token, tag):
        self.token = token
        self.tag = tag

    def is_preceded_by_space(self):
        return self.token != self.tag and self.token != "'"

    def is_noun(self):
        return self.is_singular_noun() or self.is_plural_noun()

    def is_singular_noun(self):
        return self.tag == "NN"

    def is_plural_noun(self):
        return self.tag == "NNS"