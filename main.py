from fastapi import FastAPI

from routes.user import router as user_router


server = FastAPI()

server.include_router(user_router)
