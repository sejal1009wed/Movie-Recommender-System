import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    response=requests.get("https://api.themoviedb.org/3/movie/{}?api_key=1fd2e6917058cb08b71b43b47a3adc8f".format(movie_id))
    data=response.json()
    return "https://image.tmdb.org/t/p/w500/" +data['poster_path'];
    


movies_dict=pickle.load(open('movies.pkl','rb'))
movies=pd.DataFrame(movies_dict)
similarity=pickle.load(open('similarity.pkl','rb'))

recommended_movies=[]
recommended_movies_posters=[]
def recommend(movie):
    movie_index=movies[movies['title']==movie].index[0]
    distances=similarity[movie_index]
    movies_list=sorted(enumerate(distances),reverse=True,key=lambda x:x[1])[1:6]
    for i in movies_list:
        index=i[0]
        movie_id=movies.iloc[index].movie_id
        movie_titles=movies.iloc[index].title
        recommended_movies.append(movie_titles)
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_posters;

st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    "How would you like to be contacted?",
    (movies['title'].values)
)

if st.button("Recommend"):
    names, posters=recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.header(names[0])
        st.image(posters[0])
    with col2:
        st.header(names[1])
        st.image(posters[1])
    with col3:
        st.header(names[2])
        st.image(posters[2])
    with col4:
        st.header(names[3])
        st.image(posters[3])
    with col5:
        st.header(names[4])
        st.image(posters[4])
