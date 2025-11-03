from openai import OpenAI
client = OpenAI()
response = client.embeddings.create(
    model = "text-embedding-ada-002",
    input = "cat"
 )
#print(response)
print(response.data[0].embedding) 