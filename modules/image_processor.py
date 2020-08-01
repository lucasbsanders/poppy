# pip install ics
# pip install pyspellchecker
# pip install pytesseract
import numpy as np
import glob
import cv2
import pytesseract
import re
import os


# Resize based on the image size
def resize(img):
    height = img.shape[0]
    width = img.shape[1]

    if (height <= 1499) & (width <= 1999):
        img = cv2.resize(img, None, fx=2, fy=2)
    elif (height >= 1500) & (width >= 2000):
        img = cv2.resize(img, None, fx=0.25, fy=0.25)
    else:
        img = cv2.resize(img, None, fx=0.5, fy=0.5)
    return img


def img_pipeline():
    # pytesseract.pytesseract.tesseract_cmd = r".\Tesseract-OCR\tesseract.exe"

    # Reading in the images to process
    # Test images
    # img_one = cv2.imread("images/alamy.jpg")  # Nope lol
    # img_two = cv2.imread("images/amoxicillin.jpeg")  # Good
    # img_three = cv2.imread("images/calvin.jpeg")  # Good but there needs to be some unnecessary text removed
    # img_four = cv2.imread("images/chris.jpg")  # Not Good (directive)
    # img_five = cv2.imread("images/elvis.jpeg")  # Good (duration)
    # img_six = cv2.imread("images/chris2.jpg")  # Good Further processing required
    # img_seven = cv2.imread("images/jane.jpeg")  # Good
    # img_eight = cv2.imread("images/miley.png")  # Good
    # img_nine = cv2.imread("images/opioid-bottle.jpg")  # Good
    # img_ten = cv2.imread("images/warfarin.jpg")  # Good

    # tr_exe_dir = os.path.join(os.path.abspath(
    #     os.path.dirname((__file__))), "Tesseract-OCR/tesseract.exe")
    # pytesseract.pytesseract.tesseract_cmd = tr_exe_dir
    pytesseract.pytesseract.tesseract_cmd = '/app/.apt/usr/bin/tesseract'
    img_list = []
    # find the file with a .png extension
    for file in glob.glob('imageToSave.png'):
        img_list.append(file)

    if len(img_list) == 0:
        print("Can't find the file")
        exit()

    # Building the Image Processing Pipeline.
    # 1
    # Resize image_three to make it easier for OCR to analyze
    # This size depends on the size of the picture's text
    # If the image is larger than a certain size reduce its size else increase its size
    # Change this so the user can select the image
    resized = resize(cv2.imread(img_list[0]))

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
    threshold = cv2.adaptiveThreshold(
        greyscale, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 85, 20)

    img_to_return = threshold

    # Use NLTK To complete the Directives and their Durations
    # Convert Directives and Logic into events on an ics file.

    # cv2.imshow("IMG2", resized)
    # cv2.imshow("IMG1", threshold)
    # Keep the image open
    cv2.waitKey(0)  # Use NLTK To complete the Directives and their Durations
    # Convert Directives and Logic into events on an ics file.
    preprocessed_string = pytesseract.image_to_string(img_to_return)
    # I had to write the text to a file to remove the formatting that pytessaract has on the string
    write_to_file("tessaract_text.txt", preprocessed_string)

    string_from_file = get_text("tessaract_text").replace("\n", " ")

    return string_from_file


def get_text(filename_root):
    name = open(filename_root + '.txt')
    text = name.read()
    name.close()
    return text


def write_to_file(filename, string):
    file_name = open(filename, 'w')
    file_name.write(string)
    file_name.close()
