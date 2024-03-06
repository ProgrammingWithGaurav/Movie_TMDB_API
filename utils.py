from dotenv import load_dotenv
import os

load_dotenv()  # take environment variables from .env.

API_KEY = os.getenv('API_KEY')

categories = [
    {"title": 'Top Rated', "url": "/movie/top_rated?api_key={API_KEY}&language=en-US".format(API_KEY=API_KEY)},
    {"title": 'Action', "url": "/discover/movie?api_key={API_KEY}&with_genres=28".format(API_KEY=API_KEY)},
    {"title": 'Comedy', "url": "/discover/movie?api_key={API_KEY}&with_genres=35".format(API_KEY=API_KEY)},
    {"title": 'Horror', "url": "/discover/movie?api_key={API_KEY}&with_genres=27".format(API_KEY=API_KEY)},
    {"title": 'Romance', "url": "/discover/movie?api_key={API_KEY}&with_genres=10749".format(API_KEY=API_KEY)},
    {"title": 'Mystery', "url": "/discover/movie?api_key={API_KEY}&with_genres=9648".format(API_KEY=API_KEY)},
    {"title": 'Sci-Fi', "url": "/discover/movie?api_key={API_KEY}&with_genres=878".format(API_KEY=API_KEY)},
    {"title": 'Western', "url": "/discover/movie?api_key={API_KEY}&with_genres=37".format(API_KEY=API_KEY)},
    {"title": 'Animation', "url": "/discover/movie?api_key={API_KEY}&with_genres=16".format(API_KEY=API_KEY)},
    {"title": 'TV Movie', "url": "/discover/movie?api_key={API_KEY}&with_genres=10770".format(API_KEY=API_KEY)},
]

def get_movie_url(title):
    if title:
        for category in categories:
            if category['title'] == title:
                return category['url']
    return ''

def get_search_url(query: str):
    return f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={query}"