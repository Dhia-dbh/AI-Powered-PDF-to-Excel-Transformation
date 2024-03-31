from pdf2image import convert_from_path
import os
import shutil
from rectdetection import detect_rectangles
from cropping import crop_whole_photo
from convort_excel import convert_info_to_excel
from convort_excel import convert_info_to_excel
from info_extraction import process_image_to_text



def convert_pdf(path, save_dir, res=400):
    pages = convert_from_path(path, res)
    name = "test"
    for idx, page in enumerate(pages):
        page.save(f'{save_dir}/{name}_{idx}.png', 'PNG')
    return idx


def pdf_to_imgs(path):
    if os.path.exists("testing"):
        shutil.rmtree("testing")  # Use shutil.rmtree() to remove directory and its contents
    # Create the directory
    os.makedirs("testing")
    return convert_pdf(path,"testing")

def convert_all_imgs(pathpdf):
    num=pdf_to_imgs(pathpdf)
    for i in range(num):
        path="testing//test_"+str(i)+".png"
        list_of_rect=detect_rectangles(path)
        crop_whole_photo(list_of_rect,path)
        listinfo=process_image_to_text(path)
        listPhoto = []
        for root, dirs, files in os.walk("photos"):
            for file in files:
                listPhoto.append(os.path.join(root, file))

        convert_info_to_excel('example.xlsx',listPhoto,listinfo,i*6)












