from sys import exit

import tpp_scenes


# The main Engine on which the game runs, by using its own play() method.
class Engine(object):
    
    # Initializes the Engine() object, and takes one argument. In this case it's theMap, which is a Map() instance.
    def __init__(self, sceneMap):
        self.sceneMap = sceneMap

    # The main loop of the script, which gets called by theGame instance of the Engine().
    def play(self):
        currentScene = self.sceneMap.openingScene() # Calls the openingScene() method from Map(), by using theGame instance.
        lastScene = self.sceneMap.nextScene("Finish") # Calls the nextScene() method from Map() by giving it an argument "Finish".

        while currentScene is not lastScene: # Will execute until the player reaches the Finish(Scene) object or Dead(Scene) object.
            nextSceneName = currentScene.enter() # Calls the enter() method on the currentScene which returns the nextScene key string.
            currentScene = self.sceneMap.nextScene(nextSceneName) # Calls nextScene() method depending on the returned key from nextSceneName.

        currentScene.enter() # Starts the current enter() method of the current Scene.

# The Map class which controls the scenes of the game.
class Map(object):
    
    scenes = {
        "Dungeon": tpp_scenes.Dungeon(),
        "CityMarket": tpp_scenes.CityMarket(),
        "OldShack": tpp_scenes.OldShack(),
        "CourtRoom": tpp_scenes.CourtRoom(),
        "CityRuler": tpp_scenes.CityRuler(),
        "FinishGood": tpp_scenes.FinishGood(),
        "FinishBad": tpp_scenes.FinishBad(),
        "Death": tpp_scenes.Death()
    }

    # Initializes the Map() object, and takes one argument.
    def __init__(self, startScene):
        self.startScene = startScene

    # Creates a variable that returns the next scene object, and takes one argument, which is some Scene object, depending on dict key.
    def nextScene(self, sceneName):
        mapInstance = Map.scenes.get(sceneName)
        return mapInstance
    
    # Returns the Scene() object which opens the game. In this case it's Dungeon(Scene).
    def openingScene(self):
        return self.nextScene(self.startScene)

# Greets the user with a simple message.
print("Welcome to The Prisoner of Pyland v1.0")

# Creates an instance of Map() with the starting scene predefined.
theMap = Map("Dungeon")

# Creates an instance of Engine() with theMap instance as an argument.
theGame = Engine(theMap)

# Starts the game by calling the play() method in Engine().
theGame.play()
