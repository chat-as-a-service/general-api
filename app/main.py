from dotenv import load_dotenv


load_dotenv()
import logging  # noqa: F401, E402

from fastapi import FastAPI  # noqa: E402
from fastapi.middleware.cors import CORSMiddleware  # noqa: E402

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

from .routers import account  # noqa: E402
from .routers import attachment  # noqa: E402

app.include_router(account.router, prefix="/accounts", tags=["accounts"])
app.include_router(attachment.router, prefix="/attachments", tags=["attachments"])
