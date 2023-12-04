from dotenv import load_dotenv

load_dotenv()
import logging  # noqa: F401, E402

from fastapi import FastAPI  # noqa: E402

app = FastAPI()

from .routers import account, organization  # noqa: E402

app.include_router(account.router, prefix="/accounts", tags=["accounts"])
app.include_router(organization.router, prefix="/organizations", tags=["organizations"])

from app.routers import user

app.include_router(user.router, prefix="/users", tags=["users"])

from app.routers import channel

app.include_router(channel.router, prefix="/channels", tags=["channels"])