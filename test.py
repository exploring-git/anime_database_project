import requests 
import concurrent.futures
import pprint
import time
def get_anime_data(anime_id):
    id=[]
    ids=[]
    genres=[]
    counter=0
    for i in range(len(anime_id)):
        id.append(anime_id[i])
        counter+=1
        if counter==2 :
            counter=0
            genres.append(anime_data(id))
            id=[]
            time.sleep(1.3)
        elif counter!=2 and i == len(anime_id)-1:
            counter=0
            genres.append(anime_data(id))
            id=[]
    return genres

    



def anime_data(anime_id):
    genre=[]
    episode=[]
    anime_title=[]
    anime_popularity=[]
    anime_suit_age=[]
    for index,i in enumerate(anime_id):
        url = f"https://api.jikan.moe/v4/anime/{i}"
        response = requests.get(url)
        data = response.json()["data"]
        try:
            genres= data["genres"]
            episodes=data["episodes"]
            titles=data["title_synonyms"]
            popularity=data["popularity"]
            age=data["rating"]
        except KeyError:
            print(data)
            genre.append(None)
            episode.append(None)
            anime_title.append(None)
            anime_popularity.append(None)
            anime_suit_age.append(None)
        else:
            gen=[]
            for type in genres:
                gen.append(type["name"])
            genre.append(gen)
            episode.append(episodes)
            if len(titles)>=1:
                anime_title.append(titles[0])
            else:
                if data["title_english"] != None:
                    anime_title.append(data["title_english"])
                else:
                    anime_title.append("undefined")
            anime_popularity.append(popularity)
            if age != None:
                anime_suit_age.append(age.split("-",1)[1].strip())
            else:
                anime_suit_age.append("undefined")
            print("___________________________________________")
            print(f"ANIME ID : {i} ,\n GENRES : {gen} ,\n EPISODES : {episode[index]} , \n TITLES : {anime_title[index]} , \n POPULARITY RANK: {anime_popularity[index]} , \n RECOMMENDED AGE : {anime_suit_age[index]}")
            print("___________________________________________")

    return(data)
  
ids=["55426","25","45852","51535"]
dt=get_anime_data(ids)

#pprint.pprint(dt)