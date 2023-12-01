from dotenv import load_dotenv

load_dotenv()
import logging  # noqa: F401, E402
from app.core.api_key_auth import check_api_token  # noqa: E402
from fastapi import FastAPI, Depends  # noqa: E402

<<<<<<< Updated upstream
=======
from fastapi import FastAPI  # noqa: E402
>>>>>>> Stashed changes

app = FastAPI(dependencies=[Depends(check_api_token)])

from .routers import account, organization  # noqa: E402

app.include_router(account.router, prefix="/accounts", tags=["accounts"])
app.include_router(organization.router, prefix="/organizations", tags=["organizations"])
