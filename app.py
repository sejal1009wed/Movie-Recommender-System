import streamlit as st
import pickle
import pandas as pd

similarity = pickle.load(open('similarity.pkl','rb'))

def recommend(movie):
    movie_index = movies[movies['Series_Title']==movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),reverse=True,key = lambda x:x[1])[1:6]
    
    recommended_movies = []
    recommended_movies_poster=[]
    for i in movies_list:
        #Fetch poster
    
        recommended_movies.append(movies.iloc[i[0]].Series_Title)
        recommended_movies_poster.append(movies.iloc[i[0]].Poster_Link)
    return recommended_movies,recommended_movies_poster

movies_dict = pickle.load(open('movies.pkl','rb'))
movies = pd.DataFrame(movies_dict)

st.title('Movie Recommender System')

selected_movie = st.selectbox('Select the movie',
                      movies['Series_Title'].values)


if st.button('Recommend'):
    names,posters = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.beta_columns(5)
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
