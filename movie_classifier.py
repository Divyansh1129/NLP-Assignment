import requests
import pandas as pd

movie_url = "https://api.themoviedb.org/3/movie/top_rated"
genre_url = "https://api.themoviedb.org/3/genre/movie/list"

api_key="8265bd1679663a7ea12ac168da84d2e8"

genre_params={
    "api_key":api_key,
    "language":"en-US"
}

genre_response=requests.get(genre_url,params=genre_params)


print(genre_response.status_code)
