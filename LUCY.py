import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
engine = pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)

def speak (audio): 
    engine.say(audio)
    engine.runAndWait()
    #wishes user acc to time

def WishMe():
    hour = int (datetime.datetime.now().hour)
    if hour >= 0 and hour<12:
        speak("good morning ")
    elif hour >=12 and hour< 18:
        speak("good afternoon")
    else:
        speak("good evening")

def takecommand():
    #take microphone input from input and string 
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.8
        print("listening...")
        audio = r.listen(source)
        try:
            print("recognizing....")
            query =r.recognize_google(audio,language='en-in')
            print(f"user said:  {query}\n")
        except Exception as e:
            print("say that again please...")
            return"None"
        return query

if __name__=="__main__": 
    WishMe()
    speak("   I AM LUCY . HOW MAY I HELP YOU ")
    while True :
        query = takecommand().lower()
#logic for wikipedia

        if 'wikipedia' in query:  #if wikipedia found in the query then this block will be executed
            query = query.replace("wikipedia", " ")
            speak(f'Searching Wikipedia for {query}...')
            results = wikipedia.summary(query, sentences=5)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'youtube' in query :
            webbrowser.open("youtube.com")
        elif 'google' in query :
            webbrowser.open("google.com")
        elif 'spotify' in query :
            webbrowser.open("spotify.com")
        elif 'gana' in query :
            webbrowser.open("gaana.com")
        elif 'whatsapp' in query :
            webbrowser.open("whatsapp.com")
        elif 'instagram' in query :
            webbrowser.open("instagram.com")
        elif 'facebook' in query :
            webbrowser.open("facebook.com")
        elif 'prime video' in query :
            webbrowser.open("primevideo.com")
        elif 'byjus' in query :
            webbrowser.open("byjus.com")   
        elif 'unacademy' in query :
            webbrowser.open("unacademy.com")
        elif 'book train' in query :
            webbrowser.open("irctc.co.in")
        elif 'book plane' in query :
            webbrowser.open("air.irctc.co.in")
        elif 'how are you' in query :
            speak("i am fine , what about you")
        elif 'fine' in query :
            speak("happy to hear that")
        elif'kaisi hai' in query:
            speak("bus theeek")
        elif'aur suna' in query:
            speak("tu bata")
        elif'how to find out if i have cold' in query:
            print("you might have Runny or stuffy nose or Sore    or scratchy throat     or Cough Sneezing     or Generally feeling unwell   or Slight body aches     or a mild headache    or lowgrade fever. ")
            speak('you might have Runny or stuffy nose or Sore    or scratchy throat     or Cough Sneezing     or Generally feeling unwell   or Slight body aches     or a mild headache    or lowgrade fever. ')
        elif 'close' in query :
            exit()
