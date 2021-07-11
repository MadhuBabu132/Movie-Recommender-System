from urllib import response

import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'.format(movie_id))
    data= response.json()
    return "https://image.tmdb.org/t/p/w500/"+data['poster_path']

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_sorted = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommend_movies = []
    recommend_movies_poster=[]
    for i in movies_sorted:
        movie_id=movies.iloc[i[0]].movie_id
        # fetch poster from API
        recommend_movies.append(movies.iloc[i[0]].title)
        recommend_movies_poster.append(fetch_poster(movie_id))
    return recommend_movies, recommend_movies_poster
similarity=pickle.load(open('similarity.pkl','rb'))
movies_list=pickle.load(open('movies.pkl','rb'))
movies=pd.DataFrame(movies_list)
st.title('Movie Recommender System')

selected_movie_name=st.selectbox(
    'what do you want',
    movies['title'].values)

if st.button('Recommend'):
    names, posters=recommend(selected_movie_name)
    col1, col2, col3, col4, col5=st.beta_columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])

