# use the any keyword to iterate over a list or any iterable to chaech if any of the characters meet a certain condition
# in this case if any of the characters is a number or digit
number = input("Plate: ")
if any(num.isdigit() for num in number):
    print("There are Digits!")
else:
    print("No digits!!!")
