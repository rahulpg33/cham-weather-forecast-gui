import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk,Image
import arima_rh
import arima_temp
import arima_precp
import arima_windspeed

root=Tk ()
root.title("Weather App")
root.geometry("302x408")
root.configure(bg="#FFFFFF")

def getweather(): 
    datetime=textfield.get()
    print(datetime)
    temperature = arima_temp.Temper(datetime)
    relative_humidity = arima_rh.RelHum(datetime)
    windspeed = arima_windspeed.Wind(datetime)
    precipitation = arima_precp.Precipit(datetime)
    

    t.config(text=("%.2f" % temperature, "°C"))

    h.config(text= ("%.2f" % relative_humidity, "%"))

    p.config(text=("%.2f" % precipitation, "mm/day")) 
    
    w.config(text=("%.2f" % windspeed, "m/s"))
    
    print("%.2f" % temperature)
    print("%.2f" % relative_humidity)
    print("%.2f" % precipitation)
    print("%.2f" % windspeed)
    
t=Label(root, font=("Helvetica", 11), fg="Black", bg="#FFFFFF")
t.place(x=55,y=240) 

h=Label(root, font=("Helvetica", 11), fg="Black", bg="#FFFFFF")
h.place(x=55,y=375)

p=Label(root, font=("Helvetica", 11), fg="Black", bg="#FFFFFF")
p.place(x=185,y=240)

w=Label(root, font=("Helvetica", 11), fg="Black", bg="#FFFFFF")
w.place(x=185,y=375)


aa=Label(root,text="CHAM",font=("Calisto MT", 25, "bold"),bg="#FFFFFF",fg="Black")
aa.place(x=20,y=20)

#icon
image_icon=PhotoImage(file=os.path.join(BASE_DIR, "icon", "logo1.png"))
root.iconphoto(False,image_icon)


#textbox
textfield=tk.Entry(root,width=20, font=("Californian FB", 10, "bold")) 
textfield.place(x=70,y=90)


#search icon
Search_icon=PhotoImage(file=os.path.join(BASE_DIR, "icon", "search.png")) 
myimage_icon=Button(image=Search_icon, borderwidth=0, cursor="hand2",command=getweather) 
myimage_icon.place(x=220,y=90)

#images
temp=ImageTk.PhotoImage(Image.open(os.path.join(BASE_DIR, "icon", "Tempert.png")))
my_label=Label(image=temp)
my_label.place(x=55,y=180)
my_label.configure(bg="#FFFFFF")

prep=ImageTk.PhotoImage(Image.open(os.path.join(BASE_DIR, "icon", "Precpit.png")))
my_label=Label(image=prep)
my_label.place(x=180,y=180)
my_label.configure(bg="#FFFFFF")

hum=ImageTk.PhotoImage(Image.open(os.path.join(BASE_DIR, "icon", "Rel_Hum.png")))
my_label=Label(image=hum)
my_label.place(x=50,y=310)
my_label.configure(bg="#FFFFFF")

ws=ImageTk.PhotoImage(Image.open(os.path.join(BASE_DIR, "icon", "WindS.png")))
my_label=Label(image=ws)
my_label.place(x=180,y=310)
my_label.configure(bg="#FFFFFF")


#labels

label1=Label(root, text="Temperature", font=("Helvetica",11), fg="Black", bg="#FFFFFF")
label1.place(x=50,y=140)
label2=Label(root, text="Humidity", font=("Helvetica", 11), fg="Black", bg="#FFFFFF")
label2.place(x=50,y=280)
label3=Label(root, text="Precipitation", font=("Helvetica", 11), fg="Black", bg="#FFFFFF")
label3.place(x=170,y=140)
label4=Label(root, text="Wind Speed", font=("Helvetica", 11), fg="Black", bg="#FFFFFF")
label4.place(x=170,y=280)




root.mainloop()