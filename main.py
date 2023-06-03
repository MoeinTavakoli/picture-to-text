from PIL import Image
import pytesseract
from os import path

def picture_to_text(picture_path):
    try:
        if not (path.isfile(picture_path)):
            raise ValueError('file not found !!!') 
        image = Image.open(picture_path)
        image = image.convert('L')
        image = image.point(lambda x:0 if x < 128 else 255 , "1")
        text = pytesseract.image_to_string(image)
        return text
    except ValueError as exp:
        print("Error", exp) 
    
picture_path = input('please insert picture path : ')
text = picture_to_text(picture_path)

print(text)
