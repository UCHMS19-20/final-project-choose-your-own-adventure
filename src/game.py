# Spaces out portions of the storyline and choices, makes it easier to read
import time

# Used at the end of the game to calculate probability of winning
import random

# Used to play music at the end of the game
import pygame

from pygame import mixer
pygame.mixer.init()

import sys

# Setting variables for friendship points to 0, will increase or decrease depending on choices
tori_friend = 0
andre_friend = 0
robbie_friend = 0
jade_friend = 0
cat_friend = 0
beck_friend = 0
sinjin_friend = 0
sikowitz_friend = 0
trina_friend = 0 
lane_friend = 0

# Variable for popularity and preparedness
popularity = 0
prepare = 0

# Setting a list for inventory that objects will be added to
inventory = []

# Introduction to game
print("\n We are pleased to inform you that you have been accepted into Hollywood Arts High School! \n")

time.sleep(5)

print("You came to the realization that engineering isn't your true calling in life, but performing arts instead! \n")

time.sleep(5)

print("Every year, Hollywood Arts hosts an event called 'The Big Showcase,' where agents and talent spotters around the country are invited. \n")

time.sleep(5)

print("It is your job to prepare a showstopping performance by the end of this week. \n")

time.sleep(5)

print("But to do this, you will need to get all of your materials together before the show. You will need to make friends and make smart choices! \n")

time.sleep(5)

print("Before you can begin your adventure in Hollywood Arts, we will need to know more about you. \n")

time.sleep(5)

# Set variable for name, will be called later in the code to address player
name = input("What is your name? ")

print("\n Hello, " + name + "!")

print("Congratulations! You have finished registration for Hollywood Arts. See you on the first day!")

time.sleep(5)

# Monday's events and choices
print("\n ---------------------------------------------------------")

print("\n MONDAY. First day at Hollywood Arts. Four more days until the Big Showcase! \n")

print("You walk into your new school, nervous. What if you don't make new friends? What if you're not talented enough? \n")

time.sleep(5)

print("""When you walk in, you see six students standing by the lockers.

\n 1  The brunette girl seems friendly and could definitely help you for your Big Showcase, though she seems almost obnoxiously confident about her talents.

\n 2  The boy holding the keyboard seems like a gifted musical prodigy, which means he could be of big help, and he looks like he could be a very supportive friend.

\n 3  The boy with curly hair seems shy and socially awkward, and he's holding this puppet that's giving you the creeps.

\n 4  The girl wearing all black gives off scary vibes. She seems very confident, which could be of help for the Big Showcase.

\n 5  The girl with fluorescent red hair always seems to be smiling, and she has a very eccentric personality. She seems... interesting, to say the least.

\n 6  The boy with the very attractive hair seems like a very nice guy, though the scary girl in all black is clinging to him tightly. You make the safe assumption that they are dating.

--------------------------------------------------------- \n""")

time.sleep(10)

# First choice, different paths depending on inputted number
# Friendship points go up, an integer is added to the variable for friendship
initial_friend = input("\n Who do you approach first? ")
if initial_friend == "1":
    print("\n You walk towards the brunette girl and tap her shoulder. \n You say, 'Hi! My name is " + name + ". This is my first day here at Hollywood Arts.'")
    print("\n The girl smiles and says, 'Hi " + name + "! I'm Tori Vega! I remember my first day at Hollywood Arts vividly! It didn't go so great, to be honest. But I'll help make yours the best one ever!'")
    tori_friend += 15
    print("\n Your friendship with Tori has increased by 15 points! It is now at " + str(tori_friend) + " points.")
if initial_friend == "2":
    print("\n You walk towards the boy carrying the keyboard and tap his shoulder. \n You say, 'Hi! My name is '" + name + ". This is my first day here at Hollywood Arts.'")
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
    print("\n The girl looks at you and takes another sip of her coffee. \n She says, 'I don't really care. My name is Jade. Hope to see you around school! Hopefully not.' She then walks away.")
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
    print("\n You walk towards the boy with the attractive hair. \n You say, 'Hi! My name is " + name + ". This is my first day here at Hollywood Arts.'")
    print("\n The boy smiles and says, 'Hi " + name + "! I'm Beck! Nice to meet you, and welcome to Hollywood Arts! If you ever need someone to talk to, I will always be here!'")
    beck_friend += 15
    print("\n Your friendship with Beck has increased by 15 points! It is now at " + str(beck_friend) + " points.")

time.sleep(10)

print("--------------------------------------------------------- \n")

print("Classes will start in an hour. You have time to roam around the school.")
print("\n You should begin looking for supplies that you will need for the Big Showcase.")
print("\n And most importantly, you should continue making new friends!")
print("""\n There are five different locations you can go to.

1  Sikowitz's classroom

2  Black box theatre

3  Outside lunch area

4  Hallway

5  Lockers

--------------------------------------------------------- \n""")

time.sleep(5)

# Another choice, different paths depending on input
# Added to friendship variable, if applicable
# Added items to inventory, if applicable
location = input("\n Where would you like to go first? ")
if location == "1":
    print("You walk into Sikowitz's classroom.")
    print("\n You see a man sitting on a stool drinking from a coconut.")
    print("\n 'Hello! I'm Mr. Sikowitz! And you are?' he says after taking another sip.")
    print("\n 'I'm " + name + ", and I'm new here at Hollywood Arts. Would you by any chance have any supplies that I could use for the Big Showcase this week?'")
    print("\n 'Of course, young duckling! Have this,' he exclaims, setting aside his coconut and stepping off his stool.")
    inventory.append("Microphone")
    inventory.append("Speakers")
    inventory.append("Coconut")
    sikowitz_friend += 10
    print("\n Congratulations! You have added to your inventory. You now have: " + str(inventory) + ".")
if location == "2":
    print("You walk into the black block theatre.")
    print("\n You see an awkward boy with curly hair standing by the lights.")
    print("\n 'Hello. I'm Sinjin,' he says creepily.")
    print("\n 'Um... hi. I'm " + name + ", and I'm new here at Hollywood Arts. Do you know where any of the supplies are kept, so I can use them for the Big Showcase? ")
    print("\n 'Of course. Have this,' he says without blinking.")
    inventory.append("Microphone")
    inventory.append("Speakers")
    inventory.append("Sinjin's phone number")
    sinjin_friend += 10
    print("\n Congratulations! You have added to your inventory. You now have: " + str(inventory) + ".")
