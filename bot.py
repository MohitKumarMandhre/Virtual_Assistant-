import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import time

engine = pyttsx3.init('sapi5')

voice = engine.getProperty('voices') #getting details of current voice

engine.setProperty('voice', voice[0].id)
#print(voice[0].id)


def speak(audio):
    engine.say(audio) 
    engine.runAndWait() 


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Jarvis Sir. Please tell me how may I help you")  


def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query


def sendEmail(to, content):
    subject = "ASSISTANT JARVIS DEPLOYED ON YOUR SERVICE SIR"
    msg = f"Subject: {subject}\n\n{content}" 
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('your@gmail.com', 'your-passkey')
    server.sendmail('your@gmail.com', to, msg)
    server.close()
    print("HEY EMAIL HAS BEEN SENT SUCCESSFULLY !")


if __name__=="__main__" :
    speak("WELCOME , MOHIT KUMAR MANDHRE !")
    wishMe()
    while True :
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:  #if wikipedia found in the query then this block will be executed
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2) 
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'open github' in query:
            webbrowser.open("github.com")
        elif 'open linkedin' in query:
            webbrowser.open("linkedin.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'play music' in query:
            music_dir = 'song'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'the time' in query:
                    strTime = datetime.datetime.now().strftime("%H:%M:%S")    
                    speak(f"Sir, the time is {strTime}")
        elif 'open code' in query:
                    codePath = "C:/ProgramData/Microsoft/Windows/Start Menu/Programs/Google Chrome"
                    os.startfile(codePath)
        elif 'email to mohit' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "whomtosend@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend mohit bro, I am not able to send this email")    


