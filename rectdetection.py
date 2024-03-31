import cv2
import numpy as np
def correct(approx):
    list_of_cord=[]
    for i in approx:
        x=i[0][0]
        y=i[0][1]
        list_of_cord.append(tuple([x,y]))
    return list_of_cord



def detect_rectangles(image_path):
    # Read the image
    image = cv2.imread(image_path)

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to remove noise
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Detect edges using Canny
    edges = cv2.Canny(blurred, 50, 150)

    # Find contours in the edged image
    contours, _ = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    cordinations=[]
    # Loop over the contours
    for contour in contours:
        # Approximate the contour
        peri = cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, 0.02 * peri, True)

        # If the contour has four vertices, it is likely a rectangle
        if len(approx) == 4 and peri>400:
            # Draw the contour on the original image
            cv2.drawContours(image, [approx], -1, (0, 255, 0), 2)
            cordinations.append(correct(approx))
    return  cordinations[::-1]