if location == "3":
    print("You walk outside to the lunch area.")
    print("\n You see a brunette girl sitting at one of the tables by the food truck on her phone.")
    print("\n 'Hi, I'm " + name + ", and I'm new here at Hollywood Arts. Do you have anything to help me with the Big Showcase later this week?")
    print("\n 'OMG hi!! I'm Trina! THE Trina Vega. Of course I can help!! Only if you come to my show next week. It's ChicagooOOOoooO!' she sings obnoxiously.")
    inventory.append("Trina's phone number")
    inventory.append("Used napkin")
    trina_friend += 10
    print("\n Congratulations! You have added to your inventory. You now have: " + str(inventory) + ".")
if location == "4":
    print("You continue walking through the hallway.")

    # Depending on if variable for friendship is 0 (means you didn't meet that character) or > 0 (meaning you met that character) affects your interaction
    if beck_friend == 15:
        print("\n You recognize Beck from earlier, standing next to his girlfriend. She looks intimidating.")
        print("\n You call out, 'Hey Beck!'")
        print("\n He smiles and answers, 'Hey " + name + "! Jade and I were just talking about you, and we would love to help you out at the Big Showcase.'")
        print("\n 'Wow! Thank you, Beck!' you exclaim. Jade just rolls her eyes.")
        print("""\n Three ideas pop into your mind.
        
        1  Flirt with Beck
        2  Flirt with Jade
        3  Thank them and walk away
        
        --------------------------------------------------------- \n""")
        choice = input("\n What would like to do now? ")
        if choice == "1":
            print("\n Beck is so cute, you can't restrain yourself.")
            print("\n You say, 'Hey, Beck. Your shirt looks really nice today. It really matches your beautiful eyes. Talk to you later!'")
            print("\n Jade gasps and angrily stares you down as you walk away.")
            jade_friend -= 20
            beck_friend += 10
            print("\n Your friendship with Beck has increased by 10 points! It is now at " + str(beck_friend) + " points.")
            print("\n Oh no! Your friendship with Jade has decreased by 20 points! It is now at " + str(jade_friend) + " points.")
        if choice == "2":
            print("\n Jade is so pretty cute, you can't restrain yourself.")
            print("\n You say, 'Hey, Jade. Your shirt looks really nice today. It really matches your beautiful eyes. Talk to you later!'")
            print("\n Beck looks at you awkwardly. Jade smiles, but quickly hides it from Beck.")
            jade_friend += 15
            beck_friend -= 10
            print("\n Your friendship with Jade has increased by 15 points! It is now at " + str(jade_friend) + " points.")
            print("\n Oh no! Your friendship with Beck has decreased by 10 points! It is now at " + str(beck_friend) + " points.")
        if choice == "3":
            inventory.append("Costumes")
            print("\n Congratulations! You have added to your inventory. You now have: " + str(inventory) + ".")
    if jade_friend == 5:
        print("\n You recognize Jade from earlier, standing next to her boyfriend. His hair looks really soft.")
        print("\n You call out, 'Hey Jade!'")
        print("\n She turns to you and says, 'Hey " + name + "! Beck and I were just talking about you, and we decided that if you need it, we would be willing to help you for the Big Showcase, I guess.'")
        print("\n 'Wow! Thank you, Jade!' you exclaim.")
        print("\n Beck smiles at you and says, 'Of course, " + name + "! Anytime.'")
        print("""\n Three ideas pop into your mind.
        
        1  Flirt with Beck
        2  Flirt with Jade
        3  Thank them and walk away
        
        --------------------------------------------------------- \n""")
        choice = input(" \n What would you like to do now? ")
        if choice == "1":
            print("\n Beck is so cute, you can't restrain yourself.")
            print("\n You say, 'Hey, Beck. Your shirt looks really nice today. It really matches your beautiful eyes. Talk to you later!'")
            print("\n Jade gasps and angrily stares you down as you walk away.")
            jade_friend -= 20
            beck_friend += 10
            print("\n Your friendship with Beck has increased by 10 points! It is now at " + str(beck_friend) + " points.")
            print("\n Oh no! Your friendship with Jade has decreased by 20 points! It is now at " + str(jade_friend) + " points.")
        if choice == "2":
            print("\n Jade is so pretty cute, you can't restrain yourself.")
            print("\n You say, 'Hey, Jade. Your shirt looks really nice today. It really matches your beautiful eyes. Talk to you later!'")
            print("\n Beck looks at you awkwardly. Jade smiles, but quickly hides it from Beck.")
            jade_friend += 15
            beck_friend -= 10
            print("\n Your friendship with Jade has increased by 15 points! It is now at " + str(jade_friend) + " points.")
            print("\n Oh no! Your friendship with Beck has decreased by 10 points! It is now at " + str(beck_friend) + " points.")
        if choice == "3":
            inventory.append("Costumes")
            print("\n Congratulations! You have added to your inventory. You now have: " + str(inventory) + ".")
    if beck_friend == 0 and jade_friend == 0:
        print("\n You catch the girl in black making out with the boy with the attractive hair. They seem like such interesting people. You should have spoken with one of them before.")
if location == "5":
    print("You walk over to the lockers.")

    # Depending on if variable for friendship is 0 (means you didn't meet that character) or > 0 (meaning you met that character) affects your interaction
    if tori_friend == 15:
        print("\n You recognize Tori from earlier, standing by her locker.")
        print("\n You call out, 'Hey Tori!'")
        print("\n She turns to you, smiles, and says, 'Hey " + name + "! How are you?")
        print("\n 'I'm good, thanks! Wow, I love your locker!' you exclaim.")
        print("\n 'Thanks! Have you decorated yours yet? It's a Hollywood Arts tradition!' Tori giggles.")
        print("\n 'I will soon. See you around, Tori!' you say before turning to leave to class.")
        print("\n 'Oh, wait! Here, have this. It'll help you for at the Big Showcase,' she says.")
        inventory.append("Costumes")
        inventory.append("Art supplies")
        print("\n Congratulations! You have added to your inventory. You now have: " + str(inventory) + ".")
    else: 
        print("\n You see a brunette girl standing by her locker. You remind yourself that you should be making more friends.")
        print("\n You call out, 'Hello! I'm " + name + "! What's your name?")
        print("\n She turns to you, smiles, and says, 'Hey " + name + "! I'm Tori. How are you?")
        print("\n 'I'm good, thanks! Wow, I love your locker!' you exclaim.")
        print("\n 'Thanks! You must be new. Have you decorated your locker yet? It's a Hollywood Arts tradition!' Tori giggles.")
        print("\n 'I will soon. See you around, Tori!' you say before turning to leave to class.")
        print("\n 'Oh, wait! Here, have this. It'll help you for at the Big Showcase,' she says.")
        tori_friend += 3
        inventory.append("Speakers")
        inventory.append("Art supplies")
        print("\n Congratulations! You have added to your inventory. You now have: " + str(inventory) + ".")

