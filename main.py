import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8b4e833aad5bd62dd668d92ea23af265&language=en-US'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/"+data['poster_path']

#function
def recommend(movie_name):
    movie_index = movies[movies['title'] == movie_name].index[0]
    distance = similarity[movie_index]
    movie_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    recommended_posters = []
    for i in movie_list:
        movie_id = i[0]
        recommended_movies.append(movies.iloc[i[0]].title)
        # fetch poster from API
        #recommended_posters.append(fetch_poster(movie_id))
    return recommended_movies

movies_dict = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl','rb'))



st.title('Movie Recommender System')
selected_movie_name = st.selectbox(
    'Specify the movie name ',movies['title'].values)

st.write('You selected:', selected_movie_name)

#add a recommend button
if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)



