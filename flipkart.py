import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook
import re
main_url='https://www.flipkart.com/search?q=baby%20milk&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'
page=requests.get(main_url)
soup=BeautifulSoup(page.content,'html.parser')
productdeatils=soup.findAll("div",{'class':'_4ddWXP'})

wb=Workbook()
ws=wb.create_sheet('flipkart_data')


def row(productId):
    pass


for product in productdeatils:
    product=product.find('a')
    product=product['href']
    soup_data=BeautifulSoup(requests.get('https://www.flipkart.com'+product).content,'html.parser')
    try:
        productname=soup_data.find('span',{'class':'B_NuCI'}).getText()
    except:
        pass
    try:
        price=''.join(re.findall("\d+",soup_data.find('div',{'class':'_25b18c'}).getText().replace(',','')))
    except:
        pass
    sponsored='No'
    review_details=soup_data.find('div',{'class':'gUuXy- _16VRIQ'})
    try:
        average_rating=review_details.find('div',{'class':'_3LWZlK'}).getText()
    except:
        pass
    try:
        rating=soup_data.find('span',{'class':'_2_R_DZ'}).getText()
    except:
        pass
    try:
        productId=''.join(re.findall('pid=(.*?)id','https://www.flipkart.com'+product))
    except:
        pass
    row=[productId,productname,price,sponsored,average_rating,rating]
    print(productId)
    print(productname)
    print(sponsored)
    print(average_rating)
    print(rating)
    ws.append(row)
wb.save('flipkart.xlsx')


