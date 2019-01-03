from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20cards'

# opening up connection, grabbing the page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
# parse the html
page_soup = soup(page_html, "html.parser")

# convert every line item into a csv file

# grabs each product
containers = page_soup.findAll("div", {"class":"item-container"})

filename = "products.csv"
f = open(filename, "w")

headers = "brand, features\n"
f.write(headers)

for container in containers:
	brand = container.img["title"]
	features_container = container.ul.findAll("li")
	features = features_container[0].text.strip()
	
	print("brand: " + brand)
	print("features: " + features)
	
	
	for container in features_container:
		f.write(brand.replace(",", "|") + "," + features.replace(",", "|") + "\n")

f.close()

	