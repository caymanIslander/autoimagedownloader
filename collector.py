import os
from PIL import Image
import hashlib
from bing_image_downloader import downloader

def downloadimg(query_str,limit_int,destination):
    downloader.download(query_str, limit_int, output_dir= destination)


def dhash(image, hash_size=8):
    image = image.convert('L').resize((hash_size + 1, hash_size), Image.ANTIALIAS)
    pixels = list(image.getdata())
    diff = []
    for row in range(hash_size):
        for col in range(hash_size):
            pixel_left = image.getpixel((col, row))
            pixel_right = image.getpixel((col + 1, row))
            diff.append(pixel_left > pixel_right)
    decimal_value = 0
    hex_string = []
    for index, value in enumerate(diff):
        if value:
            decimal_value += 2**(index % 8)
        if (index % 8) == 7:
            hex_string.append(hex(decimal_value)[2:].rjust(2, '0'))
            decimal_value = 0
    return ''.join(hex_string)



def remove_duplicates(directory):
    # Create a dictionary to store the image hashes
    image_hashes = {}

    for filename in os.listdir(directory):
        if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".jpeg"):
            filepath = os.path.join(directory, filename)

            # Open the image using PIL (Python Imaging Library)
            image = Image.open(filepath)

            # Calculate the image hash using the dhash function
            image_hash = dhash(image)

            # Check if the hash is already in the dictionary
            if image_hash in image_hashes:
                # Remove the duplicate image
                os.remove(filepath)
                print(f"Removed duplicate: {filename}")
            else:
                # Add the hash to the dictionary
                image_hashes[image_hash] = filename



def createdir(destination):


def welcome():
    destination = input("Choose destination directory:")
    user_query = input("Image you want to search:")
    limit_int = int(input("How many images do you want to search:"))
    i = 0
    while i != 1 :
        choice = input(f"You will search for {user_query}, it will be also your folder name under {destination} \n Y/n \n")
        if choice == "Y" or choice == "y":
            i += 1
            createdir(destination)
        if choice == "N" or choice == "n":
            downloadimg(query_str= user_query, limit_int= limit_int, destination= destination)
