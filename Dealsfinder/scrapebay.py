import requests
from bs4 import BeautifulSoup

#product = input("Enter product name:")
#product = product.replace('+', '').strip()

#url = 'https://www.ebay.com/sch/i.html?_nkw='+product+'&_pgn=1'

titles = []
prices = []
solds = []
link = []

def job_data(url,items):

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')

    links = soup.find_all('a', class_='s-item__link')
    urls = [item.get('href') for item in links]
    titles.clear()
    prices.clear()
    solds.clear()
    link.clear()
    #print(titles,prices,solds,link)    
    for i in urls:
    	response = requests.get(i)
    	soup = BeautifulSoup(response.text, 'lxml')
        
    	try:
            title = soup.find('h1', id='itemTitle')
            #print(title)
    	except:
           title = ''
           
    	try:
           price = soup.find('span', id='prcIsum').text.strip()
           #print(price)
    	except:
           price = ''
           
    	try:
           sold = soup.find('span', class_='vi-qtyS-hot-red').text.strip()
           #print(sold)
    	except:
           sold = ''
        
    	titles.append(title.text.strip())
    	prices.append(price)
    	solds.append(sold)
    	#link.append(urls)
    #print(prices)
    #print(titles)
    #print(solds)
    #print(urls)
    

    return titles,prices,solds,urls


  
