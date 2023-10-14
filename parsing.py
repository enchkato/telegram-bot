import requests
from bs4 import BeautifulSoup

def get_semei_weather():
    url = 'https://tengrinews.kz/weather/semey/'

    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')
    weather_block = soup.find('div', class_='temp')

    weather_info = weather_block.get_text().strip()
    return "Погода в Семее: " + weather_info

def statistics_mistermax():
    url = 'https://whatstat.ru/channel/UC_8PAD0Qmi6_gpe77S1Atgg'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    statistics = soup.find('table', class_='table')
    statistics_info = statistics.get_text().strip()
    return statistics_info

def newskz():
    url = 'https://tengrinews.kz/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    news = soup.find('span', class_='tn-main-news-title')
    news_info = news.get_text().strip()
    return news_info