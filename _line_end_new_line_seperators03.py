# \n is an escape character which is set to True by defaultin the print command

# override that behaviour by looking at the docs for the print function

# print(*objects, sep=' ', end='\n', file=sys.stdout, flush-False)

# set end='' to override the new line parameter

print("Hello,", "Oloche", end='')
print(", How are you")
# notice the output all on same line

# whenever you use multiple aguments with the print command, sep=" " by default. 
# override that behaviour if you wish by setting sep='_' with no spaces
print("oloche", "aboje", 'emmanuel', sep='_')
# notice each name is seperated by underscores

