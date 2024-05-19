# match works like switch in js or java

# consider the following code:

day = input("What day of the week: ")
            
match day.title().strip():
    case "1" | "One":
        print("Monday")
    case "2" |"Two":
        print("Tuesday")
    case "3" | "Three":
        print("Wednesday")
    case "4" | "Four":
        print("Thursday")
    case "5" | "Five":
        print("Friday")
    case "6" | "Six":
        print("Saturday")
    case "7" | "Seven":
        print("Sunday")
    case _:
        print("Invalid day")
        
        
# it turns out that you can combine cases seperating them with |