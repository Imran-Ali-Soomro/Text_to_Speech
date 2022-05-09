# To convert text into Speech
from gtts import gTTS

# OS can automatically play converted audio
import os   

# Read from textfile
Textfile = open("SomeText.txt").read()
# text = "Hi, This is Imran Ali"

# select language
language = "en"

# 
speech = gTTS(text = Textfile, lang = language, slow=False)

# to save the speech
speech.save("speech.mp3")

# to play Convered file
os.system("speech.mp3")