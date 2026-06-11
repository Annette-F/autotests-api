from pydantic import BaseModel, Field


class Address(BaseModel):
    city: str
    zip_code: str


class User(BaseModel):
    id: int
    name: str
    email: str
    address: Address
    is_active: bool = Field(alias='isActive')


user_data = {
    'id': 1,
    'name': 'Alice',
    'email': 'alice@example.com',
    'address': {'city': 'Moscow', 'zip_code': '123456'},
    'isActive': True
}
user = User(**user_data)
print(user.model_dump())
print(user.model_dump_json())

user = User(
    id=1,
    name='Mary',
    email='mary@exampli.com',
    # address={'city': 'Moscow', 'zip_code': '123456'}
    address=Address(city='Moscow', zip_code='123456'),
    isActive=True
)
print(user, user.name)
print(user)
print(user.address, type(user.address))
print(user.model_dump())
print(user.model_dump_json(), type(user.model_dump_json()))