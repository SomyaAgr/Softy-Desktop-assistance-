from Weather import *
import pyttsx3 as p
import speech_recognition as sr  # using for voice
import  webbrowser
import randfacts
import pyjokes
import time
from datetime import datetime
import pyautogui
import cv2
import numpy as np
import pywhatkit
import os
import smtplib
from email.message import EmailMessage

engine = p.init()
engine.getProperty("rate")
engine.setProperty("rate", 167)
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)

def send_email(receiver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    # Make sure to give app access in your Google account
    Myemail_id = os.environ['email_id']
    my_Pass=os.environ['my_pass']
    server.login(Myemail_id, my_Pass)
    email = EmailMessage()
    email['From'] = Myemail_id
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)

def speak(text):
    engine.say(text)
    engine.runAndWait()


def wishMe():
    hours = int(datetime.now().hour)
    if 0 < hours <= 12:
        return "Good Morning"
    elif 12 <= hours < 17:
        return "Good Afternoon "
    else:
        return "Good Evening"


def softyMain():
    try:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("test")
            r.energy_threshold = 10000
            r.adjust_for_ambient_noise(source, 1.2)
            print("listening")
            audio = r.listen(source)
            text = r.recognize_google(audio)

        if"What" and "about" and "you" in text:
            print(text)
            speak("I am doing pretty well, thanks for asking")
        elif"perfectly imperfectly"or "not feeling well" in text:
            speak("ohh what happened? have you concerned with doctor? get well soon")
        
        while True:

            speak("what can i do for you?")

            with sr.Microphone() as source:
                r.energy_threshold = 10000
                r.adjust_for_ambient_noise(source, 1.2)
                print("listening...")
                audio = r.listen(source)
                text2 = r.recognize_google(audio)

                print(f"{text2 = }")
                if "information" in text2:
                    print(text2)
                    speak("what do you want me to search for?")  # calling say method
                    with sr.Microphone() as source:
                        r.energy_threshold = 10000
                        r.adjust_for_ambient_noise(source, 1.2)
                        print("listening")
                        audio = r.listen(source)
                        info = r.recognize_google(audio)
                    speak(f"searching in wikipedia for {info}")
                    print(f"searching in wikipedia for {info}")

                    def wiki(query):
                        webbrowser.open_new_tab("https://en.wikipedia.org/wiki/"+query)
                    wiki(info)
                    time.sleep(10)


                elif "play" in text2 and "video" in text2:
                        print(text2)
                        speak("What video would you like me to play?")
                        with sr.Microphone() as source:
                            r.energy_threshold = 10000
                            r.adjust_for_ambient_noise(source, 1.2)
                            print("listening...")
                            audio = r.listen(source)
                            vid = r.recognize_google(audio)
                        speak(f"searching in youtube for {vid}")
                        print(f"searching in youtube for {vid}")
                        pywhatkit.playonyt(vid)
                        time.sleep(15)

                elif "tell" and "news" in text2:
                    print(text2)
                    speak("Sure ma'am, just a moment")
                    speak("here's your news top headlines")
                    data = requests.get("https://newsapi.org/v2/top-headlines?country=in&apiKey=6788007d69374a64be70fb6d97c75654")
                    result = data.json()
                    print(result['status'])
                    news = result['articles']
                    speak("Here are some top news")
                    i = 1
                    while i <= 5:
                        print(i)
                        print(news[i]['title'])
                        speak(news[i]['title'])
                        i += 1
                        time.sleep(1)
                    speak("Thanks for listening ! Have a nice day  ma'am")

                elif "fact" in text2 or 'facts' in text2:
                    print(text2)
                    speak("sure ma'am")
                    x = randfacts.get_fact()
                    print(x)
                    speak("Did you know that, " + x)

                elif "joke" in text2:
                    print(text2)
                    speak("sure ma'am, get ready for some chuckles")
                    speak(pyjokes.get_joke())
                    speak('ha ha ha ha ha ')
                    time.sleep(1)

                elif "weather report" in text2:
                    print(text2)
                    speak("Sure ma'am.")
                    speak("Kindly Enter you city name")
                    location = (input("Enter city name: "))
                    speak("Entered location is")
                    speak(location)
                    user_api = os.environ['weatherReportApi']

                    complete_api = "https://api.openweathermap.org/data/2.5/weather?q=" + location + "&appid=" + user_api

                    api_link = requests.get(complete_api)
                    api_data = api_link.json()

                    if api_data['cod'] == '404':
                        print(f"Invalid city: {location}, please check your city name")
                    else:
                        temp_city = ((api_data['main']['temp']) - 273)
                        weather_desc = api_data['weather'][0]['description']
                        humidity = api_data['main']['humidity']
                        wind_speed = api_data['wind']['speed']
                        date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

                        print("-------------------------------------------------------------")
                        print(f"Weather Stats for - {location.upper()}  || {date_time}")
                        speak(f"Weather Stats for {location} on {date_time}")
                        print("-------------------------------------------------------------")

                        print("Current temperature is: {:.2f} degree Celsius".format(temp_city))
                        speak("Current temperature is {:.2f} degree Celsius".format(temp_city))
                        print(f"Current weather desc {weather_desc}")
                        speak(f"Current weather is {weather_desc}")
                        print(f"Current Humidity      : {humidity}%")
                        speak(f"Current Humidity is {humidity} percentage")
                        print(f"Current wind speed    : {wind_speed} kmph")
                        speak(f"Current wind speed is {wind_speed} kilo meters per hour")

                elif "Screen Recorder" in text2:
                    print(text2)
                    speak("sure ma'am")
                    speak("Opening screen Recorder")
                    speak("to stop screen recoder press key q from keyboard")
                    print("to stop screen recoder press key q from keyboard")  # Specify resolution
                    resolution = (1920, 1080)  # Specify video codec
                    codec = cv2.VideoWriter_fourcc(*"XVID")
                    # Specify name of Output file
                    time_stamp = datetime.now().strftime(' %H-%M-%S')
                    file_name = f'{time_stamp}.avi'
                    # Specify frames rate. We can choose any
                    # value and experiment with it
                    fps = 60.0
                    # Creating a VideoWriter object
                    out = cv2.VideoWriter(file_name, codec, fps, resolution)
                    # Create an Empty window
                    cv2.namedWindow("Live", cv2.WINDOW_NORMAL)
                    # Resize this window
                    cv2.resizeWindow("Live", 480, 270)

                    while True:
                        img = pyautogui.screenshot()  # Convert the screenshot to a numpy array
                        frame = np.array(img)  # Convert it from BGR(Blue, Green, Red) to  RGB(Red, Green, Blue)
                        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Write it to the output file
                        out.write(frame)  # Optional: Display the recording screen
                        cv2.imshow('Live', frame)  # Stop recording when we press 'q'
                        if cv2.waitKey(1) == ord('q'):
                            break
                    out.release()
                    cv2.destroyAllWindows()

                elif "selfie" in text2:
                    print(text2)
                    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
                    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
                    smile_cascade = cv2.CascadeClassifier('smile.xml')
                    while True:
                        _, frame = cap.read()
                        original_frame = frame.copy()
                        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                        face = face_cascade.detectMultiScale(gray, 1.3, 5)
                        for x, y, w, h in face:
                            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2)
                            face_roi = frame[y:y + h, x:x + w]
                            gray_roi = gray[y:y + h, x:x + w]
                            smile = smile_cascade.detectMultiScale(gray_roi, 1.3, 25)
                            for x1, y1, w1, h1 in smile:
                                cv2.rectangle(face_roi, (x1, y1), (x1 + w1, y1 + h1), (0, 0, 255), 2)
                                time_stamp = datetime.now().strftime('%H-%M-%S')
                                file_name = f'selfie-{time_stamp}.png'
                                cv2.imwrite(file_name, original_frame)
                        cv2.imshow('cam star', frame)
                        if cv2.waitKey(10) == ord('q'):
                            break

                    cv2.destroyAllWindows()
                    speak("press exit key to exit from web cam")
                    time.sleep(1)

                elif "go offline" or "bye " or "leave me alone " in text2 :
                    speak("Are you asking me to go")
                    print("Are you asking me to go")
                    speak("thanks for talking to me")
                    print("Thanks for talking to me")
                    exit()

                elif "play me a song" in text2 :
                    music_dir = "D:\\songs\\PROG"
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir, songs[0]))
                    time.sleep(5)
    except Exception as e:
        if e==KeyboardInterrupt:
            speak("opp's pressed any key")
        if e==ConnectionError :
            speak("check your PC is connected")
        else:
            speak('unable to get any query ')
            print('unable to get any query ')
            speak('i think nobody is here')
            print('i think nobody is here')
            speak("bye  have a nice day")
            speak("bye  have a nice day")
            exit()


