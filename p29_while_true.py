# while True implements an infinite loop and causes something to happen infinitely until a condition breaks the loop

# if we want a user to input a negative integer, we can implemet this with a while loop



while True:
    num = int(input("Type a positive number: "))
    if num >= 0:        
        break
    
for _ in range(num):
    print("Hello")
    
# this way, the program will prompt the user over and over until it gets what it wants and then breaks
