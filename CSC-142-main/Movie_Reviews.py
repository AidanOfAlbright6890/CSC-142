# Credit for original code goes to vlogize from YouTube(Link: https://www.bing.com/videos/riverview/relatedvideo?q=how+to+find+a+movie%27s+rating+using+Python&&mid=4392F4648A60840B116F4392F4648A60840B116F&FORM=VRDGAR).

class Film:
    
    film = [{"title": "Monsters, Inc.", "imdb": 8.1, "category": "Comedy", "imdb2": "10/10", "imbd3": "1/10"}]
    def find_high_rated_films(films, threshold):
        high_rated_films = []
        for film in films:
            if film['imdb'] > threshold:
                high_rated_films.append(film)
        return high_rated_films

#class reviews:
    films_above_threshold = find_high_rated_films(film, 5.5)
    for film in films_above_threshold:
        print(f"{film['title']}'s overall rating on IMDB is {film['imdb']}, its best rating is {film['imdb2']} and its worst rating is {film['imbd3']}. As for the genre, Monsters Inc. is a {film['category']} film.")