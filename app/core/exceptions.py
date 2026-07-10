class StudentNotFoundException(Exception):
    def __init__(self, student_id: int):
        self.student_id = student_id
        super().__init__(f"Student with ID {student_id} not found")


class EmailAlreadyExistsException(Exception):
    def __init__(self, email: str):
        self.email = email
        super().__init__(f"Student with email '{email}' already exists")