time.sleep(5)

print("--------------------------------------------------------- \n")

print("You go to your only class of the day: Improvisation. Next thing you know, Monday is over!")
print("\n Your adventures at Hollywood Arts will continue tomorrow, on Tuesday.")

time.sleep(5)

# Tuesday's events and choices
print("\n ---------------------------------------------------------")

print("\n TUESDAY. Second day at Hollywood Arts. Three more days until the Big Showcase! \n")

print("You walk inside, ready for today's adventures. Who will you befriend? Who will you anger? The drama!!! \n")

time.sleep(5)

print("""\n There are four different locations you can go to.

1  Janitor's closet

2  Guidance counselor's office

3  Sikowitz's classroom

4  Black box theatre

--------------------------------------------------------- \n""")

time.sleep(10)

# Another choice, more complex because different pathways depend on whether or not friendship variable = 0 or > 0
location2 = input("\n Where would you like to go first? ")
if location2 == "1":
    print("You walk into the janitor's closet, out of pure curiousity. Maybe you'll make friends with someone in there. Who knows?")
    print("\n Sure enough, when you open the door, you find someone sitting in the corner munching on something.")
    if cat_friend == 10:
        print("\n You recognize her as the girl you met before... Cat!")
        print("\n 'Cat...' you say. She turns around. She grins when she sees you.")
        print("\n 'OMG hi " + name + "! Do you want to try some bibble? It's so good!")
        bibble = input("""\n Three ideas pop into your mind.

        1  Take the bibble

        2  Tell her that she should probably stop eating bibble

        3  Walk out of the janitor's closet

        --------------------------------------------------------- \n""")
        bibble = input("\n What will you do? ")
        if bibble == "1":
            print("\n You decide to try some bibble. If Cat is eating it all the time, it has to be good, right?")
            print("\n 'OMG yay!' she giggles, handing you a handful of bibble.")
            print("\n You put the bibble in your mouth and... wOw, that's good!")
            print("\n 'Wow... Cat... this is so good! Give me another handful!' you laugh.")
            print("\n 'I know right!' Cat giggles. You and Cat spend the rest of the morning eating bibble in the janitor's closet.")
            cat_friend += 20
            inventory.append("Bag of bibble")
            print("\n Your friendship with Cat has increased by 20 points! It is now at " + str(cat_friend) + " points.")
            print("\n Congratulations! You have added to your inventory. You now have: " + str(inventory) + ".")
        if bibble == "2":
            print("\n This is too much. Cat is addicted to bibble. You have to help her.")
            print("\n 'Cat... I think you should stop eating bibble! You're obsessed! Look at you! You're in the janitor's closet for crying out loud! You have to stop,' you say.")
            print("\n 'Oh... but it's so goOD!' Cat cries out.")
            print("\n You do what needs to be done. You grab the bag of bibble out of Cat's hand.")
            print("\n 'Hey! Give it back!' Cat shouts, on the verge of tears.")
            print("\n Determined to help Cat overcome her addiction, you run out the janitor's closet and throw it into the trash can. It's for her own good.")
            cat_friend -= 5
            print("\n Oh no! Your friendship with Cat has decreased by 5 points! It is now at " + str(cat_friend) + " points.")
        if bibble == "3":
            print("\n You decide that this is too strange for your liking. You leave the janitor's closet.")
    else:
        print("\n A girl with fluorescent red hair is sitting on the floor with a bag of bibble.")
        print("\n 'Hello...' you start to say. She turns around. She grins when she sees you.")
        print("\n 'OMG hi! I'm Cat! Do you want to try some bibble? It's so good!")
        print("\n 'Oh, like the animal?' you joke.")
        print("\n 'What is that supposed to mean??' she gasps.")
        print("\n 'Nothing... sorry. I'm " + name + ",' you reply.")
        print("\n 'Anyway... OMG do you want to try some bibble?' Cat asks with a grin.")
        print("""\n Three ideas pop into your mind.

        1  Take the bibble

        2  Tell her that she should probably stop eating bibble

        3  Walk out of the janitor's closet

        --------------------------------------------------------- \n""")
        bibble = input("\n What will you do? ")
        if bibble == "1":
            print("\n You decide to try some bibble.")
            print("\n 'OMG yay!' she giggles, handing you a handful of bibble.")
            print("\n You put the bibble in your mouth and... wOw, that's good!")
            print("\n 'Wow... Cat... this is so good! Give me another handful!' you laugh.")
            print("\n 'I know right!' Cat giggles. You and Cat spend the rest of the morning eating bibble in the janitor's closet.")
            cat_friend += 20
            inventory.append("Bag of bibble")
            print("\n Your friendship with Cat has increased by 20 points! It is now at " + str(cat_friend) + " points.")
            print("\n Congratulations! You have added to your inventory. You now have: " + str(inventory) + ".")
        if bibble == "2":
            print("\n You notice that the entire bag is almost empty. She ate a whole 5 pounds of bibble already!")
            print("\n 'Cat... I think you should stop eating bibble! You're obsessed! Look at you! You're in the janitor's closet for crying out loud! You have to stop,' you say.")
            print("\n 'Oh... but it's so goOD!' Cat cries out.")
            print("\n You do what needs to be done. You grab the bag of bibble out of Cat's hand.")
            print("\n 'Hey! Give it back!' Cat shouts, on the verge of tears.")
            print("\n Determined to help Cat overcome her addiction, you run out the janitor's closet and throw it into the trash can. It's for her own good.")
            cat_friend -= 5
            print("\n Oh no! Your friendship with Cat has decreased by 5 points! It is now at " + str(cat_friend) + " points.")
        if bibble == "3":
            print("\n You decide that this is too strange for your liking. You leave the janitor's closet.")
