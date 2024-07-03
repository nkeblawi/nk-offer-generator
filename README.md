# Offer Generator and Evaluator
- This module takes in a current offer, generates more compelling offers, then evaluates
those compelling offers against Alex Hormozi's Value Framework.
- Credit to Brandon Phillips for the original idea
- Forked from https://github.com/PhiBrandon/dspy-nuxt3-offer-creation-framework
- Repurposed for marketing by changing the inputs and optimizing outputs for speed

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


# To get started, follow these instructions
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
7. python offers.py
