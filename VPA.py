import os
import datetime
import smtplib
import webbrowser
import random
import pyttsx3
import sys
import json
import requests
import time
import pyautogui
import wikipedia
from win10toast import ToastNotifier
import speech_recognition as sr
from urllib.request import urlopen
from bs4 import BeautifulSoup as soup


# Importing my python files
import bot
from flikr_download import flikrDownload

engine = pyttsx3.init()
voices = engine.getProperty('voices')

ans = 'no'

def talk(audio):
    if "yes" in ans or "yeah" in ans:
        print("Veronica: "+ audio, end="\n\n")
    else:
        print("JARVIS: " + audio, end="\n\n")
    engine.say(audio)
    engine.runAndWait()
    

def greetMe():
    CurrentHour = int(datetime.datetime.now().hour)
    if CurrentHour >= 0 and CurrentHour < 12:
        talk('Good Morning Sir')
    elif CurrentHour >=12 and CurrentHour < 18:
        talk("Good Afternoon Sir")
    else:
        talk("Good Evening Sir")
        

def GiveCommand():
    try:
        k = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            k.pause_threshold = 1
            audio = k.listen(source)
        try:
            Input = k.recognize_google(audio, language='en-in')
            print("Yuvraj Singh: " + Input + "\n")
            
        except sr.UnknownValueError:
            talk("Sorry! I didn\'t get that! Try typing it here!")
            Input = str(input("Command: "))
    
        return Input
    except:
        talk("This thing requires Internet connection..")
        talk("Please connect to Internet.")
        sys.exit()


def get_Quote():
    params = {
        'method':'getQuote',
        'lang':'en',
        'format':'json'
    }
    response = requests.get('http://api.forismatic.com/api/1.0/',params)
    jsonText =json.loads(response.text)
    return jsonText["quoteText"], jsonText["quoteAuthor"]


def wait():
    talk("Ok sir waiting for 16 seconds..")
    time.sleep(16)
    talk("I am ready to talk now.")


def PreDino():
    webbrowser.open("www.google.com")
    time.sleep(5)
    pyautogui.click(645, 53)
    pyautogui.typewrite("chrome://dino")
    pyautogui.keyDown('enter')
    pyautogui.keyUp('enter')


