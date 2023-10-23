from typing import List
from fastapi.routing import APIRouter
from fastapi import Depends
from .services import UserService
from .models import CreateUserModel, RetrieveUserModel, UpdateUserModel


router = APIRouter()


@router.get('/users/', response_model=List[RetrieveUserModel], status_code=200)
async def get_all_users(service: UserService = Depends(UserService)):
    return await service.get_all_users()


@router.get('/users/{user_id}', response_model=RetrieveUserModel, status_code=200)
async def get_user(user_id: int, service: UserService = Depends(UserService)):
    return await service.get_user(user_id)


@router.post('/users/', response_model=RetrieveUserModel, status_code=201)
async def create_user(user_model: CreateUserModel, service: UserService = Depends(UserService)):
    return await service.create_user(user_model)


@router.patch('/users/{user_id}', response_model=RetrieveUserModel, status_code=200)
async def update_user(user_model: UpdateUserModel, user_id: int, service: UserService = Depends(UserService)):
    return await service.update_user(user_id, user_model)
