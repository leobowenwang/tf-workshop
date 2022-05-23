# Write a Python script with TensorFlow and Matplotlib to implement image reading, augmentation and
# saving functions, and to allow the user to manipulate the images using the Python input() function
# (ref: https://www.w3schools.com/python/python_user_input.asp ). The Python script is to output suitably
# formatted text to the display. A simple menu system is to be created to allow the user to:

# 1. List the names of the available images.
# 2. Read a given RGB colour image using the image file name in order to select the image.
# 3. Convert the image to grayscale.
# 4. Convert the image to a black & white image where the RGB colour image is initially converted to
# a grayscale image, and the grayscale image is then converted to a black & white image by setting
# a threshold value from 0 to 255. If a pixel value is below or equal to the threshold value, it is set to
# black and if above the threshold value, it is set to white.
# 5. Adjust the individual red, green and blue values for the pixels in the image with a number from 0
# to 255.
# 6. View the original and modified image using Matplotlib.
# 7. Save the modified image with a given image file name.
# 8. Quit the Python script run.

# Here, image augmentation is a technique that is used to artificially expand a dataset of available images
# that then can be used in machine learning and deep learning applications.
# Using a digital camera, firstly take photographs of 10 different objects to form the initial image dataset.
# These then form the image dataset that can be read by the Python script.

def print_hi(name):
    print(f'Hi, {name}')


if __name__ == '__main__':
    print_hi('PyCharm')
