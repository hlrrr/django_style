from fastapi import status, HTTPException, APIRouter, Depends
from fastapi.security.oauth2    import OAuth2PasswordRequestForm
from typing     import Annotated, Union
from sqlalchemy.orm     import Session

import app.common.schemas  as schemas
import app.common.utils     as utils
from app.database.database  import MyAlchemy as ma

router = APIRouter()

@router.post(path="/signup",
             status_code=status.HTTP_201_CREATED,
             response_model=schemas.UserInfo)
def create_user(user: schemas.UserInfo,
                db:Annotated[Session, Depends(ma.get_databse)]):
    
    query = db.query(user).filter(user.email == user.email)
    if query.first() is not None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"already exists, email={user.email}")
    
    hashed_pswd = utils.hash(user.password)
    user.password = hashed_pswd
    
    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)    # show the new post
    return new_user


# @router.post('/token', 
#              status_code=status.HTTP_200_OK,
#              response_model=schemas.Token)
# def token():
#     access_token = oauth2.token_create(data={'user_id':3})
#     return {'access_token':access_token, 'token_type':'bearer'}

    
@router.post('/login', 
             status_code=status.HTTP_200_OK,
             response_model=schemas.Token)
def login(db:database,
          user_credentials:OAuth2PasswordRequestForm=Depends()):
    user = db.query(models.User).filter(models.User.email == user_credentials.username).first()     # fields of OAuth2PasswordRequestForm  -> username, password

    if user is None:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f'Invalid Credentials')
    elif not utils.verify(user_credentials.password, user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f'Invalid Credentials')
    
    access_token = oauth2.token_create(data={'user_id':user.id})
    return {'access_token':access_token, 'token_type':'bearer'}


@router.get("/{id}",
            status_code=status.HTTP_200_OK,
            response_model=schemas.UserInfo)
def get_user(id: int,
             db:database):
    user = db.query(models.User).filter(models.User.id == id).first()

    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail = f"not exists, user_id = {id}")
    return user