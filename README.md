CLOTHING SIMILARITY SEARCH :
	This project implements a clothing item similarity search made for Men's cloths like( shirt, tshirt, jeans, kurta, jacket, sweatshirt, hoodie) system using natural language processing techniques. Given an input text describing a clothing item, the system retrieves the top-N most similar items from a database of clothing item descriptions.(where we have taken the N value to be 20 for example).

PROJECT STRUCTURE :
The project is structured as follows:

	1) Data/: Directory containing the dataset of clothing item descriptions(Clothing_Dataset_Myntra).
	2) Preprocessing: Used Browse AI Web Scraping tool for data collection and preprocessing.
	3) Similarity: Python script for computing similarity and ranking results.
	4) Main: Python script for deploying the similarity search function.
	5) Requirements: File listing the required Python packages.

PREREQUISITES :

	1) Python 3.x
	2) Web scraping tools BrowseAI (BeautifulSoup) - Install using pip.
	3) Required Python packages - Install using pip: pip install -r requirements.txt.

USAGE :
1) Data Collection and Preprocessing:

Use web scraping tools to gather a dataset of clothing item descriptions and save it in the data/ directory.
Run the preprocessing.py script to preprocess the text data and clean it. Adjust the script as needed for your specific dataset.

2) Similarity Computation:

Implement a method in the similarity.py script to extract useful features from the text descriptions and compute the similarity between the input text and the texts in the database.
The similarity.py script should include a function that accepts an input text and returns a ranked list of similar items.
3) Deployment:

Deploy the similarity search function using a serverless platform such as Google Cloud Functions or Google Cloud Run.
Update the main.py script with the necessary code to trigger the similarity search function based on incoming requests.
4) Testing:

Send HTTP requests to the deployed function with an input text to retrieve the top-N most similar clothing items.
Receive the URLs of the similar items as the response from the deployed function.

CREDITS :
BrowseAI - Web Scraping Application.
scikit-learn - Machine learning library for cosine similarity computation.
Google Cloud Functions - Serverless computing platform.
Google Cloud Run - Fully managed serverless container platform.
