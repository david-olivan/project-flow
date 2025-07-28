import secrets
import bcrypt
from typing import Optional
from fastapi import HTTPException, status, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from ..database.models import User, API_Key


security = HTTPBearer()


async def generate_and_save_api_key(*, role: str, user: User) -> API_Key:
    raw_key = "pFlow010-" + secrets.token_urlsafe(32)
    salt = bcrypt.gensalt()
    hashed_key = bcrypt.hashpw(raw_key.encode(), salt)
    new_key = API_Key(role=role, api_key=hashed_key.decode())

    await user.set({"api_key": new_key})

    return API_Key(api_key=raw_key, role=role)


async def validate_api_key(api_key: str) -> Optional[str]:
    users = await User.find_all().to_list()

    for user in users:
        if user.api_key is not None:
            hash_bytes = user.api_key.api_key.encode()

            if bcrypt.checkpw(api_key.encode(), hash_bytes):
                return user.api_key.role
    return None


async def get_api_key_from_header(
    credentials: HTTPAuthorizationCredentials = Depends(security),
):
    if not credentials:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="API Key requerida"
        )

    return credentials.credentials
