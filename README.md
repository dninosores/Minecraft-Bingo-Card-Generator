# Minecraft Bingo Card Generator

This program allows you to generate perfectly fair bingo cards from a spreadsheet of prompts to put on the squares of the bingo card.

In order to add and remove squares from the bingo card, you will need to edit the bingocategories.csv spreadsheet. Each row in this spreadsheet represents a single potential square on the bingo card. The columns of the spreadsheet are:
 #### Category
   The category that a square belongs to. When a card is generated, five categories will be selected at random and a space from each of those categories will be present in each row, column, and diagonal exactly once.
  ####  Difficulty 
   Can be 'easy' 'medium' or 'hard'. Each category must contain at least one square of each difficulty level. When a card is generated, each row, column, and diagonal will contain 2 easy, 2 medium, and 1 hard square. 
  #### Text 
  The optional text to display on the square 
  #### Image 
   The filename of the optional image to display on the square. By default, all images should be placed in the images folder. 
   
When opening/saving the .csv file, your spreadsheet editing software may ask you how you want to format the csv file. If the options are available, make sure that the csv is comma-separated and uses " as its text delimiter.

Once you've filled in the bingocategories.csv spreadsheet, double-click GenerateBingoCard.py to run it. It will create a file called bingocard.png located in the same directory as GenerateBingoCard.py.

In order to customize the names/locations of the files created and used by the programs, you can change the constants on lines 10-19 of GenerateBingoCard.py.

## Dependencies
This program requires [Python 3.8](https://www.python.org/downloads/).

This program also requires Pillow to be installed. In order to install Pillow, first make sure that you have Python installed, then open your command prompt and run "pip install Pillow"

## Troubleshooting
 If the program doesn't run, it's most likely because you either don't have python or don't have Pillow and you need to install them.
