from typing import Optional, Type
from pydantic import BaseModel, Field
from langchain.tools import BaseTool
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage
from langchain_core.callbacks.manager import CallbackManagerForToolRun
from langchain_core.prompts import ChatPromptTemplate, PromptTemplate, MessagesPlaceholder

from langchain_google_vertexai import ChatVertexAI

class CalculatorInput(BaseModel):
    """Input to the Calculator."""

    expression: str = Field(
        description="evaluate mathematical expression"
    )

class CalculatorTool(BaseTool):
    name: str = "Calculator"
    args_schema: Optional[Type[BaseModel]] = CalculatorInput
    description: str = (
        "Useful for when you need to evaluate a mathematical expression."
    )

    def _run(self, expression: str, run_manager: Optional[CallbackManagerForToolRun] = None) -> str:
        return eval(expression)

calculator_tool = CalculatorTool()

llm = ChatVertexAI(model_name="gemini-2.0-flash-exp", temperature=0.)

calculator_prompt = (
   "You have access to calculator that can solve mathematical problems. "
   "If you want to ask a calculator, start with CALCULATOR: and generate an expression "
   "to be evaluated by a calculator (it should have only numbers and mathematical operators)."
   "If you ask CALCULATOR, don't do anything else."
   "If you think you have a final solution, start it with FINAL_ANSWER=.\n"
)

calculator_prompt_template = ChatPromptTemplate(
    [("system", calculator_prompt),
     MessagesPlaceholder(variable_name="messages")]
)

math_problem = "How much is 23*3?"

# Step 1: Model generates a tool call request
step1 = llm.invoke([math_problem], tools=[calculator_tool])
print("\nStep 1 (Generate Tool call parameters): \n", step1)

# Step 2: Extract expression and call the tool manually
tool_call = step1.tool_calls[0]  # Extract tool call request
expression = tool_call["args"]["expression"]  # Get expression to evaluate
tool_result = calculator_tool._run(expression)  # Manually invoke the tool
print("\nStep 2 (Tool Call Results): ", tool_result)

# Step 3: Feed tool response back to the model
step3 = (calculator_prompt_template | llm).invoke(
    [
        HumanMessage(content=math_problem),  # Original user input
        step1,  # AI response with tool request
        ToolMessage(content=tool_result, tool_call_id=tool_call["id"]),  # Tool result
    ]
)
print("\nStep 3 (Final Response From LLM): ", step3.content)
