import os
import textwrap

from google import genai
from google.genai.types import Tool, ToolCodeExecution, GenerateContentConfig

def main():
    location = 'us-central1'
    model_id = 'gemini-2.0-flash-exp'

    project_id = os.getenv('GOOGLE_CLOUD_PROJECT')
    if project_id == None:
        print('GOOGLE_CLOUD_PROJECT env variable is not set.')
        exit(1)

    client = genai.Client(vertexai=True, project=project_id, location=location)
    code_execution_tool = Tool(code_execution=ToolCodeExecution())

    config = GenerateContentConfig(
        tools=[code_execution_tool],
        temperature=0,
    )

    prompt = """\
        What is the sum of the first 50 prime numbers?
        Generate code and run code for the calculation.
    """
   
    prompt = textwrap.dedent(prompt) 
    response = client.models.generate_content(
        model=model_id,
        contents=prompt,
        config=config,
    )

    # print generated code
    for part in response.candidates[0].content.parts:
        if part.executable_code:
            print(part.executable_code.code)

    # print code execution results
    for part in response.candidates[0].content.parts:
        if part.code_execution_result:
            print(part.code_execution_result.output)
            print(part.code_execution_result.outcome)


if __name__  == '__main__':
    main()
