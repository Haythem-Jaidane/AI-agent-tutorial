from fastapi import APIRouter, UploadFile, File
from services import chatbot, finAgent, rag
from requests import ai as schemas
import os

router = APIRouter()

@router.post("/chat", response_model=schemas.ChatResponse)
def chat(request: schemas.ChatRequest):
    model = chatbot.create_chatbot()
    response = model.generate_content(request.message)
    return schemas.ChatResponse(reply=response.text)

@router.post("/fin-agent", response_model=schemas.FinAgentResponse)
async def financial_agent(question: str, file: UploadFile = File(...)):
    # Save the uploaded file
    file_path = f"temp_{file.filename}"
    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    agent = finAgent.create_fin_agent(file_path)
    response = agent.run(question)
    
    # Clean up the temporary file
    os.remove(file_path)

    return schemas.FinAgentResponse(answer=response)

@router.post("/rag", response_model=schemas.RAGResponse)
def retrieval_augmented_generation(request: schemas.RAGRequest):
    # This is a simplified example. In a real-world scenario, 
    # you would have a more sophisticated way of handling documents.
    from langchain.document_loaders import TextLoader
    from langchain.docstore.document import Document

    # In this example, we'll just treat the strings as content of documents.
    documents = [Document(page_content=doc) for doc in request.documents]

    qa = rag.create_rag_service(documents)
    response = qa.run(request.question)
    return schemas.RAGResponse(answer=response)
