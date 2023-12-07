import logging  # noqa: F401, E402
from fastapi import FastAPI  # noqa: E402
from app.routers import user
from .routers import account, organization  # noqa: E402

app = FastAPI()

app.include_router(account.router, prefix="/accounts", tags=["accounts"])
app.include_router(organization.router, prefix="/organizations", tags=["organizations"])

app.include_router(user.router, prefix="/users", tags=["users"])
