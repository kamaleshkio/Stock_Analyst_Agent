from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
import openai

import os 
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

web_search = Agent(
    name = "web_search",
    description = "Asearch the web for information",
    model = Groq(id = "meta-llama/llama-4-maverick-17b-128e-instruct"),
    tools = [DuckDuckGo()],
    instructions = """Always include a web search to find the most up-to-date information.""",
    show_tools_calls = True,
    markdown = True,
)

yahoo_finance = Agent(
    name = "yahoo_finance",
    description = "Get stock data from Yahoo Finance",
    model = Groq(id = "meta-llama/llama-4-maverick-17b-128e-instruct"),
    tools = [YFinanceTools(stock_price = True, stock_history = True, analyst_recommendations = True, strock_fundamentals = True, comapny_news = True),],
    instructions = "Use tables to display stock data. Use the Yahoo Finance API to get stock data.",
    show_tools_calls = True,
    markdown = True,
)


multi_ai_agent = Agent(
    team = [web_search, yahoo_finance],
    instructions = ["always include sources", "use table to display the data", "always include stock data"],
    show_tools_calls = True,
    markdown=True,
)

multi_ai_agent.print_response("Summaraize analyst recommemdation and share the latest news for top 5 indian market  stocks", stream=True)

