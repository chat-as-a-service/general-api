from dotenv import load_dotenv

load_dotenv()
import logging  # noqa: F401, E402

from fastapi import FastAPI # noqa: E402

app = FastAPI()

from .routers import account  # noqa: E402

app.include_router(account.router, prefix="/accounts", tags=["accounts"])
