from langchain_ollama import ChatOllama

llm = ChatOllama(model='llama3.1')

print(llm.invoke("Why is the sky blue?"))
