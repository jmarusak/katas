import asyncio
import motor.motor_asyncio
from pydantic import BaseModel, Field

class StudentModel(BaseModel):
    name: str = Field(...)
    location: str = Field(...)
    age: int = Field(...)

async def main():
    url = "mongodb://127.0.0.1:27017"

    student = StudentModel(name="Pepe", location="Rome", age=44)
    print(student)
    print(type(student))

    try:
        client = motor.motor_asyncio.AsyncIOMotorClient(url)
        db = client.get_database("college")
        coll = db.get_collection("students")

        result = await coll.insert_one(student.model_dump())
        return result

    except Exception as e:
        print(f"MongoDB Error: {e}")
        return None
    finally:
        if client:
            client.close()

if __name__ == "__main__":
   asyncio.run(main()) 
