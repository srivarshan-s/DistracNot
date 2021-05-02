import speech_recognition as SpeechRecog
from word import word_filter
import pyaudio

init_rec = SpeechRecog.Recognizer()

while True:
	words = []
	for i in range(3):
		with SpeechRecog.Microphone() as source:
			audio_data = init_rec.record(source, duration=10)
			try:
				text = init_rec.recognize_google(audio_data)
			except:
				text = ''
		text_filtered = word_filter(text)
		for j in text_filtered:
			words.append(j)
	print(words)
