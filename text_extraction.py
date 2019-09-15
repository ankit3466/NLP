import pytesseract
import cv2

img = cv2.imread('exam.jpeg')

text = pytesseract.image_to_string(img)

print(text)
