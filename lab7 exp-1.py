from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate

from langchain.chains import LLMChain
from langchain.chains import SimpleSequentialChain

llm = OpenAI(temperature = 0.9)

template = "Suggest a good name for a company that makes {product}"
prompt1 = PromptTemplate.from_template(template)
chain1 = LLMChain(llm=llm, prompt = prompt1)


template = "Generate a catchy phrase for this company {company}"
prompt2 = PromptTemplate.from_template(template)
chain2 = LLMChain(llm=llm, prompt = prompt2)


final_chain = SimpleSequentialChain(
    
    chains = [chain1,chain2], 
    verbose = True)

response = final_chain.run("Noodles")
          
print(response) 