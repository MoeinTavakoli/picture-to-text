# Picture Text Extractor


## Description
This Python script uses the `pytesseract` library to extract text from a picture and print it to the console.

## Requirements
This project requires Python 3.x and the following libraries to be installed:

  - PIL (Python Imaging Library)
  - pytesseract

  
You can install these dependencies using pip:

```
pip install pillow pytesseract
```


In addition, you will need to have Tesseract OCR installed on your system. You can install Tesseract OCR on Ubuntu using the following command:

```
sudo apt-get install tesseract-ocr
```

## Usage

To use this script, run the `main.py` file with the path to the picture you want to extract text from as a command-line argument. For example:

```python
python main.py /path/to/picture.jpg
```

The script will then use `pytesseract` to extract any text from the picture and print it to the console.
