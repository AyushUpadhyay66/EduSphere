from app.core.security.hashing import PasswordService

password = "Noveau@123"

hashed = PasswordService.hash_password(password)

print(hashed)

print(
    PasswordService.verify_password(
        password,
        hashed,
    )
)