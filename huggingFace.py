from sentence_transformers import SentenceTransformer
from nltk.tokenize import sent_tokenize

def chunk_text_semantically(text, chunk_size=512):
    sentences = sent_tokenize(text)  # Split into sentences
    chunks, current_chunk = [], ""

    for sentence in sentences:
        if len(current_chunk) + len(sentence) <= chunk_size:
            current_chunk += " " + sentence
        else:
            chunks.append(current_chunk.strip())
            current_chunk = sentence

    if current_chunk:  # Add last chunk if exists
        chunks.append(current_chunk.strip())

    return chunks

# Usage Example
pdf_text = """Keppra (Levetiracetam) is an anticonvulsant medication used primarily for the treatment of epilepsy.
It helps in controlling seizures and is often used as adjunctive therapy in partial-onset seizures, myoclonic seizures, and generalized tonic-clonic seizures.
The mechanism of action involves binding to the synaptic vesicle protein SV2A, stabilizing neuronal activity.
Keppra is typically administered orally or intravenously and is prescribed in doses ranging from 500 mg to 1500 mg twice daily."""
  
text_chunks = chunk_text_semantically(pdf_text)
print(len(text_chunks), "chunks created")
for i, chunk in enumerate(text_chunks):
    print(f"Chunk {i+1}: {chunk}\n")
