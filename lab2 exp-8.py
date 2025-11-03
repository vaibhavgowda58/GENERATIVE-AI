from langchain_openai import OpenAI

#temperature indicates the randomness in the response. Between 0 to 1. Its 0 when the 
#response is determininstic and 1 when the response is more creative
#default openAI model is text-danvinci-003

llm  = OpenAI(temperature = 0.9)


prompt = "Suggest a good name for a company that produces socks"

print(llm(prompt))

#get a deterministic response with temp = 0

#generate 5 creative responses using the prompt repeatedly

responses = llm.generate([prompt]*5)

for name in responses.generations:
    print(name[0].text)