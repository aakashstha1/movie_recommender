import streamlit as st
import pickle
import requests
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("TMDB_API_KEY")

if not API_KEY:
    raise ValueError("TMDB_API_KEY not found")
# ------------------------------
# Load movie data and similarity matrix
# ------------------------------
movies = pickle.load(open('movies_list.pkl','rb'))  # DataFrame containing movie info
similarity = pickle.load(open('similarity.pkl','rb'))  # Precomputed similarity matrix

# Extract movie titles for the dropdown menu
movies_list = movies['title'].values

# ------------------------------
# Streamlit App Header
# ------------------------------
st.header("🎬 Movie Recommender System")

# Dropdown to select a movie
select_value = st.selectbox("Select Movie", movies_list)

# ------------------------------
# Function to fetch movie poster from TMDB API
# ------------------------------
def fetch_poster(movie_id):
    # TMDB API endpoint to get movie details
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US"
    
    # Send GET request to API
    data = requests.get(url)
    data = data.json()  # Convert response to JSON
    
    # Extract poster path and construct full URL
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500" + poster_path
    return full_path

# ------------------------------
# Function to recommend movies based on similarity
# ------------------------------
def recommend(movie):
    # Get the index of the selected movie in the DataFrame
    index = movies[movies['title'] == movie].index[0]
    
    # Get similarity scores for the selected movie and sort in descending order
    distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector: vector[1])
    
    recommend_movie = []
    recommend_poster = []

    # Get top 5 similar movies (skip the first one, which is the selected movie itself)
    for i in distance[1:6]:
        movie_id = movies.iloc[i[0]].id  # Movie ID to fetch poster
        recommend_movie.append(movies.iloc[i[0]].title)  # Add movie title to list
        recommend_poster.append(fetch_poster(movie_id))  # Add poster URL to list

    return recommend_movie, recommend_poster

# ------------------------------
# Display recommendations when button is clicked
# ------------------------------
if st.button("Recommend"):
    movie_name, movie_poster = recommend(select_value)
    
    # Create 5 columns to display recommended movies side by side
    col1, col2, col3, col4, col5 = st.columns(5)
    
    # Display movie title and poster in each column
    with col1:
        st.text(movie_name[0])
        st.image(movie_poster[0])
    with col2:
        st.text(movie_name[1])
        st.image(movie_poster[1])
    with col3:
        st.text(movie_name[2])
        st.image(movie_poster[2])
    with col4:
        st.text(movie_name[3])
        st.image(movie_poster[3])
    with col5:
        st.text(movie_name[4])
        st.image(movie_poster[4])
