# Simple-UHG-Rag-Chat-Demo
# Example RAG chat for UHG Documents 

1️⃣ Ingest UHG documents → Chunk & Embed
2️⃣ Store embeddings in MongoDB Atlas
3️⃣ Retrieve relevant chunks using $vectorSearch
4️⃣ Send retrieved data to LLM for response generation
5️⃣ Return final answer to the user

🛠️ Implementation Details
1️⃣ Convert UHG Documents into Chunks & Create Embeddings
Break long documents into smaller chunks (e.g., 512-1024 tokens)
Generate vector embeddings for each chunk using OpenAI, Hugging Face, or Unsloth:
```
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")
documents = ["UHG policy document section 1...", "UHG claim process details..."]
embeddings = model.encode(documents)
```

Store these embeddings in MongoDB Atlas.
2️⃣ Store in MongoDB Atlas Vector Search
Define a schema like:

json
Copy
Edit
{
    "_id": ObjectId("..."),
    "text": "UHG document chunk...",
    "embedding": [0.12, -0.03, 0.75, ...],
    "source": "claims_policy.pdf",
    "metadata": {
        "section": "Claims Processing",
        "date": "2024-02-18"
    }
}
Index the Vector Field (embedding)
javascript
Copy
Edit
db.uhg_docs.createIndex(
    { "embedding": "vector" },
    { "index": "vector_index", "numDimensions": 768, "similarity": "cosine" }
);
3️⃣ Retrieve Relevant Chunks using $vectorSearch
When a user asks a question:

python
Copy
Edit
query_embedding = model.encode(["How do I submit a claim?"])
pipeline = [
    {
        "$vectorSearch": {
            "queryVector": query_embedding.tolist(),
            "path": "embedding",
            "numCandidates": 50,
            "limit": 5,
            "index": "vector_index"
        }
    }
]
retrieved_docs = list(db.uhg_docs.aggregate(pipeline))
4️⃣ Send Retrieved Chunks to LLM for Context-aware Answer
python
Copy
Edit
import openai

context = "\n".join([doc["text"] for doc in retrieved_docs])

prompt = f"Answer based on the UHG documents:\n{context}\nUser: How do I submit a claim?"
response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[{"role": "user", "content": prompt}]
)

print(response["choices"][0]["message"]["content"])

