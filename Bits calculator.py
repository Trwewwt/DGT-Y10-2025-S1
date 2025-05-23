keep_going = ""
while keep_going == "":
    Whats_height = int(input("Whats the height of the picture:"))
    print ()
    print (f"You entered {Whats_height}")
    Whats_width = int(input("Whats the width of the picture:"))
    print ()
    area = Whats_height * Whats_width
    print (f"The area is {area}")
    keep_going =input("Press <Enter> to continue or any other key to quit")
