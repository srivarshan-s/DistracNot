import speech_recognition as SpeechRecog
from word import word_filter
import pyaudio

init_rec = SpeechRecog.Recognizer()
print("Let's speak!!")
with SpeechRecog.Microphone() as source:
    audio_data = init_rec.record(source, duration=7)
    print("Recognizing your text.............")
    text = init_rec.recognize_google(audio_data)
    # text = init_rec.recognize_google(audio_data)
    # text = word_filter(text)
# print(text)
text_filtered = word_filter(text)
print(text_filtered)
