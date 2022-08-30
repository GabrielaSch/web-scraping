from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import requests
from bs4 import BeautifulSoup

# origem dos dados
url = 'https://g1.globo.com/busca/?q=intelig%C3%AAncia+artitificial'

option = Options() 
option.headless = True 

driver = webdriver.Chrome('C:/Users/User/Downloads/driver/chromedriver', options=option)
driver.get(url)

# scroll na página do site
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") 
time.sleep(10)

element = driver.find_element_by_id('content') 
html = element.get_attribute('outerHTML') 
print(element)
html = element.get_attribute('outerHTML')
driver.quit()  

# pegar seção de manchetes
soup = BeautifulSoup(html, 'lxml') 

text_list = []

for section in soup.find_all(class_='widget--info__text-container'):
    for href in section.find_all('a'): 
        title = href.find(class_='widget--info__title product-color')
        if(title != None): 
            print('title',title.text[7:-2]) 
            text_list.append(title.text[7:-2]) 
        description = href.find(class_='widget--info__description')
        if(description != None):
            text_list.append(description.text) 
            
text_list = ' '.join(text_list) 
print(text_list)

# obter a frequência de palavras mais usadas
pip install nltk
import nltk
from nltk.tokenize import RegexpTokenizer 
 
tokenizer = RegexpTokenizer(r'[a-zA-Z]\w+') 
tokens = tokenizer.tokenize(text_list)
 
stopwords = nltk.corpus.stopwords.words()

new_list = [token.lower() for token in tokens if token.lower() not in stopwords]
 
frequencia = nltk.FreqDist(new_list)
(frequencia.most_common(20))
