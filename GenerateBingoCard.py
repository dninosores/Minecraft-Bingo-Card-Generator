import os

from PIL import Image

from BingoCardModel.BingoCard import BingoCard
from BingoCardModel.BingoCardFileReader import readBingoFile, BingoFileException
from BingoCardModel.BingoSquare import BingoSquare
from BingoCardModel.Category import Category

# Name of bingo card output file
CARDNAME = "bingocard"
# File type of bingo card output file
CARDEXT = ".png"
# Size of bingo card output file
CARDSIZE = 1800
# Directory to search for images when reading output file
IMAGELOCATION = "images/"
# Name of csv containing bingo card categories
CATEGORYCSV = "bingocategories.csv"
# Whether program asks user to press enter to quit
PROMPTEXIT = False

if __name__ == "__main__":
    try:
        bingocard = readBingoFile(CATEGORYCSV, IMAGELOCATION)
        if not os.path.exists(CARDNAME + CARDEXT):
            bingocard.Generate(CARDSIZE, CARDNAME + CARDEXT)
        else:
            imagenumber = 0
            while os.path.exists(CARDNAME + str(imagenumber) + CARDEXT):
                imagenumber += 1
            bingocard.Generate(CARDSIZE, CARDNAME + str(imagenumber) + CARDEXT)
    except BingoFileException as e:
        print("ERROR! " + str(e))
    
    if PROMPTEXIT:
        input("Press enter to exit.")
