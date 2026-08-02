from dotenv import load_dotenv
load_dotenv()


from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


#1. Prompt template
prompt=ChatPromptTemplate.from_template(

    "Explain {topic} in simple words"
)


#2 model load

model=ChatMistralAI(model="mistral-small-2503")


#3 output parser

parser= StrOutputParser()


#step by step manual floew

#format  the prompt
formatted_prompt=prompt.format_messages(topic="Machine learning")

#Call the model manually

response=model.invoke(formatted_prompt)

#parse the output manually
final_output=parser.parse(response.content)

print(final_output)
