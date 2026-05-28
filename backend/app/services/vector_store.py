import faiss
import numpy as np

index = faiss.IndexFlatL2(384)

documents = []

def store_embeddings(chunks, embeddings):

    global documents

    vectors = np.array(embeddings).astype("float32")

    index.add(vectors)

    documents.extend(chunks)

def search(query_embedding, top_k=3):

    query_vector = np.array([query_embedding]).astype("float32")

    distances, indices = index.search(query_vector, top_k)

    results = [documents[i] for i in indices[0]]

    return results