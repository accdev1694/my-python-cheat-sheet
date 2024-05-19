# we can also combine 'or' statements inside if statements to improve our logic
# lets execute a logic for an invite for a teenagers party as follows:

age = int(input("How old are you? "))

if age <= 12 or age >= 20:
    print("You cannot attend")
else:
    print("You are invited")