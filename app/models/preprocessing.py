from pydantic import BaseModel, Field

from app.models.response import *



class PreprocessingIn(BaseModel):
    """Use this data model to preprocessing the request data."""


    origin_data_path: str = Field(..., example="1/data.csv")
    columns: list = Field(..., example=["load"])
    db_id: int = Field(..., example=1)



class PreprocessingOut(BaseModel):
    """Use this data model to preprocessing the request data."""

    origin_data_path: str = Field(..., example="1/data.csv")
    pre_data_path: str = Field(..., example="1/data.csv")
    columns: list = Field(..., example=["load"])
    db_id: int = Field(..., example=1)


class TransformationIn(BaseModel):
    origin_data_path: str = Field(..., example='data.csv')
    pre_data_name: str = Field(..., example='happycom_analysis.csv')
    db_id: int = Field(..., example=1)


class TransformationOut(BaseModel):
    origin_data_path: str = Field(..., example='data.csv')
    pre_data_path: str = Field(..., example='happycom_analysis.csv')
    db_id: int = Field(..., example=1)