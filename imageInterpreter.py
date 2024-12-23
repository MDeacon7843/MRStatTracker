import pytesseract
from PIL import Image
import os
import cv2
import player

def splitImages(images: list, includeEnemy=False) -> list:
    """
    Splits the image(s) by the predetermined sectors to ensure only relevant information is processed

    :param images: A list of PIL Image objects to be split
    :type images: list of PIL.Image
    :param includeEnemy: A boolean to determine whether to include the enemy players when splitting the image
    :type includeEnemy: bool

    :return: A list of cropped images corresponding to sectors of the image
    :rtype: list of PIL.Image
    """
    
    # Check edge case
    if not images:
        return []

    # Define the list to return
    cropped_images = []

    # Define number of players according to the includeEnemy flag
    num_players = 12 if includeEnemy else 6

    # Define constants
    PLAYER_HEIGHT = 49  # Height offset for each player
    ENEMY_OFFSET = 3    # When including enemies increase offset on their crops
    TOP_LEFT_CORNER = (159, 244) # Predetermined pixel coordinates for the first player's top left corner
    BOTTOM_RIGHT_CORNER = (1729, 290) # Predetermined pixel coordinates for the first player's bottom right corner

    # Loop through images
    for image in images:
        for player in range(num_players):
            offset = PLAYER_HEIGHT * player
            if player > 4:
                offset += ENEMY_OFFSET
            cropped_images.append(image.crop((TOP_LEFT_CORNER[0], TOP_LEFT_CORNER[1] + offset, BOTTOM_RIGHT_CORNER[0], BOTTOM_RIGHT_CORNER[1] + offset)))
    
    # Return the list of cropped images
    return cropped_images


def grabStats(img: Image):
    pass


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
    images = grabImages("C:/Users/MDeac/OneDrive/Desktop/CS Projects/marvelRivalsScreenshots")
    cropped_image = splitImages(images[:1], True)
    for i in range(len(cropped_image)):
        cropped_image[i].save("test_crop.png")
        img = cv2.imread("test_crop.png")
        cv2.imshow("TEST WINDOW", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        del img
        os.remove("./test_crop.png")






if __name__ == "__main__":
    test()