# Write a Python script with TensorFlow and Matplotlib to implement image reading, augmentation and
# saving functions, and to allow the user to manipulate the images using the Python input() function
# (ref: https://www.w3schools.com/python/python_user_input.asp ). The Python script is to output suitably
# formatted text to the display. A simple menu system is to be created to allow the user to:

# Here, image augmentation is a technique that is used to artificially expand a dataset of available images
# that then can be used in machine learning and deep learning applications.
# Using a digital camera, firstly take photographs of 10 different objects to form the initial image dataset.
# These then form the image dataset that can be read by the Python script.
import sys
import time
import os
import matplotlib as mpl
import matplotlib.pyplot as plt
import cv2

path = './images/'
selected_file = ''
modified_file = ''


def show_setup():
    # ------------------------------------------------------
    # -- Start of script run actions
    # ------------------------------------------------------

    print('----------------------------------------------------')
    print('-- Start script run ' + str(time.strftime('%c')))
    print('----------------------------------------------------\n')

    print('-- Python version     : ' + str(sys.version))
    print('-- Matplotlib version : ' + str(mpl.__version__))
    print('-- Opencv version     : ' + str(cv2.__version__))


def list_menu():
    print('')
    if selected_file:
        print('-- Selected File: [' + selected_file + '] --')
    else:
        print('----------------------------------------------------')
        print('Please select first image!')
        list_names()
        list_menu()

    print('1: List the names of the available images.')
    print('2: Read a given RGB colour image using the image file name in order to select the image.')
    print('3: Convert the image to grayscale.')
    print('4: Convert the image to a black & white image where the RGB colour image is initially converted to a '
          'grayscale image.')
    print('5. Adjust the individual red, green and blue values for the pixels in the image with a number from 0 '
          'to 255.')
    print('6: View the original and modified image using Matplotlib.')
    print('7: Save the modified image with a given image file name.')
    print('8: Quit the Python script run.')
    choice = input(
        '''Please enter your choice: ''')

    if choice == '1':
        list_names()
    elif choice == '2':
        read_rgb(selected_file)
    elif choice == '3':
        convert_gray(selected_file)
    elif choice == '4':
        convert_gray(selected_file)
    elif choice == '5':
        rgb_modify(selected_file)
    elif choice == '6':
        plot_image(selected_file)
    elif choice == '8':
        sys.exit()
    else:
        print('You must only select either a number from 1 - 8, please try again')

    list_menu()


def select_file():
    global selected_file
    filename = input(
        '''Please choose your image: ''')
    selected_file = filename
    return selected_file


def show_single_img(image):
    plt.figure()
    plt.imshow(image)
    plt.show()


# 1. List the names of the available images.
def list_names():
    print('-- List of images --')
    filelist = []

    for files in os.listdir(path):
        filelist.append(files)
        print(files)

    if select_file() not in filelist:
        print('Please input valid file name!')
        print('')
        list_names()


# 2. Read a given RGB colour image using the image file name in order to select the image.
def read_rgb(filename):
    image = cv2.imread(path + filename)
    print(image.shape)


# 3. Convert the image to grayscale.
def convert_gray(filename):
    image = cv2.imread(path + filename)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    print(gray_image.shape)
    show_single_img(gray_image)


# 4. Convert the image to a black & white image where the RGB colour image is initially converted to
# a grayscale image, and the grayscale image is then converted to a black & white image by setting
# a threshold value from 0 to 255. If a pixel value is below or equal to the threshold value, it is set to
# black and if above the threshold value, it is set to white.
def convert_bw(filename):
    image = cv2.imread(path + filename)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray_not = cv2.bitwise_not(gray)
    thresh = 150
    img_threshold = cv2.threshold(gray_not, thresh, 255, cv2.THRESH_BINARY)[1]
    cv2.imshow('threshold', img_threshold)

    show_single_img(img_threshold)
    # print(img_threshold.shape)


# 5. Adjust the individual red, green and blue values for the pixels in the image with a number from 0
# to 255.
def rgb_modify(filename):
    image = cv2.imread(path + filename)
    (b, g, r) = image[20][50]
    print('The (B,G,R) value at 50th pixel of the 20th row is ', (b, g, r))
    image[20][50] = (0, 0, 255)
    (b, g, r) = image[20][50]
    print('The (B,G,R) value at 50th pixel of the 20th row is ', (b, g, r))
    adjusted_img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    show_single_img(adjusted_img)

# 6. View the original and modified image using Matplotlib.
def plot_image(original):
    org_image = cv2.imread(path + original)

    fig, axs = plt.subplots(1, 2)
    plt.suptitle('Images')

    axs[0].imshow(cv2.cvtColor(org_image, cv2.COLOR_BGR2RGB))
    axs[0].set_title('Original image', fontsize=10)
    axs[0].set_xlabel('x pixel', fontsize=10)
    axs[0].set_ylabel('y pixel', fontsize=10)

    plt.show()


# 7. Save the modified image with a given image file name.

# main
if __name__ == '__main__':
    show_setup()
    list_menu()
