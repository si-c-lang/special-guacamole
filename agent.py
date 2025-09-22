from langchain_openai import ChatOpenAI
from browser_use import Agent
from dotenv import load_dotenv
load_dotenv()

import asyncio
from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
)

# llm = ChatOpenAI(model="gpt-4o")

async def main():
    agent = Agent(
        task="Compare the price of gpt-4o and DeepSeek-V3 and click search and return the top 5 urls",
        llm=llm,
    )
    result = await agent.run()
    print(result)

asyncio.run(main())