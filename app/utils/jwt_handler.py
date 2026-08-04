from jose import JWTError, jwt
from datetime import datetime, timedelta


from app.config import (
    SECRET_KEY, 
    ALGORITHM,
    ACCESS_TOKEN_EXPIRES_MINUTES
)

def create_access_token(data:dict):
    payload = data.copy()

    expire = datetime.utcnow() + timedelta(
        minutes=ACCESS_TOKEN_EXPIRES_MINUTES
    )

    payload.update({"exp": expire})

    token = jwt.encode(
        payload, 
        SECRET_KEY, 
        algorithm=ALGORITHM
    )

    return token


def verify_access_token(token:str):
    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        return payload
    except JWTError:
        return None


