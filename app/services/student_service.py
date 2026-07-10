from app.core.exceptions import (
    EmailAlreadyExistsException,
)
from app.core.exceptions import (
    StudentNotFoundException,
)
from app.database.models.student import Student
from app.repositories.student_repository import StudentRepository
from app.schemas.student import StudentCreate, StudentUpdate


class StudentService:

    def __init__(self, repository: StudentRepository):
        self.repository = repository

    def create_student(self, request: StudentCreate) -> Student:

        existing_student = self.repository.find_by_email(request.email)

        if existing_student:
            raise EmailAlreadyExistsException()

        student = Student(
            name=request.name,
            email=request.email,
            branch=request.branch,
            semester=request.semester,
            cgpa=request.cgpa,
        )

        return self.repository.save(student)

    def get_student_by_id(self, student_id: int) -> Student:

        student = self.repository.find_by_id(student_id)

        if student is None:
            raise StudentNotFoundException(student_id)

        return student

    def get_all_students(self) -> list[Student]:
        return self.repository.find_all()

    def update_student(
        self,
        student_id: int,
        request: StudentUpdate,
    ) -> Student:

        student = self.repository.find_by_id(student_id)

        if student is None:
            raise StudentNotFoundException(student_id)

        update_data = request.model_dump(exclude_unset=True)

        if "email" in update_data:

            existing_student = self.repository.find_by_email(
                update_data["email"]
            )

            if (
                existing_student
                and existing_student.id != student.id
            ):
                raise EmailAlreadyExistsException()

        for field, value in update_data.items():
            setattr(student, field, value)

        self.repository.update(student)

        return student

    def delete_student(self, student_id: int):

        student = self.repository.find_by_id(student_id)

        if student is None:
            raise StudentNotFoundException(student_id)

        self.repository.delete(student)