import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

myurl =  "https://www.amazon.es/s/ref=nb_sb_noss_2?__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&url=search-alias%3Daps&field-keywords=gtx+1050+ti"
#open connection and grab page
uClient = uReq(myurl)
#raw html
page_html= uClient.read()
#close file
uClient.close()
#html parser
page_soup = soup(page_html, "html.parser")

#Grab objects
containers = page_soup.findAll("div",{"class":"s-item-container"})
#count how many
#    len(containers)
#see html
#item[index]
#    containers[0]

container = containers[0]

filename = "products.csv"
f = open(filename, "w")

headers = "name, brand \n"

f.write(headers)

for container in containers:
    name = container.div.div.div.a.img["alt"]

    brand = container.findAll("span", {"class":"a-size-small a-color-secondary"})
    brand_formatted = brand[1].text

    print("-  -  --  -  --  -  --  -  --  -  -")
    print("NAME: " + name.replace(",", "|"))
    print("BRAND: " + brand_formatted)
    print("-  -  --  -  --  -  --  -  --  -  -")

    f.write(name.replace(",", "|") + "," + brand_formatted + "\n")


f.close()
