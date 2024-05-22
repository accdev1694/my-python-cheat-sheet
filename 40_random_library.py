import random
 # you may also use the from keyword to import just the choice function from the random module
 # from random import choice
 # in which case you dont need the dot notation
 # choices = choice(["Head", "Tail"]) 

# the random.py file is inbuilt with with python and i can be imported to be used in your code
# note, this choice function only works on lists
# lets flip a coin

choices = random.choice(["Tail", "Head"])
print(choices)



