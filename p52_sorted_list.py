# lets collect three names from the user, append them to a sorted list  and print them out

names = []

for _ in range(3):
    names.append(input("What is your name? "))

for name in sorted(names):
    print(f"Hello {name}")
