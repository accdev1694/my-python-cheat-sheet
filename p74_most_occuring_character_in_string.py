# this exercise is to find the most occcuringcharacter in this string

sentence = "This is a common interview question"

occurence = 0
most_occuring = ''

for letter in sentence:
    occurence_count = sentence.count(letter)
    if occurence_count > occurence:
        occurence = occurence_count
        most_occuring = letter
        
print(f"The most occurring letter is '{most_occuring}', occuring {occurence} times")