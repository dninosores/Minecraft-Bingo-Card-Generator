# A Category contains a collection of BingoSquares that can be selected from in order to fill in a BingoCard
from random import random, randrange


class Category:

    # Lists of easy, medium, and hard squares for given category
    easysquares = None
    mediumsquares = None
    hardsquares = None

    # Copies of easy/medium/hard squares for given category for use during selection
    easycopy = None
    mediumcopy = None
    hardcopy = None

    # Creates Category from given lists of easy, medium, and hard squares in that category
    def __init__(self, easysquares=[], mediumsquares=[], hardsquares=[]):
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

    # Adds square to category
    def AddEasy(self, square):
        self.easysquares.append(square)
        self.easycopy.append(square)

    def AddMedium(self, square):
        self.mediumsquares.append(square)
        self.mediumcopy.append(square)

    def AddHard(self, square):
        self.hardsquares.append(square)
        self.hardcopy.append(square)

    # Chooses square from category
    def PickEasy(self):
        return self.Pick(self.easysquares, self.easycopy)

    def PickMedium(self):
        return self.Pick(self.mediumsquares, self.mediumcopy)

    def PickHard(self):
        return self.Pick(self.hardsquares, self.hardcopy)

    # Resets copies to their original configurations
    def Reset(self):
        self.easycopy = self.easysquares.copy()
        self.mediumcopy = self.mediumsquares.copy()
        self.hardcopy = self.hardsquares.copy()

    # Returns a bingo square from given copy and then removes it from the copy
    # If the copy is now empty, reset it to be equal to the reference list before choosing
    def Pick(self, reference, copy):
        if (len(copy) == 0):
            copy = reference.copy()

        return copy.pop(randrange(len(copy)))


