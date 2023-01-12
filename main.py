import requests
from bs4 import BeautifulSoup



# Example 2
def search_google(keyword):
    with requests.session() as c:
        url = 'https://www.google.com'
        query = {'q': keyword}
        res = requests.get(url, params=query)
        print(res.url)

# Example 3
def get_images(url):
    images = []
    res = requests.get(url=url)
    soup = BeautifulSoup(res.text, 'html.parser')
    for item in soup.find_all('img'):
        images.append(item['src'])
    return images

# Example 4
def get_university_rankings():
    url = "https://www.shanghairanking.com/rankings/arwu/2022"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')

    table = soup.find('table')
    universities = []
    for row in table.tbody.find_all('tr'):
        uni = {}
        columns = row.find_all('td')
        uni["rank"] = columns[0].text.strip()
        uni["name"] = columns[1].find("span",{"class":"tooltiptext"}).text.strip()
        uni["Total_score"] = columns[4].text.strip()
        universities.append(uni)
    return universities

# Example 5
def get_products_prices():
    url = "https://www.elkor.lv/eng/for-women/outwear/jackets/?page=1"
    res = requests.get(url=url)
    soup = BeautifulSoup(res.text,'html.parser')
    prods = soup.find_all("div","product light-top-box-shadow small-shadow-on-hover bg-cl-white border-box h-100 relative brdr-r-16 overflow-visible product-tile-dynamic-width product-listing-item flex mr15 mb20 product-tile-small")
    products = []
    for p in prods:
        prod = {}
        price = p.find("span",{"class","price-svg cl-black fs28 lh33 current-price"}).text.strip()
        name = p.find("div",{"class","product-name-wrapper bg-cl-white border-box product-name brdr-r-16 bg-cl-white"}).text.strip()
        prod["name"] = name
        prod["price"] = price
        products.append(prod)
    return products


# 1.1
url = "https://www.google.com"
res = requests.get(url=url)
print("status COde",res.status_code)
print("Response",res.text)

# 1.2
res = requests.post('https://httpbin.org/post', data={'key': 'value'})
print("status COde",res.status_code)
print("response",res.text)


# # 1.3
res = requests.delete('https://httpbin.org/delete', data={'key': 'value'})
print("status COde",res.status_code)
print("response",res.text)


# 2
search = search_google("python")

# 3
images = get_images("https://www.shanghairanking.com/rankings/arwu/2022")
for img in images:
    print(img)

# 4
unis = get_university_rankings()
for uni in unis:
    print(uni)

# 5
products = get_products_prices()
for prod in products:
    print(prod)
