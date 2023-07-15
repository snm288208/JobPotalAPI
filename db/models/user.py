from pydantic import BaseModel
from typing import Optional

class User(BaseModel) :
    id : Optional[str]
    name : str
    userName : str
    password : str
    email : str
    
