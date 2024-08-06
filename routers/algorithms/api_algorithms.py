from fastapi import Request, APIRouter, HTTPException
from fastapi.encoders import jsonable_encoder
from datetime import datetime

from routers.algorithms.controllers.average_clustering_controller import AverageLinkageClusteringController
from routers.algorithms.controllers.complete_clustering_controller import CompleteLinkageClusteringController
# from routers.algorithms.controllers.get_all_users_controller import ProductsAllController
from routers.algorithms.controllers.needleman_wunsh_controller import NeedlemanWunshController
from routers.algorithms.controllers.sequence_identifier_controller import SequenceIdentifierController
from routers.algorithms.controllers.single_clustering_controller import SingleLinkageClusteringController
from routers.algorithms.controllers.smith_waterman_controller import SmithWatermanController
from routers.algorithms.controllers.star_alignment_controller import StarAlignmentController
from routers.algorithms.schemas.algorithms_schema import AlignmentBody, ClusteringBody

router = APIRouter(prefix="/algorithms")

# =============== GET -> Create products ===============
@router.get("/")
def get_products():
    return jsonable_encoder({"rpta", "Products"})

# @router.get("/all", status_code = 200)
# # def get_roles(auth = Auth()):
# def get_roles():
#     controller = ProductsAllController()
#     # return jsonable_encoder(controller.run(auth))
#     return jsonable_encoder(controller.run())

@router.get('/identify/{seq}', status_code=200)
def update_transportation(seq: str):
    controller = SequenceIdentifierController()
    return jsonable_encoder(
        controller.run(seq)
    )

@router.post('/needleman', status_code=200)
def update_transportation(body: AlignmentBody):
    controller = NeedlemanWunshController(body)
    return jsonable_encoder(
        controller.run()
    )

@router.post('/waterman', status_code=200)
def update_transportation(body: AlignmentBody):
    controller = SmithWatermanController(body)
    return jsonable_encoder(
        controller.run()
    )

@router.post('/star_alignment', status_code=200)
def star_alignment(body: AlignmentBody):
    controller = StarAlignmentController(body)
    return jsonable_encoder(
        controller.run()
    )

@router.post("/single-linkage")
async def single_linkage_clustering(body: ClusteringBody):
    controller = SingleLinkageClusteringController(body)
    try:
        response = controller.run()
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/complete-linkage")
async def complete_linkage_clustering(body: ClusteringBody):
    controller = CompleteLinkageClusteringController(body)
    try:
        response = controller.run()
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# @router.post("/average-linkage")
# async def average_linkage_clustering(body: ClusteringBody):
#     controller = AverageLinkageClusteringController(body)
#     try:
#         response = controller.run()
#         return response
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))