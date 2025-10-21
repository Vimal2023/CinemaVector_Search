import pymongo
import os
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer

# -------------------------------
# Load environment variables
# -------------------------------
load_dotenv()
mongo_uri = os.getenv("MONGO_URI")
if not mongo_uri:
    raise ValueError("MONGO_URI not found in .env file")

# -------------------------------
# Connect to MongoDB
# -------------------------------
client = pymongo.MongoClient(mongo_uri)
db = client.sample_mflix
collection = db.movies  # Change if your collection name is different

# -------------------------------
# Load SentenceTransformer model locally
# -------------------------------
print("Loading embedding model...")
model = SentenceTransformer('all-MiniLM-L6-v2')
print("Model loaded!")

# -------------------------------
# Generate embedding function
# -------------------------------
def generate_embedding(text: str) -> list[float]:
    return model.encode(text).tolist()

# -------------------------------
# Step 1: Precompute embeddings for all plots
# -------------------------------
print("Generating embeddings for movie plots...")
for doc in collection.find({'plot': {"$exists": True}}).limit(50):
    if 'plot_embedding_hf' not in doc:
        doc['plot_embedding_hf'] = generate_embedding(doc['plot'])
        collection.replace_one({'_id': doc['_id']}, doc)
print("All embeddings generated and stored!")

# -------------------------------
# Step 2: Ensure vector index exists in MongoDB Atlas
# -------------------------------
# NOTE: This is usually done via Atlas UI or using Atlas CLI
# The index should be of type knnVector, dimension=384, on 'plot_embedding_hf'

# -------------------------------
# Step 3: Semantic search query
# -------------------------------
query = "imaginary characters from outer space at war"
query_vector = generate_embedding(query)

print("Performing semantic search...")
results = collection.aggregate([
    {
        "$vectorSearch": {
            "queryVector": query_vector,
            "path": "plot_embedding_hf",
            "numCandidates": 100,
            "limit": 4,
            "index": "PlotSemanticSearch",  # Must match the Atlas index name
        }
    }
])

# -------------------------------
# Step 4: Display results
# -------------------------------
for doc in results:
    print(f"Movie Name: {doc.get('title', 'N/A')}")
    print(f"Movie Plot: {doc.get('plot', 'N/A')}\n")
