import requests
import os
from dotenv import load_dotenv
from pathlib import Path
import json

# Load API key
env_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=env_path)

API_KEY = os.getenv("OPENROUTER_API_KEY")

if not API_KEY:
    print("❌ API key not found")
    exit()

print("✅ API key loaded")

DEBUG = False  # Set to True for development debugging


# 🛠️ TOOL 1 — Calculator
def calculate(expression):
    try:
        return str(eval(expression))
    except:
        return "Invalid expression"


# 🛠️ TOOL 2 — Fake stock price
def get_stock_price(company):
    fake_data = {
        "reliance": "₹2900",
        "tcs": "₹3800",
        "infosys": "₹1500"
    }

    return fake_data.get(company.lower(), "Not found")


# 🤖 AI call with tools
def call_ai(messages):
    response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "meta-llama/llama-3.3-70b-instruct",
            "messages": messages
        }
    )

    result = response.json()

    # Debug print (controlled)
    if DEBUG:
        print("\nDEBUG:", result)

    # Handle API error responses safely
    if "choices" not in result:
        print("❌ API returned error, retrying...")
        return None

    return result


# 🧠 Decide action with AI
def decide_with_ai(user_input):
    prompt = f"""
You are an AI agent.

Decide what action to take based on user input.

Available actions:
1. calculate → for math
2. stock → for stock price
3. chat → normal response

Respond ONLY in JSON format:

{{
  "action": "calculate | stock | chat",
  "input": "clean input"
}}

User input:
{user_input}
"""

    response = call_ai([
        {"role": "user", "content": prompt}
    ])

    if response is None:
        return {"action": "chat", "input": user_input}

    content = response["choices"][0]["message"]["content"]

    try:
        return json.loads(content)
    except:
        return {"action": "chat", "input": user_input}

# 🚀 MAIN LOOP
if __name__ == "__main__":
    messages = [
        {"role": "system", "content": "You are an AI assistant with tools."}
    ]

    while True:
        user_input = input("\nAsk something (or exit): ")

        if user_input.lower() == "exit":
            break

        # Step 1: Decide action FIRST (no full answer call)
        decision = decide_with_ai(user_input)
        action = decision.get("action", "chat")
        clean_input = decision.get("input", user_input)

        # Step 2: Execute based on action
        if action == "calculate":
            result = calculate(clean_input)

            print("\n🛠️ Using tool: calculate")
            print("\n🤖 Answer:")
            print(result)

        elif action == "stock":
            result = get_stock_price(clean_input)

            print("\n🛠️ Using tool: get_stock_price")
            print("\n🤖 Answer:")
            print(result)

        else:
            # Only now call AI for full answer
            messages.append({"role": "user", "content": user_input})

            response = call_ai(messages)
            if response is None:
                continue

            message = response["choices"][0]["message"]

            print("\n🤖 Answer:")
            print(message["content"])