from PIL import Image
import pytesseract
from os import path
import sys



def picture_to_text():
    try:
        picture_path = sys.argv[1]
        if not (path.isfile(picture_path)):
            raise ValueError('file not found !!!') 
        image = Image.open(picture_path)
        image = image.convert('L')
        image = image.point(lambda x:0 if x < 128 else 255 , "1")
        text = pytesseract.image_to_string(image)
        return text
    except ValueError as exp:
        print("Error", exp) 
    
text = picture_to_text()

print(text)
