'''
A program that repeatedly prompts a user for integer numbers until the user enters 'done'.
Once 'done' is entered, print out the largest and smallest of the numbers.
If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number.
Enter 7, 2, bob, 10, and 4 and match the output below. 
'''

largest = None
smallest = None

while True:

    num = input("Enter a number: ")

    if num == "done":
        break

    try: 
        num = float(num)

        if largest == None and smallest == None:

            smallest = num
            largest = num

        if num < smallest:
                smallest = num
        elif num > largest:
                largest = num

    except:
        print("Invalid input")

print("Maximum is", int(largest))
print("Minimum is", int(smallest))