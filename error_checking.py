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

'''def test_int_num():
    done = False
    while not done:
        try:
            num = int(input("Please enter a number (integer)"))
            done = True
        except ValueError:
            print("That is not a valid integer.\n")
    print(f"The number that you entered is {num}. ")
test_int_num()'''

'''def test_int(question):
    done = false
    while not done:
        error = "That's not a valid number"
        print(question)
        try:
            num = int(input())
            done = True
        except ValueError:
            print(error)
    return(num)

num1 = test_int("Please enter your value:")
print("Your numbers added together is num2")

num2 = test_int'''

# version 1.3
# 24/10/25

if __name__ == "__main__":
    def valid_num(question, low, high):
        error = f"whoops, that is not an integer between {low} and {high}"
        while True:
            try:
                response = int(input(question))
                if low <= response <= high:
                    break
                else:
                    print(f"{error} \n")
            except ValueError:
                print(f"{error} \n")
        return response

    num_1 = valid_num("enter a number between 1 and 10: ",1,10)
    print("you entered {num_1}\n")

    num_2 = valid_num("enter a number between 15 and 25: ",15,25)
    print(f"you entered {num_2}\n")

    num_3 = valid_num("enter a number between 70 and 90: ",70,90)
    print(f"you entered {num_3}\n")

    sum = num_1 + num_2 + num_3
    print(f"The total of {num_1}, {num_2} and {num_3} is {sum}.\n")

