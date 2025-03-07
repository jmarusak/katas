from smolagents.agents import ToolCallingAgent
from smolagents import tool, LiteLLMModel

@tool
def get_weather(location: str) -> str:
    """
    Get weather at given location

    Args:
        location(str): the location
    Return (str): weather description
    """

    return f"It is rainy in {location}, temperature is 10C."


model = LiteLLMModel(
    model_id="vertex_ai/gemini-2.0-flash",
)

agent = ToolCallingAgent(tools=[get_weather], model=model)

print(agent.run("What's the weather like in Paris?"))
