import numpy as np
from openai import OpenAI
client = OpenAI()

doc1 = "This study explores groundbreaking advancements in renewable energy technologies, focusing on solar and wind power's efficiency improvements. By analyzing recent developments, we highlight the potential for these technologies to significantly reduce global dependency on fossil fuels, thereby mitigating climate change impacts."
doc2 = "Artificial Intelligence (AI) holds transformative potential for environmental protection, offering tools for better predicting climate change patterns and optimizing resource use. This paper examines AI applications in monitoring environmental degradation and managing natural resources more efficiently, presenting a case for integrating AI strategies into conservation efforts"
doc3 = "Marine biodiversity faces significant threats from climate change, with rising temperatures and acidification leading to coral bleaching and loss of habitat. This research analyzes the consequences of these changes on marine ecosystems and emphasizes the urgency of adopting conservation strategies to protect marine life"
plag_text = "Recent advancements in solar and wind energy technologies have shown promising potential to lessen the world's reliance on non-renewable energy sources, thus playing a crucial role in combating climate change. Furthermore, the utilization of Artificial Intelligence offers unparalleled opportunities in the realm of environmental conservation, aiding in the accurate prediction of climatic trends and the efficient management of ecological resources. Additionally, the adverse effects of climate change on ocean life, particularly through the phenomenon of coral bleaching, underscore the need for immediate action to safeguard marine ecosystems"

docs = [plag_text, doc1,doc2,doc3] 

response = client.embeddings.create(
    model = "text-embedding-ada-002",
    input = docs
     )
plag_embd = response.data[0].embedding

for i in range(1, len(docs)):
    embd = response.data[i].embedding
    sim_score = np.dot(plag_embd,embd) * 100
    print("Similarity between plag text and doc{0} is {1}%".format( i, sim_score))  