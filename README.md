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

Absolutely! Here’s the ready-to-copy-paste Installation & Run section for your README:

## Installation

1. **Clone the repository:**

```bash
git clone https://github.com/aakashstha1/movie_recommender.git
cd movie_recommender


Create a virtual environment (optional but recommended):

python -m venv venv


Activate the virtual environment:

Windows:

venv\Scripts\activate


Mac/Linux:

source venv/bin/activate


Install dependencies:

pip install -r requirements.txt


Run the app:

streamlit run app.py