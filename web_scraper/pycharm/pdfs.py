from bs4 import BeautifulSoup
import requests
from PIL import Image
from io import BytesIO
import os


def PdfSearch():
    search = input("PDF SEARCHER. Enter search term: ")
    parameters = {"q": search}
    dir_name = search.replace(" ", "_").lower()  #lower quita las mayusculas

    if not os.path.isdir(dir_name):
        os.makedirs(dir_name)

    r = requests.get("http://www.bing.com/search", params=parameters)

    soup = BeautifulSoup(r.text, "html.parser")  #acess content of the html, soup = entire webpage
    links = soup.find_all("a", {"class": "b_attribution"})  #find elements in results with the class thumb

    for item in links:
        try:
            url_pdf = requests.get(item.attrs["href"])
            print("Getting...", item.attrs["href"])
            title = item.attrs["href"].split("/")[-1]
            try:
                pdf = requests.get(str(url_pdf))
#                pdf.save("./" + dir_name + "/" + title, format='pdf')
            except:
                print("Can't save.")
        except:
            print("Couldnt request.")

    PdfSearch()


PdfSearch()
