# Welcome to Prayer Pal!

Prayer Pal allows users to view the Islamic prayer times for their location.

## To run Prayer Pal

1. If you don't have Python already installed, go to https://www.python.org/downloads/ and install the latest version.
2. Ensure you have the latest version of pip installed by following the instructions on https://pip.pypa.io/en/latest/installation/#ensurepip
3. Import the necessary libraries using the following commands:

`pip3 install beautifulsoup4`

`pip3 install requests`

`pip3 install PySimpleGUI`

4. Navigate to the project folder (`cd PrayerPal`) and run the command `python3 main.py` to run the program!

## To use Prayer Pal

To get started, enter the name of your city in the space provided and select a prayer. There is an option to view the time as either a 12-hour format or military format. Prayer Pal should work for most cities in the world. If no data can be retrieved for your city, check your spelling and try inputting another city near you.

![image](https://user-images.githubusercontent.com/106503860/170929457-e2f9ea0b-3b54-4f9f-b575-9d104ebdd715.png)


## About

All prayer times are retrieved from https://prayertimes.date, using webscraping with the BeautifulSoup4 library.

Created by Omar Khan

https://github.com/omarkhan03

omarahmadkhan2003@gmail.com
