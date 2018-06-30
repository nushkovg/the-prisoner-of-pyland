from random import randint
from textwrap import dedent


# A function that throws an error message if the user input is invalid.
def strError(choiceOne, choiceTwo):
    print(f"Are you feeling alright? Decide, " +  choiceOne + " or " +  choiceTwo + ".")

# A function that keeps track of the conditions in the Dungeon scene.
def dungeonConditions():
    choice = input('> ')
    
    if "lockpick" in choice and "trick" in choice:
        strError("lockpick", "trick")
        return dungeonConditions()
    elif "Lockpick" in choice and "Trick" in choice:
        strError("lockpick", "trick")
        return dungeonConditions()
    elif "Lockpick" in choice and "trick" in choice:
        strError("lockpick", "trick")
        return dungeonConditions()
    elif "lockpick" in choice and "Trick" in choice:
        strError("lockpick", "trick")
        return dungeonConditions()
    
    elif "lockpick" in choice or "Lockpick" in choice:
        codeFirstTwoDigits = "{}{}".format(randint(1, 9), randint(1, 9))
        codeLastDigit = "{}".format(randint(1, 9))
        code = codeFirstTwoDigits + codeLastDigit
        print("Guess the code: {}?".format(codeFirstTwoDigits))
        
        guess = input("> ")
        guesses = 0

        while guess != code and guesses < 4:
            print("Wrong! Try again.")
            guesses += 1
            guess = input("> ")
        
        if guess == code:
            print(dedent("""
                    You got it! You sneak past the guard and escape the dungeon. You found
                    some clothes and went to the City Market, where you must find materials
                    for the weapon you need to create to confront the ruler and his guards.
                    """))
            return "CityMarket"
        else:
            print(dedent("""
                    You woke up the guard, who happens to be extremely nervous that day
                    because his wife left him. He opened the cell door and bashed your
                    head in. What a shame!
                    """))
            return "Death"
    
    elif "trick" in choice or "Trick" in choice:
        trick = "{}".format(randint(1, 100))

        print("Try to convince him. Enter a number between 1 and 100.")
        guess = input("> ")
        guesses = 0

        while guess > trick and guesses < 1:
            print("He doesn't seem convinced. Try once again.")
            guesses += 1
            guess = input("> ")

        if guess < trick:
            print(dedent("""
                    You made it! You told him that you found a bag of gold in your cell and
                    as dumb as he is, he opened the door. You banged his head with a stone
                    and he is out of the picture. You took his clothes and you headed to the
                    City Market, where you must find materials for the weapon you need to
                    create to confront the ruler and his guards.
                    """))
            return "CityMarket"
        else:
            print(dedent("""
                    The guard saw through your plan, and since you woke him up for nothing,
                    he got angry and stabbed you through the eye and went to sleep again. So
                    much of your plan!
                    """))
            return "Death"
    
    else:
        strError("lockpick", "trick")
        return dungeonConditions()

# A function that keeps track of the conditions in the City Market scene.
def cityMarketConditions():
    choice = input('> ')
    
    if "steal" in choice and "convince" in choice:
        strError("steal", "convince")
        return cityMarketConditions()
    elif "Steal" in choice and "Convince" in choice:
        strError("steal", "convince")
        return cityMarketConditions()
    elif "Steal" in choice and "convince" in choice:
        strError("steal", "convince")
        return cityMarketConditions()
    elif "steal" in choice and "Convince" in choice:
        strError("steal", "convince")
        return cityMarketConditions()
    
    elif "steal" in choice or "Steal" in choice:
        codeFirstTwoDigits = "{}{}".format(randint(1, 9), randint(1, 9))
        codeLastDigit = "{}".format(randint(1, 9))
        code = codeFirstTwoDigits + codeLastDigit
        print("Guess the code: {}?".format(codeFirstTwoDigits))
        
        guess = input("> ")
        guesses = 0

        while guess != code and guesses < 4:
            print("Wrong! Try again.")
            guesses += 1
            guess = input("> ")
        
        if guess == code:
            print(dedent("""
                    You sneaky bastard! You managed to open the backdoor of the store,
                    and you gathered all you need without being noticed! Now it's time
                    to visit your old man's shack, where you've hidden all the tools
                    necessary for completing the weapon.
                    """))
            return "OldShack"
        else:
            print(dedent("""
                    The city guards saw you trying to sneak into the store. They stabbed
                    you multiple times in the torso, cut you in many parts and threw what's
                    left of you in the kennels. Nice way to die, eh?
                    """))
            return "Death"
    
    elif "convince" in choice or "Convince" in choice:
        convince = "{}".format(randint(1, 100))

        print("Try to convince him. Enter a number between 1 and 100.")
        guess = input("> ")
        guesses = 0

        while guess > convince and guesses < 1:
            print("He doesn't seem convinced. Try once again.")
            guesses += 1
            guess = input("> ")

        if guess < convince:
            print(dedent("""
                    You got lucky! It turns out that the vendor hated the ways of the ruler as
                    much as anyone in the city. He gave you all the parts you need, even gave
                    you new clothes. Now off to your old man's shack, where you've hidden all
                    the tools necessary for completing the weapon.
                    """))
            return "OldShack"
        else:
            print(dedent("""
                    While you were trying to convince the vendor, the ruler himself entered the
                    store. You thought you can finish him now, until his guards showed up and
                    burned you alive in the middle of the city. At least it was not raining...
                    """))
            return "Death"
    
    else:
        strError("steal", "convince")
        return cityMarketConditions()

