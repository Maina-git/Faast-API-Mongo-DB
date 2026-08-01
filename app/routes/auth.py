""""
from fastapi import APIRouter, HTTPException

from app.schemas.user_schema import (
    RegisterUser,
    LoginUser
)

from app.services.auth_service  import AuthService


router = APIRouter(
    prefix="/auth",
    tags = ["Authentication"]
)


@router.post('/register')
async def register(user: RegisterUser):
    result = await AuthService.register(user)
    if result is None:
        raise HTTPException(
            status_code=400,
            detail = "Email already exists"
        )

    return {
        "massage":"User created successfully"
    }


@router.post("/login")
async def login(user: LoginUser):

    token = await AuthService.login(user)

    if token is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    return {
        "access_token": token,
        "token_type": "bearer"
    }

"""

from fastapi import APIRouter, HTTPException

from app.schemas.user_schema import RegisterUser, LoginUser
from app.services.auth_service import AuthService

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post("/register")
async def register(user: RegisterUser):
    result = await AuthService.register(user)

    if result is None:
        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )

    return {
        "message": "User created successfully"
    }


@router.post("/login")
async def login(user: LoginUser):

    token = await AuthService.login(user)

    if token is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    return {
        "access_token": token,
        "token_type": "bearer"
    }