if location2 == "2":
    print("\n You walk into the guidance counselor's office.")
    print("\n 'Hi, I'm Lane!' the counselor greets you as you walk in. 'And you are " + name + ", correct?'")
    print("\n 'That's me!' you say with a smile. You decided to come to the counselor's office because you were feeling quite overwhelmed with this whole Big Showcase. You sit down and tell him why you're feeling stressed.")
    print("\n 'It is perfectly normal to feel nervous about your first big performance at a new school. It's frigtening, I understand. But I need you to take a deep breath and realize that every single student here at Hollywood Arts has gone through the same thing,' Lane explains.")
    print("\n You smile. He's right. You're not alone.")
    print("\n 'Have you made some friends yet?' he asks, leaning back in his chair.")
    
    # Depending on whether friendship variable = 0 or > 0 affects whether text is printed, represents whether or not you met a character in your past choices
    if tori_friend > 0:
        print("\n 'I met Tori, and she seems like such a nice person! I'm really glad that I met her,' you say.")
        print("\n 'Good. She's a good friend. And she'll definitely help you at the Big Showcase,' Lane responds.")
    if andre_friend > 0:
        print("\n 'I met Andre, and he seems like such a nice friend! I'm really glad that I met him,' you say.")
        print("\n 'Good. He's a good person. And very talented, too. And he'll definitely help you at the Big Showcase,' Lane responds.")
    if robbie_friend > 0:
        print("\n 'I met Robbie, and he seems cool. Though he always seems to have that puppet on him...' you say.")
        print("\n 'We're working on it,' Lane says, rubbing his temples. 'But that's good. Robbie's a good friend. He'll definitely help you at the Big Showcase.'")
    if jade_friend > 0: 
        print("\n 'I met Jade, and she seems cool. A little scary and standoff-ish, but cool,' you say.")
        print("\n Lane takes a deep breath. 'She's a tough cookie. Be careful, promise me. But other than that, she'll definitely help you at the Big Showcase.'")
    if cat_friend > 0:
        print ("\n 'I met Cat, and she seems fun. Though she's always eating that bibble,' you laugh.")
        print("\n 'We're working on it,' Lane says, rubbing his temples. 'But that's good. She's extremely talented. She'll help you at the Big Showcase.'")
    if beck_friend > 0:
        print("\n 'I met Beck, and he seems like such a nice person! I'm really glad that I met him,' you say.")
        print("\n 'Good. He's a nice friend to have. Just... be careful of his girlfriend. That's all,' Lane responds.")
    if sinjin_friend > 0:
        print("\n 'I met Sinjin... he's...'")
        print("\n 'Weird, I know,' Lane finishes. 'Despite that, he'll be of great help for the technical behind-the-scenes action for your Big Showcase.'")
    if sikowitz_friend > 0:
        print("\n 'I met Sikowitz, and he seems like such a great teacher. Plus, his coconuts taste great, not gonna lie,' you say.")
        print("\n 'Good, he's a good friend of mine as well,' Lane says with a smile. 'He's a very talented, yet quirky, instructor. He will definitely help you this Friday for your Big Showcase.'")
    if trina_friend > 0:
        print("\n 'I met Trina, and she's...'")
        print("\n 'Nothing like her sister,' Lane sighs. 'Definitely try to see if you can meet some more people at Hollywood Arts. More talented people.'")
    print("\n 'Well, I hope this session helped a bit to calm your nerves!' Lane says finally, getting up from his seat.")
    print("\n You definitely feel a lot better now. You got this! As long as you have your friends by your side, your show on Friday will be fantastic! You thank Lane for his time and leave his office.")
    lane_friend += 5
if location2 == "3":
    if sikowitz_friend == 0:
        print("You walk into Sikowitz's classroom.")
        print("\n You see a man sitting on a stool drinking from a coconut.")
        print("\n 'Hello! I'm Mr. Sikowitz! And you are?' he says after taking another sip.")
        print("\n 'I'm " + name + ", and I'm new here at Hollywood Arts. Would you by any chance have any supplies that I could use for the Big Showcase this week?'")
        print("\n 'Of course, young duckling! Have this,' he exclaims, setting aside his coconut and stepping off his stool.")
        inventory.append("Microphone")
        inventory.append("Speakers")
        inventory.append("Coconut")
        sikowitz_friend += 10
        print("\n Congratulations! You have added to your inventory. You now have: " + str(inventory) + ".")
    else:
        print("You walk into Sikowitz's classroom.")
        print("\n Sikowitz spots you entering, and with a big smile he exclaims, " + name + "! My favorite student! What brings you here today?'")
        print("\n 'Just wanted to say hello again to my favorite teacher at Hollywood Arts!' you say.")
        print("\n Sikowitz blushes. 'Thank you, thank you...'")
        print("\n He pauses for a moment. 'I've been thinking. I really like you, " + name + ". You have potential. And I want to help you for your Big Showcase.'")
        print("\n 'That's awesome, thank you!' you say, grateful. Going to Sikowitz's classroom yesterday before first period definitely paid off!")
        print("\n 'Make sure you decorate your locker by Friday. It will help you gain popularity, which is very important for Friday's performance. Especially with talent spotters watching,' he says, leaning in.")
        print("\n 'Wow, thank you, Sikowitz. Noted,' you answer, smiling.")
        print("\n 'I believe in you! Here, have this. For good luck,' Sikowitz says with a wink.")
        inventory.append("Art supplies")
        inventory.append("A really big coconut")
if location2 == "4":
    print("You walk into the black box theatre.")
    if robbie_friend == 10:
        print("\n You recognize Robbie sitting in the front row with Rex on his lap. You walk over to him.")
        print("\n 'Hey Robbie!' you say, sitting down next to him.")
        print("\n 'Hey " + name + "! I was just telling Rex here how I was going to go find you and ask how your second day at Hollywood Arts is going!'")
        print("\n 'Nah... you just wanted to get the new kid to be your friend so that you would actually have a friend,' Rex says.")
        print("\n Robbie gasps and covers Rex's mouth. 'Lies...' Robbie mutters.")
    else: 
        print("\n You see a curly-haired boy sitting in the front row with a puppet on his lap. You walk over to him.")
        print("\n 'Hi, I'm " + name + "!' you introduce yourself. The boy turns to face you.")
        print("\n 'H-hi... I'm Robbie!' he says.")
        print("\n 'Excuse him, he's socially awkward,' Rex blurts out.")
        print("\n 'Am not!' Robbie gasps.")
        print("\n 'Are too!' Rex blurts back.")
    print("""\n Three ideas pop into your mind.

    1  Tell Robbie that you think that him having a puppet is weird

    2  Talk to Rex

    3  Walk out of the theatre

    --------------------------------------------------------- \n""")
    rex = input("\n What will you do? ")
    if rex == "1":
        print("\n This is strange. You decide to be brutally honest to Robbie.")
        print("\n 'Robbie, don't you think it's weird that you have this puppet?' you say.")
        print("\n Robbie gasps. 'He's not just a puppet, he's my friend!'")
        print("\n 'I'm no puppet!' Rex adds.")
        robbie_friend -= 10
        print("\n Oh no! Your friendship with Robbie has decreased by 10 points! It is now at " + str(robbie_friend) + " points.")
    if rex == "2":
        print("You decide to be nice to Robbie... and Rex.")
        print("'Hi Rex!' you say with a smile.")
        print("'Hello Robbie's friend! Nice to meet ya,' Rex replies. Robbie smiles back at you.")
        robbie_friend += 10
        print("\n Your friendship with Robbie has increased by 10 points! It is now at " + str(robbie_friend) + " points.")
    if rex == "3":
        print("\n This is strange. You don't really want to be here right now. You turn around and leave the theatre.")

