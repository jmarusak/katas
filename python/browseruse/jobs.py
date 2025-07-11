import os
import asyncio
import sys
from typing import List

from dotenv import load_dotenv
from browser_use import Agent, BrowserSession, BrowserConfig, Controller
from pydantic import BaseModel, SecretStr

#from browser_use.llm import ChatGoogle
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv(dotenv_path='../.env')
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY environment variable not set.")

class Job(BaseModel):
    title: str

class Jobs(BaseModel):
    jobs: List[Job]

controler = Controller(output_model=Jobs)

browser_session = BrowserSession(
    # Path to a specific Chromium-based executable (optional)
    executable_path='/usr/bin/google-chrome',

    # Use a specific data directory on disk (optional, set to None for incognito)
    #user_data_dir='~/.config/browseruse/profiles/default',   # this is the default
    
    # ... any other BrowserProfile or playwright launch_persistnet_context config...
    # headless=False,
)

# Initialize the model
#llm = ChatGoogle(model='gemini-2.0-flash-exp')
llm = ChatGoogleGenerativeAI(model='gemini-2.0-flash', api_key=SecretStr(api_key))


# Read LLM prompt from file, use default if not provided
prompt_file = sys.argv[1] if len(sys.argv) > 1 else 'jobs.md'
with open(prompt_file, 'r') as file:
    prompt = file.read()

# Create agent with the model
agent = Agent(
    task=prompt,
    llm=llm,
#    browser=browser_session,
    controller=controler,
)

async def main():
    print("Agent is exploring the website...")
    
    history = await agent.run()
    
    result = history.final_result()

    if result:
        parsed: Jobs = Jobs.model_validate_json(result)

        for job in parsed.jobs:
            print(job.title)
            print()
    else:
        print("No result found.")
    
if __name__ == '__main__':
    asyncio.run(main())
