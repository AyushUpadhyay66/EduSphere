from app.core.security.jwt import JWTService

token = JWTService.create_access_token(
    subject="ayush@example.com"
)

print(token)

payload = JWTService.decode_access_token(token)

print(payload)