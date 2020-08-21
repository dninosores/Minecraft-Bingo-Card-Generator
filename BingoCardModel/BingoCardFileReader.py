# Reads in bingo card from a .csv file and returns the built BingoSquare object
from csv import DictReader

from BingoCardModel.BingoCard import BingoCard
from BingoCardModel.BingoSquare import BingoSquare
from BingoCardModel.Category import Category


class BingoFileException(Exception):
    pass

# Reads a bingofile with given filename
# ImageLocation is the complete path up until the last '/' for the directory where images are located
def readBingoFile(filename, imagelocation=""):
    # Stores all squares in a dictionary of categoryname : square
    squares = dict()
    rownumber = 1
    imagerror = False
    with open(filename) as file:
        for row in DictReader(file):
            rownumber += 1
            if row.get('category') is None:
                raise BingoFileException("File must contain a 'category' column!")
            elif row.get('difficulty') is None:
                raise BingoFileException("File must contain a 'difficulty' column!")
            elif row.get('text') is None and row.get('image') is None:
                raise BingoFileException("File must contain either a 'text' or an 'image' column!")

            image = None
            if row.get('image') == "":
                image = None
            elif row.get('image') is not None:
                image = imagelocation + row['image']

            # Need to catch broken image paths here and replace the image with None
            try:
                cursquare = BingoSquare(row['text'], image)
            except FileNotFoundError:
                print("Image file '" + image + "' could not be found! Error on row " + str(rownumber) + ".")
                imagerror = True
                cursquare = BingoSquare(row['text'], None)

            if squares.get(row['category']) is None:
                squares[row['category']] = Category()
            category = squares[row['category']]
            level = row['difficulty']

            if level == "easy":
                category.AddEasy(cursquare)
            elif level == 'medium':
                category.AddMedium(cursquare)
            elif level == 'hard':
                category.AddHard(cursquare)
            else:
                raise BingoFileException("'" + level + "' is not a valid difficulty level! Error in row " + str(rownumber))

        file.close()


    categories = []
    for name, category in squares.items():
        if len(category.easysquares) <= 0:
            raise BingoFileException("Category '" + name + "' contains no easy prompts!")
        if len(category.mediumsquares) <= 0:
            raise BingoFileException("Category '" + name + "' contains no medium prompts!")
        if len(category.hardsquares) <= 0:
            raise BingoFileException("Category '" + name + "' contains no hard prompts!")

        categories.append(category)

    if imagerror:
        input("Some of your images couldn't be found. Press enter to continue.")

    return BingoCard(categories)