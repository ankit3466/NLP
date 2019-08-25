import speech_recognition as sr

s = sr.Recognizer()

print(sr.__version__)
#print(sr.Microphone.list_microphone_names())

with sr.Microphone() as source:
	print('Say something...')
	audio = s.listen(source)
	text = s.recognize_google(audio)
print('you said')
print(text)