time.sleep(5)

print("--------------------------------------------------------- \n")

# Depending on friendship variable, other friendship variables increase or decrease
# New variable introduced for player's best friend, will be called later in game for a more personalized customization
if cat_friend > 19:
    print("You spend the next half hour in the janitor's closet eating bibble with Cat. You check your watch, and -- oh no! You're late to Sikowitz's class!")
    print("\n You turn to face Cat. 'We're late for class!' you say, frantically getting your things together. Quickly, you and Cat gather up your bibble and run to Sikowitz's class.")
    print("\n As you two walk into Sikowitz's classroom, you know something is wrong.")
    print("\n 'Cat. " + name + ". You two are late! Minus fifteen points for classroom participation today!' Sikowitz shouts as he sets his coconut down.")
    print("\n You sigh. Second day at Hollywood Arts and you have already gotten yourself into some trouble.")
    sikowitz_friend -= 30
    best_friend = "Cat"
else: 

    # New list created for potential best friends, items will be added to this list only if friendship variable > 0
    print("It is now your second day here at Hollywood Arts. You have already gotten to know some of the people here. It is now time to decide who you would like to get closer to.")
    print("\n Here are all the people you like so far.")
    possible_best_friends = []
    if tori_friend > 0:
        possible_best_friends.append("Tori")
    if andre_friend > 0:
        possible_best_friends.append("Andre")
    if beck_friend > 0:
        possible_best_friends.append("Beck")
    if jade_friend > 0:
        possible_best_friends.append("Jade")
    if cat_friend > 0:
        possible_best_friends.append("Cat")
    if robbie_friend > 0:
        possible_best_friends.append("Robbie")
    print(possible_best_friends)

    # Make sure input is valid, must be one of the main characters
    while True:
        best_friend = input("\n Who would you like to become closer to? Make sure you spell their name correctly; after all, he or she is going to be your new BFF! ")
        if best_friend not in ("Tori", "Andre", "Beck", "Jade", "Cat", "Robbie"):
            print("Silly goose! That person doesn't go to Hollywood Arts! Pick someone else")    
        else:
            print("Congratulations! Your new BFF at Hollywood Arts is " + str(best_friend) + "!")
            break
        
time.sleep(5)

print("--------------------------------------------------------- \n")

print("You go to your next class of the day: Ballet dance. Next thing you know, Tuesday is over!")
print("\n Your adventures at Hollywood Arts will continue tomorrow, on Wednesday.")

time.sleep(5)

# Wednesday's events and choices
print("\n ---------------------------------------------------------")

print("\n WEDNESDAY. Third day at Hollywood Arts. Two more days until the Big Showcase! \n")

print("What exciting things will happen today at school? Are you ready for Friday's performance? Do you have what it takes? \n")

time.sleep(5)

print("""\n There are four different locations you can go to.

1  Sikowitz's classroom

2  Guidance counselor's office

3  Black box theatre

4  Outdoor eating area

---------------------------------------------------------\n """)

# Depending on if variable for friendship is 0 (means you didn't meet that character) or > 0 (meaning you met that character) affects your interaction
location3 = input("\n Where would you like to go first? ")
if location3 == "1":
    print("\n You walk into Sikowitz's classroom")
    if sikowitz_friend < 0:
        print("\n Sikowitz turns to face you, and he puts his coconut down. '"+ name + ". I've been meaning to speak to you.'")
        print("\n This is probably about the incident with Cat. You gained a very close friend from the experience, and a bag of bibble, but at what cost?")
        print("\n 'I'm sorry...' you start to say, but Sikowitz cuts you off.")
        print("\n 'It's not just about that, " + name + ". It's also about your grades. I'm worried about you. You need to step it up, especially if you want a shot at making it big after Hollywood Arts.'")
        print("\n 'I understand,' you reply.")
        print("\n 'I want you practicing for your Big Showcase, which is in two days! No more cadoodling. Got it?' Sikowitz asks.")
        print("\n You nod. You thank Sikowitz for his time and turn to leave. Time to turn your life around!")
    if sikowitz_friend == 0 or sikowitz_friend > 0: 
        print("\n Sikowitz turns to face you and grins when he sees you walk in. '" + name + "! Good to see you! I've been meaning to speak to you!'")
        print("\n 'About what?' you ask, taking a seat.")
        print("\n Sikowitz hands you a coconut. 'I wanted to give you the contact information of one of the talent spotters who is going to be here on Friday.'")
        print("\n 'No way!' you say in-between sips.")
        print("\n 'Yes way!' Sikowitz laughs, handing you a piece of paper. 'This is his phone number. Please: make a good impression on him this Friday. It's crucial. Have you started preparing?'")
        print("\n 'A little,' you respond.")
        print("\n 'Then go, my duckling! Practice! Prepare! I cannot wait to see what you're capable of!' Sikowitz says with a grin.")
        print("\n You nod, beaming. You thank Sikowitz for his time and turn to leave. Time to make this the best show ever!")
        inventory.append("Talent spotter's phone number")
        print("\n Congratulations! You have added to your inventory. You now have: " + str(inventory) + ".")
