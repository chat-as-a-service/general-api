from dotenv import load_dotenv

load_dotenv()

from fastapi import FastAPI


app = FastAPI()

from .routers import account
app.include_router(account.router, prefix="/accounts", tags=["accounts"])
# testing lint