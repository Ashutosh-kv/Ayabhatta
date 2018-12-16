
#dependencies - pre-installed =  webbrowser, smtplib, datetime, random, os, sys
import pyttsx3, webbrowser, smtplib, datetime, random, wikipedia, wolframalpha, os, sys
import speech_recognition as sr
from playsound import playsound
from gtts import gTTS


#Wolfram alpha client setup
client = wolframalpha.Client(Your_Wolfram_App_ID)

#Text-to-Speech setup - pyttsx3 module
engine = pyttsx3.init('sapi5')
engine.setProperty('rate', 140)

def speak(audio, file):
    try:
        tts = gTTS(text=audio, lang='en-us')
        tts.save(file + '.mp3')
        playsound(file + '.mp3')
    except:
        print('Computer: ' + audio)
        engine.say(audio)
        engine.runAndWait()

#greeting function       
def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Good Morning!', 'greetMe')

    if currentH >= 12 and currentH < 18:
        speak('Good Afternoon!', 'greetMe')

    if currentH >= 18 and currentH != 0:
        speak('Good Evening!', 'greetMe')

#speech recognition function
def myCommand():
   
    r = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:                                                                       
        print("Speak...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration = 1)
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio)
        print('User: ' + command + '\n')
        return command
        
    except sr.UnknownValueError:
        speak('Try writing...', 'tw')
        command = input("Try writing...")
    
if __name__ == '__main__':
    
    greetMe()
    while True:
        speak('What can I do for you?', 'Intro')
        query = myCommand()
        
        #Pre-defined commands
        if 'YouTube' in query:
            speak('okay', 'okay')
            webbrowser.open('www.youtube.com')

        elif'Google' in query:
            speak('okay', 'okay')
            webbrowser.open('www.google.co.in')

        elif 'Gmail' in query:
            speak('okay', 'okay')
            webbrowser.open('www.gmail.com')

        elif 'Khan Academy' in query:
            speak('okay', 'okay')
            webbrowser.open('www.khanacademy.org')

        elif "what\'s up" in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!']
            speak(random.choice(stMsgs), 'status')

        elif 'email' in query:
            speak('Who is the recipient? ', 'email')
            recipient = myCommand()

            if 'me' in recipient or 'I' in recipient:
                    speak('What should I say? ', 'email2')
                    content = myCommand()

                    #Emal details
                    fromAddr = Your_name
                    toAddr = The_Recipient_email_address
                    username = Your_Username
                    password = Your_Password
                    
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.ehlo()
                    server.starttls()
                    server.login(username, password)
                    server.sendmail(fromAddr, toAddr, content)
                    server.close()
                    
                    speak('Email sent!', 'notify')

        elif 'nothing' in query or 'abort' in query or 'stop' in query:
            speak('okay', 'okay')
            speak('Bye Sir, have a good day.', 'bye')
            sys.exit()
    
        elif 'hello' in query:
            speak('Hello Sir', 'hello')

        elif 'bye' in query:
            speak('Bye Sir, have a good day.', 'bye')
            sys.exit()

        elif 'now' in query and 'time' in query:
            currentdatetime = str(datetime.datetime.now())
            speak(currentdatetime, 'cdt')

        #Search for a something or solve a problem
        else:
            try:
                try:
                    #Wolframalpha search
                    res = client.query(query1)
                    results = next(res.results).text
                    speak(results, 'res')
                except:
                    #Wikipedia search
                    results = wikipedia.summary(query, sentences = 3)
                    speak('Got it.', 'mm')
                    speak(results, 'resultwiki')
            except:
                speak("I don't know!")
