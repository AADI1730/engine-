from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("all-MiniLM-L6-v2")

documents = ["This is a search engine", "We are building an AI-powered search engine"]
doc_embeddings = model.encode(documents)

query = "How to create a search engine?"
query_embedding = model.encode(query)

scores = util.pytorch_cos_sim(query_embedding, doc_embeddings)
print(scores)
