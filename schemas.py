from pydantic import BaseModel, ConfigDict
from typing import Optional

class SignUpModel(BaseModel):
    id: Optional[int] = None
    username: str
    email: str
    password: str
    isActive: Optional[bool] = None
    isStaff: Optional[bool] = None

    model_config = ConfigDict(
        json_schema_extra={
            'example':{
                "username":"johndoe",
                "email":"johndoe@gmail.com",
                "password":"password",
                "is_staff":False,
                "is_active":True
            }
        }
    )


class UserResponseModel(BaseModel):
    id: int
    username: str
    email: str
    isActive: bool
    isStaff: bool

    model_config = ConfigDict(from_attributes=True)