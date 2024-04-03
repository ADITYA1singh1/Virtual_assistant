import speech_recognition as sr
import pyttsx3
import pywhatkit


listener = sr.Recognizer() #recognise of your voice
machine = pyttsx3.init()

def talk(text):
     machine.say(text)
machine.runAndWait()

def input_instruction():

 try:                        #sometime an error occur
    with sr.Microphone() as source:
     print("listining")     #gives green flag to talk
     speech = listener.listen(source)
     instruction = listener.recognize_google(speech)
     instruction= instruction.lower()
     print(instruction)


 except:
    pass

def play_jarvis():
 instruction=input_instruction
 print(instruction)