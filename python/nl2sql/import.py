import json

from langchain_community.utilities import SQLDatabase
with open("data.json") as input_file:
    items = json.load(input_file)

sanitize = lambda string: string.replace("'", "")

records = [
    ", ".join(f"'{sanitize(value)}'" if isinstance(value, str) else str(value) for colname, value in item.items())
        for item in items
]

db = SQLDatabase.from_uri("sqlite:///store.sqlite")

for record in records:
    statement = f"INSERT INTO item VALUES ({record})"
    try:
        db.run(statement)
    except Exception as err:
        print(f"{err} : {statement}")
