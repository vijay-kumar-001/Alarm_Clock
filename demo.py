# used for pre-testing whether audio is playing ,alarm 
# to know how to load audio file into tkinter 


from pygame import mixer
from tkinter import *
from tkinter import ttk
from datetime import datetime
from time import sleep


win = Tk()
win.title("")
win.geometry("350x150")


def play_sound():
    mixer.music.load('hutch.mp3')
    mixer.music.play()


def sound_alarm():
    while True:
        control = 1
        print(control)
        alarm_hour = '03'
        alarm_minutes = '44'
        alarm_seconds = '00'
        alarm_period = "PM".upper()

        now = datetime.now()
        hour = now.strftime("%I")
        minutes = now.strftime("%M")
        seconds = now.strftime("%S")
        period = now.strftime("%p")
        if control == 1:
            if period == alarm_period:
                if alarm_hour == hour:
                    if alarm_minutes == minutes:
                        if alarm_seconds == seconds:

                            print("Time to Wake Up 😂")
                            play_sound()
        sleep(1)


mixer.init()
sound_alarm()
win.mainloop()
