from fastapi import APIRouter, Request
from controllers.PayrollrunController import PayrollrunController

router = APIRouter(
        prefix='/paroll-run'
)


@router.get('/')
def get_all():
    return PayrollrunController.get_all()


@router.post('/')
def create(request: Request):
    return PayrollrunController.create()
