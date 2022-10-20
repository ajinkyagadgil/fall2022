name = input("Enter your name: ")
age = int(input("Enter your age: "))
if age >= 18:
    print(f'Hi {name} you are eligible to vote')
else:
    print(f'Hi {name} you are NOT eligible to vote')