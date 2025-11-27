from typing import List
from pydantic import BaseModel, Field

class Source(BaseModel):
    """ Schema for a source used by an Agent """
    url: str = Field(description="The URL of the Source")

class AgentResponse(BaseModel):
    """ Schema for an Agent response with answer and sources"""

    answer: str = Field(description="The answer to the query")
    sources: List[Source] = Field(
        default_factory=list, description="The list of sources used to generate the answer"
    )

