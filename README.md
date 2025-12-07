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

## Demo

![Demo](images/demo.png)

---

## Installation

1. **Clone the repository:**

```bash
git clone https://github.com/yourusername/movie-recommender.git
cd movie-recommender

---

## Create a virtual environment (optional but recommended):

python -m venv venv
venv\Scripts\activate       # On Windows
source venv/bin/activate   # On Mac/Linux
---

## Install dependencies:

pip install -r requirements.txt

---

## Run

streamlit run app.py
```
