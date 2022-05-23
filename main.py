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
selected_file = None
modified_file = None


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
        print('-- Selected File: [' + str(selected_file) + '] --')
    else:
        print('----------------------------------------------------')
        print('Please select first image!')
        list_names()
        list_menu()

    if modified_file is not None:
        print('-- Modified File exists --')

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
    choice = input('Please enter your choice: ')

    if choice == '1':
        list_names()
    elif choice == '2':
        read_rgb(selected_file)
    elif choice == '3':
        convert_gray(selected_file)
    elif choice == '4':
        convert_bw(selected_file)
    elif choice == '5':
        rgb_modify(selected_file)
    elif choice == '6':
        plot_image(selected_file, modified_file)
    elif choice == '7':
        save_image(modified_file)
    elif choice == '8':
        sys.exit()
    else:
        print('You must only select either a number from 1 - 8, please try again')

    list_menu()


def select_file():
    global selected_file
    global modified_file
    filename = input('Please choose your image: ')
    selected_file = filename
    # reset modified_file
    modified_file = None
    return selected_file


def cache_mod_file(filename):
    global modified_file
    modified_file = filename


def show_img(image, title):
    print(image.shape)
    plt.figure()
    plt.title(title)
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
    show_img(cv2.cvtColor(image, cv2.COLOR_BGR2RGB), 'read_rgb() ' + filename)


# 3. Convert the image to grayscale.
def convert_gray(filename):
    image = cv2.imread(path + filename)
    # convert to grayscale value
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # convert to three gray color channel
    gray_image = cv2.merge([gray, gray, gray])
    cache_mod_file(gray_image)
    show_img(gray_image, 'convert_gray() ' + filename)


# 4. Convert the image to a black & white image where the RGB colour image is initially converted to
# a grayscale image, and the grayscale image is then converted to a black & white image by setting
# a threshold value from 0 to 255. If a pixel value is below or equal to the threshold value, it is set to
# black and if above the threshold value, it is set to white.
def convert_bw(filename):
    image = cv2.imread(path + filename)
    # convert to grayscale value
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # convert to three gray color channel
    gray_image = cv2.merge([gray, gray, gray])
    # set threshold
    try:
        thresh = int(input('Threshold between 0 - 255: '))
        # TODO: check int
        if thresh < 0 or thresh > 256:
            print('please input threshold value between 0 - 255!')
            convert_bw(filename)
        # covert to black & white image
        bw_image = cv2.threshold(gray_image, thresh, 255, cv2.THRESH_BINARY)[1]
        cache_mod_file(bw_image)
        show_img(bw_image, 'convert_bw() ' + filename)
    except ValueError:
        print("Illegal Input!")


# 5. Adjust the individual red, green and blue values for the pixels in the image with a number from 0
# to 255.
def rgb_modify(filename):
    try:
        image = cv2.imread(path + filename)

        x, y = map(int, input("Enter x, y coordinate: ").split(","))
        (b, g, r) = image[x, y]
        print('Before: The (B,G,R) value at [' + str(x) + ', ' + str(y) + '] is ', (b, g, r))

        b_input, g_input, r_input = map(float, input("Enter B, G, R value: ").split(','))
        # set BGR value
        image[x, y] = (b_input, g_input, r_input)

        # test actual color change with bigger area
        # image[0:x, 0:y] = (b_input, g_input, r_input)

        (b, g, r) = image[x, y]
        print('After: The (B,G,R) value at [' + str(x) + ', ' + str(y) + '] is ', (b, g, r))
        adjusted_img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        cache_mod_file(adjusted_img)
        show_img(adjusted_img, 'rgb_modify() ' + filename)
    except ValueError:
        print("Illegal Input!")


# 6. View the original and modified image using Matplotlib.
def plot_image(original, modified):
    if modified_file is None:
        print('please modify image first!')
        list_menu()

    org_image = cv2.imread(path + original)

    fig, axs = plt.subplots(1, 2)
    plt.suptitle('plot_image()')

    # original picture
    axs[0].imshow(cv2.cvtColor(org_image, cv2.COLOR_BGR2RGB))
    axs[0].set_title('Original image', fontsize=10)
    axs[0].set_xlabel('x pixel', fontsize=10)
    axs[0].set_ylabel('y pixel', fontsize=10)

    # modified picture
    axs[1].imshow(cv2.cvtColor(modified, cv2.COLOR_BGR2RGB))
    axs[1].set_title('Modified image', fontsize=10)
    axs[1].set_xlabel('x pixel', fontsize=10)
    axs[1].set_ylabel('y pixel', fontsize=10)

    plt.show()


# 7. Save the modified image with a given image file name.
def save_image(modified):
    filename = input('Input file name for modified image: ')
    # store in mod_images directory
    os.chdir('./mod_images/')
    # store image
    cv2.imwrite(filename, modified)
    print('-- ' + filename + 'stored successfully in ./mod_images/ --')
    # return to previous folder
    os.chdir('..')


# main
if __name__ == '__main__':
    show_setup()
    list_menu()
