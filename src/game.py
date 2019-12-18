import time
tori_friend = 0
andre_friend = 0
robbie_friend = 0
jade_friend = 0
cat_friend = 0
beck_friend = 0

print("\n We are pleased to inform you that you have been accepted into Hollywood Arts High School! \n")

time.sleep(5)

print("You came to the realization that engineering isn't your true calling in life, but performing arts instead! \n")

time.sleep(5)

print("Every year, Hollywood Arts hosts an event called 'The Big Showcase,' where agents and talent spotters around the country are invited. \n")

time.sleep(5)

print("It is your job to prepare a showstopping performance by the end of this week. \n")

time.sleep(5)

print("But to do this, you will need to get all of your materials together before the show. You will need to make friends, make smart choices, and make sure you don't run out of turns! \n")

time.sleep(5)

print("Before you can begin your adventure in Hollywood Arts, we will need to know more about you. \n")

time.sleep(5)

name = input("What is your name? ")

print(name)

print("\n Hello, " + name)

print("Congratulations! You have finished registration for Hollywood Arts. See you on the first day!")

time.sleep(5)

print("\n ---------------------------------------------------------")

print("\n MONDAY. First day at Hollywood Arts. Four more days until the Big Showcase! \n")

print("You walk into your new school, nervous. What if you don't make new friends? What if you're not talented enough? \n")

time.sleep(5)

print("""When you walk in, you see six students standing by the lockers.

1  The brunette girl seems friendly and could definitely help you for your Big Showcase, though she seems almost obnoxiously confident about her talents.

2  The boy holding the keyboard seems like a gifted musical prodigy, which means he could be of big help, and he looks like he could be a very supportive friend.

3  The boy with curly hair seems shy and socially awkward, and he'd holding this puppet that's giving you the creeps.

4  The girl wearing all black gives off scary vibes. She seems very confident, which could be of help for the Big Showcase.

5  The girl with fluorescent red hair always seems to be smiling, and she has a very eccentric personality. She seems... interesting, to say the least.

6  The boy with the very attractive hair seems like a very nice guy, though the scary girl in all black is clinging to him tightly. You make the safe assumption that they are dating.

--------------------------------------------------------- \n""")

time.sleep(10)

initial_friend = input("\n Who do you approach first? ")
if initial_friend == "1":
    print("\n You walk towards the brunette girl and tap her shoulder. \n You say, 'Hi! My name is " + name + ". This is my first day here at Hollywood Arts.'")
    print("\n The girl smiles and says, 'Hi " + name + "! I'm Tori Vega! I remember my first day at Hollywood Arts vividly! It didn't go so great, to be honest. But I'll help make yours the best one ever!'")
    tori_friend += 15
    print("\n Your friendship with Tori has increased by 15 points! It is now at " + str(tori_friend) + " points.")
if initial_friend == "2":
    print("\n You walk towards the boy carrying the keyboard and tap his shoulder. \n You say, 'Hi! My name is '" + name + "'. This is my first day here at Hollywood Arts.'")
    print("\n The boy smiles and says, 'Hi " + name + "! I'm Andre! Nice to meet you, and welcome to Hollywood Arts! If you ever need someone to talk to, I will always be here!'")
    andre_friend += 15
    print("\n Your friendship with Andre has increased by 15 points! It is now at " + str(andre_friend) + " points.")
if initial_friend == "3":
    print("\n You walk towards the boy with curly hair and tap his shoulder. \n You say, 'Hi! My name is " + name + ". This is my first day here at Hollywood Arts.'")
    print("\n The boy fumbles with his glasses and nervously says, 'Hi " + name + "! I'm Robbie Shapiro. Nice to meet you! This here is my best friend, Rex.'")
    print("\n You hear Rex say,'This has got to be the most awkward thing I have ever seen!' Robbie gasps and covers Rex's mouth.")
    print("\n Robbie says, 'Don't listen to him! Anyway, if you need anything, just let me know!' He quickly scampers off.")    
    robbie_friend += 10
    print("\n Your friendship with Robbie has increased by 10 points! It is now at " + str(robbie_friend) + " points.")
if initial_friend == "4": 
    print("\n You walk towards the girl wearing all black and tap her shoulder. \n You say, 'Hi! My name is " + name + ". This is my first day here at Hollywood Arts.'")
    print("\n The girl looks at you and takes another sip of your coffee. \n She says, 'I don't really care. My name is Jade. Hope to see you around school! Hopefully not.' She then walks away.")
    jade_friend += 5
    print("\n Your friendship with Jade has increased by 5 points! It is now at " + str(jade_friend) + " points.")
if initial_friend == "5":
    print("\n You walk towards the red-haired girl and tap her shoulder. \n You say, 'Hi! My name is " + name + ". This is my first day here at Hollywood Arts.'")
    print("\n The girl smiles and says, 'OMG hi " + name + "! I'm Cat!'")
    print("\n 'Like the animal?' you ask.")
    print("\n 'What is that supposed to mean??' she gasps.")
    print("\n 'Um... nothing!' you say.")
    print("\n 'Oh, okay!' Cat exclaims. 'Welcome to Hollywood Arts! Do you by any chance... have any bibble on you?'")
    cat_friend +=10
    print("\n Your friendship with Cat has increased by 10 points! It is now at " + str(cat_friend) + " points.")
if initial_friend == "6":
    print("\n You walk towards the boy with the attractive hair. \n You say, 'Hi! My name is '" + name + "'. This is my first day here at Hollywood Arts.'")
    print("\n The boy smiles and says, 'Hi " + name + "! I'm Beck! Nice to meet you, and welcome to Hollywood Arts! If you ever need someone to talk to, I will always be here!'")
    beck_friend += 15
    print("\n Your friendship with Beck has increased by 15 points! It is now at " + str(beck_friend) + " points.")

time.sleep(10)