from openai import OpenAI
client = OpenAI()
instruction = """EXPLAIN THE PYTHON CODE GIVEN BELOW
number = int(input("Enter a number:"))
primeFlag = True
for i in range(2, number):
    if number % i == 0:
        primeFlag = False
        break
if primeFlag == True:
    print(number, " is prime.")
else:
    print(number, " is not prime.")"""
response = client.chat.completions.create(
  model="gpt-3.5-turbo",
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
