import pyttsx3
import SpeechRecognition as sr 
import wikipedia
import datetime
import webbrowser
import os
import smtplib

print("Intialising Honey")
MASTER = "NIDHI"

engine=pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
engine.setProperty('voice',voices[0],id)

# Speak function will pronounce the text passed through it
def speak(text):
    engine.say(text)
    engine.runAndWait()
    speak("Intialising Honey...")

# This function will wish you as per the given time
def wishMe():

    hour= int(datetime.datetime.now().hour)
    print(hour)
    if hour>=0 and hour <12:
        speak("Good Morning" + MASTER) 
    elif hour>=12 and hour<18:
        speak("Good Afternoon"+ MASTER)
    else:
        speak("Good Evening"+ MASTER)

    speak("I am honey.How may I help you?")

#Main program starts here
#This functiom will take command from microphone
def takeCommand():

    r = sr.Recogniser()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        print("Recognising...")
        query = r.recognise_google(audio.Language = 'en-in')
        print(f"user said:{query}\n")

    except Exception as e:
        print("Say that again please")
        query = NONE

    return query

def sendEmail( to,content):
    server = smtplib.SMIP("smtp.gmail.com",587)
    server.ehlo()
    server.startls()
    server.login("youremail@gmail.com",'password')
    server.sendmail("sender@gmail.com",to,content)
    server.close()

def main():

    speak("Intialising honey...")
    query= takeCommand()
    wishMe()

    #Logic for executing the task as per query

    if 'wikipedia' in query.lower():
        speak('Searching wikipedia...')
        query= query.replace("wikipedia","")
        results = wikipedia.summary(query,sentences = 2)
        print(results)
        speak(results)

    elif 'open youtube' in query.lower():
        webbrowser.open("youtube.com")

    elif 'open google' in query.lower():
        webbrowser.open("google.com")

    elif 'open stackoverflow' in query.lower():
        webbrowser.open("stackoverflow.com")



    elif 'the time' in query.lower():
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"{MASTER} the time is {strTime}")

    elif 'email to krupa' in query.lower():
        try:
            speak("What should I send ?")
            content = takeCommand()
            to="sender@gmail.com"
            sendEmail(to,content)
            speak("Email has been sent successfully")

        except Exception as e:
            print(e)


main()

