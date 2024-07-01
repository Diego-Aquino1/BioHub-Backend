from fastapi import Request, APIRouter, HTTPException
from fastapi.encoders import jsonable_encoder
from datetime import datetime

from routers.algorithms.controllers.get_all_users_controller import ProductsAllController
from routers.algorithms.controllers.needleman_wunsh_controller import NeedlemanWunshController
from routers.algorithms.schemas.algorithms_schema import NeedlemanWunshBody

router = APIRouter(prefix="/algorithms")

# =============== GET -> Create products ===============
@router.get("/")
def get_products():
    return jsonable_encoder({"rpta", "Products"})

@router.get("/all", status_code = 200)
# def get_roles(auth = Auth()):
def get_roles():
    controller = ProductsAllController()
    # return jsonable_encoder(controller.run(auth))
    return jsonable_encoder(controller.run())

@router.post('/needleman', status_code=200)
def update_transportation(body: NeedlemanWunshBody):
    controller = NeedlemanWunshController(body)
    return jsonable_encoder(
        controller.run()
    )