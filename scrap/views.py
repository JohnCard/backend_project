from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome()
def get_prod_list():
    driver.get('https://www.amazon.com.mx/s?k=electronica&rh=n%3A9687880011&__mk_es_MX=%C3%85M%C3%85%C5%BD%C3%95%C3%91&ref=nb_sb_noss')
    soup = BeautifulSoup(driver.page_source,'lxml')
    
    text_tags = soup.find_all('span', class_='a-size-base-plus a-color-base a-text-normal')
    prices_list = soup.find_all('span', class_='a-offscreen')
    link_list = soup.find_all('div', class_='a-section a-spacing-none a-spacing-top-small s-price-instructions-style')
    img_list = soup.find_all('img', class_='s-image')
    ratings = soup.find_all('span',class_='a-icon-alt')
    
    cont = -1
    for a in text_tags:
        try:
            link_var = 'https://www.amazon.com.mx'+link_list[cont].a.get('href')
            driver_two = webdriver.Chrome()
            driver_two.get(link_var)
            soup_two = BeautifulSoup(driver_two.page_source,'lxml')
            descriptions = soup_two.find_all('li', class_='a-spacing-mini')
            description = ''
            for i in descriptions:
                description += f'- {i.span.text}\n'
            users_amount = soup_two.find('span', id='acrCustomerReviewText').text[:3] + ' Users'
        except:
            description = 'We don´t have description for this item'
            users_amount = 'Undefined'
        cont += 1
        print(f'''\nTitle: {a.text}
Link: {link_var}
Price: {prices_list[cont].text}
Text image or picture (description): {img_list[cont].get('alt')}
Amount sent itmes: {users_amount}
Score (qualification): {ratings[cont].text[:3]}
Description: {description}''')
        with open('file.txt','a') as file:
            file.write(f'''\n\n{a.text} | {link_var} | {prices_list[cont].text} | {img_list[cont].get('alt')} | {ratings[cont].text[:3]} | ''')
        driver_two.close()

get_prod_list()
driver.close()
