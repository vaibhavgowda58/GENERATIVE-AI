from openai import OpenAI
client = OpenAI()

response = client.images.generate(
    prompt = "water color image of Zurich with color reflections in water",
    size = "1024x1024"
    
    )
#print(response)
print(response.data[0].url)