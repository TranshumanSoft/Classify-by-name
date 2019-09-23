print("Some people will have chocolate or vanilla icecream, it depends on their names.")
name = str(input("What's your name?"))
name = name.lower()
group = ""
if name.startswith("a" or "b" or "C" or "d" or "e" or "f" or "g" or "h" or "i" or "j" or "k" or "l" or "m"):
    print("You are from group 'A'." )
    group = group + "A"
else:
    print("You are from group 'B'.")
    group = group + "B"
icecream = str(input("What is your group?"))
icecream = icecream.upper()
if icecream == "A":
    print("Here's your vanilla icecream!")
elif icecream == "B":
    print("Here's your chocolate icecream!")
else:
    print("That group doesn't exist.")