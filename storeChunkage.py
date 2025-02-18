from pymongo import MongoClient

# MongoDB Connection
client = MongoClient("mongodb+srv://your_mongodb_uri")
db = client["drug_database"]
collection = db["drug_embeddings"]

# Insert documents
def store_embeddings(text_chunks, embeddings):
    docs = []
    for text, embedding in zip(text_chunks, embeddings):
        docs.append({"text": text, "embedding": embedding.tolist()})
    
    collection.insert_many(docs)
    print(f"{len(docs)} documents stored in MongoDB")

# Usage
store_embeddings(text_chunks, embeddings)
