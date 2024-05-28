#from langchain_core.prompts import PromptTemplate
from langchain_community.llms import HuggingFaceEndpoint
import streamlit as st

user_prompt = st.text_input("Input here", placeholder = "Ask me!")

template = f"Share your response based on {user_prompt} as a python code. Share only python code, nothing else."

#prompt = PromptTemplate.from_template(template)

repo_id = "mistralai/Mixtral-8x7B-Instruct-v0.1"


def HuggingFacefunction(query):
    HUGGINGFACEHUB_API_TOKEN = str("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")
    
    #new_prompt= str(system_prompt)+ str("\n\n\n user query:")+ str(user_prompt)

 # Groq model set up with llama2-70b model
    llm = HuggingFaceEndpoint(repo_id = repo_id,
                          temperature = 0.5,
                          max_new_tokens=512,
                          top_k=10,
                          top_p=0.95,
                          huggingfacehub_api_token = HUGGINGFACEHUB_API_TOKEN)
   # llm_chain = prompt | llm
    response = llm.invoke(query)
  
  
    return response
if user_prompt:
    response=HuggingFacefunction(template)
    st.write(response)
