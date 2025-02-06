from typing import Literal

from langchain_core.tools import tool
from langchain_core.messages import AnyMessage
from langchain_core.messages import HumanMessage, SystemMessage
from langgraph.graph import StateGraph, MessagesState, END
from langgraph.prebuilt import ToolNode

from langchain_community.utilities import SQLDatabase
from langchain_google_vertexai import ChatVertexAI

@tool
def execute_query(query: str) -> str:
    """ Executes a query against the clothing items database.
    The schema of the database is the following:
    ```sql
        CREATE TABLE item 
        (
            name TEXT, -- Name of the item
            type TEXT, -- Type of the item can be 't-shirt', 'pants' or 'coat'
            color TEXT, -- Color of the item. Can be "red", "blue", "black" or "white"
            season TEXT, -- Can be "summer", "winter" "fall" or "spring"
            price FLOAT, -- Prize in dollars.
            description TEXT -- Description of the item
        )
    ```
    """
    print(query)
    return db.run_no_throw(query)


db = SQLDatabase.from_uri("sqlite:///store.sqlite")

tools = [execute_query]

graph = StateGraph(MessagesState)

generator = ChatVertexAI(
    model_name="gemini-2.0-flash-exp",
    temperature=0,
).bind(tools=tools)

def invoke_generator(state: MessagesState) -> None:
    response = generator.invoke(state["messages"])
    state["messages"].append(response)

def use_execute_query(state: MessagesState) -> Literal["query_tool", END]:
    if not state["messages"]:
        return END
    if state["messages"][-1].tool_calls:
        return "query_tool"
    return END

graph.add_node("generator", invoke_generator)
graph.add_node("query_tool", ToolNode(tools))
graph.set_entry_point("generator")

graph.add_conditional_edges("generator", use_execute_query)
graph.add_edge("query_tool", "generator")

agentic_sql = graph.compile()

#print(agentic_sql.get_graph().draw_mermaid())
agentic_sql.get_graph().print_ascii()

messages = [
    SystemMessage(
        """
        - You are a useful assistant that help users navigate a catalog of clothing items.
        - You can retrieve clothing items from the catalog using a SQL query.
        - Answer in natural language and format your output using paragraph or bullet points if
          necessary.
        """
    ),
    HumanMessage("Can you show me the name and price of all coats?")
]

stream_generator = agentic_sql.stream({"messages": messages}, stream_mode="values")

for state in stream_generator:
    state["messages"][-1].pretty_print()
state["messages"][-1].pretty_print()
