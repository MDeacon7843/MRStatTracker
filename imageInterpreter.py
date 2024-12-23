import pytesseract
from PIL import Image
import os
import cv2


def splitImages(images: list, includeEnemy=False) -> list:
    """
    Splits the image(s) by the predetermined sectors to ensure only relevant information is processed

    :param images: A list of PIL Image objects to be split
    :type images: list of PIL.Image
    :param includeEnemy: A boolean to determine whether to include the enemy players when splitting the image
    :type includeEnemy: bool

    :return: A list of lists of sectors of each image as PIL.Image objects
    :rtype: list of lists of PIL.Image
    """
    
    # Define the list to return
    cropped_images = []

    # Define whether enemies will be included
    players = 10 if includeEnemy else 5

    # Loop through images
    for image in images:
        for player in range(players):
            offset = 49 * player
            if player > 4:
                offset += 3
            cropped_images.append(Image.crop((159, 244 + offset, 1729, 290 + offset)))

        



def grabStats(img: Image):
    pytesseract.image_to_string


def grabImages(target: str) -> list:
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