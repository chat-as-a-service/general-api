from fastapi import Request

from app.schemas.account import AccountPrincipal


class AuthRequest(Request):
    account: AccountPrincipal