if __name__ == "__main__":
    talk("Welcome this is Your Personal Assistant.")
    #talk("Whom do you wanna talk Veronica or JARVIS ?")
    talk("You have two JARVIS and Veronica, Default is JARVIS do you wanna change it ?")
    ans = GiveCommand().lower()
    if "yes" in ans or 'yeah' in ans:
        PA = "Veronica"
        engine.setProperty('voice', voices[1].id)
    else:
        PA = "JARVIS"

    tn = ToastNotifier()
    tn.show_toast(PA + " has Started", "Best Personal Assistant", duration=5 , icon_path="jarvis.ico")
    
    greetMe()
    talk("Hello sir "+ PA + " at your service")
    talk("What can i do for you ?")

    while True:
        Input = GiveCommand()
        Input = Input.lower()
        
        if "wait" in Input:
            wait()

        if "get lost" in Input:
            talk("Can you say it in a proper manner because this thing hurts me.")
            talk("You can say exit or bye")
            talk("And here is my reply, You get lost...")
            continue
        
        elif Input in ["do you have some time", "can you talk to me", "can i talk to you", "can we have a talk"]:
            talk("Yeah, i am always there for you, tell me whats going on ?")
            inn = GiveCommand()
            quote, author = get_Quote()
            talk(quote + " by " + author)
            talk("Well i am just a simple computer program and don't understand humans, tell me how can i help you ?")
            talk("You can say open youtube, play music for your enjoyment.")


        elif Input in ["exit", "quit", "bye", "nothing"]:
            talk("Okkk bye, have a great time.")
            sys.exit()
        
        elif "what you can do" in Input or "can i get a manual" in Input:
            talk("Well a lot of things.. ")
            talk("Here is the manual")
            print("1. ")

        elif "open google" in Input:
            talk("Opening Google...")
            webbrowser.open("www.google.com")
            
        elif "open youtube" in Input:
            talk("Sure.")
            talk("What you wanna search for ?")
            ysearch = GiveCommand()
            webbrowser.open("https://www.youtube.com/results?search_query=" + "+".join(ysearch.split()))
            talk("Done sir")
            
        elif "what\'s up" in Input or "how are you" in Input:
            setReplies = ['Just doing some stuff!', 'I am good!',                                     
                              'Nice!', 'I am amazing and full of power']
            talk(random.choice(setReplies))
            talk("By the way thanks for asking, it mean a lot to me.")
            

        elif "email" in Input:
            talk("Who is the recipient ?")
            recipient = GiveCommand()
            if 'me' in recipient:
                try:
                    talk('What should I say? ')
                    content = GiveCommand()
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.ehlo()
                    server.starttls()
                    server.login("Your_Username", 'Your_Password')
                    server.sendmail('Your_Username', "Recipient_Username", content)
                    server.close()
                    talk('Email sent!')
                except:
                    talk('Sorry ! I am unable to send your message at this moment!')
            
        elif "play music" in Input:
            music_folder = "D:\\Music\\"
            music = []
            for file in os.listdir(music_folder):
                if file.endswith(".mp3"):
                    music.append(file)
            
            talk("Which one sir")
            playmusic = GiveCommand()
            if ("random" in playmusic) or ("your choice" in playmusic) or ("any" in playmusic):
                random_music = music_folder + '"' + random.choice(music) + '"'
                print("Playing >> ", random_music)
                os.system(random_music)
            else:
                music_choice = music_folder + '"' + playmusic + '"' + ".mp3"
                if playmusic + ".mp3" in music:
                    print("Playing -- ", music_choice)
                    os.system(music_choice)
                if playmusic or music_choice:
                    talk('Okay, here is your music! Enjoy!')
                else:
                    talk("Music not found try another one")
                    talk("Taking you back to command Listening")
                    continue        
            
        elif "play dino game" in Input:
            talk("Launching the game")
            bot.main()

        elif ("download images" in Input) or ("download some images" in Input):
            talk("Ok please enter the required inputs")
            topic = input("What you wanna search for ? ")
            num = int(input("How many ? "))
            fullpath = input("Enter the full path for storing the images :-")

            talk("Download in progress")
            talk(flikrDownload(fullpath, topic, num))
            os.startfile(fullpath)
            talk("You can check the folder.")
            talk("What's next >>")


        elif "getting bored" in Input or "boring today" in Input:
            talk("You might wanna see something special.")
            talk("Check this thing out")
            topics = ["Shiba Inu", "Desert Eagle", "Top SUV's of the year", "Best places to visit around the world", "Adventurous places to visit", "Best luxuries of the world", "Top webseries to watch"]
            searchFor = random.choice(topics)
            webbrowser.open('https://www.google.co.in/search?q=' + "+".join(searchFor.split()))
            talk("If you did not find this helpful try watching youtube.")
            
        elif 'news for today' in Input:
            try:
                news_url="https://news.google.com/news/rss"
                Client=urlopen(news_url)
                xml_page=Client.read()
                Client.close()
                soup_page=soup(xml_page,"xml")
                news_list=soup_page.findAll("item")
                talk("Okk sir tell me how may top news you wanna know ?")
                n = int(input("Enter the number -> "))
                talk("Here is what you need to know.")
                for news in news_list[:n]:
                    newsList = news.title.text.split("-")
                    talk("According to " + newsList[1])
                    talk(newsList[0])
                    print("\n")

                talk("That's about updates...")
            except Exception as e:
                    print(e)
        
        else:
            if not Input:
                talk("Try inputting something")
                continue
                
            talk('Searching...')
            try:
                outputs = wikipedia.summary(Input, sentences=3)
                talk('Gotcha')
                talk('Wikipedia says')
                talk(outputs)
            except:
                talk("searching on google for " + Input)
                say = Input.replace(' ', '+')
                webbrowser.open('https://www.google.co.in/search?q=' + Input)
            talk('Next Command! Please!')