import csv
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity   #Importing cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer  # Importing TF-IDF 

# Read data from CSV file
def read_csv_file(file_path, text_column, url_column, rating_column):
    texts = []
    urls = []
    ratings = []
    with open(file_path, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            texts.append(row[text_column])
            urls.append(row[url_column])
            ratings.append(float(row[rating_column]))
    return texts, urls, ratings

# Extract features from text using TF-IDF vectorization
def extract_features(texts):
    vectorizer = TfidfVectorizer()
    features = vectorizer.fit_transform(texts)
    return features

# Compute cosine similarity between input text and database texts
def compute_similarity(input_text, database_texts):
    features = extract_features([input_text] + database_texts)
    input_features = features[0]
    database_features = features[1:]
    similarity_scores = cosine_similarity(input_features, database_features)
    return similarity_scores[0]

# Get top N similar items based on cosine similarity scores
def get_top_similar_items(input_text, database_texts, database_ratings, N=20):
    similarity_scores = compute_similarity(input_text, database_texts)
    sorted_indices = np.argsort(similarity_scores)[::-1]
    top_indices = sorted_indices[:N]
    top_ratings = [database_ratings[index] for index in top_indices]
    sorted_top_indices = [x for _, x in sorted(zip(top_ratings, top_indices), reverse=True)]
    return sorted_top_indices


# Compare input text with data in CSV file and print top N similar items
def compare_csv_with_input(csv_file_path, text_column, url_column, rating_column, input_text, N=20):

    # Read the CSV file and store texts, URLs, and ratings
    database_texts, database_urls, database_ratings = read_csv_file(csv_file_path, text_column, url_column, rating_column)
     # Get the top N similar items based on input text
    top_indices = get_top_similar_items(input_text, database_texts, database_ratings, N)
    
    # Access URLs or other relevant information using the indices
    for index in top_indices:
        url = database_urls[index]
        print(url)

# Main Block of Code
csv_file_path = 'Clothing_Dataset_Myntra.csv'
text_column = 'Product_Description'
url_column = 'Product_Link'
rating_column = 'Rating'

# Prompt user for input text
input_text1 = input("Enter the Product Name to Search: ")
input_text = input_text1.lower()


# Compare input text with CSV data and print top similar items
# Calling the function
compare_csv_with_input(csv_file_path, text_column, url_column, rating_column, input_text, N=20)
