from random import randint

from parsing import Text


def buttify(message):
    text = Text(message)
    index_to_replace = None
    plural = None
    n_nouns = 0
    for index, token in enumerate(text.get_tokens()):
        if token.is_noun():
            i = randint(0, n_nouns)
            if i == 0:
                index_to_replace = index
                plural = token.is_plural_noun()
            n_nouns += 1

    if index_to_replace is not None:
        if plural:
            text.replace(index_to_replace, "butts")
        else:
            text.replace(index_to_replace, "butt")

    buttified = index_to_replace is not None

    return text.compile(), buttified


if __name__ == "__main__":
    print(buttify("Anyone who has lost track of time when using a computer knows the propensity to dream, the urge to make dreams come true and the tendency to miss lunch."))