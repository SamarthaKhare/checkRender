from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json
import os
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    query: str

def generate_response(question: str):
    return f"Generated response for: {question}"

@app.post("/chat")
async def chat(request: ChatRequest):
    try:
        logging.info(f"Received request: {request}")
        response = generate_response(request.query)
        
        if response:
            return {"answer": response}
        else:
            raise HTTPException(status_code=500, detail="Error generating response")
    
    except Exception as e:
        logging.error(f"Internal Server Error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))
# Run the server (for local testing)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))
