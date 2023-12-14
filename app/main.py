# flake8: noqa: E402
from dotenv import load_dotenv

load_dotenv()
import sentry_sdk
from prometheus_fastapi_instrumentator import Instrumentator
from .settings import settings
from .core.log import getLogger
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

log = getLogger(__name__)

sentry_sdk.init(
    dsn="https://examplePublicKey@o0.ingest.sentry.io/0",
    enable_tracing=True,
)
if settings.disable_docs:
    app = FastAPI(redoc_url=None, docs_url=None, openapi_url=None)
    log.info("FASTAPI Docs URLs disabled")
else:
    app = FastAPI()

from .routers import (
    user,
    account,
    channel,
    organization,
    application,
    attachment,
    health,
)

app.include_router(account.router, prefix="/accounts", tags=["accounts"])
app.include_router(account.secured_router, prefix="/accounts", tags=["accounts"])
app.include_router(attachment.router, prefix="/attachments", tags=["attachments"])
app.include_router(organization.router, prefix="/organizations", tags=["organizations"])
app.include_router(user.router, prefix="/users", tags=["users"])
app.include_router(channel.router, prefix="/channels", tags=["channels"])
app.include_router(application.router, prefix="/applications", tags=["applications"])
app.include_router(health.router, prefix="/health", tags=["health"])

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
Instrumentator().instrument(app).expose(app)
