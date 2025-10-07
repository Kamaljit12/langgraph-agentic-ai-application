from pydantic import BaseModel, Field
from typing import Optional, TypedDict


class ChatRequest(BaseModel):
    message: str = Field(..., description="The user's query")
    
class ChatResponse(BaseModel):
    response: str = Field(..., description="The AI's response to the user's query")
    source_documents: Optional[list[dict]] = Field(None, description="Optional source documents related to the response")


# message = ChatRequest(message="Hello, how can I use LangGraph?")
# response = ChatResponse(
#     response="You can use LangGraph to build applications that leverage language models and graph databases.",
#     source_documents=[
#         {"title": "LangGraph Overview", "url": "https://langgraph.com/overview"},
#         {"title": "Getting Started with LangGraph", "url": "https://langgraph.com/getting-started"}
#     ]
# )
# print(message)
# print(response)
# --- IGNORE ---