# Write a Python script with TensorFlow and Matplotlib to implement image reading, augmentation and
# saving functions, and to allow the user to manipulate the images using the Python input() function
# (ref: https://www.w3schools.com/python/python_user_input.asp ). The Python script is to output suitably
# formatted text to the display. A simple menu system is to be created to allow the user to:

# Here, image augmentation is a technique that is used to artificially expand a dataset of available images
# that then can be used in machine learning and deep learning applications.
# Using a digital camera, firstly take photographs of 10 different objects to form the initial image dataset.
# These then form the image dataset that can be read by the Python script.
import sys
import os


def list_menu():
    print("************Image Augmentation Workshop Project**************")
    choice = input(
        """1: List the names of the available images.
2: Read a given RGB colour image using the image file name in order to select the image.
3: Convert the image to grayscale.
4: Convert the image to a black & white image where the RGB colour image is initially converted to a grayscale image.
5. Adjust the individual red, green and blue values for the pixels in the image with a number from 0 to 255.
6: View the original and modified image using Matplotlib.
7: Save the modified image with a given image file name.
8: Quit the Python script run.

Please enter your choice: """)

    if choice == "1":
        list_names()
        list_menu()
    elif choice == "8":
        sys.exit()
    else:
        print("You must only select either a number from 1 - 8")
        print("Please try again")
        list_menu()


# 1.
def list_names():
    path = './images'

    files = os.listdir(path)

    for f in files:
        print(f)


# main
if __name__ == '__main__':
    list_menu()
