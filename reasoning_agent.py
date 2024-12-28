from langchain_groq import ChatGroq
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.agents import Tool, create_react_agent, AgentExecutor
from utils.custom_tools import calculator
from langchain import hub

def get_reasoning_agent(groq_api_key: str):
    """
    Get the reasoning agent with the given Groq API key.
    """
    
    # Initialize the LLM
    llm = ChatGroq(
        api_key=groq_api_key,
        model="mixtral-8x7b-32768",
        streaming=True,
        temperature=0.1  # Lower temperature for faster responses
    )

    # Define the tools to be used by the agent
    mathematical_tool = calculator
    reasoning_tool = Tool(
        name="Reasoning",
        func=lambda x: llm.invoke(x),  # Direct LLM call for reasoning
        description="Use this tool for logic-based and reasoning questions."
    )
    wikipedia_tool = Tool(
        name="Wikipedia",
        func=WikipediaAPIWrapper(top_k_results=2).run,
        description="Use this tool for searching Wikipedia."
    )
    tools = [
        reasoning_tool,
        mathematical_tool,
        wikipedia_tool
    ]
    
    # Create the agent and agent executor
    agent = create_react_agent(
        llm=llm,
        tools=tools,
        prompt=hub.pull("hwchase17/react")
    )
    agent_executor = AgentExecutor(
        agent=agent,
        tools=tools,
        verbose=True,
        handle_parsing_errors=True,
        max_iterations=5
    )

    return agent_executor