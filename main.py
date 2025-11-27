from dotenv import load_dotenv
from langchain_classic.agents.react.agent import create_react_agent
from langchain_core.output_parsers.pydantic import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableLambda
from langchain_classic.agents import AgentExecutor
from langchain_classic import hub
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch
from sqlalchemy.testing.util import count_cache_key_tuples

from prompt import REACT_PROMPT_WITH_FORMAT_INSTRUCTIONS
from schemas import AgentResponse

load_dotenv()

llm = ChatOpenAI(model="gpt-4")
tools = [TavilySearch()]
react_prompt = hub.pull('hwchase17/react')
output_parser = PydanticOutputParser(pydantic_object=AgentResponse)

react_prompt_with_format_options = PromptTemplate(
    template=REACT_PROMPT_WITH_FORMAT_INSTRUCTIONS,
    input_variables=["input", "agent_scratchpad", "tools_name"]
).partial(format_instructions=output_parser.get_format_instructions())

agent = create_react_agent(
    llm=llm,
    tools=tools,
    prompt=react_prompt_with_format_options
)

agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
output_executor = RunnableLambda(lambda x: x["output"])
parse_output = RunnableLambda(lambda x: output_parser.parse(x))

chain = agent_executor | output_executor | parse_output

def main():
    print("Hello from langchain-course!")
    result = chain.invoke(
        input={
            "input": "search for 2 job postings for an ai engineer using langchain in the bay area on linkedin and list their details"
        })
    print(result)

if __name__ == "__main__":
    main()
