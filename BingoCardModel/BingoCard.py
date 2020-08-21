
from math import ceil
from random import randrange

from PIL import Image, ImageDraw


class BingoCard:
    """Represents a full bingo card that can generate a 5x5 square image using 5 stored categories"""
    BORDER_SIZE = 0.01
    BORDER_FILL_PERCENTAGE = 0.5
    categories = None

    def __init__(self, categories):
        """Creates bingocard from given list of categories"""
        self.categories = categories

    
    def Generate(self, size, savelocation = None):
        """Generates a square bingo card of given size and saves image of card to specified URL."""
        print("Generating random category mappings")
        for category in self.categories:
            category.Reset()

        # Category mapping maps each category number to a random and distinct other category number.
        # This prevents each category from always occupying the same spaces on the card.
        categorymapping = list()
        numcat = len(self.categories)
        if numcat >= 5:
            for i in range(5):
                number = randrange(numcat)
                while number in categorymapping:
                    number = randrange(numcat)
                categorymapping.append(number)
        else:
            for i in range(numcat):
                number = randrange(numcat)
                while number in categorymapping:
                    number = randrange(numcat)
                categorymapping.append(number)
            for i in range(5 - numcat):
                categorymapping.append(randrange(numcat))

        bordersize = int(ceil(size * self.BORDER_SIZE * self.BORDER_FILL_PERCENTAGE))
        usablesize = size - bordersize * 2
        tilesize = int(ceil(usablesize/5))
        fullsquare = Image.new('RGB', (size, size), (255, 255, 255))

       
        def getCategory(number):
            """Gets a category based on its number from 1 to 5"""
            return self.categories[categorymapping[number - 1]]

        print("Picking squares from categories")
        tiles = ((getCategory(2).PickEasy(), getCategory(1).PickEasy(), getCategory(4).PickMedium(), getCategory(3).PickHard(), getCategory(5).PickMedium()),
         (getCategory(1).PickMedium(), getCategory(3).PickMedium(), getCategory(5).PickEasy(), getCategory(4).PickEasy(), getCategory(2).PickHard()),
         (getCategory(5).PickMedium(), getCategory(4).PickEasy(), getCategory(1).PickHard(), getCategory(2).PickMedium(), getCategory(3).PickEasy()),
         (getCategory(4).PickHard(), getCategory(2).PickMedium(), getCategory(3).PickMedium(), getCategory(5).PickEasy(), getCategory(1).PickEasy()),
         (getCategory(3).PickEasy(), getCategory(5).PickHard(), getCategory(2).PickEasy(), getCategory(1).PickMedium(), getCategory(4).PickMedium()))

        for x in range(0, 5):
            for y in range(0, 5):
                print("Drawing square at (" + str(x) + "," + str(y) + ")")
                image = tiles[y][x].render(tilesize)
                fullsquare.paste(image, (bordersize + x * tilesize, bordersize + y * tilesize))

        print("Drawing border")
        drawer = ImageDraw.Draw(fullsquare)
        drawer.rectangle([0, 0, size-1, size-1], None, (0, 0, 0),
                         int(ceil(size * self.BORDER_SIZE * self.BORDER_FILL_PERCENTAGE)))

        if savelocation is None:
            pass
        else:
            print("Saving to", savelocation)
            fullsquare.save(savelocation)
        fullsquare.show()

        print("Done!")
