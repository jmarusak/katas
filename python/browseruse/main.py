import os
import asyncio
import sys

from dotenv import load_dotenv
from browser_use import Agent, BrowserSession
from pydantic import SecretStr

#from browser_use.llm import ChatGoogle
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv(dotenv_path='../.env')
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY environment variable not set.")

# Initialize the model
#llm = ChatGoogle(model='gemini-2.0-flash-exp')
llm = ChatGoogleGenerativeAI(model='gemini-2.0-flash', api_key=SecretStr(api_key))

# Read LLM prompt from file, use default if not provided
prompt_file = sys.argv[1] if len(sys.argv) > 1 else 'loblaw.md'
with open(prompt_file, 'r') as file:
    prompt = file.read()

browser_session = BrowserSession(
        executable_path='/usr/bin/google-chrome',
)

# Create agent with the model
agent = Agent(
    task=prompt,
    llm=llm,
    browser_session=browser_session,
)

async def main():
    print("Agent is exploring the website...")
    
    history = await agent.run()
    result = history.final_result()

if __name__ == '__main__':
    asyncio.run(main())
