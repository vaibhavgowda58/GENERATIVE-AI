from langchain_openai import OpenAI
from langchain import PromptTemplate

from langchain.chains import LLMChain
from langchain.chains import SequentialChain

llm = OpenAI(temperature = 0.5)
prompt1 = PromptTemplate(
              input_variables = ['company', 'product_name'], 
              template = "Tell me when the {company} launched the product {product_name}?"
              )
chain1 = LLMChain(llm = llm, prompt = prompt1, verbose = True, output_key = 'year')

prompt2 = PromptTemplate(
          input_variables = ["year"], 
          template = "List four similar products launched in the year {year}"
          )
chain2 = LLMChain(llm = llm, prompt =  prompt2, verbose = True, output_key = 'four similar')

final_chain = SequentialChain(
       chains = [chain1,chain2], 
       input_variables = ['company', 'product_name'], 
       output_variables = ['year', 'four similar'], verbose = True)

response = final_chain({"company": "Ford", "product_name":"Eco_sport" })
print(response) 