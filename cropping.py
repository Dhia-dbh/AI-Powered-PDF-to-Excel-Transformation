import os
import shutil

from PIL import Image, ImageFilter

from PIL import Image, ImageDraw
import  rectdetection as rd
from PIL import Image

def crop_image(image_path, points,save_path):
    # Open the original image
    image = Image.open(image_path)

    # Get the bounding box of the detected rectangle
    x_min = min(points[0][0], points[1][0], points[2][0], points[3][0])
    x_max = max(points[0][0], points[1][0], points[2][0], points[3][0])
    y_min = min(points[0][1], points[1][1], points[2][1], points[3][1])
    y_max = max(points[0][1], points[1][1], points[2][1], points[3][1])

    # Crop the image based on the bounding box
    cropped_image = image.crop((x_min, y_min, x_max, y_max))
    cropped_image.save(save_path)

def crop_whole_photo(list_poits,path):
    if os.path.exists("photos"):
        shutil.rmtree("photos")  # Use shutil.rmtree() to remove directory and its contents
        # Create the directory
    os.makedirs("photos")
    for i in range(len(list_poits)):
        crop_image(path,list_poits[i],"photos//img"+str(i)+".png")
'''
points = rd.detect_rectangles("testing//test_0.png")[3]
print(points)
cropped_img = crop_image("testing//test_0.png", points)
cropped_img.show()
'''