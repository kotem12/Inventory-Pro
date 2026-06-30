from passlib.context import CryptContext

from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto",
)


class UserService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def create_user(self, payload: UserCreate):

        hashed_password = pwd_context.hash(payload.password)

        user = User(
            first_name=payload.first_name,
            last_name=payload.last_name,
            email=payload.email,
            phone=payload.phone,
            organization_id=payload.organization_id,
            role_id=payload.role_id,
            password_hash=hashed_password,
        )

        return self.repository.create(user)

    def get_user(self, user_id):
        return self.repository.get_by_id(user_id)

    def get_by_email(self, email):
        return self.repository.get_by_email(email)

    def list_users(self):
        return self.repository.list()