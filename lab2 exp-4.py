from openai import OpenAI
client = OpenAI()

response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {
      "role": "system",
      "content": [
        {
          "type": "text",
          "text": "You are a cake baker"
        }
      ]
    },
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "Get me a recipe to bake a cake"
        }
      ]
    },
  
  ],
  
  n=3,
  max_tokens=300,
  
)

#print(response)

for i in range(3):
    print("Recipe : ", i+1)
    print("")
    print(response.choices[i].message.content)