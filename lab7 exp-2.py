#Sequential chain with single input and single output variable
from langchain_openai import OpenAI
from langchain import PromptTemplate

from langchain.chains import LLMChain
from langchain.chains import SequentialChain

llm = OpenAI(temperature = 0.5)
prompt1 = PromptTemplate(
              input_variables = ['name'], 
              template = "Tell me when the car model {name} was launched"
              )
chain1 = LLMChain(llm = llm, prompt = prompt1, verbose = True, output_key = 'year')

prompt2 = PromptTemplate(
          input_variables = ["year"], 
          template = "Tell me the top 5 car model in the year {year}"
          )
chain2 = LLMChain(llm = llm, prompt =  prompt2, verbose = True, output_key = 'top 5')

final_chain = SequentialChain(
       chains = [chain1,chain2], 
       input_variables = ['name'], 
       output_variables = ['year', 'top 5'], verbose = True)

response = final_chain({"name": "Ford"})
print(response) 