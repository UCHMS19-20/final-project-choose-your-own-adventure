import time
import random

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

inventory = []

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

name = input("What is your name? ")

print("\n Hello, " + name + "!")

print("Congratulations! You have finished registration for Hollywood Arts. See you on the first day!")

time.sleep(5)

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

time.sleep(10)

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
    if beck_friend == 15:
        print("\n You recognize Beck from earlier, standing next to his girlfriend. She looks intimidating.")
        print("\n You call out, 'Hey Beck!'")
        print("\n He smiles and answers, 'Hey " + name + "! Jade and I were just talking about you, and we would love to help you out at the Big Showcase.'")
        print("\n 'Wow! Thank you, Beck!' you exclaim. Jade just rolls her eyes.")
        choice = input("""\n What would you like to do now?
        
        1  Flirt with Beck
        2  Flirt with Jade
        3  Thank them and walk away
        
        --------------------------------------------------------- \n""")
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
        print("You walk over to the lockers.")
        print("\n You recognize Jade from earlier, standing next to her boyfriend. His hair looks really soft.")
        print("\n You call out, 'Hey Jade!'")
        print("\n She turns to you and says, 'Hey " + name + "! Beck and I were just talking about you, and we decided that if you need it, we would be willing to help you for the Big Showcase, I guess.'")
        print("\n 'Wow! Thank you, Jade!' you exclaim.")
        print("\n Beck smiles at you and says, 'Of course, " + name + "! Anytime.")
        choice = input("""\n What would you like to do now?
        
        1  Flirt with Beck
        2  Flirt with Jade
        3  Thank them and walk away
        
        --------------------------------------------------------- \n""")
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
    else:
        print("\n You catch the girl in black making out with the boy with the attractive hair. They seem like such interesting people. You should have spoken with one of them before.")
if location == "5":
    print("You walk over to the lockers.")
    if tori_friend == 15:
        print("\n You recognize Tori from earlier, standing by her locker.")
        print("\n You call out, 'Hey Tori!'")
        print("\n She turns to you, smiles, and says, 'Hey " + name + "! How are you?")
        print("\n 'I'm good, thanks! Wow, I love your locker!' you exclaim.")
        print("\n 'Thanks! Have you decorated yours yet? It's a Hollywood Arts tradition!' Tori giggles.")
        print("\n 'I will soon. See you around, Tori!' you say before turning to leave to class.")
        print("\n 'Oh, wait! Here, have this. It'll help you for at the Big Showcase,' she says.")
        inventory.append("Costumes")
        print("\n Congratulations! You have added to your inventory. You now have: " + str(inventory) + ".")
    else: 
        print("\n You see a brunette girl standing by her locker. You remind yourself that you should be making more friends.")
        print("\n You call out, 'Hello! I'm " + name + "! What's your name?")
        print("\n She turns to you, smiles, and says, 'Hey " + name + "! I'm Tori. How are you?")
        print("\n 'I'm good, thanks! Wow, I love your locker!' you exclaim.")
        print("\n 'Thanks! You must be new. Have you decorated your locker yet? It's a Hollywood Arts tradition!' Tori giggles.")
        print("\n 'I will soon. See you around, Tori!' you say before turning to leave to class.")
        print("\n 'Oh, wait! Here, have this. It'll help you for at the Big Showcase,' she says.")
        inventory.append("Speakers")
        print("\n Congratulations! You have added to your inventory. You now have: " + str(inventory) + ".")

time.sleep(5)

print("--------------------------------------------------------- \n")

print("You go to your only class of the day: Improvisation. Next thing you know, Monday is over!")
print("\n Your adventures at Hollywood Arts will continue tomorrow, on Tuesday.")

time.sleep(5)

print("\n ---------------------------------------------------------")

print("\n TUESDAY. Second day at Hollywood Arts. Three more days until the Big Showcase! \n")

print("You walk inside, ready for today's adventures. Who will you befriend? Who will you anger? The drama!!! \n")

time.sleep(5)

print("""\n There are five different locations you can go to.

1  Lockers

2  Janitor's closet

3  Guidance counselor's office

4  Sikowitz's classroom

5  Black box theatre

--------------------------------------------------------- \n""")

time.sleep(10)

