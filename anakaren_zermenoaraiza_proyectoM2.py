## COORDENATE LOCATION

# used a bucle to make sure the usuary write a correct character, in this case
# we need a number negative or positive to assign to the x coordenate. If the usuary don't write a
# number, the bluce goes again until we got a number.
while True:
    try:
        x = float(input("Write a number for the coordenate x: "))
        if x !=  "":
            break
        else:
            print("you need to write a number, please, try again.")
    except ValueError:
        print("Incorrect, enter a valid number.")

# used a bucle to make sure the usuary write a correct character, in this case
# we need a number negative or positive to assign to the y coordenate. If the usuary don't write a
# number, the bluce goes again until we got a number.
while True:
    try:
        y = float(input("Write a number for the coordenate y: "))
        if y !=  "":
            break
        else:
            print("you need to write a number, please, try again.")
    except ValueError:
        print("Incorrect, enter a valid number.")

# if the x number is bigger than 0 and y number also too, then the coordinate given for the usuary
# will be in the first quadrant
if x > 0 and y > 0:
    quadrant = "first"
# if the x number is less than 0 and y bigger than 0, then the coordinate given for the usuary
# will be in the second quadrant
elif x < 0 and y > 0:
     quadrant = "second"
# if the x number is less than 0 and y number also too, then the coordinate given for the usuary
# will be in the third quadrant
elif x < 0 and y < 0:
     quadrant = "third"
# if the x number is bigger than 0 and y number less than 0, then the coordinate given for the usuary
# will be in the fourth quadrant
elif x > 0 and y < 0:
     quadrant = "fourth"
# if the x number is 0 and y number also too, then the coordinate given for the usuary
# will be in the origin, therefore it is not in any quadrant
else :
    quadrant = print("On an axis or at the origin, therefore it is not in any quadrant")

# print the coordinate given for the usuary indicating the quadrant in which it is located
print(f"The({x},{y}) is in the {quadrant} quadrant.")



## WORD LENGHT

# ask the user to enter a word between 4 and 8 characters.
word = input("Write a word between 4 and 8 characters: ")
# rename the variable so the keyword 'len' count the number of characters entered.
lenght = len(word)

# check if the word written have more than 4  and less than 8 characters, if it's is correct
# we send a message to say that's correcth lenght asked.
if lenght >= 4 and lenght <= 8:
    print("The word is correct and got the right lenght")

# if the word written is less than 4 characters, send a message saying the numbers of
# characters writed and itemize the usuary need to write more characters.
if lenght <4:
    print(f"Need to write more characters, it just got {lenght} characters")

# if the word written is more than 8 characters, send a message saying the numbers of
# characters writed and itemize the usuary need to write less characters.
if lenght > 8:
    print(f"Extra characters.It got {lenght} characters.")