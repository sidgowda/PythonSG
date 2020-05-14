from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as ureq
my_url = 'https://www.flipkart.com/search?q=samsung%20mobiles&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'

uclient = ureq(my_url)
page_html = uclient.read()
#print(page_html)
uclient.close()

page_soup = soup(page_html, "html.parser")

containers = page_soup.find_all("div", {"class": "_3O0U0u"})

#print(len(containers))
#print(soup.prettify((containers[0])))

#c = containers[0]
'''
print(c.div.img["alt"])
price = c.findAll("div", {"class": "_1vC4OE _2rQ-NK"})
print(price[0].text)
ratings = c.findAll("div",{"class": "hGSR34"})
print(ratings[0].text)
memory = c.findAll("div",{"class": "_3ULzGw"})
print(memory[0].text)
'''
#filename ="prodcut.csv"
#f = open(filename,"w")

with open("prodcut.csv", "w", encoding="utf-8") as f:
 headers = "ProductName,Price,Rating,Features"
 f.write(headers)
 f.write("\n")
 for c in containers:
    product_name = c.div.img["alt"]
    price_c = c.findAll("div", {"class": "_1vC4OE _2rQ-NK"})
    price = price_c[0].text.strip()
    ratings_c = c.findAll("div", {"class": "hGSR34"})
    ratings = ratings_c[0].text
    features_c = c.findAll("div", {"class": "_3ULzGw"})
    features = features_c[0].text.strip()

    '''print("Product Name:::" + product_name)
    print("Price:::" + price)
    print("Ratings:::" + ratings)
    print("Features:::" + features)
    '''
    print(product_name.replace(",","|") + "," + price + "," + ratings + "," + features.replace("," , "*"))
    f.write(product_name + "," + price + "," + ratings + "," + features + "\n")