if location3 == "2":
    print("\n You walk into the guidance counselor's office.")
    if lane_friend == 0:
        print("\n 'Hi, I'm Lane!' the counselor greets you as you walk in. 'And you are " + name + ", correct?'")
        print("\n 'That's me!' you say with a smile. You decided to come to the counselor's office because you were feeling quite overwhelmed with this whole Big Showcase. You sit down and tell him why you're feeling stressed.")
        print("\n 'It is perfectly normal to feel nervous about your first big performance at a new school. It's frigtening, I understand. But I need you to take a deep breath and realize that every single student here at Hollywood Arts has gone through the same thing,' Lane explains.")
        print("\n You smile. He's right. You're not alone.")
        print("\n 'Have you made some friends yet?' he asks, leaning back in his chair.")
        if tori_friend > 0:
            print("\n 'I met Tori, and she seems like such a nice person! I'm really glad that I met her,' you say.")
            print("\n 'Good. She's a good friend. And she'll definitely help you at the Big Showcase,' Lane responds.")
        if andre_friend > 0:
            print("\n 'I met Andre, and he seems like such a nice friend! I'm really glad that I met him,' you say.")
            print("\n 'Good. He's a good person. And very talented, too. And he'll definitely help you at the Big Showcase,' Lane responds.")
        if robbie_friend > 0:
            print("\n 'I met Robbie, and he seems cool. Though he always seems to have that puppet on him...' you say.")
            print("\n 'We're working on it,' Lane says, rubbing his temples. 'But that's good. Robbie's a good friend. He'll definitely help you at the Big Showcase.'")
        if jade_friend > 0: 
            print("\n 'I met Jade, and she seems cool. A little scary and standoff-ish, but cool,' you say.")
            print("\n Lane takes a deep breath. 'She's a tough cookie. Be careful, promise me. But other than that, she'll definitely help you at the Big Showcase.'")
        if cat_friend > 0:
            print ("\n 'I met Cat, and she seems fun. Though she's always eating that bibble,' you laugh.")
            print("\n 'We're working on it,' Lane says, rubbing his temples. 'But that's good. She's extremely talented. She'll help you at the Big Showcase.'")
        if beck_friend > 0:
            print("\n 'I met Beck, and he seems like such a nice person! I'm really glad that I met him,' you say.")
            print("\n 'Good. He's a nice friend to have. Just... be careful of his girlfriend. That's all,' Lane responds.")
        if sinjin_friend > 0:
            print("\n 'I met Sinjin... he's...'")
            print("\n 'Weird, I know,' Lane finishes. 'Despite that, he'll be of great help for the technical behind-the-scenes action for your Big Showcase.'")
        if sikowitz_friend > 0:
            print("\n 'I met Sikowitz, and he seems like such a great teacher. Plus, his coconuts taste great, not gonna lie,' you say.")
            print("\n 'Good, he's a good friend of mine as well,' Lane says with a smile. 'He's a very talented, yet quirky, instructor. He will definitely help you this Friday for your Big Showcase.'")
        if trina_friend > 0:
            print("\n 'I met Trina, and she's...'")
            print("\n 'Nothing like her sister,' Lane sighs. 'Definitely try to see if you can meet some more people at Hollywood Arts. More talented people.'")
        print("\n 'Well, I hope this session helped a bit to calm your nerves!' Lane says finally, getting up from his seat.")
        print("\n You definitely feel a lot better now. You got this! As long as you have your friends by your side, your show on Friday will be fantastic! You thank Lane for his time and leave his office.")
        lane_friend += 5
    if lane_friend > 0:
        print("\n 'Hey Lane,' you say as you walk in.")
        print("\n 'Hey " + name + "! How are you?'")
        print("\n 'I'm doing good,' you respond. 'Just a little nervous about this Friday.'")
        print("\n 'Understandable,' Lane replies. 'Have you gotten a little closer to anyone the past couples of days?")
        if tori_friend > 15:
            print("\n 'I've gotten pretty close to Tori. She's so nice and talented... she's honestly such an amazing friend.")
        if andre_friend > 15:
            print("\n 'I've gotten pretty close to Andre. He's so nice and friendly... and I know how talented he is. He's such a great friend.'")
        if beck_friend > 15:
            print("\n 'I've gotten pretty close to Beck. He's really nice.'")
        if jade_friend > 15:
            print("\n 'I've gotten pretty close to Jade. She seems intimidating at first, but she's actually so chill to be around.'")
        if cat_friend > 15:
            print("\n 'I've gotten pretty close to Cat. She's so funny and friendly, and plus, she's introduced me to a very delicious snack.'")
        if robbie_friend > 15: 
            print("\n 'I've gotten pretty close to Robbie. He's super chill and nice.'")
        else:
            print("\n 'To be honest, I haven't really gotten the chance to get close with anyone.'")
        print("\n 'Great,' Lane replies, nodding as he listens to you. 'I wish you all the luck for Friday's performance. Remember: continue to make friends and make smart choices!'")
        print("\n You thank Lane for his wise words before heading out.")
if location3 == "3":
    print("\n You walk into the black box theatre.")
    if andre_friend == "0":
        print("\n You see a boy sitting at the far right, strumming on his guitar. You decide to make a new friend.")
        print("\n 'Hello!' you say with a smile as you approach him. The boy looks up and grins.")
        print("\n 'Hi, I'm Andre! You're new here, aren't you?' he asks.")
        print("\n You nod. 'I'm " + name + ". My Big Showcase is this Friday and I'm a little nervous.'")
    else:
        print("\n You recognize Andre from earlier sitting at the far right, strumming on his guitar.")
        print("\n 'Hey Andre!' you call out as you approach him.")
        print("\n 'Hey " + name + "! How it's going?' Andre asks.")
        print("\n 'To be honst, I'm a little nervous about my Big Showcase this Friday,' you confess.")
        print("\n 'Don't fret!' Andre assures you. 'Everything will be okay. In fact, have you chosen a song yet for the Big Showcase?'")
        print("\n You realize that you haven't even chosen a song yet! 'Actually... no,' you say, worried.")
        print("\n 'Hey! Don't worry about it,' Andre says with a smile. 'I've been working out some chords for some songs. You can also borrow some of my instruments for Friday.'")
        print("\n 'Wow, thank you!' you say. 'How can I ever repay you?'")
        print("\n 'Don't worry about it!' Andre laughs. 'Just have fun and put on a great performance!")
        inventory.append("Andre's sheet music")
        inventory.append("Instruments")
        andre_friend += 30
        print("\n Congratulations! You have added to your inventory. You now have: " + str(inventory) + ".")
        print("\n Your friendship with Andre has increased by 30 points! It is now at " + str(andre_friend) + " points.")
