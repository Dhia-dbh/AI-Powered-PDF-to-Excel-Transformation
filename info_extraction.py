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


def image_to_text(image_path):
    crop_image(image_path, 120, 1360, 850, 200).save(image_path.split(".")[0] + "__1" + ".png")
    crop_image(image_path, 1720, 1360, 850, 200).save(image_path.split(".")[0] + "__2" + ".png")
    crop_image(image_path, 120, 2650, 850, 200).save(image_path.split(".")[0] + "__3" + ".png")
    crop_image(image_path, 1720, 2650, 850, 200).save(image_path.split(".")[0] + "__4" + ".png")
    crop_image(image_path, 120, 3950, 850, 200).save(image_path.split(".")[0] + "__5" + ".png")
    crop_image(image_path, 1720, 3950, 850, 200).save(image_path.split(".")[0] + "__6" + ".png")
        # Read the image
    img1 = cv2.imread(image_path.split(".")[0]+"__1"+".png")
    img2 = cv2.imread(image_path.split(".")[0]+"__2"+".png")
    img3 = cv2.imread(image_path.split(".")[0]+"__3"+".png")
    img4 = cv2.imread(image_path.split(".")[0]+"__4"+".png")
    img5 = cv2.imread(image_path.split(".")[0]+"__5"+".png")
    img6 = cv2.imread(image_path.split(".")[0]+"__6"+".png")
    # Convert the image to grayscale (recommended for OCR)
    gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    gray3 = cv2.cvtColor(img3, cv2.COLOR_BGR2GRAY)
    gray4 = cv2.cvtColor(img4, cv2.COLOR_BGR2GRAY)
    gray5 = cv2.cvtColor(img5, cv2.COLOR_BGR2GRAY)
    gray6 = cv2.cvtColor(img6, cv2.COLOR_BGR2GRAY)

    # Apply any pre-processing techniques if needed (e.g., denoising, thresholding)

    # Extract text using Tesseract (config='' removes background noise)
    text = ""
    lastList=[]
    text = image_to_string(gray1, config='')
    lastList.append(proccess_text(text))
    text = image_to_string(gray2, config='')
    lastList.append(proccess_text(text))
    text = image_to_string(gray3, config='')
    lastList.append(proccess_text(text))
    text = image_to_string(gray4, config='')
    lastList.append(proccess_text(text))
    text = image_to_string(gray5, config='')
    lastList.append(proccess_text(text))
    text = image_to_string(gray6, config='')
    lastList.append(proccess_text(text))

    print(lastList)
    correct_mistakes(lastList)
    print(lastList)

    # Print the extracted text
    return lastList
def proccess_text(t):
    text = t.splitlines()
    filtered_list = [item for item in text if item]
    if filtered_list[0].count("-")==2:
        return filtered_list
    else:
        return ["",filtered_list[0],filtered_list[1]]





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
    text = text.splitlines()
    filtered_list = [item for item in text if item]

    for line in filtered_list:
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
    print(sublists)
    correct_mistakes(sublists)
    print(sublists)
    return sublists

def correct_mistakes(s):
    t=['DA-201-NVY', 'KNIT PATCH HAT WITH POM - NAVY', 'Qty On-Hand: 33']
    for i in s:
        if i[0].count("-")!=2:
            i[0]=t[0]
        if i[1].count("-")!=1:
            i[1]=t[1]
        if i[2].count(":") != 1:
            i[2] = t[2]
def process_image_to_text(img_path):
    return image_to_text(img_path)


