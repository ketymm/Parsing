import requests
from bs4 import BeautifulSoup
import csv
import time
from random import randint

file = open('iPads.csv', 'w', encoding='utf-8_sig', newline='\n')
write_obj = csv.writer(file)
write_obj.writerow(['მოდელი', 'შიდა მეხსიერება', 'ფერი', 'პროდუქტის კოდი', 'ფასი', 'მოდელის ფოტო'])


page_number = 1
while page_number <= 5:
    url = f'https://ispace.ge/ipad?page={page_number}&filter_price%5Bfrom%5D=999&filter_price%5Bto%5D=3500'
    response = requests.get(url)
    content = response.text

    # code = response.status_code
    # print(response.headers)
    # print(code)

    soup = BeautifulSoup(content, 'html.parser')
    ipad_section = soup.find('ul', class_='cards-list')
    all_ipads = ipad_section.find_all('li')
    for ipad in all_ipads:
        right = ipad.find('div', class_='overflow-hidden')
        descr = right.find('div', class_='mb-3')
        full_title = descr.a.h2.text.strip()
        title = full_title.split(", ")[0]
        capacity = full_title.split(", ")[1]
        color = full_title.split(", ")[3]
        product_code = descr.p.text.strip()[16:]
        price = ipad.find('span', class_='price-text__value').text
        image_address = ipad.img.attrs.get('src')
        write_obj.writerow([title, capacity, color, product_code, price, image_address])
    page_number += 1
    time.sleep(randint(15, 20))