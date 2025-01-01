from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo

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


multi_ai_agent=Agent(
    team=[web_search_agent,financial_agent],
    model=Groq(id="llama-3.1-70b-versatile"),
    instructions=["Always include source","Use tables to display data"],
    show_tool_calls=True,
    markdown=True
)

multi_ai_agent.print_response("Summarise analyst recommendations for Apple Inc.",stream=True)