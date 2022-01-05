import requests
from win32com.client import Dispatch
from tkinter import *
window=Tk()
window.geometry("1200x700")
window.configure(bg="black")
window.title("Daily short News")
lable=Label(window,text="Welcome to our News World",bg="red",fg="white",font=(None,20,'bold'))
lable.pack(pady=30)
frame1=Frame(window,bg="black",pady="50")
frame1.pack(side=LEFT,fill="y",padx="20")
T=Text(window,width="900",height="500")
T.pack(side=TOP,pady="40",padx="40")

# frame2 = Frame(window,bg="white",width="900",height="500")
# frame2.pack(side=TOP,pady="40")
stop=False
def speak(str):
    T.insert(END, f"{str}\n")
    window.update()
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)


def technology_news():
    try:
        response = requests.get('https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=318229509c7b45cdbeaafe8d6d405185')
        r = response.json()
        articles = r['articles']
        count = 1
        speak("Todays technology news are")
        for item in articles:
            global stop
            if stop:
                break
            else:
                newsTitle = item['title']
                speak(f"news {count}")
                speak(newsTitle)
                count = count + 1
        stop = False

    except Exception as e:
        T.insert(END,"please check your Internet connection ! thank you \n")
        window.update()




def business_news():
    try:
        response = requests.get(
            'https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=318229509c7b45cdbeaafe8d6d405185')
        r = response.json()
        articles = r['articles']
        count = 1
        speak("Todays  business news are")
        for item in articles:
            global stop
            if stop:
                break
            else:
                newsTitle = item['title']
                speak(f"news {count}")
                speak(newsTitle)
                count = count + 1
        stop = False
    except Exception as e:
        T.insert(END,"please check your Internet connection ! thank you \n")
        window.update()


def entertainment_news():
    try:
       response = requests.get(
           'https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=318229509c7b45cdbeaafe8d6d405185')
       r = response.json()
       articles = r['articles']
       count = 1
       speak("Todays  entertainment news are")
       for item in articles:
           global stop
           if stop:
               break
           else:
               newsTitle = item['title']
               speak(f"news {count}")
               speak(newsTitle)
               count = count + 1
       stop = False
    except Exception as e:
        T.insert(END,"please check your Internet connection ! thank you \n")
        window.update()
def health_news():
    try:
        response = requests.get(
            'https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=318229509c7b45cdbeaafe8d6d405185')
        r = response.json()
        articles = r['articles']
        count = 1
        speak("Todays  health news are")
        for item in articles:
            global stop
            if stop:
                break
            else:
                newsTitle = item['title']
                speak(f"news {count}")
                speak(newsTitle)
                count = count + 1
        stop = False
    except Exception as e:
        T.insert(END,"please check your Internet connection ! thank you \n")
        window.update()
def  science_news():
    try:
        response = requests.get(
            'https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=318229509c7b45cdbeaafe8d6d405185')
        r = response.json()
        articles = r['articles']
        count = 1
        speak("Todays  science news are")
        for item in articles:
            global stop
            if stop:
                break
            else:
                newsTitle = item['title']
                speak(f"news {count}")
                speak(newsTitle)
                count = count + 1
        stop = False

    except Exception as e:
        T.insert(END,"please check your Internet connection ! thank you \n")
        window.update()
def sports_news():
    try:
        response = requests.get(
            'https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=318229509c7b45cdbeaafe8d6d405185')
        r = response.json()
        articles = r['articles']
        count = 1
        speak("Todays  sports news are")
        for item in articles:
            global stop
            if stop:
                break
            else:
                newsTitle = item['title']
                speak(f"news {count}")
                speak(newsTitle)
                count = count + 1
        stop=False
    except Exception as e:
        T.insert(END,"please check your Internet connection ! thank you \n")
        window.update()
def stop_news():
    global stop
    stop=True
    return stop

tech_butt=Button(frame1,text="Technology News",padx=10,pady=10,font=(None,10,'bold'),bg="skyblue",fg="white",relief=GROOVE,command=technology_news).pack(padx=20,pady=20,anchor="nw")
sport_butt=Button(frame1,text="Sports News",padx=27,pady=10,font=(None,10,'bold'),bg="skyblue",fg="white",relief=GROOVE,command=sports_news).pack(padx=20,anchor="nw")
Ente_butt=Button(frame1,text="Entertainment News",pady=10,font=(None,10,'bold'),bg="skyblue",fg="white",relief=GROOVE,command=entertainment_news).pack(padx=20,pady=20,anchor="nw")
busi_butt=Button(frame1,text="Business News",padx=18,pady=10,font=(None,10,'bold'),bg="skyblue",fg="white",relief=GROOVE,command=business_news).pack(padx=20,anchor="nw")
health_butt=Button(frame1,text="Health News",padx=25,pady=10,font=(None,10,'bold'),bg="skyblue",fg="white",relief=GROOVE,command=health_news).pack(padx=20,pady=20,anchor="nw")
science_butt=Button(frame1,text="Science News",padx=18,pady=10,font=(None,10,'bold'),bg="skyblue",fg="white",relief=GROOVE,command=science_news).pack(padx=20,anchor="nw")
stop_button=Button(frame1,text="Stop and Return",padx=18,pady=10,font=(None,10,'bold'),bg="red",fg="white",relief=GROOVE,command=stop_news)
stop_button.pack(padx=20,pady=20,anchor="nw")
window.mainloop()









