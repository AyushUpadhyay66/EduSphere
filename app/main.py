from fastapi import FastAPI

from app.api.students import router as student_router

app = FastAPI(
    title="University ERP Backend"
)

app.include_router(student_router)