if location3 == "4":
    print("\n You walk outside to the lunch area.")
    print("\n You realize that you're hungry and want to get a snack before your next class?")
    print("""\n Here are the two food items you can buy from the food truck:

    1  Burrito

    2  Salad

    --------------------------------------------------------- \n""")

    food = input("\n What would you like to get? ")
    if food == "1":
        print("\n You decide to get a burrito. You take a bite from it; it's delicious. You turn to find a table to sit at.")
    if food == "2":
        print("\n You decide to get a salad. Keeping it healthy! You take a forkful from it; it's delicious. You turn to find a table to sit at.")
    print("\n 'Hey " + name + "! How are you?'")
    print("\n You turn around to see who called your name. You smile when you see that it is " + best_friend + ".")
    print("\n 'So what do you have next class?' " + best_friend + " asks, sitting down next to you.")
    print("\n 'Math,' you groan. 'Such a boring class.'")
    print("\n 'Yikes. Boring! Well, have fun! See you after school!' " + best_friend + "says as you two finish up your lunch.")

time.sleep(5)

print("--------------------------------------------------------- \n")

print("You go to your next class of the day: Math class. The day is almost over!")

print("--------------------------------------------------------- \n")

time.sleep(5)

print("\n As you leave math class, you spot " + best_friend + " in the hallway.")
print("\n 'Hey " + name + "!' " + best_friend + " calls out.")
if best_friend == "Cat":
    print("\n 'Got any bibble?' she asks.")
    print("\n You laugh. 'You bet!'")
    print("The two of you walk together into the hallway.")
else:
    print("\n 'You ready for Friday's performance? " + best_friend + " asks.")
    print("\n 'I think so... though I still have to do a full run-through,' you confess.")
    print("\n The two of you continue walking through the hallway.")

print("""\n There are two different locations you can go to.

1  Guidance counselor's office

2  Sikowitz's classroom

--------------------------------------------------------- \n""")
location4 = input("\n What will you do? ")
if location4 == "1":
    print("\n You walk into the guidance counselor's office.")
    if lane_friend == "0":
        print("\n 'Hello!' the guidance counselor says as you walk in. 'I'm Lane. I don't think we've met yet this year. And you are?'")
        print("\n 'Hi!' you say. 'I'm " + name + ". This is my third day here. My Big Showcase is coming up this Friday, so I've been looking forward to that!'")
        print("\n 'Awesome!' Lane says, leaning back in his chair. 'I know that your performance will be phenomenal.'")
    else:
        print("\n 'Hey Lane!' you call out as you walk in.")
        print("\n 'Hey " + name + "! Good to see you back here.")
    print("\n 'So, have you gotten close with any of your friends?")
    print("\n 'Yes,' you reply. 'I've gotten really close with " + best_friend + "! We eat lunch together now, and we've been spending some time together.'")
    
    # Depending on the input for best friend, certain text will be printed
    if best_friend == "Jade":
        print("\n 'Jade is... interesting, to say the least. But it's good that you've gotten close with her, and gotten on her good side,' Lane says, putting on some lotion.")
    if best_friend == "Tori":
        print("\n 'Tori! Good! She's a nice person,' Lane says, putting on some lotion.")
    if best_friend == "Cat":
        print("\n 'Cat! She's... interesting. But it's good that you've gotten close with her,' Lane says, putting on some lotion.")
    if best_friend == "Andre":
        print("\n 'Andre! He's a very good friend,' Lane says, putting on some lotion.")
    if best_friend == "Robbie":
        print("\n 'Robbie! He's... interesting. But it's good that you've found someone,' Lane says, putting on some lotion.")
    if best_friend == "Beck":
        print("\n 'Beck! He's a very chill, nice dude. A good friend to have,' Lane says, putting on some lotion.")
    if andre_friend > 25:
        print("\n 'Also, Andre has been of great help. He's helping me so much for Friday's performance,' you add.")
        print("\n 'That's awesome,' Lane says. 'He is a very talented friend to have.'")
    print("\n 'Well, thank you for coming in! Again, good luck for Friday!' Lane calls out.")
    print("\n 'Thank you!' you grin.")
    print("\n 'Oh! One more thing. Have this. My gift to you,' Lane says.")
    inventory.append("Lotion from Lane")
    print("\n Congratulations! You have added to your inventory. You now have: " + str(inventory) + ".")
if location4 == "2":
    print("\n You walk into Sikowitz's classroom.")
    if sikowitz_friend < 0:
        print("\n 'Hello, " + name + ". I'm heading out for lunch now. I'm sorry, I will not be able to stay to talk, Sikowitz says as he puts his coconut away.")
        print("\n You sigh as he leaves the room. It seems like you will not be getting much of Sikowitz's help for the Big Showcase.")
        time.sleep(3)
        print("\n You step out, and see Cat skipping through the hallway.")
        print("\n 'Hey Cat!' you call out with a smile.")
        print("\n 'Hellooo " + name + "! Guess what??' she squeals.")
        print("\n 'What?' you ask.")
        print("\n 'I got you some sheet music and instruments and even some backup singers and musicians to help you at the Big Showcase!' she exclaims.")
        print("\n 'No way!' you laugh. You give Cat a big hug. You may not have received Sikowitz's help, but Cat's got your back!")
        inventory.append("Cat's Sheet Music")
        print("\n Congratulations! You have added to your inventory. You now have: " + str(inventory) + ".")
    else: 
        print("\n 'Hello " + name + "!!' Sikowitz cheers as you walk in.")
        print("\n 'Big Showcase is in two days, huh? Have you gotten any sheet music ready?' Sikowitz asks.")
        if "Andre's Sheet Music" in inventory:
            print("\n 'Andre wrote me amazing sheet music,' you exclaim.")
        if "Cat's Sheet Music" in inventory:
            print("\n 'Cat got me awesome sheet music,' you say with a smile.")
        else: 
            print("\n 'Unfortunately, I haven't started,' you say with a sigh.")
            print("\n Sikowitz sighs. 'You should have spoken with either Andre or Cat. They would have helped a lot.'")
            print("\n 'But that's okay!' Sikotitz says loudly. 'You have time! But not much...'")
            print("\n 'Thank you, noted,' you say as you turn to leave.")

time.sleep(5)

print("--------------------------------------------------------- \n")

print("You go to your last class of the day: Theatrical Makeup. Next thing you know, Wednesday is over!")
print("\n Your adventures at Hollywood Arts will continue tomorrow, on Thursday.")

time.sleep(5)

# Thursday's events and choices
print("\n ---------------------------------------------------------")

print("\n THURSDAY. Fourth day at Hollywood Arts. One more day until the Big Showcase! Woohoo! \n")

print("\n Today, you will need to begin practicing for tomorrow's performance! You got this! Continue to make smart choices.")

time.sleep(5)

print("""\n Before class starts, you can do one of two things:

1  Decorate your locker

2  Practice for the Big Showcase

---------------------------------------------------------\n """)

