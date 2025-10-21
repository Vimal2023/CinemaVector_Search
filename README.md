# CinemaVector Search

## Overview
CinemaVector Search is a Python-based project that implements a **semantic search engine** for movies using **MongoDB Atlas Vector Search** and **Hugging Face embeddings** (all-MiniLM-L6-v2 model). It allows users to find movies by entering natural language queries, such as "imaginary characters from outer space at war," by matching the semantic meaning of movie plots rather than relying on keyword-based search.

## Features
- **Semantic Search**: Uses vector embeddings to find movies based on plot similarity.
- **MongoDB Atlas**: Stores movie data and embeddings, leveraging the free M0 tier.
- **Hugging Face Model**: Generates 384-dimensional embeddings for movie plots using the `all-MiniLM-L6-v2` model.
- **Natural Language Queries**: Supports intuitive queries for better user experience.
- **Scalable Design**: Demonstrates embedding generation and vector search for a sample dataset of 20,000+ movies.

## Prerequisites
- Python 3.x
- MongoDB Atlas account (free tier M0 cluster)
- Hugging Face account and API token (free tier)
- Required Python packages: `pymongo`, `requests`

## Setup Instructions
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/cinemavector-search.git
   cd cinemavector-search
   ```

2. **Install Dependencies**:
   ```bash
   pip install pymongo requests
   ```

3. **Set Up MongoDB Atlas**:
   - Create a MongoDB Atlas account and a free M0 cluster.
   - Load the `sample_mflix` dataset (movies collection) in MongoDB Atlas.
   - Copy your MongoDB URI (`mongodb+srv://<username>:<password>@cluster0.mongodb.net`).

4. **Configure Hugging Face API**:
   - Create a Hugging Face account and generate an API token (read permission).
   - Store the token securely (preferably in an environment variable).

5. **Environment Variables**:
   Create a `.env` file in the project root:
   ```env
   MONGODB_URI=mongodb+srv://<username>:<password>@cluster0.mongodb.net
   HUGGINGFACE_API_TOKEN=<your-huggingface-token>
   ```

6. **Run the Project**:
   - Update `movie_rex.py` with your MongoDB URI and Hugging Face token (or use environment variables).
   - Run the script to generate embeddings and perform searches:
     ```bash
     python movie_rex.py
     ```

## Project Structure
- `movie_rex.py`: Main script for connecting to MongoDB, generating embeddings, creating a vector search index, and performing semantic searches.
- `.env`: Environment file for storing MongoDB URI and Hugging Face API token (not committed to Git).

## How It Works
1. **Data Loading**: Connects to MongoDB Atlas and loads the `sample_mflix.movies` collection (20,000+ movies).
2. **Embedding Generation**: Uses Hugging Face's `all-MiniLM-L6-v2` model to create 384-dimensional embeddings for movie plots (stored in `plot_embedding_hf` field).
3. **Vector Search Index**: Creates a MongoDB Atlas vector search index with `dotProduct` similarity and `knnVector` type.
4. **Semantic Search**: Executes queries (e.g., "imaginary characters from outer space at war") using MongoDB’s aggregation pipeline to find semantically similar movies.
5. **Limitations**: Due to Hugging Face API rate limits, embeddings are generated for only 50 documents in this demo. For full dataset processing, a paid endpoint is recommended.

## Example Query
**Query**: "imaginary characters from outer space at war"  
**Output**: Returns movies with plots related to war (limited by 50-document embedding set). For better results, generate embeddings for the entire dataset.

## Future Improvements
- Use a paid Hugging Face inference endpoint for full dataset embedding generation.
- Implement caching for faster query processing.
- Add a web interface (e.g., using Gradio) for user-friendly interaction.
- Experiment with other embedding models (e.g., OpenAI) for comparison.

## Acknowledgments
- Built with a grant from **MongoDB** for leveraging **Atlas Vector Search**.
- Uses **Hugging Face** for free embedding generation.
- Inspired by the need for intuitive, meaning-based movie search systems.

## License
This project is licensed under the MIT License.
