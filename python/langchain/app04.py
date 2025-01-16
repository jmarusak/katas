from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_google_vertexai import VertexAI

description = """
 Prepares specifications for CIHI vendor clients including detailed logic and flow diagrams. Supports the creation of test data for the implementation of vendor test systems as necessary.
6. Facilitates discussions and interviews while working with Business Area(s) and External stakeholders and ITS resources to ensure client needs are met through the delivery of annual product and system enhancements.
"""

def main():
    llm = VertexAI(model_name="gemini-2.0-flash-exp")
    prompt_template = PromptTemplate.from_template(
        """Extract {entities} from the job description:\n\n{description}\n.
        Answer with a valid json as an output."""
    )

    chain = prompt_template | llm | JsonOutputParser()
    result = chain.invoke({"entities": "company, teams", "description": description})
    print(result)

if __name__ == '__main__':
    main()
