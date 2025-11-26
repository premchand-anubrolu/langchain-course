from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
# from tavily import TavilyClient
from langchain_tavily import TavilySearch

load_dotenv()
# tavily = TavilyClient()

# @tool
# def search(query: str) -> str:
#     """
#     Tool that do online query search
#     Args:
#         query (str): search query
#     Returns:
#         str: search result
#     """
#     print(f"Searching... for string {query}")
#     return tavily.search(query=query)

llm = ChatOpenAI(model="gpt-5")
tools = [TavilySearch()]
agent = create_agent(model=llm, tools=tools)

def main():
    print("Hello from langchain-course!")
    result = agent.invoke({"messages": HumanMessage(content="search for 3 job postings for an ai engineer using langchain in the bay area on linkedin and list their details")})
    print(result)

if __name__ == "__main__":
    main()
