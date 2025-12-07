# 🎬 Movie Recommender System

A simple web app built with **Streamlit** that recommends movies based on a selected movie. It fetches movie posters using the **TMDB API** and displays the top 5 similar movies.

---

## Features

- Select a movie from a dropdown list
- Get top 5 recommended movies
- Display movie posters alongside titles
- Uses a precomputed similarity matrix for recommendations
- Built with Python, Streamlit, and TMDB API

---

## Requirements

- Python
- Streamlit
- Requests
- Pandas
- Numpy
- TMDB API Key

---

## To create TMDB API key visit and login:

     https://www.themoviedb.org/

---

## Demo

![Demo](images/demo.png)

---

## Installation

1. **Clone the repository:**

````bash
git clone https://github.com/aakashstha1/movie_recommender.git
cd movie-recommender

---

2. **Create a virtual environment:**

```bash
python -m venv venv
venv\Scripts\activate       # On Windows
source venv/bin/activate   # On Mac/Linux

---

3. **Install dependencies:**

```bash
pip install -r requirements.txt

---

4. **Create file:**

 Create .env file in your folder and add

 ```bash
 TMDB_API_KEY=<your-api-key>

---

5. **Run:**

```bash
streamlit run app.py

````
