from openai import OpenAI
client =OpenAI()
instruction = """ Classify the companies given below :
           Microsoft Corporation, Roche Holding AG, Apple Inc, "Amazon.com, Inc,Pfizer Inc, JPMorgan Chase & Co.,Johnson & Johnson, Bank of America Corporation, Industrial and Commercial Bank of China
"""

response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
   
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": instruction
        }
      ]
    },
  
  ],
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

#print(response)
print(response.choices[0].message.content)