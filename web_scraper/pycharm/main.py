from bs4 import BeautifulSoup
import requests


search = input("Enter search term: ")
parameters = {"q": search}

r1 = requests.get("http://www.bing.com/search", params=parameters)

soup = BeautifulSoup(r1.text, "html.parser")  #acess content of the html, soup = entire webpage
results = soup.find("ol", {"id": "b_results"})  #certain results of the webpage
links = results.find_all("li", {"class": "b_algo"})  #find elements in results with the class b_algo

item_text = None
item_href = None

for item in links:
    item_text = item.find("a").text
    item_href = item.find("a").attrs["href"]
    item_summary = results.find("a").parent.parent.find("p").text

    if item_text and item_href:
        print(item_text)
        print(item_href)
     #   print(item_summary)
        print("Parent:", item.find("a").parent)
        print("Summary:", )
        children = item.children("h2")
        for child in children:
            print("Child: ", child)
