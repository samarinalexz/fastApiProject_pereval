from fastapi import APIRouter

router = APIRouter(
    prefix="/pereval",
    tags=['Pereval']
)


@router.get("/")
async def get_pereval():
    return