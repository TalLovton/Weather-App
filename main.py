from datetime import datetime as dt
from tkinter import messagebox
import pytz
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
import requests
from tkinter import *
import tkinter as tk

app = Tk();
app.title("Weather App")
app.geometry('900x500+300+200')
app.resizable(False,False)

def getWeather():
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
    # ? at the end is for adding more paramaters like API key...
    API_KEY = "e35c55874558830792a90a839740464d"
    CITY = textField.get()
    url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY
    response = requests.get(url).json()


    if(response['cod'] != '404'):
        getLocalTime(CITY)
        # collecting the data into variables:
        tempKelvin = response['main']['temp']
        tempCelsius = int(kelvinToCelsius(tempKelvin))

        feelsLikeKelvin = response['main']['feels_like']
        feelsLikeCelsius = int(kelvinToCelsius(feelsLikeKelvin))

        humidity = response['main']['humidity']
        windSpeed = response['wind']['speed']
        description = response['weather'][0]['description']
        sunriseTime = dt.utcfromtimestamp(response['sys']['sunrise'] + response['timezone']).strftime("%I:%M %p")
        sunsetTime = dt.utcfromtimestamp(response['sys']['sunset'] + response['timezone']).strftime("%I:%M %p")
        setWeatherAttributes(tempCelsius,feelsLikeCelsius,windSpeed,humidity,description,sunriseTime,sunsetTime)
    else:
        messagebox.showerror("Weather App","City not found ):\n Try again")

def kelvinToCelsius(kelv):
     celsius = kelv - 273.15
     return celsius

def getLocalTime(CITY):
    geolocator = Nominatim(user_agent="geoapiExcercises")
    location = geolocator.geocode(CITY)
    obj = TimezoneFinder()
    result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
    home = pytz.timezone(result)
    localTime = dt.now(home)
    currTime = localTime.strftime("%I:%M %p")
    clock.config(text=currTime)
    name.config(text="Local time:")


    #Search Box

def setWeatherAttributes(temp,feelsLikeTemp,wind,humid,desc,sunrise,sunset):
    tempatureTxt.config(text=(temp, "°C"))
    fellLikeTempTxt.config(text=("FEELS", "LIKE", feelsLikeTemp, "°C"))
    windTxt.config(text=(wind, "km/h"))
    humidTxt.config(text=(humid, "%"))
    descripTxt.config(text=desc)
    sunTxt.config(text=('Sunrise: ' + sunrise + "\n" + "Sunset: " + sunset))


    #Search Box
SearchImage = PhotoImage(file="Images/Copy of search.png")
myImage = Label(image=SearchImage)
myImage.place(x=20, y=20)
textField = tk.Entry(app, justify="center", width=17, font=("poopins", 25, "bold"), bg= "#404040", border=0, fg="white")
textField.place(x=50, y=40)
textField.focus()

SearchIcon = PhotoImage(file="Images/Copy of search_icon.png")
icon = Button(image=SearchIcon,borderwidth=0,cursor="hand2",bg="#404040",command=getWeather)
icon.place(x=400, y=34)

    #Logo
LogoImage = PhotoImage(file="Images/Copy of logo.png")
logo = Label(image=LogoImage)
logo.place(x=150, y=100)

    #Bottom box
FrameImage = PhotoImage(file="Images/Copy of box.png")
frameImage =Label(image=FrameImage)
frameImage.pack(padx=5, pady=5, side=BOTTOM)

    #Time
name = Label(app,font=("arial",15,"bold"))
name.place(x=30,y=100)
clock = Label(app,font=("Helvetica",20))
clock.place(x=30, y=130)

    #Lables
label1 = Label(app,text="WIND",font=("Helvetica",15,'bold'), fg="white", bg="#1ab5ef")
label1.place(x=120,y=400)

label2 = Label(app,text="HUMIDITY",font=("Helvetica",15,'bold'), fg="white", bg="#1ab5ef")
label2.place(x=250,y=400)

label3 = Label(app,text="DESCRIPTION",font=("Helvetica",15,'bold'), fg="white", bg="#1ab5ef")
label3.place(x=430,y=400)

label4 = Label(app,text="SUN CYCLES",font=("Helvetica",15,'bold'), fg="white", bg="#1ab5ef")
label4.place(x=640,y=400)

tempatureTxt =Label(font=("arial",70,"bold"), fg="#ee666d")
tempatureTxt.place(x=400, y=150)
fellLikeTempTxt = Label(font=("arial",15,"bold"))
fellLikeTempTxt.place(x=400,y=250)

windTxt=Label(text="...",font=("arial",15),bg="#1ab5ef")
windTxt.place(x=120,y=430)

humidTxt=Label(text="...",font=("arial",15),bg="#1ab5ef")
humidTxt.place(x=280,y=430)

descripTxt=Label(text="...",font=("arial", 15),bg="#1ab5ef")
descripTxt.place(x=430,y=430)

sunTxt=Label(text="...",font=("arial", 13, "bold"), bg="#1ab5ef")
sunTxt.place(x=640,y=430)

app.mainloop()

