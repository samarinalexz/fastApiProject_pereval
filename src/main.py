from fastapi_users import FastAPIUsers

from fastapi import FastAPI, Depends

from src.pereval.router import router as pereval_router

app = FastAPI(
    title='src'
)


app.include_router(pereval_router)
