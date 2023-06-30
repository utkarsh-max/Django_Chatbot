from gtts import gTTS
from playsound import playsound
tts = gTTS('kya hal hi')
tts.save('speak.mp3')
for i in range(4):
    playsound('speak.mp3')