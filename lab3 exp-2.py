import numpy as np
from openai import OpenAI
client = OpenAI()
texts = ["I love reading", "I am angry", "I play tennis", "I am taller"]
response = client.embeddings.create(
    model = "text-embedding-ada-002",
    input = texts
    )
for i in range(len(texts)-1):
    embd1 = response.data[i].embedding
    for j in range(i+1,len(texts)):
        embd2 = response.data[j].embedding
        sim_score = np.dot(embd1, embd2) * 100
        print("Similarity between texts {0} and {1} is {2}%".format( texts[i], texts[j], sim_score)) 
