

'''  VALIDATION ERROR WARING
schema inheritance or with config > response_model > ex)fields.exclude, validation error possibility
'''
from pydantic   import BaseModel, EmailStr, SecretStr
from datetime   import datetime
from enum   import Enum
from typing  import Union

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenInfo(BaseModel):
    id: Union[int, None] = None
    

class UserInfo(BaseModel):
    id: int
    create_at: datetime
    updated_at: Union[datetime, None] = None
    password: SecretStr   

    class Config:
        orm_mode = True
        # fields = {'password': {'exclude': True}}

