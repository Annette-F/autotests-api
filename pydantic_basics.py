'''
{
  "course": {
    "id": "string",
    "title": "string",
    "maxScore": 0,
    "minScore": 0,
    "description": "string",
    "previewFile": {
      "id": "string",
      "filename": "string",
      "directory": "string",
      "url": "https://example.com/"
    },
    "estimatedTime": "string",
    "createdByUser": {
      "id": "string",
      "email": "user@example.com",
      "lastName": "string",
      "firstName": "string",
      "middleName": "string"
    }
  }
}
'''
import uuid
from pydantic import BaseModel, Field, ConfigDict, computed_field, HttpUrl, EmailStr, ValidationError, IP
from pydantic.alias_generators import to_camel


class FileSchema(BaseModel):
    id: str
    filename: str
    directory: str
    url: HttpUrl


class UserSchema(BaseModel):
    id: str = Field(e)
    email: EmailStr
    last_name: str = Field(alias='lastName')
    first_name: str = Field(alias='firstName')
    middle_name: str = Field(alias='middleName')

    @computed_field
    def username(self) -> str:
        return f'{self.first_name} {self.last_name}'

    def get_username(self) -> str:
        return f'{self.first_name} {self.last_name}'


class CourseSchema(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    title: str = 'Playwright'
    max_score: int = Field(alias='maxScore', default=1000)
    min_score: int = Field(alias='minScore', default=100)
    description: str = 'Playwright'
    preview_file: FileSchema = Field(alias='previewFile')
    estimated_time: str = Field(alias='estimatedTime', default='2 weeks')
    created_by_user: UserSchema = Field(alias='createdByUser')


course_default_model = CourseSchema(
    id='course_id',
    title='Playwright',
    maxScore=100,
    minScore=10,
    description='Playwright',
    previewFile=FileSchema(
        id='file-id',
        filename='file.png',
        directory='courses',
        url='http://localhost:8000',
    ),
    estimatedTime='1 week',
    createdByUser=UserSchema(
        id='user-id',
        email='user@email.com',
        lastName='Ford',
        firstName='Tom',
        middleName='J.',
    ),
)
print('Course default model:', course_default_model)

course_dict = {
    "id": "course_id",
    "title": "Playwright",
    "maxScore": 100,
    "minScore": 10,
    "description": "Playwright",
    "previewFile": {
        "id": 'file-id',
        "filename": 'file.png',
        "directory": 'courses',
        "url": 'http://localhost:8000',
    },
    "estimatedTime": "1 week",
    "createdByUser": {
        "id": 'user-id',
        "email": 'user@email.com',
        "lastName": 'Ford',
        "firstName": 'Tom',
        "middleName": 'J.',
    }
  }
course_dict_model = CourseSchema(**course_dict)
print('Course dict model:', course_dict_model)

course_json = """
{
   "id": "course_id",
    "title": "Playwright",
    "maxScore": 100,
    "minScore": 10,
    "description": "Playwright",
    "previewFile": {
        "id": "file-id",
        "filename": "file.png",
        "directory": "courses",
        "url": "http://localhost:8000"
    },
    "estimatedTime": "1 week",
    "createdByUser": {
        "id": "user-id",
        "email": "user@email.com",
        "lastName": "Ford",
        "firstName": "Tom",
        "middleName": "J."
    }
}
"""

course_json_model = CourseSchema.model_validate_json(course_json)
print('Course json model:', course_json_model)

print(course_json_model.model_dump())
print(course_json_model.model_dump_json(by_alias=True))


user = UserSchema(
    id='user-id',
    email='user@email.com',
    lastName='Ford',
    firstName='Tom',
    middleName='J.',
)
print(user.get_username(), user.username)


try:
    file = FileSchema(
        id='file-id',
        filename='file.png',
        directory='courses',
        url='localhost:8000',
    )
except ValidationError as error:
    print(error)
    print(error.errors())

