from dotenv import load_dotenv
load_dotenv()

from langchain_mistralai import ChatMistralAI
from langchain.tools import tool
from rich import print


#1 creating a tool

@tool
def get_text_length(text: str) -> int:
    """Returns the number of character in the given text """

    return len(text)


llm=ChatMistralAI(model="mistral-small-2506")
result=llm.invoke("Returns the number of character in the given text : 'hello how are you ' ")

#Tool binding #step:1 LLM decides tool
llm_with_tool=llm.bind_tools([get_text_length])
result2=llm_with_tool.invoke("Use the get_text_length tool to find the length of: hello how are you ")


"""print(result)
print("\n\n")
print(result2)
print("\n\n\n")"""
#tool caLL

print(result2.tool_calls)

 #step2-4: Execute tool
if result2.tool_calls:
   tool_call=result2.tool_calls[0]
   tool_result=get_text_length.invoke(tool_call["args"])

#tool_name=tool_call["name"]
#tool_args=tool_call['args']


#step: 5 send back to LLM
   final_response=llm_with_tool.invoke(f"the length of text is {tool_result}")

print(final_response.content)


 
