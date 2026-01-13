print("Welcome to Credit Card Application Simulator!")
print("this is accurate to real life (NO HE'S LYING)")

# Age input
age = int(input("Enter age here: "))
print(f"You entered: {age}")

# Age check
if age == 0:
    print("YOU WERE JUST BORN")
elif age < 18:
    print("NOPE")
else:
    print("Age accepted, let's continue!")

# Question 1
q1 = input("Ok, now I have to ask you: What is the square root of 64? ")

# Check q1 answers
if q1 == "8":
    print("Correct! Now for the next question...")
elif q1 == "55":
    print("WRONG! DUMMY")
elif q1.lower() == "gg":
    print("THERMONUCLEAR GET THE RPG")
else:
    print("Interesting answer... moving on!")

# Question 2
q2 = input("If you wrote a book about the main character slowly going insane, what would the last line be? ")

# Check q2 answers
if "insane" in q2.lower():
    print("Congratulations, credit card is yours!")
elif q2.lower() == "i dont know":
    print("Dang, that's crazy!")
elif q2.lower() == "gg":
    print("BYE")
else:
    print("Hmm, noted.")

# Prevent program from closing immediately
input("\nPress Enter to exit the game...")
