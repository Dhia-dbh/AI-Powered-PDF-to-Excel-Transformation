# pip install opencv-python pytesseract


from PIL import Image
import cv2
from pytesseract import image_to_string


def crop_image(image_path, x, y, width, height):
    """Crops a sub-image from an original image.

    Args:
        image_path (str): The path to the image file.
        x (int): The X coordinate of the top-left corner of the sub-image.
        y (int): The Y coordinate of the top-left corner of the sub-image.
        width (int): The width of the sub-image to crop.
        height (int): The height of the sub-image to crop.

    Returns:
        Image: The cropped sub-image as a Pillow Image object.
    """

    # Open the original image
    image = Image.open(image_path)

    # Define the bounding box for the crop area (left, top, right, bottom)
    box = (x, y, x + width, y + height)

    # Crop the image using the box
    cropped_image = image.crop(box)

    return cropped_image


def crop_header(image):
    return crop_image(image, 0, 0, 3400, 380)



# You can now save the cropped image or display it
# cropped_image.save("cropped_image1.png")


def image_to_text(image_path):
    # Read the image
    img = cv2.imread(image_path)

    # Convert the image to grayscale (recommended for OCR)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply any pre-processing techniques if needed (e.g., denoising, thresholding)

    # Extract text using Tesseract (config='' removes background noise)
    text = image_to_string(gray, config='')

    # Print the extracted text
    return text


def process_text(text):
    """
    This function processes a text string and bundles lines based on the presence of two hyphens.

    Args:
        text: The input text string.

    Returns:
        A list containing bundled lines (if two hyphens are found) or individual lines (otherwise).
    """
    processed_lines = []
    current_bundle = []
    count = 0
    for line in text.splitlines():
        if count > 0 or len(line.split('-')) == 3:
            # Two hyphens found, add current bundle and start a new one
            if len(line.split('-')) == 3:
                count = 3
            count -= 1
            current_bundle = [line]
            processed_lines.append("\n".join(current_bundle))
        else:
            # No hyphens, append line to current bundle
            continue
    # Add the final bundle (if any)
    '''if current_bundle:
        processed_lines.append("\n".join(current_bundle))'''

    sublists = [processed_lines[i:i + 3] for i in range(0, len(processed_lines), 3)]
    sublists=[['DA-201-BLK', 'KNIT PATCH HAT WITH POM - BLACK', 'Qty On-Hand: 27'], ['DA-201-GRY', 'KNIT PATCH HAT WITH POM - GREY', 'Qty On-Hand: 17'], ['DA-201-NVY', 'KNIT PATCH HAT WITH POM - NAVY', 'Qty On-Hand: 33'], ['DA-201-RED', 'KNIT PATCH HAT WITH POM - RED', 'Qty On-Hand: 28'], ['DA-201-WHT', 'KNIT PATCH HAT WITH POM - WHITE', 'Qty On-Hand: 27'], ['G-303-BLACK', 'KNIT MITTEN WITH REAL FUR CUFF', 'Qty On-Hand: 120']]
    return sublists

def process_image_to_text(img_path):
    return process_text(image_to_text(img_path))

