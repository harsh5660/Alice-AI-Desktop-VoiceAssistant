import datetime
import os
import smtplib
import time
import webbrowser
import kit
import pyautogui
import pyjokes
import pyttsx3
import requests
import speech_recognition as sr
import wikipedia
from pywhatkit import send_mail

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    t = time.strftime("%I:%M %p")
    day = Cal_day()
    print(t)
    if hour>=0 and hour<12 and 'AM' in t:
        speak(f"Good Morning , its {day} and the time is {t}")
    elif hour>=12 and hour<15 and 'PM' in t:
        speak(f"Good Afternoon , its {day} and the time is {t}")
    elif hour>=16 and hour<21:
        speak(f"Good Evening , its {day} and the time is {t}")

    speak("Hello Boss I am Alice your Assistant.Please tell me how can I help you")

def Cal_day():
        day = datetime.datetime.today().weekday() + 1
        Day_dict = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday',4: 'Thursday', 5: 'Friday', 6: 'Saturday',7: 'Sunday'}
        if day in Day_dict.keys():
            day_of_the_week = Day_dict[day]
            print(day_of_the_week)
        return day_of_the_week

def takeCommand():
    #it takes microphone input from the user and returns string output#
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"Harshit said : {query}\n")

    except Exception as e:
        #print(e)
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com','password')
    server.sendmail('youremail@gmail.com',to,content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching  Wikipedia....')
            query = query.replace(" wikipedia", "")
            results =  wikipedia.summary(query, sentences=4)
            speak("According to Wikipedia")
            print(results)
            speak(results) 

        elif 'open google' in query:
            speak("openeing google")
            webbrowser.open("www.google.com")

        elif 'open youtube' in query:
            speak("opening youtube")
            webbrowser.open("www.youtube.com")

        elif 'open stackoverflow' in query:
            speak("openeing stackoverflow")
            webbrowser.open("www.stackoverflow.com")

        elif 'open facebook' in query:
            speak("opening facebook")
            webbrowser.open("www.facebook.com")

        elif 'open instagram' in query:
            speak("opening instagram")
            webbrowser.open("www.instagram.com")
        
        elif 'open twitter' in query:
            speak("opening twitter")
            webbrowser.open("www.twitter.com")

        elif 'open spotify' in query:
            speak("opening spotify")
            webbrowser.open("www.spotify.com")

        elif 'open hotstar' in query:
            speak("opening hotstar")
            webbrowser.open("www.hotstar.com")

        elif 'open netflix' in query:
            speak("opening netflix")
            webbrowser.open("www.netflix.com")
        
        elif 'open amazonprime' in query:
            speak("opening amazonprimevideo")
            webbrowser.open("www.primevideo.com")
        
        elif 'open sonyliv' in query:
            speak("opening sonyliv")
            webbrowser.open("www.sonyliv.com")
        
        elif 'open flipcart' in query:
            speak("opening flipcart")
            webbrowser.open("www.flipcart.com")
        
        elif 'open amazon' in query:
            speak("opening amazon")
            webbrowser.open("www.amazon.com")
        
        elif 'open myntra' in query:
            speak("opening myntra")
            webbrowser.open("www.myntra.com")

        elif 'open github' in  query:
            speak("opening github")
            webbrowser.open("www.github.com")
        
        elif 'open geeksforgeeks' in query:
            speak("opening geeksforgeeks")
            webbrowser.open("www.geeksforgeeks.org")
        
        elif 'open makemytrip' in query:
            speak("opening makemytrip")
            webbrowser.open("www.makemytrip.com")
        
        elif 'open bookingcom' in query:
            speak("opening bookingcom")
            webbrowser.open("www.booking.com")
        
        elif 'open leetcode' in query:
            speak("opening leetcode")
            webbrowser.open("www.leetcode.com")
        
        elif 'open hackerrank' in query:
            speak("opening hackerrank")
            webbrowser.open("www.hackerrank.com")
        
        elif 'open temperature' in query:
            speak("opening accuweather")
            webbrowser.open("www.accuweather.com")
        
        elif 'open ookla' in query:
            speak("opening ookla")
            webbrowser.open("www.speedtest.net")
        
        elif 'tell me a joke' in query:
            joke = pyjokes.get_joke()
            speak(joke)
        
        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "singh.harshit5660@gamil.com"    
                send_mail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry, Couldn't able to send the mail.")
 
        elif 'take a screenshot' in query:
            speak("Sir,Please tell me the name for screenshot file")
            name = takeCommand().lower()
            speak("Please hold the screen for few secreen Iam taking screenshot")
            time.sleep(1)
            img = pyautogui.screenshot()
            img.save(f"{name}.jpg")
            speak("Iam done sir, the screenshot is saved in our main folder")
        
        elif 'where we are' in query:
            speak("Wait sir let me check")
            try:
                ipAdd = requests.get('http://api.ipfy.org').text
                print(ipAdd)
                url = 'http://get/geojs.io/v1/ip/geo/' + ipAdd + '.json'
                geo_request = requests.get(url)
                geo_data = geo_request.json()
                print(geo_data)
                city = geo_data['city']
                State = geo_data['state']
                country = geo_data['country']
                speak(f"Sir Iam not sure, but I thimk we are in {city} of {country} country")

            except Exception as e:
                speak("Sorry sir due to network issue Iam unable to find where we are")
                
        elif 'send whatsapp message' in query:
            kit.sendwhatsmsg("+919431330801", "this is testing protocal",4,13)
            time.sleep(1)
            speak("message has been send")

        elif 'open whatsapp' in query:
            path = "C://Users//User//AppData//Local//WhatsApp//WhatsApp.exe"
            os.startfile(path)
            
        elif 'finally sleep' in query:
            speak("Going to sleep,sir")
            exit()