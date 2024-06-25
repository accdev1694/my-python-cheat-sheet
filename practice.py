sentence = "This is a common interview question"
print(sentence)

frequency = 0
frequent_letter = ''

for letter in sentence:
    if sentence.count(letter) > frequency:
        frequency = sentence.count(letter)
        frequent_letter = letter
        
print(frequency, frequent_letter)





