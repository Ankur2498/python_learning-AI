try:
    count = int(input("Tell a number."))
    if count > 100:
        print("Too big")
    for i in range(1, count+1):
        print(i)
except ValueError:
    print("That's not a number.")