print("\n You know that the smart thing to do here is practice, since your performance is tomorrow. But, you know you can always practice at home. You can gain some popularity if you get your locker decorated!")
prep = input("\n What would you like to do? ")
if prep == "1":
    print("\n You decide to decorate your locker!")
    if "Art supplies" in inventory:
        print("\n Good thing you made some friends that past few days! You use the art supplies you have in your inventory to begin decorating the best locker ever!")
        popularity += 30
    else:
        print("\n Unfortunately, you weren't able to ask any friends to borrow some art supplies; you should've been more outgoing and talked to more people! Nevertheless, you begin work on your locker.")
        popularity += 15
    print("\n After half an hour goes by, your locker is done!")
    print("\n Congratulations! Your popularity at Hollywood Arts has increased! It is now at " + str(popularity) + " points.")
if prep == "2":
    print("\n You decide to practice your chosen song for the Big Showcase in the black box theatre. You know that an undecorated locker may cost you popularity, but being prepared for tomorrow's performance is worth it!")
    popularity -= 5
    prepare += 30
    print("\n Oh no! Your popularity at Hollywood Arts has decreased! It is now at " + str(popularity) + " points.")
    print("\n Congratulations! Your preparedness for your performance has increased! It is now at " + str(prepare) + " points.")

print("--------------------------------------------------------- \n")

print("You go to your first class of the day: Scriptwriting. The day is almost over!")

print("--------------------------------------------------------- \n")

time.sleep(5)

print("\n After class, you head outside to eat lunch. You spot " + best_friend + " as you grab a burrito from the food truck.")
print("\n 'Hey " + name + "!' " + best_friend + " calls out.")
print("\n You wave and join " + best_friend + " at a table.")
print("\n 'You ready for your Big Showcase?' " + best_friend + " asks.")
print("\n You nod. 'Now, all I need is a backup singer!'")
print("\n 'OMG!' " + best_friend + " squeals. 'I would love to be your backup singer!'")
if best_friend == "Beck":
    print("\n 'Are you sure you feel comfortable singing? I know you don't sing often, Beck,' you say.")
    print("\n 'No, it's fine, I got this!' Beck replies calmly.")
    print("\n 'Okay then! Thank you, thank you, thank you!' you reply, giving him a hug.")
if best_friend == "Robbie":
    print("\n 'Are you sure you feel comfortable singing? I know you don't sing often, Robbie,' you say.")
    print("\n 'No, it's fine, I got this!' Robbie replies calmly.")
    print("\n 'Okay then! Thank you, thank you, thank you!' you reply, giving him a hug.")
if best_friend == "Andre":
    print("\n 'I can also do some of the piano, if you would like,' Andre adds.")
    print("\n 'That would be amazing! Thank you, Andre!' you reply, giving him a hug.")
if best_friend == "Jade":
    print("\n 'I got the alto parts,' Jade adds.")
    print("\n 'Awesome! Thank you again, Jade!' you reply, giving her a small hug.")
if best_friend == "Tori":
    print("\n 'I remember my Big Showcase like it was just yesterday...' Tori says, gazing off into the distance.")
    print("\n 'Okay...' you reply. 'Well, the past is in the past! It's my time to shine now!'")
if best_friend == "Cat":
    print("\n 'This is going to be fuUUuuUn!' Cat sings.")
    print("\n 'It sure is!' you laugh, giving her a hug.")

time.sleep(5)

print("--------------------------------------------------------- \n")

print("You go to your last class of the day: Vocal Music. Next thing you know, Thursday is over!")
print("\n Your adventures at Hollywood Arts will continue tomorrow, on Friday.")

time.sleep(5)

# Friday's events and choices
print("\n ---------------------------------------------------------")

print("\n FRIDAY. Fifth day at Hollywood Arts. IT'S SHOWTIME! \n")

print("\n Today is the big day! You get a good night's sleep, a hearty breakfast, and a big kiss from your mom before coming to school.")

time.sleep(5)

print("\n Classes goes by in a blur. Next thing you know, it's time for the Big Showcase!")

if lane_friend > 0:
    print("\n Because you met with Lane during the week, you are feeling calm and prepared.")
    prepare += 20 
    print("\n Congratulations! Your preparedness for your performance has increased! It is now at " + str(prepare) + " points.")
if sikowitz_friend > 0:
    print("\n Because you met with Sikowitz during the week, you now already have special connections with a few of the talent spotters and agents in the audience.")
    print("\n You notice a few talent spotters perk up when they hear your name announced.")
    prepare += 20
    print("\n Congratulations! Your preparedness for your performance has increased! It is now at " + str(prepare) + " points.")
if sinjin_friend > 0:
    print("\n Because you met Sinjin, you now have special lighting for your performance, courtesy of Sinjin, of course.")
    prepare += 5
    print("\n Congratulations! Your preparedness for your performance has increased! It is now at " + str(prepare) + " points.")

time.sleep(5)

print("""\n Your name is called next. It's your turn! After a week of preparations, it is now your time to shine!

1  Take a Hint

2  Begging on Your Knees

3  Best Friend's Brother

4  Give it Up

5  Freak the Freak Out

---------------------------------------------------------\n """)

# Plays song based on player's input
song = input("What song have you been preparing for us? ")
if song == "1":
    mixer.music.load("music/take_a_hint.mp3")
    mixer.music.play()
if song == "2":
    mixer.music.load("music/knees.mp3")
    mixer.music.play()
if song == "3":
    mixer.music.load("music/bfb.mp3")
    mixer.music.play()
if song == "4":
    mixer.music.load("music/give_it_up.mp3")
    mixer.music.play()
if song == "5":
    mixer.music.load("music/freak.mp3")
    mixer.music.play()

print("\n You sing your heart out! Next thing you know, your performance is over!")

# Probability of winning the game
if random.randrange(0,100)<50:
    print("\n As you leave the stage, a talent agent comes up to you.")
    print("\n 'Hello " + name + "! Your performance was spectacular. It was so phenomenal that I would like to speak to you regarding a potential music deal.'")
    time.sleep(2)
    print("\n Congratulations! You earned yourself a music deal!!! All of your hard work has paid off, " + name + "!")
else:
    print("\n Unfortunately, no talent spotters approach you for the rest of the night. Better luck next time.")

time.sleep(5)

print("--------------------------------------------------------- \n")

print("Wow! You survived your first week at Hollywood Arts! We hope you had a great time and made a bunch of amazing friends! See you next week!")

time.sleep(60)