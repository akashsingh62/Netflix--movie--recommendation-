# Movie Recommendation System

A Flask-powered web app to recommend movies similar to a given title, complete with poster images and a focus on recent releases. This project leverages machine learning (using scikit-learn and pandas), TMDB API, and modern Python best practices.

## Features

- **Content-Based Recommendations:** Finds similar movies using vectorized metadata (`overview`, `genres`, etc.) and cosine similarity.
- **Poster Retrieval:** Fetches movie posters via TMDB API, falling back to a placeholder when unavailable.
- **Modern UX:** Easy-to-use single-page interface for quick recommendations.
- **Recent Movie Preference:** Prioritizes newer movies (2010 and above) in recommendations.
- **Robust Error Handling:** Gracefully handles missing data, API errors, and edge cases.

## Demo

![Movie Recommendation Screenshot](https://via.placeholder.com/800x400?text=Demo+Screenshot)

## Getting Started

### Prerequisites

- Python 3.8+
- `pip`
- TMDB API Key ([Get yours here](https://www.themoviedb.org/documentation/api))

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/movie-recommendation-system.git
   cd movie-recommendation-system
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Download or prepare your `movies.csv` dataset:**
   - The CSV should have at least the columns: `title`, `overview`, `genres`, and ideally `year`.

4. **(Optional) Generate or update the similarity matrix:**
   ```bash
   python generate_similarity.py
   ```
   This will create `similarity.pkl` and update your `movies.csv`.

5. **Set your TMDB API Key:**
   - Update the `TMDB_API_KEY` variable in `app.py` with your API key.

6. **Run the app:**
   ```bash
   python app.py
   ```
   By default, the app runs on [http://127.0.0.1:5000](http://127.0.0.1:5000)

### File Structure

```
.
├── app.py                  # Main Flask application
├── generate_similarity.py  # Script to generate similarity.pkl
├── movies.csv              # Movie dataset (input/output)
├── similarity.pkl          # Cosine similarity matrix (auto-generated)
├── templates/
│   └── index.html          # Main HTML template
├── requirements.txt        # Python dependencies
└── README.md
```

## Usage

- Enter a movie name on the homepage and submit to get 5 similar movie recommendations.
- Each recommendation includes the title and poster.
- If the movie is not found, a "Not Found" placeholder is displayed.

## Customizing

- **Dataset:** You can use any CSV with at least `title`, `overview`, and `genres`.
- **Recommendation Logic:** Tweak `recommend()` in `app.py` to change how recommendations are ranked or filtered.
- **UI:** Modify `templates/index.html` for a custom look.

## API Key Security

**Note:** Never expose your TMDB API key in a public repository. Consider using environment variables or a `.env` file for production deployments.

## Contributing

Contributions are welcome! Please open issues or pull requests for enhancements, bug fixes, or new features.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

- [TMDB API](https://www.themoviedb.org/documentation/api)
- [scikit-learn](https://scikit-learn.org/)
- [pandas](https://pandas.pydata.org/)
- Inspiration from various open-source movie recommender tutorials

---

**Happy coding and movie discovering!**