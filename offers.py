import os
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from dsp.modules import anthropic
from dotenv import load_dotenv
from modules.modules import *
from langfuse import Langfuse
from langfuse.decorators import observe, langfuse_context
from langfuse.openai import openai  # OpenAI integration
from pydantic import ValidationError
import logging

load_dotenv()

anthropic_api_key = os.getenv("ANTHROPIC_API_KEY")
langfuse_secret_key = os.getenv("LANGFUSE_SECRET_KEY")
langfuse_public_key = os.getenv("LANGFUSE_PUBLIC_KEY")
langfuse_host = os.getenv("LANGFUSE_HOST")

langfuse = Langfuse(
    secret_key=langfuse_secret_key, public_key=langfuse_public_key, host=langfuse_host
)

# claude-3-5-sonnet-20240620
# claude-3-haiku-20240307
# claude-3-opus-20240229
anthropic_model = "claude-3-5-sonnet-20240620"  # Choose Claude model
anthropic_client = anthropic.Claude(
    model=anthropic_model, max_tokens=4000, api_key=anthropic_api_key
)
dspy.settings.configure(lm=anthropic_client)

# Start the app
app = FastAPI()

# Set up Jinja2 templates
templates = Jinja2Templates(directory="templates")

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Initialize logging
logging.basicConfig(level=logging.ERROR)


# Load index.html
@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


# Generate offers
@app.post("/generate", response_model=OfferGenerationPack)
async def generate_offers(occupation: OfferInput) -> OfferGenerationPack:
    if occupation.occupation == "":
        return ValueError
    offer_gen = OfferGenerationModule(anthropic_client)
    offer_gen_solutions = offer_gen(occupation=occupation.occupation)

    return offer_gen_solutions


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
