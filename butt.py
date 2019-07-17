import nltk

def buttify(message):
    output = ""
    words = nltk.word_tokenize(message)
    for word in words:
        if is_plural_noun(word):
            output += "butts"
        elif is_singular_noun(word):
            output += "butt"
        else:
            output += word

        output += " "

    return output


def is_plural_noun(word):
    tag = get_parts_of_speech_tag(word)
    return tag == "NNS"


def is_singular_noun(word):
    tag = get_parts_of_speech_tag(word)
    return tag == "NN"


def get_parts_of_speech_tag(word):
    tagged_words = nltk.pos_tag([word])
    _, tag = tagged_words[0]
    return tag


if __name__ == "__main__":
    print(buttify("I am losing my freaking mind"))