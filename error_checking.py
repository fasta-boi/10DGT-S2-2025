# lachlan gaeth
# error checking
# date: 22/10/2025
# code that tests whether a valid input is given

# version 1

'''done = False
while not done:
    num = int(input("Please enter your value: "))
    done = True
print(f"The number that you entered is {num}. ")'''

# version 1.1
'''
done = False
while not done:
    try:
        num = int(input("Please enter a number (integer): "))
        done = True
    except ValueError:
        print("That is not a valid number.\n")
print(f"The number that you entered is {num}. ")'''

# version 1.2

def test_int_num():
    done = False
    while not done:
        try:
            num = int(input("Please enter a number (integer)"))
            done = True
        except ValueError:
            print("That is not a valid integer.\n")
    print(f"The number that you entered is {num}. ")

test_int_num()