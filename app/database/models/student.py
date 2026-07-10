from sqlalchemy import String, Integer, Numeric
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base


class Student(Base):
    __tablename__ = "students"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True
    )

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    email: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        nullable=False,
        index=True
    )

    branch: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )

    semester: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    cgpa: Mapped[float] = mapped_column(
        Numeric(4, 2),
        nullable=False
    )