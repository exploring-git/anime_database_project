import requests
import time
from time import perf_counter
import re
import concurrent.futures
import pprint
from bs4 import BeautifulSoup



def main():
    start=perf_counter()
    url = 'https://myanimelist.net/anime.php?letter='
    anime_ids=set(get_anime_id(url))
    with open("ids.txt","w") as file:
        for i in anime_ids:
            file.write(f"{i}\n")
    finish=perf_counter()
    time = round(finish-start,2)
    print(time,"secs")

def get_anime_id(url):
    animes_Ids=[]
    urls=[url+chr(letter) for letter in range(97,123)]
    with concurrent.futures.ProcessPoolExecutor() as excuter:
        result=list(excuter.map(anime_id,urls))
        for r in result:
            animes_Ids.extend(r)
    return animes_Ids

def anime_id(url):
    animes_Ids=set()
    response=requests.get(url)
    soup=BeautifulSoup(response.content,"lxml")
    for anime in soup.find_all("a",{"href":True}):
        if "/anime/" in anime["href"]:
            if anime_id:=re.search(r"^.+\/(\d+)\/.+$",anime["href"]):
                animes_Ids.add(anime_id.group(1)) 
    return animes_Ids


if __name__ == "__main__":
    main()
