from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

from .scrapebay import job_data
from .amazon import pro_data



def home(request):

    if request.method == 'POST':
        product = request.POST['title']
        
        product = product.strip()
        p = product.title
        items = p
        product = product.replace(' ', '+')

    
        url = 'https://www.ebay.com/sch/i.html?_nkw='+product+'&_pgn=1'
        url2 = 'https://www.amazon.com/s?k='+product+'&ref=nb_sb_noss_1'

        q,w,e,r = pro_data(url2)
        adata = zip(q,w,e,r)
        x,y,z,a = job_data(url, items)
        data = zip(x,y,z,a)
        
        if len(x)>0:
            context={
                'data':data,
                'adata':adata                
                
                
                
            }
        else:
            context ={
                'message':'No data Found!',
            }
            
        return render(request,'index.html',context)
      
     
    return render(request,'index.html')
    
