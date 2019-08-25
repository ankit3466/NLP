import speech_recognition as sr
from textblob import TextBlob
import goslate

s = sr.Recognizer()

print(sr.__version__)
#print(sr.Microphone.list_microphone_names())

with sr.Microphone() as source:
	print('Say something...')
	audio = s.listen(source)
	text = s.recognize_google(audio)

print('Origin Language : ')
print(text)

word = TextBlob(text)
print('Translated language : ')
print(word.translate(from_lang='en' , to='hi'))

# Another method
gs = goslate.Goslate()
print(gs.translate(text,'hi'))
print(gs.translate(text,'es'))

