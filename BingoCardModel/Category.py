from random import random, randrange

class Category:
    """A Category contains a collection of BingoSquares that can be selected randomly in order to fill in a BingoCard"""
    # Lists of easy, medium, and hard squares for given category
    easysquares = None
    mediumsquares = None
    hardsquares = None

    # Copies of easy/medium/hard squares for given category for use during selection
    easycopy = None
    mediumcopy = None
    hardcopy = None

    def __init__(self, easysquares=[], mediumsquares=[], hardsquares=[]):
        """Creates Category from given lists of easy, medium, and hard squares in that category"""
        self.easysquares = []
        self.mediumsquares = []
        self.hardsquares = []
        self.easycopy = []
        self.mediumcopy = []
        self.hardcopy = []
        for easy in easysquares:
            self.AddEasy(easy)
        for medium in mediumsquares:
            self.AddMedium(medium)
        for hard in hardsquares:
            self.AddHard(hard)

    def AddEasy(self, square):
        """Safely adds easy square to category"""
        self.easysquares.append(square)
        self.easycopy.append(square)

    def AddMedium(self, square):
        """Safely adds medium square to category"""
        self.mediumsquares.append(square)
        self.mediumcopy.append(square)

    def AddHard(self, square):
        """Safely adds hard square to category"""
        self.hardsquares.append(square)
        self.hardcopy.append(square)

    def PickEasy(self):
        """Safely chooses easy square from category"""
        return self.Pick(self.easysquares, self.easycopy)

    def PickMedium(self):
        """Safely chooses medium square from category"""
        return self.Pick(self.mediumsquares, self.mediumcopy)

    def PickHard(self):
        """Safely chooses hard square from category"""
        return self.Pick(self.hardsquares, self.hardcopy)

    def Reset(self):
        """Resets category list copies to their original configurations"""
        self.easycopy = self.easysquares.copy()
        self.mediumcopy = self.mediumsquares.copy()
        self.hardcopy = self.hardsquares.copy()


    def Pick(self, reference, copy):
        """Returns a bingo square from given list copy and then removes it from the copy
        If the copy is now empty, reset it to be equal to the reference list before choosing"""
        
        if (len(copy) == 0):
            copy = reference.copy()

        return copy.pop(randrange(len(copy)))


