from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from pygame import mixer
from datetime import datetime
from time import sleep 
from threading import *

#colours
bg_color = '#ffffff' #white color
co1='blue'
co2='black'


#main
win =Tk()
win.title("")
win.geometry("350x150")
win.configure(bg=bg_color)
#frameline border differentiating 


frameline= Frame(win,width =400,height= 5,bg=co1).grid(row=0,column=0)
frame_body = Frame(win,width =400,height= 290,bg=bg_color).grid(row=1,column=0)
#inside


img = Image.open('icon.png')
img.resize((200,200))
img =ImageTk.PhotoImage(img)
icon  =Label(frame_body,image=img,height=100,bg = bg_color)
icon.place(x=10,y=10)


# Creating labels and combo boxes


name = Label(frame_body,text='Alarm',height=1,bg=bg_color,font='ivay 18 bold ')
name.place(x=125,y=10)

hour = Label(frame_body,text='Hour',height=1,bg=bg_color,font='ivay 10 ')
hour.place(x=127,y=40)
#crearting combobox for hours minutes seconds am/pm
c_hour =ttk.Combobox(frame_body,width=2,font=('arial 15 bold'))
c_hour['values']=['00','01','02','03','04','05','06','07','08','09','10','11','12']
c_hour.current(0)
c_hour.place(x=125,y=58)


min = Label(frame_body,text='Mins',height=1,bg=bg_color,font='ivay 10 ')
min.place(x=177,y=40)
c_min =ttk.Combobox(frame_body,width=2,font=('arial 15 bold '))
c_min['values']=['00','01','02','03','04','05','06','07','08','09','10',
                 '11','12','13','14','15','16','17','18','19','20',
                 '21','22','23','24','25','26','27','28','29','30',
                 '31','32','33','34','35','36','37','38','39','40',
                 '41','42','43','44','45','46','47','48','49','50',
                 '51','52','53','54','55','56','57','58','59']

c_min.current(0)
c_min.place(x=180,y=58)

sec = Label(frame_body,text='Sec',height=1,bg=bg_color,font='ivay 10 ')
sec.place(x=227,y=40)
c_sec=ttk.Combobox(frame_body,width=2,font=('arial 15 bold '))
c_sec['values']=['00','01','02','03','04','05','06','07','08','09','10',
                 '11','12','13','14','15','16','17','18','19','20',
                 '21','22','23','24','25','26','27','28','29','30',
                 '31','32','33','34','35','36','37','38','39','40',
                 '41','42','43','44','45','46','47','48','49','50',
                 '51','52','53','54','55','56','57','58','59']

c_sec.current(0)
c_sec.place(x=230,y=58)

period = Label(frame_body,text='Sec',height=1,bg=bg_color,font='ivay 10 ')
period.place(x=277,y=40)
c_period=ttk.Combobox(frame_body,width=3,font=('arial 15 bold '))
c_period['values']=['AM','PM']

c_period.current(0)
c_period.place(x=280,y=58)

#creating on and off button  using radiobuttons

def activate():
    t= Thread(target=sound_alarm)
    t.start()


#deactivate
def deactivate():
    print("deactivated alarm: ",selected.get())
    mixer.music.stop()



selected =IntVar() 

rad1= Radiobutton(frame_body,text="activate",font=("ivay 10 bold "),bg=bg_color,value=1,command=activate,variable=selected)
rad1.place(x=127,y=100)




#alarm 

def  play_sound():
    mixer.music.load('hutch.mp3')
    mixer.music.play()
    selected.set(0)

    rad2= Radiobutton(frame_body,text="Deactivate",font=("ivay 10 bold "),bg=bg_color,value=2,command=deactivate,variable=selected)
    rad2.place(x=187,y=100)


def sound_alarm():
    while True:
        control = selected.get()
        print(control)
        alarm_hour = c_hour.get()
        alarm_minutes=c_min.get()
        alarm_seconds = c_sec.get()
        alarm_period =c_period.get()
        alarm_period= str(alarm_period).upper()

        now = datetime.now()
        hour =now.strftime("%I")
        minutes = now.strftime("%M")
        seconds = now.strftime("%S")
        period =now.strftime("%p")
        if control ==1 :
            if period == alarm_period:
                if alarm_hour==hour:
                    if alarm_minutes==minutes:
                        if alarm_seconds== seconds:

                            print("Time to Wake Up 👋👋")
                            play_sound()
        sleep(1)    


mixer.init()
win.mainloop()