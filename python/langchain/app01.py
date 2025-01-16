from typing import Optional, Any
from langchain_core.runnables import Runnable, RunnableConfig

def increment_by_one(x: int) -> int:
    return x+1

def fake_llm(x: int) -> str:
    return f"Result = {x}"

class MyFirstChain(Runnable[int, str]):
    def invoke(self, input: int, config: Optional[RunnableConfig]=None, **kwargs: Any) -> str:
        increment = increment_by_one(input)
        return fake_llm(increment)

def main():
    runnable = MyFirstChain()
    response = runnable.invoke(1)
    print(response)

if __name__ == '__main__':
    main()
