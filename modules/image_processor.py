# pip install ics
# pip install pyspellchecker
# pip install pytesseract
# pip install cv2
import numpy as np
import cv2
import pytesseract
import re


# Resize based on the image size
def resize(img):
    height = img.shape[0]
    width = img.shape[1]
    # print("The height is:", height)
    # print("The width is:", width)

    prescription_text = pytesseract.image_to_string(img)
    if (height <= 1499) & (width <= 1999):
        img = cv2.resize(img, None, fx=2, fy=2)
    elif (height >= 1500) & (width >= 2000):
        img = cv2.resize(img, None, fx=0.25, fy=0.25)
    else:
        img = cv2.resize(img, None, fx=0.5, fy=0.5)
    return img


def img_pipeline():
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

    # Reading in the images to process
    img_one = cv2.imread("images/alamy.jpg")  # Nope lol
    img_two = cv2.imread("images/amoxicillin.jpeg")  # Good Further Processing Required
    img_three = cv2.imread("images/calvin.jpeg")  # Good
    img_four = cv2.imread("images/chris.jpg")  # Not Good (directive)
    img_five = cv2.imread("images/elvis.jpeg")  # Not Good (duration)
    img_six = cv2.imread("images/chris2.jpg")  # Good Further processing required
    img_five = cv2.imread("images/elvis.jpeg")  # Not Good (duration)
    img_eight = cv2.imread("images/jane.jpeg")  # Good Further Processing
    img_nine = cv2.imread("images/miley.png")  # Good
    img_ten = cv2.imread("images/opioid-bottle.jpg")  # Good Further Processing // Fix me
    img_eleven = cv2.imread("images/warfarin.jpg")  # Good

    # Building the Image Processing Pipeline.
    # 1
    # Resize image_three to make it easier for OCR to analyze
    # This size depends on the size of the picture's text
    # If the image is larger than a certain size reduce its size else increase its size
    # Change this so the user can select the image
    resized = resize(img_eleven)

    # 2
    # Convert the image to grayscale to remove any filtering
    greyscale = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)

    # # 3
    # # Find some edges
    # edges = cv2.Canny(greyscale, 30, 200)
    # cv2.waitKey(0)
    # # Find the contours
    # _, contours = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    # cv2.imshow("Canny edges after contouring", edges)
    # cv2.waitKey(0)
    # This is useful for reducing the noise from a background that is not homogeneous
    threshold = cv2.adaptiveThreshold(greyscale, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 85, 20)

    img_to_return = threshold

    # Use NLTK To complete the Directives and their Durations
    # Convert Directives and Logic into events on an ics file.

    # cv2.imshow("IMG2", resized)
    # cv2.imshow("IMG1", threshold)
    # Keep the image open
    cv2.waitKey(0)   # Use NLTK To complete the Directives and their Durations
    # Convert Directives and Logic into events on an ics file.
    return img_to_return


