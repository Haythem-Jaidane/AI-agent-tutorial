from pydantic import BaseModel
from typing import List

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    reply: str

class FinAgentRequest(BaseModel):
    question: str
    csv_path: str

class FinAgentResponse(BaseModel):
    answer: str

class RAGRequest(BaseModel):
    question: str
    documents: List[str]

class RAGResponse(BaseModel):
    answer: str
