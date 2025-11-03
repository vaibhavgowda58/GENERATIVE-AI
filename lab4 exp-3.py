import base64
from openai import OpenAI
client = OpenAI()

def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

# Path to your image
image_path = "/Users/vaibhavgowda/Downloads/supercar-8589586_1280.png"

# Getting the base64 string
base64_image = encode_image(image_path)

response = client.chat.completions.create(
  model="gpt-4o-mini",
    messages=[
      {
          "role": "user",
          "content": [
              {"type": "text", "text": "What’s in this image?"},
              {
                  "type": "image_url",
                  "image_url": { 
                      "url":f"data:image/jpeg;base64, {base64_image}"
                     
                  }

              },
          ],
      }
  ],
 
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
print(response)
print(response.choices[0].message.content) 