import cv2
from PIL import Image
import pytesseract
from matplotlib import pyplot as plt

image_file = "data/caption.jpg"

img = Image.open(image_file)
img_read = cv2.imread(image_file)
# rotates images


def image_rotation(img):
    Q1 = input(
        "Hello do you want to rotate the image by 45, 90, 180, 270 or 360 degrees?: ")
    if Q1 == "90":
        img.rotate(90).show()
    elif Q1 == "45":
        img.rotate(45).show()
    elif Q1 == "180":
        img.rotate(180).show()
    elif Q1 == "270":
        img.rotate(270).show()
    elif Q1 == "360":
        img.rotate(360).show()
    else:
        print("no, this was not an option!")

# inverts RGB of images


def invert(img_read):
    inverted_image = cv2.bitwise_not(img_read)
    cv2.imwrite("temp/inverted.jpg", inverted_image)

# https://stackoverflow.com/questions/28816046/
# displaying-different-images-with-actual-size-in-matplotlib-subplot


def display(im_path):
    dpi = 80
    im_data = plt.imread(im_path)

    height, width = im_data.shape[:2]

    # What size does the figure need to be in inches to fit the image?
    figsize = width / float(dpi), height / float(dpi)

    # Create a figure of the right size with one axes that takes up the full figure
    fig = plt.figure(figsize=figsize)
    ax = fig.add_axes([0, 0, 1, 1])

    # Hide spines, ticks, etc.
    ax.axis('off')

    # Display the image.
    ax.imshow(im_data, cmap='gray')

    plt.show()

# convert image to grayscaling


def grayscale(img_read):
    gray = cv2.cvtColor(img_read, cv2.COLOR_BGR2GRAY)
    cv2.imwrite("temp/original image", img_read)
    cv2.imwrite("temp/gray image", gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# print(img) #shows image meta-data
grayscale(img_read)
# display(image_file)