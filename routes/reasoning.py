from fastapi import APIRouter, Query
from reasoning_agent import get_reasoning_agent
from constants import GROQ_API_KEY


reasoning_router = APIRouter()


@reasoning_router.post("/reasoning")
async def reasoning(query: str = Query(..., description="The query to be reasoned about")):
    agent = get_reasoning_agent(groq_api_key=GROQ_API_KEY)
    response = agent.invoke({"input": query})
    return {"agentic_response": response["output"]}

