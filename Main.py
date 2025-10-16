# Lachlan Gaeth
# 10/10/25
# Version 1
# TODO: ask the user if they like coffee
#       Record the answer
#       Give a response back to the answer

'''
like_coffee = input("Do you like coffee? ")
print(f'Your answer was"{like_coffee}".')
if like_coffee == "yes" or "Yes" or "Y" or "y" :
    print("That is great! I like coffee too.")
else:
    print("You are missing out! Why not giving it a try")
'''

# Version 2
# While loop
keep_going = ""
while keep_going == "":
    like_coffee = input("Do you like coffee? ")

    if like_coffee == "yes" or like_coffee == "Yes" or like_coffee == "Y" or like_coffee == "y":
        print("That is great! I like coffee too.")
        keep_going = "finished"

    elif like_coffee == "no" or like_coffee == "No" or like_coffee == "n" or like_coffee == "N":
        print("You are missing out! Why not giving it a try? ")
        keep_going = "finished"
    
    else:
        print("I dont't understand. ")
