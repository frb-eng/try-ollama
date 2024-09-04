from langchain_community.chat_models import ChatOllama
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

prompt = ChatPromptTemplate.from_template("Why is the sky blue?")

llm = ChatOllama(model='mistral')

chain = (
            prompt
            | llm
            | StrOutputParser()
        )

chain.invoke({})