location2 = input("\n Where would you like to go first? ")
if location2 == "1":
if location2 == "2":
    print("You walk into the janitor's closet, out of pure curiousity. Maybe you'll make friends with someone in there. Who knows?")
    print("\n Sure enough, when you open the door, you find someone sitting in the corner munching on something.")
    if cat_friend == 10:
        print("\n You recognize her as the girl you met before... Cat!")
        print("\n 'Cat...' you say. She turns around. She grins when she sees you.")
        print("\n 'OMG hi " + name + "! Do you want to try some bibble? It's so good!")
        bibble = input("""\n What will you do?

        1  Take the bibble

        2  Tell her that she should probably stop eating bibble

        3  Walk out of the janitor's closet

        --------------------------------------------------------- \n""")
        if bibble == "1":
            print("\n You decide to try some bibble. If Cat is eating it all the time, it has to be good, right?")
            print("\n 'OMG yay!' she giggles, handing you a handful of bibble.")
            print("\n You put the bibble in your mouth and... wOw, that's good!")
            print("\n 'Wow... Cat... this is so good! Give me another handful!' you laugh.")
            print("\n 'I know right!' Cat giggles. You and Cat spend the rest of the morning eating bibble in the janitor's closet.")
            cat_friend += 20
            inventory.append("Bag of bibble")
            print("\n Your friendship with Cat has increased by 20 points! It is now at " + str(beck_friend) + " points.")
            print("\n Congratulations! You have added to your inventory. You now have: " + str(inventory) + ".")
        if bibble == "2":
            print("\n This is too much. Cat is addicted to bibble. You have to help her.")
            print("\n 'Cat... I think you should stop eating bibble! You're obsessed! Look at you! You're in the janitor's closet for crying out loud! You have to stop,' you say.")
            print("\n 'Oh... but it's so goOD!' Cat cries out.")
            print("\n You do what needs to be done. You grab the bag of bibble out of Cat's hand.")
            print("\n 'Hey! Give it back!' Cat shouts, on the verge of tears.")
            print("\n Determined to help Cat overcome her addiction, you run out the janitor's closet and throw it into the trash can. It's for her own good.")
            cat_friend -= 5
            print("\n Oh no! Your friendship with Cat has decreased by 5 points! It is now at " + str(jade_friend) + " points.")
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
        bibble = input("""\n What will you do?

        1  Take the bibble

        2  Tell her that she should probably stop eating bibble

        3  Walk out of the janitor's closet

        --------------------------------------------------------- \n""")
        if bibble == "1":
            print("\n You decide to try some bibble.")
            print("\n 'OMG yay!' she giggles, handing you a handful of bibble.")
            print("\n You put the bibble in your mouth and... wOw, that's good!")
            print("\n 'Wow... Cat... this is so good! Give me another handful!' you laugh.")
            print("\n 'I know right!' Cat giggles. You and Cat spend the rest of the morning eating bibble in the janitor's closet.")
            cat_friend += 20
            inventory.append("Bag of bibble")
            print("\n Your friendship with Cat has increased by 20 points! It is now at " + str(beck_friend) + " points.")
            print("\n Congratulations! You have added to your inventory. You now have: " + str(inventory) + ".")
        if bibble == "2":
            print("\n You notice that the entire bag is almost empty. She ate a whole 5 pounds of bibble already!")
            print("\n 'Cat... I think you should stop eating bibble! You're obsessed! Look at you! You're in the janitor's closet for crying out loud! You have to stop,' you say.")
            print("\n 'Oh... but it's so goOD!' Cat cries out.")
            print("\n You do what needs to be done. You grab the bag of bibble out of Cat's hand.")
            print("\n 'Hey! Give it back!' Cat shouts, on the verge of tears.")
            print("\n Determined to help Cat overcome her addiction, you run out the janitor's closet and throw it into the trash can. It's for her own good.")
            cat_friend -= 5
            print("\n Oh no! Your friendship with Cat has decreased by 5 points! It is now at " + str(jade_friend) + " points.")
        if bibble == "3":
            print("\n You decide that this is too strange for your liking. You leave the janitor's closet.")
if location2 == "3":
    print("\n You walk into the guidance counselor's office.")
    print("\n 'Hi, I'm Lane!' the counselor greets you as you walk in. 'And you are " + name + ", correct?'")
    print("\n 'That's me!' you say with a smile. You decided to come to the counselor's office because you were feeling quite overwhelmed with this whole Big Showcase. You sit down and tell him why you're feeling stressed.")
    print("\n 'It is perfectly normal to feel nervous about your first big performance at a new school. It's frigtening, I understand. But I need you to take a deep breath and realize that every single student here at Hollywood Arts has gone through the same thing,' Lane explains.")
    print("\n You smile. He's right. You're not alone.")
    print("\n 'Have you made some friends yet?' he asks, leaning back in his chair.")
    if tori_friend > 0:
        print("\n 'I met Tori, and she seems like such a nice person! I'm really glad that I met her,' you say.")
        print("\n 'Good. She's a good friend. And she'll definitely help you at the Big Showcase,' Lane responds.")
    if andre_friend > 0:
        print("\n 'I met Andre, and he seems like such a nice friend! I'm really glad that met him,' you say.")
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
if location2 == "4":
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
if location2 == "5":
    print("You walk into the black box theatre.")
    if robbie_friend == 10:
        print("\n You recognize Robbie sitting in the front row with Rex on his lap. You walk over to him.")
        print("\n 'Hey Robbie!' you say, sitting down next to him.")
        print("\n 'Hey " + name + "! I was just telling Rex here how I was going to go find you and ask how your second day at Hollywood Arts is going!'")
        print("\n 'Nah... you just wanted to get the new kid to be your friend so that you would actually have a friend,' Rex says.")
        print("\n Robbie gasps and covers Rex's mouth. 'Lies...' Robbie mutters.")
        rex = input("""\n What will you do?

        1  Tell Robbie that you think that him having a puppet is weird

        2  Talk to Rex

        3  Walk out of the theatre

        --------------------------------------------------------- \n""")
        if rex == "1":
        if rex == "2": 
        if rex == "3":
    else: 
        print("\n You see a curly-haired boy sitting in the front row with a puppet on his lap. You walk over to him.")
        print("\n 'Hi, I'm " + name "!' you introduce yourself. The boy turns to face you.")
        print("\n 'H-hi... I'm Robbie!' he says.")
        print("\n 'Excuse him, he's socially awkward,' Rex blurts out.")
        print("\n 'Am not!' Robbie gasps.")
        print("\n 'Are too!' Rex blurts back.")

time.sleep(5)

print("--------------------------------------------------------- \n")

if cat_friend == 

time.sleep(5)

print("\n ---------------------------------------------------------")