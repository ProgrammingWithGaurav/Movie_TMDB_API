from fastapi import FastAPI
import requests
from typing import List
from models.Movie import Movie
from utils import get_movie_url, get_search_url


app = FastAPI()

# fetch movie 
@app.get("/movies/{category}", response_model=List[Movie])
async def fetch_movies(category: str):
    print(category)
    category_url = get_movie_url(category)  # Define this function
    url = f"https://api.themoviedb.org/3{category_url}"
    print(url)
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        movies = [Movie(**movie) for movie in data['results']]
        return movies
    else:
        raise Exception('Failed to load movies')

# search movie
@app.get("/search/{query}", response_model=List[Movie])
async def search_movie(query: str):
    url = get_search_url(query)  
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        movies = [Movie(**movie) for movie in data['results']]
        return movies
    else:
        raise Exception('Failed to load movies')