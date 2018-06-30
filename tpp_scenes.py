from random import randint
from sys import exit
from textwrap import dedent

import tpp_conditions


# Parent class for all of the scenes.
class Scene(object):
    
    def enter(self):
        print("This map is under construction.")
        print("Sorry for the inconvenience.")
        exit(1)
    
# First child of the Scene() class. The enter() method gets overwritten.
class Dungeon(Scene):
    
    def enter(self):
        print(dedent("""
                It's been too long since you've seen the sun shine. Your decision to dismiss
                the evil city ruler's request about creating that weapon of mass murder had
                you locked up in this dungeon. You have decided not to use your engineering
                skills for evil purposes, and this is your reward. You've had enough of this
                nonsense, so you decided to escape these dark dungeons to finally have your
                revenge. You must do it for yourself and for all of the people that are being
                tortured daily by that filthy ruler. It is time. You see a lone guard sleeping
                in front of your cell. Will you use your skills of lockpicking, or will you try
                to trick the guard into opening the door?

                Hint: You have to choose, 'lockpick' or 'trick'.
                """))
        
        return tpp_conditions.dungeonConditions()

# Second child of the Scene() class. The enter() method gets overwritten.
class CityMarket(Scene):
    
    def enter(self):
        print(dedent("""
                You went to the local store to get the parts for your creation. But you don't
                have anything to pay with, so you'll have to come up with a solution. You know
                that this store is owned by the ruler himself, so it won't be easy. You still
                have a chance to convince the vendor to give you the materials, but you're not
                sure if he's ready to risk his life for this. Or are you going to try to steal
                the materials? It's your choice.

                Hint: You have to choose, 'convince' or 'steal'.
                """))

        return tpp_conditions.cityMarketConditions()

# Third child of the Scene() class. The enter() method gets overwritten.
class OldShack(Scene):

    def enter(self):
        print(dedent("""
                As you enter the shack, you get a flashback of your father's screams as the ruler's
                guards torture him to death, just because he declined the request to join them and
                leave you alone in the wilderness. You start crying while you are making the weapon,
                and your rage rises. After two days without sleep, you finished your creation. Now
                it's time to decide how you want to approach the ruler's room. Are you going to go
                full rage and clear his Court Room, or will you try to sneak directly in his room?

                Hint: You have to choose, 'courtroom' or 'rulersroom'.
                """))
        
        return tpp_conditions.oldShackConditions()

# Fourth child of the Scene() class. The enter() method gets overwritten.
class CourtRoom(Scene):

    def enter(self):
        print(dedent("""
                You entered in the Court Room with your weapon. It seems that the filthy ruler is not
                here. As soon as his advisors see your weapon, they start running. The ruler's brother,
                however, decided to give you a fair chance. He tells you to drop the weapon and face
                him in a sword duel. If you win, you can finish the job. If you lose, well, you'll be
                too dead to finish anything. Are you going to play with your pride, or your brain?

                Hint: You have to choose, 'pride' or 'brain'.
                """))
        
        return tpp_conditions.courtRoomConditions()

# Fifth child of the Scene() class. The enter() method gets overwritten.
class CityRuler(Scene):

    def enter(self):
        print(dedent("""
                You finally confront the ruler, and as soon as he sees you, he starts shaking like a little
                girl while you are raising your weapon with an evil smile on your face. He knows nobody
                can save him now, so he does what every filthy rich piece of sh*t does in a situation like
                this. He offers you a bag of gold that will keep you rich until the rest of your days. You
                stop and think for a minute, is it better to live as a poor hero or a rich as*hole?

                Hint: You have to choose, 'hero' or 'rich'.
                """))

        return tpp_conditions.cityRulerConditions()

# Sixth child of the Scene() class. The enter() method gets overwritten.
class FinishGood(Scene):
    
    def enter(self):
        print("The evil ruler's reign is over! And you were his undoing!")
        print("You've had your vengeance and Pyland is finally free.\n")
        print("Thanks for playing The Prisoner of Pyland!")
        exit(0)

# Seventh child of the Scene() class. The enter() method gets overwritten.
class FinishBad(Scene):
    
    def enter(self):
        print("You left Pyland with your bag full of gold and never turn back.")
        print("I guess gold was more important to you than releasing the city of the misery.\n")
        print("Thanks for playing The Prisoner of Pyland!")
        exit(0)

# Last child of the Scene() class. The enter() method gets overwritten.
class Death(Scene):
    
    deathCase = [
        "Your engineering mindset is non-existant. You died!",
        "Not really smart, eh? You died!",
        "I could have done this with my eyes closed. You died!",
        "Oh, the pain of watching you play. You died!",
        "Is that really the best you can do? You died!"
    ]

    def enter(self):
        print(Death.deathCase[randint(0, len(self.deathCase) - 1)]) # Prints a random case from the deathCase list.
        exit(1)