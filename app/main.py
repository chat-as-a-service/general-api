from dotenv import load_dotenv

load_dotenv()
import logging  # noqa: F401, E402

from fastapi import FastAPI  # noqa: E402

app = FastAPI()

from .routers import account, organization, application  # noqa: E402

app.include_router(account.router, prefix="/accounts", tags=["accounts"])
app.include_router(organization.router, prefix="/organizations", tags=["organizations"])
app.include_router(application.router, prefix="/applications", tags=["applications"])
