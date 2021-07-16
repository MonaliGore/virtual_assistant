import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognitionj
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import random
import sys
import time
import os
import os.path
import requests
import cv2 #pip install opencv-smtplib
from requests import get #pip install requests
import pywhatkit as kit #pip install opencv-python
import pyjokes #pip install pyjokes
import pyautogui #pip install pyautogui
import PyPDF2
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import instaloader #pip install instaloader
import operator #for calculation using voice
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from jarvisUi import Ui_jarvisUi

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices');
print(voices[0].id)
engine.setProperty('voices', voices[len(voices) - 1].id)

#text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

#to wish
def wish():
    hour = int(datetime.datetime.now().hour)
    tt = time.strftime("%I:%M %p")

    if hour >=0 and hour <= 12:
        speak(f"Good Morning, its {tt}")
    elif hour >= 12 and hour <= 18:
        speak(f"Good Afternoon, its {tt}")
    else:
        speak(f"Good Evening, its {tt}")
    speak("I am jarvis, please tell me how may i help you")

#to send email
def sendmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.startls()
    server.login('ggmonali@gmail.com', '9665770439')
    server.sendmail('ggmonali@gmail.com', to, content)
    server.close()

#def news updates
def news():
    main_url = 'https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=8797e3049fd34af28d5f613e05d94b70'
    main_page = requests.get(main_url).json()
    #print(main_page)
    articles = main_page["articles"]
    #print(articles)
    head = []
    day=["first","second","third","fourth","fifth","sixth","seventh","eight","ninth","tenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range (len(day)):
        #print(f"today's {day[i]} news is: ", head[i])
        speak(f"today's {day[i]} news is: {head[i]}")

#to read PDF
def pdf_reader():
    book = open('py3.pdf','rb')
    pdfReader = PyPDF2.PdffileReader(book) #pip install PyPDF2
    pages = pdfReader.numPages
    speak(f"Total number of pages in this book {pages} ")
    speak("please enter the page number i have to read")
    pg = int(input("please enter the page number: "))
    page = pdf_reader.getPage(pg)
    text = page.extractText()
    speak(text)
    #jarvis speaking speed should be controlled by user



class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()

    def run(self):
        self.TaskExecution()



    def takecommand(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("listening...")
            r.pause_threshold = 1
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
            #audio = r.listen(source,timeout=5,phrase_time_limit=8)

        try:
            print("Recognizing...")
            self.query = r.recognize_google(audio, language='en-in')
            print(f"user said: {self.query}\n")

        except Exception as e:
            #speak("say that again please...")
            return "none"
        self.query = self.query.lower()
        return self.query

    def TaskExecution(self):
        wish()
        while True:
            self.query = self.takecommand()

            #logic building for tasks 

            if "oepn notepad" in self.query:
                npath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Notepad"
                os.startfile(npath)

            elif "open adobe reader" in self.query:
                apath = "C:\\Program Files(x86)\\Adobe\\Reader 11.0\\Reader\\AcroRd32.exe"
                os.startfile(apath)

            elif "open command prompt" in self.query:
                os.system("start cmd")

            elif "open camera" in self.query:
                cap = cv2.VideoCapture(0)
                while True:
                    ret, img = cap.read()
                    cv2.inshow('webcam', img)
                    k = cv2.waitKey(50)
                    if k==27:
                        break;
                cap.release()
                cv2.destroyAllWindows()

            elif "play music" in self.query:
                music_dir = "C:\\music"
                songs = os.listdir(music_dir)
                rd = random.choice(songs)
                for song in songs:
                    if song.endwith('.MP3'):
                        os.startfile(os.path.join(music_dir, song))

            elif "ip address" in self.query:
                ip = get('https://api.ipify.org').text
                speak(f"your IP address is {ip}")

            elif "wikipedia" in self.query:
                speak("searching wikipedia...")
                self.query = self.query.replace("wikipedia","")
                results = wikipedia.summary(self.query, sentences=2)
                speak(results)
                print(results)

            elif "open youtube" in self.query:
                webbrowser.open("www.youtube.com")

            elif "open facebook" in self.query:
                webbrowser.open("www.facebook.com")

            elif "open stackoverflow" in self.query:
                webbrowser.open("www.stackoverflow.com")

            elif "open google" in self.query:
                speak("what should i search on google")
                cm = self.takecommand()
                webbrowser.open(f"{cm}")

            elif "play song on youtube" in self.query:
                kit.playonyt("see you again")

            elif "open github" in self.query:
                gpath = "C:\\Users\\Shailesh Gore\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\GitHub, Inc\GitHub Desktop.lnk"
                os.startfile(gpath)

            #elif "send message" in query:
                #   kit.sendwhatmsg("+6784356898", "this is testing protocol",2,24)
                #  time.sleep(120)
                # speak("message has been sent")
        ##
        #        elif "play song on youtube" in query:
        #          kit.playonyt("see you again")
        #
        #       elif "email to monali" in query:
        #          try:
        #             speak("what should i say?")
        #            content = takecommand().lower()
            #           to = "email of other person"
            #          sendmail(to,content)
            #         speak("Email has been sent to monali!")
        #
            #      except("sorry, i am unable to sent this mail")

            elif "offline" in self.query or "sleep now" in self.query or "good bye" in self.query:
                speak("Thanks for using me, have a good day.")
                sys.exit()

            
            #to close my application
            elif "close notepad" in self.query:
                speak("okay, closing notepad")
                os.system("taskkill /f /im Notepad")

            #to set an alarm
            elif "set alarm" in self.query:
                nn = int(datetime.datetime.now().hour)
                if nn==22:
                    music_dir = 'C:\\music'
                    songs = os.listdir(music_dir)
                    os.startfile(os.path.join(music_dir, songs[0]))

            #to find a joke
            elif "tell me a joke" in self.query:
                joke = pyjokes.get_joke()
                speak(joke)

            elif "shut down the system" in self.query:
                os.system("shutdown /r /t 5")

            elif "hello" in self.query or "hey" in self.query:
                speak("hello, may i help you with something?")

            elif "how are you" in self.query:
                speak("i am fine, what about you?")

            elif "thank you" in self.query or "thanks" in self.query:
                speak("it's my pleasure.")
            
            ##########################################################################
            ##########################################################################

            elif 'swith the window' in self.query:
                pyautogui.keyDown("alt")
                pyautogui.press("tab")
                time.sleep(1)
                pyautogui,keyUp("alt")

            elif "tell me news" in self.query:
                speak("please wait, fetching the latest news")
                news()

            elif "email to monali" in self.query:
                try:
                    speak("what should i say?")
                    content = self.takecommand().lower()
                    to = "goremonali400@gmail.com"
                    sendEmail(to,content)
                    speak("Email has been sent to monali!")

                except Exception as e:
                    print(e)
                    speak("sorry, i am unable to sent this email")

                    ##############################################
                    #############################################

            elif "do some calculations" in self.query or "can you calculate" in self.query:
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    speak("say what you want to calculate, example: 3 plus 3")
                    print("listening...")
                    r.adjust_for_ambient_noise(source)
                    audio = r.listen(source)
                my_string=r.recognize_google(audio)
                print(my_string)
                def get_operator_fn(op):
                    return {
                        '+' : operator.add,
                        '-' : operator.sub,
                        '*' : operator.mul,
                        'divided' : operator.__truediv__,
                        'Mod' : operator.mod,
                        'mod' : operator.mod,
                        '^' : operator.xor,
                    }[op]
                def eval_binary_expr(op1, oper, op2):
                    op1,op2 = int(op1), int(op2)
                    return get_operator_fn(oper)(op1, op2)
                print(eval_binary_expr(*(my_string.split())))

            #to find my location using IP address

            elif "where i am" in self.query or "where we are" in self.query:
                speak("wait, let me check")
                try:
                    ipAdd = requests.get('https://api.ipify.org').text
                    print(ipAdd)
                    url = 'https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
                    geo_requests = requests.get(url)
                    geo_data = geo_requests.json()
                    #print(geo_data)
                    city = geo_data['city']
                    #state = geo_data['state]
                    country = geo_data['country']
                    speak("i am not sure but i think we are in {city} city of {country} country")
                except Exception as e:
                    speak("sorry, due to network issue i am unable to find where we are")
                    pass

            #to check instagram profile
            
            #elif "instagram profile" in query or "profile on instagram" in query:
             #   speak("please enter the user name correctly")
              #  name = input("Enter username here:")
               # webbrowser.open(f"www.instagram.com/{name}")
                #speak("here is the profile of the user {name}") 
                #time.sleep(5)
               # speak(f"would you like to download profile picture of this account.")
                #condition = takecommand()
                #if "yes" in condition:
                 #   mod = instaloader.instaloader() #pip install instaloader
                  #  mod.download_profile(name, profile_pic_only=True)
                   # speak("i am done, profile picture is saved in our mail folder. now i am ready for next task")
                #else:
                 #   pass

            #to take screenshot
            
            elif "take screenshot" in self.query or "take a screenshot" in self.query:
                speak("please tell me the name for this screenshot file")
                name = self.takecommand()
                speak("please hold the screen for few seconds, i am taking screenshot")
                time.sleep(3) 
                img = pyautogui.screenshot()
                img.save(f"{name}.png")
                speak("i am done, the screenshot is saved in our main folder")       

            #to read PDF file
            elif "read pdf" in self.query:
                pdf_reader()

            #to hide files and folder
            elif "hide all files" in self.query or "hide this folder" in self.query or "visible for everyone" in self.query:
                speak("please tell me, you want to hide this folder or make it visible for everyone")
                condition = self.takecommand()
                if "hide" in condition:
                    os.system("attrib +h /s /d") #os module
                    speak("all files in this folder are now hidden")

                elif "visible" in condition:
                    os.system("attrib -h /s /d")
                    speak("all files in this folder are now visible to everyone.")

                elif "leave it" in condition or "leave it for now" in condition:
                    speak("ok")

startExecution = MainThread()

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_jarvisUi()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

    def startTask(self):
        self.ui.movie = QtGui.QMovie("../../Users/Shailesh Gore/Downloads/sFaoXq3.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("../../Users/Shailesh Gore/Downloads/T8bahf.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()

    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString('hh:mm:ss')
        label_date = current_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)

app = QApplication(sys.argv)
jarvis = Main()
jarvis.show()
exit(app.exec_())
