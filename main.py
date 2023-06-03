# import library and functions 
from PIL import Image
import pytesseract
from os import path
import sys



def picture_to_text():
    try:
        # Check argument and must be pass the file 
        # For example
        # python main.py ~/source-code/python/picture-to-text/test.png
        if len(sys.argv) != 2:
            raise ValueError('There isn\'t and picture pass as argument !') 

        picture_path = sys.argv[1]
        # Check the file is exist or not 
        # If file didn't exist , generate Error 
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
