import speech_recognition as sr
import os
import datetime
import smtplib
import webbrowser
import wolframalpha
import random
import pyttsx3
from gtts import gTTS
import sys
import wikipedia
from playsound import playsound
import time
# For Unittesting
import VPA
import unittest
import flikr_download

class TestVPA(unittest.TestCase):
    def test1(self):
        self.assertEqual(VPA.wait(), None)

unittest.main()

# engine = pyttsx3.init("sapi5")

# def talk(audio):
#     print("JARVIS: " + audio)
#     engine.say(audio)
#     engine.runAndWait()
    

# def greetMe():
#     CurrentHour = int(datetime.datetime.now().hour)
#     if CurrentHour >= 0 and CurrentHour < 12:
#         txt = 'sadf Good Morning!'
#         print("JARVIS: " + txt[4:])
#         speech = gTTS(text = txt, lang= 'en', slow=False)
#         speech.save('text.mp3')
#         playsound('text.mp3')
        
#     elif CurrentHour >=12 and CurrentHour < 18:
#         talk("Good Afternoon!")
#     else:
#         talk("Good Evening!")
        
# greetMe()

# def GiveCommand():
#     k = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Listening....")
#         k.pause_threshold = 1
#         audio = k.listen(source)
#     try:
#         Input = k.recognize_google(audio, language='en-in')
#         print("Yuvraj Singh: " + Input + "\n")
        
#     except sr.UnknownValueError:
#         talk("Sorry! I didn\'t get that! Try typing it here!")
#         Input = str(input("Command: "))
    
#     except sr.RequestError as e:
#         talk("Could not request results from Google Speech Recognition service; {0}".format(e))
        
#     return Input
    

# if __name__ == "__main__":
#     greetMe()
#     while True:
#         Input = GiveCommand()
#         Input = Input.lower()
        
#         if "get lost" in Input:
#             talk("Can you say it in a proper manner because this thing hurts me.")
#             talk("You can say exit or bye")
#             continue
        
#         if "exit" in Input or "quit" in Input or "bye" in Input:
#             talk("Ok bye, have a great time.")
#             sys.exit()

#         elif "open google" in Input:
#             talk("Opening Google...")
#             webbrowser.open("www.google.com")
            
#         elif "open youtube" in Input:
#             talk("Sure.")
#             webbrowser.open("www.youtube.com")
            
#         elif "what\'s up" in Input or "how are you" in Input:
#             setReplies = ['Just doing some stuff!', 'I am good!',                                     
#                               'Nice!', 'I am amazing and full of power']
#             talk(random.choice(setReplies))
            
#         elif "email" in Input:
#             talk("Who is the recipient ?")
#             recipient = GivenCommand()
#             if 'me' in recipient:
#                 try:
#                     talk('What should I say? ')
#                     content = GivenCommand()
#                     server = smtplib.SMTP('smtp.gmail.com', 587)
#                     server.ehlo()
#                     server.starttls()
#                     server.login("Your_Username", 'Your_Password')
#                     server.sendmail('Your_Username', "Recipient_Username", content)
#                     server.close()
#                     talk('Email sent!')
#                 except:
#                     talk('Sorry ! I am unable to send your message at this moment!')
            
#         elif "play music" in Input:
#             music_folder = "D:\\Music\\"
#             music = ['BrothersAnthem', 'BehChala-URI', 'JaggaJiteya-URI', 'Jigra-URI', 'SapnaJahan']
#             random_music = music_folder + random.choice(music) + '.mp3'
#             print("Playing >> ", random_music)
#             os.system(random_music)
#             talk('Okay, here is your music! Enjoy!')