# A function that keeps track of the conditions in the Old Shack scene.
def oldShackConditions():
    choice = input('> ')
    
    if "courtroom" in choice and "rulersroom" in choice:
        strError("courtroom", "rulersroom")
        return oldShackConditions()
    elif "Courtroom" in choice and "Rulersroom" in choice:
        strError("courtroom", "rulersroom")
        return oldShackConditions()
    elif "Courtroom" in choice and "rulersroom" in choice:
        strError("courtroom", "rulersroom")
        return oldShackConditions()
    elif "courtroom" in choice and "Rulersroom" in choice:
        strError("courtroom", "rulersroom")
        return oldShackConditions()
    
    elif "courtroom" in choice or "Courtroom" in choice:
        print(dedent("""
                You decided to go heroic on his ass and clear everyone in his Court Room
                first. Prepare for the challenge as you enter the Court Room!
                """))
        return "CourtRoom"
    
    elif "rulersroom" in choice or "Rulersroom" in choice:
        chance = randint(1, 100)

        if chance < 30:
            print(dedent("""
                    You made it! You sneaked in his room and you don't see him there, so you
                    decided to hide. You will wait as long as needed to have your revenge!
                    """))
            return "CityRuler"
        else:
            print(dedent("""
                    As you are tying the rope to climb into his chambers, he saw you from his
                    window and called his guards. They were extremely bloodthirsty that day, 
                    unlucky for you. They skinned you alive in front of the citizens. Such a 
                    beautiful sight!
                    """))
            return "Death"
    
    else:
        strError("courtroom", "rulersroom")
        return oldShackConditions()

# A function that keeps track of the conditions in the Court Room scene.
def courtRoomConditions():
    choice = input("> ")
    
    if "pride" in choice and "brain" in choice:
        strError("pride", "brain")
        return courtRoomConditions()
    elif "Pride" in choice and "Brain" in choice:
        strError("pride", "brain")
        return courtRoomConditions()
    elif "Pride" in choice and "brain" in choice:
        strError("pride", "brain")
        return courtRoomConditions()
    elif "pride" in choice and "Brain" in choice:
        strError("pride", "brain")
        return courtRoomConditions()
    
    elif "pride" in choice or "Pride" in choice:
        chance = randint(1, 100)

        if chance <= 50:
            print(dedent("""
                    It was a tough battle and you were losing. You finally came to your senses,
                    took your weapon, forgot your pride for a second, and blasted the brute's
                    brain. Your pride may not be present, but your life is! Rage rises as you
                    go after the ruler!
                    """))
            return "CityRuler"
        else:
            print(dedent("""
                    What were you thinking? Were you thinking at all? That brute can beat you in
                    a sword duel any day of the week! You lie dead on the ground, or whatever's
                    left of you. This is where your pride got you. Great job!
                    """))
            return "Death"
    
    elif "brain" in choice or "Brain" in choice:
        print(dedent("""
                No matter what they say, your life is more important than your pride and you
                know it! The big brute with the sword didn't stand a chance against your mighty
                weapon. You can finally proceed to confront the evil ruler and have your revenge!
                """))
        return "CityRuler"
    
    else:
        strError("pride", "brain")
        return courtRoomConditions()

# A function that keeps track of the conditions in the City Ruler scene.
def cityRulerConditions():
    choice = input('> ')
    
    if "hero" in choice and "rich" in choice:
        strError("hero", "rich")
        return cityRulerConditions()
    elif "Hero" in choice and "Rich" in choice:
        strError("hero", "rich")
        return cityRulerConditions()
    elif "Hero" in choice and "rich" in choice:
        strError("hero", "rich")
        return cityRulerConditions()
    elif "hero" in choice and "Rich" in choice:
        strError("hero", "rich")
        return cityRulerConditions()
    
    elif "hero" in choice or "Hero" in choice:
        print(dedent("""
                You don't care for anything else other than vengeance. You charged your
                weapon, smiled at him in the most evil way possible, and blasted his guts
                all over the room. While he's still breating, you take his knife, stab him
                in both eyes, cut his tongue and stump his head with your foot. That surely
                did the trick. The sun rised over Pyland...no it did not, because the weather
                is bad there, and this is not that kind of a happy story.
                """))
        return "FinishGood"

    elif "rich" in choice or "Rich" in choice:
        print(dedent("""
                Your priorities suddenly changed as you accept the bag of gold from the as*hole,
                but you still had to punish him in some way, so you took the knife and relieved
                him of one ear, one eye, and three fingers. He should be happy you left him there
                still breathing. You can finally be on your way to a better life.
                """))
        return "FinishBad"
    
    else:
        strError("hero", "rich")
        return cityRulerConditions()