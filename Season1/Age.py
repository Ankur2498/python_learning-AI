try:
    age = int(input("Enter your age: "))
    if age < 13:
        print("You are a child.")
    elif age < 19:
        print("You are a teenager.")
    else:
        print("You are adult.")
except ValueError:
    print("Please provide a valid integer.")
