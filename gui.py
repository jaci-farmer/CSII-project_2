from tkinter import *
import requests
from bs4 import BeautifulSoup
import csv

class GUI:
    """
    creating the layout of the application
    """
    def __init__(self, window) -> None:
        self.window = window

        self.frame_top = Frame(self.window)
        self.label_name = Label(self.frame_top, text='Enter city:')
        self.city_name = Entry(self.frame_top)
        self.label_name.pack(padx=0, side='left')
        self.city_name.pack(padx=5, side='left')
        self.frame_top.pack(anchor='w', pady=10)

        self.frame_last = Frame(self.window)
        self.button_save = Button(self.frame_last, text="SUBMIT", command=self.clicked)
        self.button_save.pack()
        self.frame_last.pack()

        self.weather = Entry(self.window)
        self.weather = Entry(
            self.window,
            width=100,
            font=('Arial', 12)
        )

        self.weather.pack(pady=5)

        self.frame_final = Frame(self.window)
        self.button_clear = Button(self.frame_last, text="CLEAR", command=self.clear)
        self.button_clear.pack()
        self.frame_final.pack()


    def clicked(self) -> None:
        """
        using the city name to scrap weather data of that city
        :return:
        """
        city = self.city_name.get()
        city = city.strip()
        if type(city) != str:
            raise TypeError

        # creating url
        url = "https://www.google.com/search?q=" + "weather" + city

        # requests instance
        html = requests.get(url).content

        # getting the raw data
        soup = BeautifulSoup(html, 'html.parser')

        # getting the temperature
        temp = soup.find("div", attrs={'class': "BNeawe iBp4i AP7Wnd"}).text

        # getting the time and sky description
        time_skyDescription = soup.find('div', attrs={'class': "BNeawe tAd8D AP7Wnd"}).text

        # formatting the data
        data = time_skyDescription.split('\n')
        time = data[0]
        sky = data[1]

        # list which has all div tags with particular class names
        listdiv = soup.findAll('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'})

        # the data we need is available at index 5
        strd = listdiv[5].text

        # formatting the string
        pos = strd.find("Wind")

        # writing weather sentence
        self.weather.insert(0, f'City: {city},   Temperature: {temp},   Time: {time},   Sky Description: {sky}')


        # clearing the city name tag
        self.city_name.delete(0, END)


    def clear(self) -> None:
        # clearing the output to run program again
        self.weather.delete(0, END)