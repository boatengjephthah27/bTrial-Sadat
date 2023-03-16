from fastapi import FastAPI, Depends, status, HTTPException, UploadFile, Form
from fastapi.responses import FileResponse
import uvicorn
import os
from .schemas import User, ShowUser, ShowLogoImage, ShowProfileImage, ProfileImage, ImageCreate
from . import models
from .database import engine, SessionLocal
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from typing import List, Dict, Union
from fastapi.staticfiles import StaticFiles
import shutil
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path


app = FastAPI()

app.mount("/images", StaticFiles(directory="images"), name="images")

models.Base.metadata.create_all(engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

BASE_DIR = Path(__file__).resolve().parent.parent
STATIC_ROOT = os.path.join(BASE_DIR, 'images')

pwd_cntxt = CryptContext(schemes=["bcrypt"], deprecated='auto')


# User Routes ....................................................................................................

@app.post('/users', tags=['Users'], response_model=ShowUser, status_code=status.HTTP_201_CREATED,)
async def create_user(request: User, db: Session = Depends(get_db)):
    hashed_pwd = pwd_cntxt.hash(request.password)
    user = models.User(
        email=request.email,
        first_name=request.first_name.capitalize(),
        last_name=request.last_name.capitalize(),
        password=hashed_pwd,
        is_active=True if request.is_active == 1 else False,
        user_type=request.user_type,
        company_name=request.company_name,
        phone=request.phone
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


@app.post("/profileimages", tags=['Profile Images'], status_code=status.HTTP_201_CREATED,)
async def create_image(myimage: UploadFile, db: Session = Depends(get_db)) -> Path:

    file_path = Path(f"images/profileimages/{myimage.filename}")

    try:
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(myimage.file, buffer)
            global tmp_path
            tmp_path = Path(buffer.name)

    finally:
        myimage.file.close()

    # db_image = models.ProfileImages(image=tmp_path, user_id=1)

    # db.add(db_image)
    # db.commit()
    # db.refresh(db_image)

    return tmp_path
    # return {'db': db_image, 'fpath': tmp_path}

    # return {"id": db_image.id, "image": db_image.image, "user_id": db_image.user_id}


# @app.post("/profileimages", tags=['Profile Images'], response_model=ShowProfileImage)
# async def create_image(request: ImageCreate, db: Session = Depends(get_db)):
#     file_path = f"images/{request.file.filename}"
#     with open(file_path, "wb") as buffer:
#         shutil.copyfileobj(request.file.file, buffer)
#     db_image = models.ProfileImages(image=file_path, user_id=request.user_id)
#     db.add(db_image)
#     db.commit()
#     db.refresh(db_image)
#     return {"id": db_image.id, "image": db_image.image}


@app.get('/users', tags=['Users'], response_model=List[ShowUser])
async def get_users(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    return users


@app.put('/users/{id}', status_code=status.HTTP_202_ACCEPTED, tags=['Users'])
def update_user(id: int, request: User, db: Session = Depends(get_db)):
    hashed_pwd = pwd_cntxt.hash(request.password)
    user = db.query(models.User).filter(models.User.id == id)
    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Update Unsuccessful, No user with id {id}')
    user.update(
        {
            'email': request.email,
            'first_name': request.first_name.capitalize(),
            'last_name': request.last_name.capitalize(),
            'password': hashed_pwd,
            'is_active': True if request.is_active == 1 else False,
            'user_type': request.user_type,
            'company_name': request.company_name,
            'phone': request.phone
        }
    )
    db.commit()
    return 'Update Successful'


@app.delete('/users/{id}', tags=['Users'])
def delete_user(id, db: Session = Depends(get_db)):
    db.query(models.User).filter(models.User.id ==
                                 id).delete(synchronize_session=False)
    db.commit()
    return 'User Deleted'


# Property Routes ....................................................................................................


if __name__ == "__main__":
    uvicorn.run(app)


# @app.post('/blog', status_code=status.HTTP_201_CREATED, tags=['Blogs'], response_model=ShowBlog)
# def create(request: Blogs, db: Session = Depends(get_db)):
#     new_post = models.Blogs(title=request.title,
#                             body=request.body, user_id=request.user_id)
#     db.add(new_post)
#     db.commit()
#     db.refresh(new_post)
#     return new_post


# @app.get('/blog', tags=['Blogs'])
# def blog(db: Session = Depends(get_db)):
#     posts = db.query(models.Blogs).all()
#     return posts


# @app.put('/blog/{id}', status_code=status.HTTP_202_ACCEPTED, tags=['Blogs'])
# def update_(id: int, request: Blogs, db: Session = Depends(get_db)):
#     post = db.query(models.Blogs).filter(models.Blogs.id == id)
#     if not post.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f'Update Unsuccessful, No post with id {id}')
#     post.update({'title': request.title, 'body': request.body})
#     db.commit()
#     return 'Update Successful'


# @app.get('/blog/{id}', status_code=status.HTTP_404_NOT_FOUND, tags=['Blogs'])
# def get_post(id: int, db: Session = Depends(get_db)):
#     post = db.query(models.Blogs).filter(models.Blogs.id == id).first()
#     if not post:
#         return 'Post does not Exist'
#     return post


# @app.delete('/blog/{id}', tags=['Blogs'])
# def delete_post(id, db: Session = Depends(get_db)):
#     db.query(models.Blogs).filter(models.Blogs.id ==
#                                   id).delete(synchronize_session=False)
#     db.commit()
#     return 'Post Deleted '
