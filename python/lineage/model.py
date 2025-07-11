from pydantic import BaseModel, RootModel, Field
from typing import List, Literal

class JoinCondition(BaseModel):
    """
    Represents a single condition within a JOIN clause.
    """
    left_column: str = Field(..., description="The column from the left table involved in the join condition.")
    right_column: str = Field(..., description="The column from the right table involved in the join condition.")

class Join(BaseModel):
    """
    Represents a single SQL JOIN operation.
    """
    join_type: Literal["INNER", "LEFT", "RIGHT", "FULL", "CROSS", "IMPLICIT"] = Field(
        ...,
        description="The type of SQL join (e.g., INNER, LEFT, RIGHT, IMPLICIT)."
    )
    left_table: str = Field(..., description="The name of the table on the left side of the JOIN.")
    right_table: str = Field(..., description="The name of the table on the right side of the JOIN.")
    join_conditions: List[JoinCondition] = Field(
        ...,
        description="A list of conditions that define how the tables are joined."

    )

class Joins(RootModel[List[Join]]):
    """
    The top-level model representing a list of SQL join operations from the LLM.
    """
    pass
