from bs4 import BeautifulSoup
import requests
import PySimpleGUI as sg
import urllib.request


def connect(host='http://google.com'):
    try:
        urllib.request.urlopen(host)
        return True
    except:
        return False


def get_time(city, prayer):
    city = city.replace(" ", "-")
    url = "https://prayertimes.date/" + city

    try:
        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")
        prayer_tag = doc.find_all(text=prayer)[0]
        parent = prayer_tag.parent.parent
        time = list(parent.children)[1].string
        return time, url

    except:
        if not connect():
            print("No internet connection.")
        else:
            print("Cannot retrieve city data, check spelling or enter another city near you.")
        return "", ""


def get_date(city):
    city = city.replace(" ", "-")
    url = "https://prayertimes.date/" + city
    result = requests.get(url)
    doc = BeautifulSoup(result.text, "html.parser")
    tag = doc.p
    date = list(tag.children)[0].string.lstrip("Prayers Today: ")
    return date


def convertTime(time):
    time_int = int(time[0] + time[1] + time[3] + time[4])
    if time_int - 1200 > 0:
        new_time_int = time_int-1200
        new_time = str(new_time_int)
        if new_time_int < 1000:
            if new_time_int < 100:
                if new_time_int < 10:
                    if new_time_int == 0:
                        return "12:00 PM"
                    return "12:0" + new_time[1] + " PM"
                return "12:" + new_time[0] + new_time[1] + " PM"
            return "0" + new_time[0] + ":" + new_time[1] + new_time[2] + " PM"
        else:
            return new_time[0] + new_time[1] + ":" + new_time[2] + new_time[3] + " PM"
    elif time[1] == "0":
        new_time = "12:" + time[3] + time[4] + " AM"
        return new_time
    else:
        return time + " AM"


def calculate(window, values, prayer):
    window.FindElement('_output_').Update('')
    city = values[0]
    time, url = get_time(city, prayer)
    if time != "":
        if values['12hr']:
            time = convertTime(time)
        print(prayer + " time in " + city + " is at: " + time + ", local time."
              "\nDate: " + get_date(city) +
              "\n\nRetrieved from " + url)


def main():
    sg.theme('DarkGreen')

    layout = [
        [sg.Text('Enter the name of your city:'), sg.InputText('Calgary', size=(37, 37))],

        [sg.Text('Which prayer would you like to retrieve the time of?')],
        [sg.Button('Fajr'), sg.Button('Dhuhr'), sg.Button('Asr'), sg.Button('Maghrib'), sg.Button('Isha'),
         sg.Checkbox('12-hour clock?', key='12hr', default=True)],
        [sg.Text('-' * 108)],
        [sg.Output(size=(60, 7), key="_output_")],
        [sg.Button('Quit'), sg.Text(' ' * 67), sg.Button('About'), sg.Button('Contact')]]

    window = sg.Window('Prayer Pal by Omar Khan', layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Quit':  # if user closes window or clicks cancel
            break

        if event == 'Fajr':
            calculate(window, values, "Fajr")

        if event == 'Dhuhr':
            calculate(window, values, "Dhuhr")

        if event == 'Asr':
            calculate(window, values, "Asr")

        if event == 'Maghrib':
            calculate(window, values, "Maghrib")

        if event == 'Isha':
            calculate(window, values, "Isha")

        if event == 'About':
            window.FindElement('_output_').Update('')
            print("Prayer Pal allows Muslims to view the Islamic prayer times for their location!"
                  "\nTo get started, enter the name of your city in the space provided and select a prayer."
                  "\nThere is an option to view the time as either a 12-hour format or military format.")

        if event == 'Contact':
            window.FindElement('_output_').Update('')
            print("Created by Omar Khan"
                  "\nhttps://github.com/omarkhan03"
                  "\nomarahmadkhan2003@gmail.com")

    window.close()


main()
