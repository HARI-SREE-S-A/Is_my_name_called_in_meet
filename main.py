import pyttsx3
import speech_recognition as sr
import sounddevice as sd

names = ["hari" , "Harry" ,"Haryysree" ,"Hari sree" ,"haris","harvis","har"]



engine = pyttsx3.init()
r = sr.Recognizer()
mic = sr.Microphone()


def play_audio(audio_data,sample_rate):
    sd.play(audio_data, sample_rate, blocking=True)


engine.say("Welcome to harvis , your personal AI , ask me anything")
engine.runAndWait()
with mic as source:
    while True:
        try:
            print("Listening for command...")
            audio = r.listen(source)
            command = r.recognize_google(audio)

            print(command)
            for name in names:
                if name.lower() in command.lower():
                    engine.say("Your name is called.")
                    engine.runAndWait()
                    break
            else:
                continue


        except sr.UnknownValueError:
            print("Could not understand command")
            engine.say("Could not understand that ,please say clearly")
            engine.runAndWait()

