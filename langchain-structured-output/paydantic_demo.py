from pydantic import BaseModel, Field, EmailStr
from typing import Optional

class Student(BaseModel):
    name: str = Field(default="talha")
    age: Optional[int] = None
    email: EmailStr
    cgpa: float = Field(gt=0, lt=4.0, default=3.5, description='A decimal value representing the cgpa of the student')

new_student = {"name": "talha", "age": 10, "email": "talha@gmail.com", "cgpa": 2}

student = Student(**new_student)

student_dict = dict(student)
student_json = student.model_dump_json()

print("student", student)
print("student_dict", student_dict)
print("student_json", student_json)
