import openai 

def ask_llm_with_rag(query):
    # Retrieve context from MongoDB Atlas Vector Search
    context_results = query_vector_search(query, num_results=3)
    context = "\n".join([res["text"] for res in context_results])
    
    # Generate LLM response
    prompt = f"Answer this based on the provided context:\n{context}\nUser Query: {query}"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    
    return response["choices"][0]["message"]["content"]

# Usage
query = "What are the side effects of Keppra?"
response = ask_llm_with_rag(query)
print(response)
