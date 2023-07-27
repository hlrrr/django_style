from fastapi import status, HTTPException, APIRouter


auth = APIRouter(
    prefix='/auth',
    tags=['Authentication'],
    )
