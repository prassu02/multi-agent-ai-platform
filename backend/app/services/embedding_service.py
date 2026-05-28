from sentence_transformers import SentenceTransformer

model = SentenceTransformer(
"all-MiniLM-L6-v2",
device="cpu"
)

def create_embeddings(chunks):
embeddings = model.encode(
chunks,
convert_to_numpy=True
)
return embeddings
