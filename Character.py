class Character:
    def __init__(self, argsList):
        self.name = argsList[0]
        self.gender = argsList[1]
        self.game = argsList[2]
        self.human = argsList[3]
        self.antagonist = argsList[4]
        self.pokemon = argsList[5]
        self.most_known = argsList[6]
        self.variation = argsList[7]
        self.child = argsList[8]
        self.top_tier = argsList[9]

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)

