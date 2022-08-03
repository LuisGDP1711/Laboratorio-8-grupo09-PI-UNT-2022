import speech_recognition as sr
import wikipedia as wk 

while True:
    mic = sr.Recognizer()

    with sr.Microphone() as source:
        print("Hable lo que desea buscar:")
        audio = mic.listen(source)
        mic.adjust_for_ambient_noise(source)

        try:
            text = mic.recognize_google(audio)
            summary = wk.summary(text)
            print(summary)
            break
        except:
            print("No lo capto, repite por f")



