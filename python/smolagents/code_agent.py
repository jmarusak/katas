from smolagents.agents import CodeAgent
from smolagents import LiteLLMModel

model = LiteLLMModel(
    model_id="vertex_ai/gemini-2.0-flash",
)

agent = CodeAgent(tools=[], model=model, add_base_tools=True)

#print(agent.run("What is 15% of 99?"))
#print(agent.run("Change case of `joe` to uppercase?"))

print(agent.run("List files in current directory."))
