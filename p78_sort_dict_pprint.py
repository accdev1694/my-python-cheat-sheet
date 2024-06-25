import pprint
sentence = "This is a common interview question"

sentence_dict = {letter: sentence.count(letter) for letter in sentence}
pprint.pprint(sorted(sentence_dict.items(), key=lambda item: item[1], reverse=True))
