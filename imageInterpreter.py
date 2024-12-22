import pytesseract
from PIL import Image
import os

def grabStats(img: Image):
    pytesseract.image_to_string


def grabImages(target: str):
    """
    Grabs the names of all image files in the directory target

    :param target: The target folder to pull images from
    :type target: String

    :return: Image objects generated from the directory
    :rtype: List of PIL.Image objects
    """

    return [Image.open().convert("L") for f in [os.path.join(target, f) for f in os.listdir(target) if f.lower().endswith((".png",".jpeg",".jpg",".bmp"))]]


def test():
    images = grabImages("")
    print(images)


if __name__ == "__main__":
    test()