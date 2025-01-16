import requests

from vertexai.generative_models import (
    Content,
    FunctionDeclaration,
    GenerativeModel,
    Part,
    Tool,
)

get_exchange_rate_func = FunctionDeclaration(
    name="get_exchange_rate",
    description="Get the exchange rate for currencies between countries",
    parameters={
    "type": "object",
    "properties": {
        "currency_date": {
            "type": "string",
            "description": "A date that must always be in YYYY-MM-DD format or the value 'latest' if a time period is not specified"
        },
        "currency_from": {
            "type": "string",
            "description": "The currency to convert from in ISO 4217 format"
        },
        "currency_to": {
            "type": "string",
            "description": "The currency to convert to in ISO 4217 format"
        }
    },
    "required": [
        "currency_from",
        "currency_date",
    ]
  },
)

def callApi(response):
    params = {}
    for key, value in response.candidates[0].content.parts[0].function_call.args.items():
        params[key[9:]] = value

    url = f"https://api.frankfurter.app/{params['date']}?base={params['from']}&symbols={params['to']}"
    print(url)
    api_response = requests.get(url, params=params)
    return api_response.text



def main():
    prompt = "What is the exchange rate from US dollars to Canadian dollars as of 2025-01-03?"

    exchange_rate_tool = Tool(
        function_declarations=[get_exchange_rate_func],
    )

    model = GenerativeModel("gemini-2.0-flash-exp")
    response = model.generate_content(
        prompt,
        tools=[exchange_rate_tool],
    )

    api_response = callApi(response)
    print(api_response)

    response = model.generate_content(
        [
        Content(role="user", parts=[
            Part.from_text(prompt + """Give your answer in steps with lots of detail
                and context, including the exchange rate and date."""),
        ]),
        Content(role="function", parts=[
            Part.from_dict({
                "function_call": {
                    "name": "get_exchange_rate",
                }
            })
        ]),
        Content(role="function", parts=[
            Part.from_function_response(
                name="get_exchange_rate",
                response={
                    "content": api_response,
                }
            )
        ]),
        ],
        tools=[exchange_rate_tool],
    )

    print(response.candidates[0].content.parts[0].text)

if __name__ == '__main__':
    main()
