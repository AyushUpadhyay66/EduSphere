from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database.models.student import Student


class StudentRepository:
    def __init__(self, db: Session):
        self.db = db

    def save(self, student: Student) -> Student:
        self.db.add(student)
        self.db.commit()
        self.db.refresh(student)
        return student

    def find_by_id(self, student_id: int) -> Student | None:
        stmt = select(Student).where(Student.id == student_id)

        result = self.db.execute(stmt)

        return result.scalar_one_or_none()

    def find_by_email(self, email: str) -> Student | None:
        stmt = select(Student).where(Student.email == email)

        result = self.db.execute(stmt)

        return result.scalar_one_or_none()

    def find_all(self) -> list[Student]:
        stmt = select(Student)

        result = self.db.execute(stmt)

        return list(result.scalars().all())

    def delete(self, student: Student) -> None:
        self.db.delete(student)
        self.db.commit()

    def update(self, student: Student) -> Student:
        self.db.commit()
        self.db.refresh(student)
        return student