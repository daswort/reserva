from pydantic import BaseModel
from typing import Optional, Union, Dict, List

class ErrorDetailModel(BaseModel):
    type: str
    loc: List[Union[str, int]]
    msg: str
    input: Optional[Union[str, int, float, dict, list]]
    ctx: Optional[Dict[str, str]] = None

class ErrorResponseModel(BaseModel):
    status_code: int
    error_code: str
    message: str
    detail: Optional[Union[str, List[ErrorDetailModel]]] = None

