import speech_recognition as stt
from gtts import gTTS
import os


done = False
r = stt.Recognizer()
r.adjust_for_ambient_noise
error_count = 0

def synthesis(speech):
    outbuffer = "speech-buffer.mp3"
    tts = gTTS(speech)
    tts.save(outbuffer)
    os.system(outbuffer)


synthesis("I'm listening")

while not done:
    with stt.Microphone() as source:
        #say that it's listening
        audio = r.listen(source)

        try:
            text = r.recognize_google(audio)

            #check input, start options
            print(text)

            if text != "":
                if text == "end":
                    synthesis("goodbye")
                    done = True
                else:
                    synthesis(text)
            else:
                print("Nothing heard...")
        except:
            error_count += 1
