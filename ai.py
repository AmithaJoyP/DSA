from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import openai

openai.api_key = OPENAI_API_KEY
app = FastAPI()
class ChatRequest(BaseModel):
    messages: List[dict]
    model: str = "gpt-3.5-turbo"
    
Default model
    temperature: float = 0.7
    max_tokens: int = 200
    
class ChatResponse(BaseModel):
    response: str
@app.get("/")
async def hello_world():
    return {"message": "Hello, World!"}
@app.post("/chat")
async def chat_completion(request: ChatRequest):
    """
    Endpoint for interacting with OpenAI's chat completion API.
    """
    try:
        completion = openai.ChatCompletion.create(model=request.model,messages=request.messages,temperature=request.temperature,max_tokens=request.max_tokens,)
        return ChatResponse(response=completion.choices[0].message.content)
    except openai.error.OpenAIError as e:
        raise HTTPException(status_code=500, detail=str(e))
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)