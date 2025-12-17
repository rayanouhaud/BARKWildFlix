import requests

def getAffiche(movie_title):
    api_key = "94487201f2075a6b8c1e7e15a02fe164"
    url = f"https://api.themoviedb.org/3/search/movie?api_key={api_key}&query={movie_title}"
    response = requests.get(url).json()
    poster_path = response['results'][0]['poster_path']
    poster_url = f"https://image.tmdb.org/t/p/w500{poster_path}"
    return poster_url