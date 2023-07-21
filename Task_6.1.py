import requests
from bs4 import BeautifulSoup

url = str(input("Enter the link on the Yandex Music platform: "))
# url = 'https://music.yandex.ru/artist/4247128/tracks'

try:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    quotes = soup.find_all('div', class_='d-track__name')

    print("The artist 's top ten tracks:")
    count_track = 1

    for quotes in quotes:
        print(count_track, ")", quotes.text, sep="")
        if count_track == 10:
            break
        count_track += 1

except requests.exceptions.RequestException as error:
    raise SystemExit(error)
