from typing import Optional, List, Dict, Any
from pydantic import BaseModel

class SurveySetting(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    is_active: Optional[bool] = None

class Variable(BaseModel):
    id: int
    name: str
    type: str
    required: bool

class ResponseEntry(BaseModel):
    id: int
    response: Dict[str, Any]
    submitted_at: Optional[str]

class Folder(BaseModel):
    id: int
    name: str
    order: Optional[int] = None

class Question(BaseModel):
    id: Optional[int]
    title: str
    type: int
    description: Optional[str] = None
    is_required: Optional[bool] = False

class APIError(BaseModel):
    status_code: int
    detail: str
