from pydantic import BaseModel, Field, EmailStr


class UserSchema(BaseModel):
    '''
    Описание структуры пользователя.
    '''
    id: str
    email: EmailStr
    first_name: str = Field(alias='firstName')
    last_name: str = Field(alias='lastName')
    middle_name: str = Field(alias='middleName')


class CreateUserRequestSchema(BaseModel):
    '''
    Описание структуры запроса на создание пользователя.
    '''
    email: EmailStr
    password: str
    first_name: str = Field(alias='firstName')
    last_name: str = Field(alias='lastName')
    middle_name: str = Field(alias='middleName')


class CreateUserResponseSchema(BaseModel):
    '''
    Описание структуры ответа создания пользователя.
    '''
    user: UserSchema


