from tkinter import *
from PIL import ImageTk, Image
from SoftyBackend import *


r = sr.Recognizer()
def greet():
    SoftyFrame.destroy()
    today = datetime.now()
    speak(f"hello ma'am, {wishMe()} I am your voice assistant Softy.")
    speak(f"Today is {today.strftime('%d')} of {today.strftime('%B')} and its currently {today.strftime('%I %p %M')} minute" )
    speak(f"temperature in nagpur is {str(round(temp_city))} degree celsius with {str(weather_desc)}")
    speak("how are you")
    softyMain()

SoftyFrame = Tk()
SoftyFrame.title("SOFTY")
SoftyFrame.geometry("510x310")
SoftyFrame.maxsize(450,260)
SoftyFrame.minsize(450,260)

img = ImageTk.PhotoImage(Image.open('LindaImg.jpg'))
panel = Label(SoftyFrame, image=img)
panel.pack(side='right', fill='both', expand='no')

user_text = StringVar()

user_text.set('Your Virtual Assistance')
userFrame = LabelFrame(SoftyFrame, text='SOFTY', font=('Railways', 22, 'bold'))
userFrame.pack(fill='both', side='top', expand='yes')

top = Message(userFrame, textvariable=user_text, bg="black", fg="white")
top.config(font=('century Gothic', 15, 'bold'))
top.pack(side='top', fill='both', expand='yes')


btnRun = Button(SoftyFrame, text='run', font=('railways', 10, 'bold'), bg='red', fg='white',command=greet).pack(fill='x', expand='no')
# btnStop= Button(SoftyFrame,text='close',font=('railways',10,'bold'),command=exit()).pack(fill='x',expand='no')

SoftyFrame.mainloop()



