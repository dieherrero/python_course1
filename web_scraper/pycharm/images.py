from bs4 import BeautifulSoup
import requests
from PIL import Image
from io import BytesIO
import os


def ImgSearch():
    search = input("IMAGE SEARCHER. Enter search term: ")
    parameters = {"q": search}
    dir_name = search.replace(" ", "_").lower()  #lower quita las mayusculas

    if not os.path.isdir(dir_name):
        os.makedirs(dir_name)

    r = requests.get("http://www.bing.com/images/search", params=parameters)

    soup = BeautifulSoup(r.text, "html.parser")  #acess content of the html, soup = entire webpage
    links = soup.find_all("a", {"class": "thumb"})  #find elements in results with the class thumb

    for item in links:
        try:
            img_object = requests.get(item.attrs["href"])
            print("Getting...", item.attrs["href"])
            title = item.attrs["href"].split("/")[-1]
            try:
                img = Image.open(BytesIO(img_object.content))
                img.save("./" + dir_name + "/" + title, img.format)
            except:
                print("Can't save.")
        except:
            print("Couldnt request.")


    ImgSearch()

ImgSearch()
