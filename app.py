import streamlit as st
import pickle
import requests

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/157336?api_key=b58cd0785be9aa5d85c7206d31a0f4e8&append_to_response=images".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data["poster_path"]
    full_path = "https://image.tmdb/org/t/p/w500/" + poster_path
    return full_path

movies = pickle.load(open("movie_list.pkl", "rb"))
similarity = pickle.load(open("similarity.pkl", "rb"))
movies_list = movies["title"].values

st.header("Movie Recommendation System")

# Create a dropdown to select a movie
selected_movie = st.selectbox("Select a movie:", movies_list)

import streamlit.components.v1 as components

def recommend(movie):
    index = movies[movies["title"]==movie].index[0]
    distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector:vector[1])
    recommended_movies = []
    recommended_poster = []
    for i in distance[0:6]:
        movie_id = movies.iloc[i[0]].id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_poster.append(fetch_poster(movie_id))
    return recommended_movies, recommended_poster


if st.button("Show Recommendations"):
    movie_name, movie_poster = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(movie_name[0])
        st.image(movie_poster[0])
    with col2:
        st.text(movie_name[2])
        st.image(movie_poster[2])
    with col3:
        st.text(movie_name[3])
        st.image(movie_poster[3])
    with col4:
        st.text(movie_name[4])
        st.image(movie_poster[4])
    with col5:
        st.text(movie_name[5])
        st.image(movie_poster[5])