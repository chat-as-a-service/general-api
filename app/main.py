from dotenv import load_dotenv
load_dotenv()
import logging  # noqa: F401, E402
from app.core.api_key_auth import check_api_token  # noqa: E402
from fastapi import FastAPI, Depends  # noqa: E402


app = FastAPI(dependencies=[
    Depends(check_api_token)
])

from .routers import account  # noqa: E402
app.include_router(account.router, prefix="/accounts", tags=["accounts"])
