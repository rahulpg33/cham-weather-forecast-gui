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
root.geometry("695x873")

def getweather(): 
    datetime=textfield.get()
    print(datetime)
    temperature = arima_temp.Temper(datetime)
    relative_humidity = arima_rh.RelHum(datetime)
    windspeed = arima_windspeed.Wind(datetime)
    precipi = arima_precp.Precipit(datetime)
    
    
    print(temperature)
    print(relative_humidity)
    print(windspeed)
    print(precipi)
    
    label5=Label(root, text= temperature, font=("Californian FB", 10), fg="white", bg="#283243")
    label5.place(x=35,y=240)
    label6=Label(root, text= relative_humidity, font=("Californian FB", 10), fg="white", bg="#283243")
    label6.place(x=35,y=240)
    label7=Label(root, text= precipi, font=("Californian FB", 10), fg="white", bg="#283243")
    label7.place(x=155,y=340)
    label8=Label(root, text= windspeed, font=("Californian FB", 10), fg="white", bg="#283243")
    label8.place(x=155,y=340)

#c=Canvas(root,bg="grey16",height=200,width=200)
filename=PhotoImage(file=os.path.join(BASE_DIR, "Finalbg.png"))
background_label=Label(root,image=filename)
background_label.place(x=0,y=0,relwidth=1,relheight=1)

aa=Label(root,text="CHAM",font=("Californian FB", 20, "bold"))
aa.place(x=20,y=20)

#icon
image_icon=PhotoImage(file=os.path.join(BASE_DIR, "icon", "logo1.png"))
root.iconphoto(False,image_icon)



#textbox
textfield=tk.Entry(root,width=20, font=("Californian FB", 10, "bold")) 
#textfield.insert(0,"yyyy-mm-dd")
textfield.place(x=70,y=100)
#textfield.focus()


#search icon
Search_icon=PhotoImage(file=os.path.join(BASE_DIR, "icon", "search.png")) 
myimage_icon=Button(image=Search_icon, borderwidth=0, cursor="hand2",command=getweather) 
myimage_icon.place(x=220,y=100)

#images
#temp=ImageTk.PhotoImage(Image.open(os.path.join(BASE_DIR, "icon", "Temp.png")))
#my_label=Label(image=temp)
#my_label.place(x=50,y=240)

#prep=ImageTk.PhotoImage(Image.open(os.path.join(BASE_DIR, "icon", "Precipitation.png")))
#my_label=Label(image=prep)
#my_label.place(x=170,y=240)

#hum=ImageTk.PhotoImage(Image.open(os.path.join(BASE_DIR, "icon", "humidity.png")))
#my_label=Label(image=hum)
#my_label.place(x=50,y=340)

#ws=ImageTk.PhotoImage(Image.open(os.path.join(BASE_DIR, "icon", "Wind speed.png")))
#my_label=Label(image=ws)
#my_label.place(x=170,y=340)




#labels

#label1=Label(root, text="Temperature", font=("Helvetica",8), fg="white", bg="#283243")
#label1.place(x=50,y=200)
#label2=Label(root, text="Humidity", font=("Helvetica", 8), fg="white", bg="#283243")
#label2.place(x=50,y=300)
#label3=Label(root, text="Precepitation", font=("Helvetica", 8), fg="white", bg="#283243")
#label3.place(x=170,y=200)
#label4=Label(root, text="Wind Speed", font=("Helvetica", 8), fg="white", bg="#283243")
#label4.place(x=170,y=300)


#c.pack()
root.mainloop()