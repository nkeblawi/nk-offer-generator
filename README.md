# Offer Generator and Evaluator
- This module takes in a current offer, generates more compelling offers, then evaluates
those compelling offers against Alex Hormozi's Value Framework.

## Prompts
You will find the prompts in the prompts folder.

## Modules
You will find the DSPY Modules here.

## Models
You will find the DSPY Models here.

## Signatures
You will find the DSPY Signatures here.

## Nuxt-app
You'll find the Nuxt application here.


# Getting Started
1. python3 -m venv venv
2. source venv/bin/activate
3. pip install -r requirements.txt
4. touch .env
    - ANTHROPIC_API_KEY=yourkey
    - LANGFUSE_SECRET_KEY=yourkey
    - LANGFUSE_PUBLIC_KEY=yourkey
    - LANGFUSE_HOST=yourhost
5. fastapi dev start.py
6. Open another terminal
7. cd nuxt-app
8. npm install
9. npm run dev