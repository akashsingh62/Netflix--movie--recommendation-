import pandas as pd
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

movies = pd.read_csv('movies.csv')


movies['tags'] = movies['overview'].fillna('') + " " + movies['genres'].fillna('')



cv = CountVectorizer(max_features=5000, stop_words='english')
vectors = cv.fit_transform(movies['tags']).toarray()

similarity = cosine_similarity(vectors)
pickle.dump(similarity, open('similarity.pkl', 'wb'))

movies.to_csv('movies.csv', index=False)
