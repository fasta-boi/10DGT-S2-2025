# Lachlan Gaeth
# 10/10/25
# Version 1
# TODO: ask the user if they like coffee
#       Record the answer
#       Give a respdwonse back to the answer

like_coffee = input("Do you like coffee? ")
print(f'Your answer was"{like_coffee}".')

if like_coffee == "yes" or "Yes" or "Y" or "y" :
    print("That is great! I like coffee too.")
else:
    print("You are missing out! Why not giving it a try")
