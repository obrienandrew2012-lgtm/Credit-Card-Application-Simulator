print("Welcome to Credit Card Application Simulator!")
print("this is accurate to real life (NO HE'S LYING)")

age = int(input("enter age here "))
print(age)

q1 = int(input("ok so now i have to ask you what is the square root of 64 "))
q2 = input("if you wrote a book about the main character slowly going insane, what would the last line be? ")

if age == 0:
    print("YOU WERE JUST BORN")
elif age < 18:
    print("NOPE")
elif age <= 18:
    print(q1)

if q1 == 8:
    print(q2)
elif q1 == 55:
    print("WRONG! DUMMY")
elif q1 == "gg":
    print("THERMONUCLEAR GET THE RPG")

if q2 == "ooo im insane i went insane aaa":
    print("weljflakjdlkfjalksdflkajeklfjalkejdf credit card is yours")
elif q2 == "i dont know":
    print("dang thats crazy")
elif q2 == "gg":
    print("BYE")

# Prevent the program from closing immediately
input("\nPress Enter to exit the game...")
