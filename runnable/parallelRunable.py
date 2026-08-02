from dotenv import load_dotenv
load_dotenv()


from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnableLambda

#1. Prompt template
prompt=ChatPromptTemplate.from_template(

    "Explain {topic} in simple words"
)


#2 model load

model=ChatMistralAI(model="mistral-small-2503")


#3 output parser

parser= StrOutputParser()

#Two different prompts

short_prompt=ChatPromptTemplate.from_template(
    "Exlpain {topic} in 1-2 lines"
)


detailed_prompt=ChatPromptTemplate.from_template(
    "Explain {topic} in detail"
) 
#input

topic="Machine Learning"

chain= RunnableParallel({
   "short":RunnableLambda(lambda x:x ['short'])|short_prompt | model |parser,
     "detailed":RunnableLambda(lambda x: x ['detailed'])|detailed_prompt | model |parser
})

result=chain.invoke({
    "short":{"topic": "Machince learning"},
    "detailed":{"topic":"Deep dearning"}
    } )

print(result['short'])
print(result['detailed'])