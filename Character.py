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

    def __getitem__(self, index):
        if index == 0:
            return self.name
        if index == 1:
            return self.gender
        if index == 2:
            return self.game
        if index == 3:
            return self.human
        if index == 4:
            return self.antagonist
        if index == 5:
            return self.pokemon
        if index == 6:
            return self.most_known
        if index == 7:
            return self.variation
        if index == 8:
            return self.child
        if index == 9:
            return self.top_tier

