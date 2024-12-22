import pytesseract
from PIL import Image
import os

def grabStats(img: Image):
    pytesseract.image_to_string


def grabImages(target: str):
    """
    Grabs all image files from the target directory, converts them to grayscale, 
    and returns them as a list of PIL Image objects.

    :param target: The target folder to pull images from.
    :type target: str

    :return: A list of PIL Image objects in grayscale.
    :rtype: list of PIL.Image
    """

    # List comprehension to get paths of valid image files and open them in grayscale
    images = [
        Image.open(os.path.join(target, f)).convert("L")
        for f in os.listdir(target)
        if f.lower().endswith(('.png', '.jpeg', '.jpg', '.bmp'))
    ]
    
    # Return the list of images
    return images

def test():
    images = grabImages("C:\Users\MDeac\OneDrive\Desktop\CS Projects\marvelRivalsScreenshots")
    print(images)


if __name__ == "__main__":
    test()