#Реалізувати “етичний” скрейпінг: перевірити robots.txt, обмежити частоту запитів,
#додати таймаути і зібрати лог, який показує дотримання пауз між запитами.

import requests
import time
import logging
from urllib.robotparser import RobotFileParser

url = 'https://books.toscrape.com/robots.txt'

response = requests.get(url)
print(response.text)

rp = RobotFileParser()
rp.set_url(url)
rp.read()

user_agent = '*'
target_url = 'https://books.toscrape.com/'

if not rp.can_fetch(user_agent, target_url):
    print('Скрапінг заборонений robots.txt')
    exit()

print('Скрапінг дозволений')

logging.basicConfig(
    filename='scraper.log',
    level=logging.INFO,
    format='%(asctime)s - %(message)s'
)

DELAY = 3
TIMEOUT = 5

headers = {
    'User-Agent': 'EthicalScraperBot/1.0'
}

pages = [
    'https://books.toscrape.com/',
    'https://books.toscrape.com/catalogue/page-1.html',
    'https://books.toscrape.com/catalogue/page-2.html'
]

for page in pages:
    start_time = time.time()

    if not rp.can_fetch(user_agent, page):
        logging.warning(f'Доступ заборонений robots.txt -> {page}')
        continue

    try:
        response = requests.get(
            page,
            headers=headers,
            timeout=TIMEOUT
        )
        print(f'Отримано {page} -> {response.status_code}')
        logging.info(f'Request -> {page} статус {response.status_code}')

    except requests.exceptions.Timeout:
        logging.warning(f'Timeout при запиті {page}')

    except requests.exceptions.RequestException as e:
        logging.error(f'Помилка {page}: {e}')

    time.sleep(DELAY)

    end_time = time.time()
    elapsed = end_time - start_time
    logging.info(f'Pause respected: {DELAY} seconds | elapsed {elapsed:.2f}')