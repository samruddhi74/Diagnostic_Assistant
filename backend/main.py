import openai
import os
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from dotenv import load_dotenv

#Load API key from environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Ensure API key is set
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY is not set in environment variables.")

# Initialize OpenAI client
openai.api_key= OPENAI_API_KEY

# Initialize FastAPI app
app = FastAPI()

# Static and template directories
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR, "static")
TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")

# Mount static files
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

# Set up templates
templates = Jinja2Templates(directory=TEMPLATES_DIR)

# Serve the frontend
@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Define request model
class SymptomRequest(BaseModel):
    symptoms: str

# Function to get diagnosis from OpenAI
def get_openai_diagnosis(symptoms: str) -> str:
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful medical assistant."},
                {"role": "user", "content": f"I have the following symptoms: {symptoms}. What could be the possible diagnosis?"}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

# Prediction endpoint
@app.post("/predict")
async def predict(request: SymptomRequest):
    try:
        symptoms = request.symptoms.strip()
        if not symptoms:
            raise HTTPException(status_code=400, detail="Symptoms cannot be empty")

        diagnosis = get_openai_diagnosis(symptoms)
        if diagnosis.startswith("Error:"):
            raise HTTPException(status_code=500, detail=diagnosis)

        return {"diagnosis": diagnosis}
    except Exception as e:
        print(f"Error: {e}")  # Log error to terminal
        raise HTTPException(status_code=500, detail="Internal Server Error")
