# use the round function to round up floats
# from the docs round(number [, ndigits])

# takes a number as input and rounds it up to nearest int


# you can then round up to nearest integer
gpa = float(input("Whats your Gpa: "))
gpa = round(gpa)
print(gpa, 'rounded to int')

# the square brackets says optionally, you can specify the number of digits to round to
price = float(input("Whats the price: "))
price = round(price, 2)
print(price)

