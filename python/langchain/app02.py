from operator import itemgetter
from typing import Optional, Any
from langchain_core.runnables import RunnableLambda 

def increment_by_one(x: int) -> int:
    return x+1

def fake_llm(x: int) -> str:
    return f"Result = {x}"

def main():
    chain = (
        itemgetter("x")
        | RunnableLambda(increment_by_one)
        | fake_llm
    )

    response = chain.invoke({"x": 1})
    print(response)

if __name__ == '__main__':
    main()
