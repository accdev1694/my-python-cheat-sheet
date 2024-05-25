# you can make a numbered list of items in python

days = ["Sunday", "Monday", "Tuesday",
        "Wednesday", "Thursday", "Friday", "Saturday"]

for day in range(len(days)):
    print(day+1, days[day])

# the range function is inly used in int data types   
# what is happenning is that the for loop creates
# a variable called day, assigns it to the first value in the range function and then executes the indented code
# i then moves to the next line, assigns day to the second range value and executes indented code
# and on and on and on until the last character in the range function
