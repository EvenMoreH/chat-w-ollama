import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()

MODEL_NAME = os.getenv("MODEL_NAME", "gemma3:1b-it-q4_K_M")
OLLAMA_URL = os.getenv("URL", "http://localhost:11434")
URL = f"{OLLAMA_URL}/api/chat"
MAX_HISTORY = 30
TIMEOUT = 30

def chat():
    messages = []
    first_interaction = True
    while True:
        if first_interaction:
            print("\nWelcome to chat with GEMMA. Type 'exit' or 'quit' to end the chat.\n")
            first_interaction = False

        user_input = input("You: ")
        if user_input.lower() not in ["exit", "quit"]:
            print("GEMMA: Thinking...")
        if user_input.lower() in ["exit", "quit"]:
            print("\n[Exiting chat]\n")
            break
        messages.append({"role": "user", "content": user_input})
        if len(messages) > MAX_HISTORY:
            messages = messages[-MAX_HISTORY]
        payload = {
            "model": MODEL_NAME,
            "messages": messages
        }

        try:
            response = requests.post(URL, json=payload, stream=True, timeout=TIMEOUT)
            reply = ""
            for line in response.iter_lines():
                if line:
                    data = json.loads(line)
                    reply += data["message"]["content"]
                    if data.get("done", False):
                        break
            print(f"GEMMA: {reply}\n")
            messages.append({"role": "assistant", "content": reply})
            if len(messages) > MAX_HISTORY:
                messages = messages[-MAX_HISTORY]
        except requests.exceptions.RequestException as e:
            print(f"GEMMA: [Error communicating with server: {e}]\n")

try:
    while True:
        chat()
        restart = input("Start a new conversation? (y/n): ").strip().lower()
        if restart != "y":
            print("\nGEMMA: See you later!\n")
            break
except KeyboardInterrupt:
    print("\n\n[GEMMA: Chat interrupted. Goodbye!]\n")