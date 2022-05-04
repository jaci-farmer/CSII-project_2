from tkinter import *
import requests
from bs4 import BeautifulSoup
import csv

class GUI:
    def __init__(self, window):
        self.window = window

        self.frame_top = Frame(self.window)
        self.label_name = Label(self.frame_top, text='Enter a city to find out weather:')
        self.city_name = Entry(self.frame_top)
        self.label_name.pack(padx=0, side='left')
        self.city_name.pack(padx=5, side='left')
        self.frame_top.pack(anchor='w', pady=10)

        self.frame_last = Frame(self.window)
        self.button_save = Button(self.frame_last, text="SAVE", command=self.clicked)
        self.button_save.pack()
        self.frame_last.pack()


    def clicked(self):
        city = self.city_name.get()

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
        otherData = strd[pos:]

        # storing data to CSV file
        info = [city, temp, time, sky]
        with open("weather.csv", 'a', newline= "") as csvfile:
            content = csv.writer(csvfile)

            content.writerow(info)

        self.city_name.delete(0, END)


