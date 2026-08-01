from app.database import users_collection
from app.utils.hashing import hash_password, verify_password
from app.utils.jwt_handler import create_access_token

class AuthService:

    @staticmethod
    async def register(user):
        existing = await users_collection.find_one(
            {"email": user.email}
        )

        if existing:
            return None

        data = user.model_dump()   # or user.dict() if using Pydantic v1

        data["password"] = hash_password(user.password)

        await users_collection.insert_one(data)

        return data

    @staticmethod
    async def login(user):
        existing = await users_collection.find_one(
            {"email": user.email}
        )

        if not existing:
            return None

        if not verify_password(
            user.password,
            existing["password"]
        ):
            return None

        token = create_access_token(
            {
                "id": str(existing["_id"]),
                "email": existing["email"]
            }
        )

        return token