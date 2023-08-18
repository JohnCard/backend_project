from django.test import TestCase

# Create your tests here.
from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome()

def get_prod_list():
    url = 'https://www.amazon.com.mx/s?k=gym&__mk_es_MX=%C3%85M%C3%85%C5%BD%C3%95%C3%91&ref=nb_sb_noss'
    driver.get(url)
    
    soup = BeautifulSoup(driver.page_source,'lxml')
    
    '''
    a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal
    '''
    
    a_class = 'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'
    a_tags = soup.find_all('a', class_=a_class)
    
    for a in a_tags:
        title = a.text.replace('\n','')
        link = a.get('href')
        print('Título: ',title)
        print('Enlace: ',link)
        print('\n')
        
        detail_link = 'https://www.amazon.com.mx'+link if 'https' not in link else link
        get_details(detail_link)
    
    # print('TARJETAS ADICIONALES :')
    # print(a_tags)
def get_details(url):
    driver.get(url)
    soup = BeautifulSoup(driver.page_source,'lxml')
    
    price_class = 'a-offscreen'
    price = float(soup.find('span', class_=price_class).text.replace('$','').replace(',',''))
    print('price:',price)
    
    description_id = 'featurebullets_feature_div'
    description = soup.find('div',id=description_id).text
    print('description:',description)
        
get_prod_list()

link = ''

driver.close()

driver = webdriver.Chrome()
url = 'https://www.amazon.com.mx/s?k=gym&__mk_es_MX=%C3%85M%C3%85%C5%BD%C3%95%C3%91&ref=nb_sb_noss'
driver.get(url)

soup = BeautifulSoup(driver.page_source,'lxml')
print(soup)

# print(float(soup.find('span', class_='a-offscreen').text.replace('$','').replace(',','')))

print(soup.find('span', class_='a-offscreen'))

print(soup.find('span', class_='a-offscreen').text)

print(soup.find('span', class_='a-offscreen').text.replace('$',''))

print(soup.find('span', class_='a-offscreen').text.replace('$','').replace(',',''))

# print(float(soup.find('span', class_='a-offscreen').text.replace('$','').replace(',','')))

print(soup.find('div',id='featurebullets_feature_div'))

driver.close()