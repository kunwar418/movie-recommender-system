from fastapi import FastAPI
from pydantic import BaseModel
import pickle

# Load model and data
movies = pickle.load(open('movie_list.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Initialize FastAPI app
app = FastAPI()

# Input schema
class MovieInput(BaseModel):
    title: str

# Recommender logic
def recommend(movie: str):
    index = movies[movies['title'] == movie].index[0]
    distances = similarity[index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    return [movies.iloc[i[0]].title for i in movie_list]

# Recommend endpoint
@app.post("/recommend")
def recommend_movies(data: MovieInput):
    recommendations = recommend(data.title)
    return {"recommendations": recommendations}
