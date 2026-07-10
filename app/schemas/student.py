from pydantic import BaseModel, ConfigDict, EmailStr, Field


class StudentCreate(BaseModel):
    name: str
    email: EmailStr
    branch: str
    semester: int = Field(ge=1, le=8)
    cgpa: float = Field(ge=0.0, le=10.0)

class StudentUpdate(BaseModel):
    name: str | None = None
    email: EmailStr | None = None
    branch: str | None = None
    semester: int | None = Field(default=None, ge=1, le=8)
    cgpa: float | None = Field(default=None, ge=0.0, le=10.0)
    model_config = ConfigDict(extra="forbid") 

class StudentResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    branch: str
    semester: int
    cgpa: float

    model_config = ConfigDict(from_attributes=True)