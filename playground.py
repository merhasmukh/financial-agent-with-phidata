from phi.agent import Agent
import phi.api
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
import phi
from phi.playground import Playground,serve_playground_app
import os
from dotenv import load_dotenv
load_dotenv()
phi.api=os.getenv('PHI_API_KEY')

#Web Search Agent
web_search_agent=Agent(
    name='Web Search Agent',
    role="Search the web for information",
    model=Groq(
        id="llama3-groq-70b-8192-tool-use-preview"
    ),
    tools=[DuckDuckGo()],
    instructions=["Always include source"],
    show_tool_calls=True,
    markdown=True
)

#Financial Agent

financial_agent=Agent(
    name='Financial Agent',
    role="Get financial data",
    model=Groq(
        id="llama3-groq-70b-8192-tool-use-preview"
    ),
    tools=[YFinanceTools(stock_price=True,analyst_recommendations=True,stock_fundamentals=True,company_news=True)],
    instructions=["Use tables to display data"],
    show_tool_calls=True,
    markdown=True
)

app=Playground(agents=[web_search_agent,financial_agent]).get_app()

if __name__ == '__main__':
    serve_playground_app("playground:app",reload=True)