# 29/10/25
# Week 1

# Area,Perimeter calculator
keep_going = ""
while keep_going == "":
    shape_width = float(input("What is the width of your shape(Number above zero)? "))
    print(f"Your width was {shape_width}")
    print()

    shape_height = float(input("What is the height of your shape(Number above zero)? "))
    print(f"Your height was {shape_height}")
    print()

    area = shape_width * shape_height
    print(f"The area of your shape is {area} square units ")
    print()

    Perimeter = shape_width +  shape_height
    print(f"The perimeter of your shape is {Perimeter} untis ")

    keep_going = input("Press <Enter> to continue, or any other key to quit. Thanks!")