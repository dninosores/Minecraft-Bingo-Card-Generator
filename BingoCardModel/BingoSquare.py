from PIL import Image, ImageDraw
from BingoCardModel.Utils import AspectScale, DrawText


class BingoSquare:
    """A BingoSquare is an object that contains text and an associated image for placement on a BingoCard"""
    image = None;
    text = "";
    # Percentage of space that border should take up
    BORDER_SIZE = 0.03
    # Percentage of border that is actually filled in
    BORDER_FILL_SIZE = 0.69
    # Percentage of vertical space that image takes up
    IMAGE_VERTICAL_SIZE = 0.69
    IMAGE_HORIZONTAL_SIZE = 1 - (BORDER_SIZE * 2)

    TEXT_VERTICAL_SPACING = 0.03
    TEXT_HORIZONTAL_SIZE = IMAGE_HORIZONTAL_SIZE
    TEXT_VERTICAL_SIZE = 1 - (BORDER_SIZE * 2) - TEXT_VERTICAL_SPACING - IMAGE_VERTICAL_SIZE

    def __init__(self, text, imagepath = None):
        """Creates new BingoSquare with given image filepath and text"""
        if imagepath is None:
            self.image = Image.new('RGB', (5, 5), (255, 255, 255))
            self.IMAGE_VERTICAL_SIZE = 0.01
            self.TEXT_VERTICAL_SIZE = 1 - (self.BORDER_SIZE * 2) - self.TEXT_VERTICAL_SPACING - self.IMAGE_VERTICAL_SIZE
        else:
            self.image = Image.open(imagepath)

        if text is None:
            self.IMAGE_VERTICAL_SIZE = 0.99
            self.TEXT_VERTICAL_SIZE = 1 - (self.BORDER_SIZE * 2) - self.TEXT_VERTICAL_SPACING - self.IMAGE_VERTICAL_SIZE
            self.text = ""
        else:
            self.text = text

    def __repr__(self):
        return self.text

    def render(self, size):
        "Returns an image representation of BingoSquare with given size in pixels"
        image = self.image.copy()
        image = AspectScale(image, size * self.IMAGE_HORIZONTAL_SIZE, size * self.IMAGE_VERTICAL_SIZE)
        imageoffset = ((int) (size/2) - (int) (image.width/2), (int) (size * self.BORDER_SIZE))
        fullsquare = Image.new('RGB', (size, size), (255, 255, 255))
        fullsquare.paste(image, imageoffset, image.convert('RGBA'))
        drawer = ImageDraw.Draw(fullsquare)
        drawer.rectangle([0, 0, size, size], None, (0, 0, 0), int(round(size * self.BORDER_SIZE * self.BORDER_FILL_SIZE)))
        textbox = DrawText(self.text, (int) (size * self.TEXT_HORIZONTAL_SIZE), (int) (size * self.TEXT_VERTICAL_SIZE))
        textboxoffset = ((int) (size/2) - (int) (textbox.width/2), (int) (imageoffset[1] + image.height +
                         self.TEXT_VERTICAL_SPACING * size))
        fullsquare.paste(textbox, textboxoffset)
        return fullsquare
