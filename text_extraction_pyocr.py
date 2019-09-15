import pyocr
from PIL import Image
import pyocr.builders

print(pyocr.get_available_tools())
tools = pyocr.get_available_tools()
tool = tools[0]

print(tool.get_available_languages())
lang = tool.get_available_languages()[0]

text = tool.image_to_string(Image.open('exam.jpeg') , lang=lang , 
                                builder=pyocr.tesseract.DigitBuilder())


print(text)

# As line Box
'''
text = tool.image_to_string(Image.open('exam.jpeg') , lang=lang , 
                                builder=pyocr.builders.LineBoxBuilder())


print(text)
print(type(text))
print(len(text))

for i in text:
	print(i.word_boxes)
	print(i.content)
	print(i.position)
'''
#As Text
'''
text = tool.image_to_string(Image.open('exam.jpeg') , lang=lang , 
                                builder=pyocr.builders.TextBuilder())


print(text)
'''
# As Box
'''
text = tool.image_to_string(Image.open('exam.jpeg') , lang=lang , 
                                builder=pyocr.builders.WordBoxBuilder())


print(text)
print(type(text))
print(len(text))

for i in text:
	print(i.content)
	print(i.position)
	print("\n")
'''
