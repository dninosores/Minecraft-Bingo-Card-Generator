
from PIL import Image, ImageFont, ImageDraw


def AspectScale(image, newwidth, newheight):
    """Scales image to fit inside a box of given width and height while preserving aspect ratio"""
    if newwidth < newheight:
        scale = newwidth / image.width
    else:
        scale = newheight / image.height
    return image.resize((int(round(image.width * scale)), int(round(image.height * scale))))


def DrawText(text, width, height):
    """Draws text to transparent image with given width and height"""
    
    def getTextHeight(text, fontsize):
        """Gets height in pixels of given text with given font size."""
        return (text.count('\n') + 1) * ImageFont.truetype("resources/bpdots.squares-bold.otf", fontsize).getsize(text)[1] + \
               0.3 * (text.count('\n')) * ImageFont.truetype("resources/bpdots.squares-bold.otf", fontsize).getsize(text)[1]

    def getTextWidth(text, fontsize):
        """Gets width in pixels of given text with given font size."""
        def width(line):
            return ImageFont.truetype("resources/bpdots.squares-bold.otf", fontsize).getsize(line)[0]
        chunks = text.split('\n')
        chunks = map(width, chunks)
        return max(chunks)

    formattedtext = text

    fontsize = 1
    # gets biggest font size that matches height without exceeding it
    while (True):
        if getTextHeight(formattedtext, fontsize) > height:
            fontsize -= 1
            break
        else:
            fontsize += 1

    letterindex = 0
    formattedtext = ""
    while letterindex < len(text):
        nextword = ""
        firstchar = True
        for character in text[letterindex:len(text)]:
            if character == ' ' and not firstchar:
                break
            else:
                nextword += character
            firstchar = False
            letterindex += 1

        newformattedtext = formattedtext + nextword

        if getTextWidth(newformattedtext, fontsize) > width:
            formattedtext += "\n"
            formattedtext += nextword
            if getTextHeight(formattedtext, fontsize) > height:
                fontsize = 1
                while (True):
                    if getTextHeight(formattedtext, fontsize) > height:
                        fontsize -= 1
                        break
                    else:
                        fontsize += 1
                letterindex = 0
                formattedtext = ""
        else:
            formattedtext = newformattedtext

    fontsize = 1
    # Now that all the newlines are in, increase the font size to the biggest it can be without overstepping bounds
    while (getTextHeight(formattedtext, fontsize) < height and getTextWidth(formattedtext, fontsize) < width):
        fontsize += 1
    fontsize -= 1

    # make a blank image for the text, initialized to transparent text color
    txt = Image.new('RGBA', (width, height), (255, 255, 255, 0))
    # get a font
    fnt = ImageFont.truetype("resources/bpdots.squares-bold.otf", fontsize)
    # get a drawing context
    d = ImageDraw.Draw(txt)
    textchunks = formattedtext.split('\n')
    y = 1
    for line in textchunks:
        if (len(line) > 0 and line[0] == " "):
            i = 0
            while (len(line) > i and line[i] == " "):
                i += 1
            line = line[i:]
        if (len(line) > 0 and line[-1] == " "):
            i = -1
            while (-len(line) < i and line[i] == " "):
                i -= 1
            i += 1
            line = line[:i]
        d.text(((width - getTextWidth(line, fontsize)) / 2, y), line, font=fnt, fill=(0, 0, 0, 255))
        y += getTextHeight(line, fontsize) * 1.3
    return txt
