from fastapi import APIRouter

router = APIRouter()


@router.post("/session_tokens")
async def create_account(dto: AccountCreate, db: Session = Depends(get_db)):
    return await account_service.create_account(dto, db)
