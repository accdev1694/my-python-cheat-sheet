import re

# this an advanced validation method beyond simply using loops to check if certain fields exist
# example for an email. its easy to check for @, .com, etc but this is not sufficient as an email can have an @ in the username
# the code becomes increasingly long if you begin to validate each and every field

# there is a library for regular expressions called re, which helps to identify patterns and use them
# here is the syntax re.search(pattern, string, flags=0)
# the first argument 'pattern' is a pattern you want to search for, (patterns in an email address)
# the 'string' argument is the actual string you want to search that pattern in (the actual email)
# the third parameter 'flags' are arguments we pass to modify the behaviour of the string
'''
.   any character except a new line
*   0 or more repetitions
+   1 or more repetitions
?   0 or 1 repetition

'''
email = input("Email: ")

# from the search module, use the re function to check if the email contains an @, the print 'Valid' if true
if re.search("@", email):
    print('Valid')

# of course this is the just the begining, we could ultimately do more to the pattern search