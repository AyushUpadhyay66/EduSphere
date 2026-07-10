from fastapi import (
    APIRouter,
    Depends,
    status,
)

from app.dependencies import get_student_service
from app.schemas.student import (
    StudentCreate,
    StudentResponse,
    StudentUpdate,
)
from app.services.student_service import StudentService

router = APIRouter(
    prefix="/students",
    tags=["Students"],
)


@router.post(
    "/",
    response_model=StudentResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_student(
    student: StudentCreate,
    service: StudentService = Depends(get_student_service),
):
    return service.create_student(student)


@router.get(
    "/",
    response_model=list[StudentResponse],
)
def get_all_students(
    service: StudentService = Depends(get_student_service),
):
    return service.get_all_students()


@router.get(
    "/{student_id}",
    response_model=StudentResponse,
)
def get_student(
    student_id: int,
    service: StudentService = Depends(get_student_service),
):
    return service.get_student_by_id(student_id)


@router.patch(
    "/{student_id}",
    response_model=StudentResponse,
)
def update_student(
    student_id: int,
    request: StudentUpdate,
    service: StudentService = Depends(get_student_service),
):
    return service.update_student(
        student_id,
        request,
    )


@router.delete(
    "/{student_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_student(
    student_id: int,
    service: StudentService = Depends(get_student_service),
):
    service.delete_student(student_id)