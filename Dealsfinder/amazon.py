from bs4 import BeautifulSoup
from selenium import webdriver

atitles = []
aprices = []
#review_counts = []
ratings = []
alink = []



def pro_data(url2):

    driver = webdriver.Chrome()
    driver.get(url2)

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    results = soup.find_all('div', {'data-component-type': 's-search-result'})
    atitles.clear()
    aprices.clear()
    ratings.clear()
    alink.clear()
    #print(atitles,aprices,ratings,alink)
    
    for item in results:
        atag = item.h2.a
        Name = atag.text.strip()
        #print(Name)
        url = 'https://www.amazon.com' + atag.get('href')
        try:
            price_parent = item.find('span', 'a-price')
            price = price_parent.find('span', 'a-offscreen').text
            #print(price)

        except:
            price = ''
        try:
            rating = item.i.text
            #review_count = item.find('span', {'class': 'a-size-base', 'dir': 'auto'}).text
		
        except:
            rating = ''
            #review_count = ''
            
        atitles.append(Name)
        aprices.append(price)
        #review_counts.append(review_count)
        ratings.append(rating)
        alink.append(url)

        
        
    #aprices.sort()        
    driver.close()
    #print(atitles)
    #print(aprices)
    #print(ratings)
    #print(alink)
 
    
    return atitles,aprices,ratings,alink   