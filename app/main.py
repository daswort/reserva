from fastapi import FastAPI, Request, Depends
from starlette.responses import JSONResponse
from app.core.middleware import configure_middlewares
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


from app.db.tenant.session import get_async_session
from app.models.tenant.user import User

from app.core.logging_config import logger

from app.core.exceptions.schemas import ErrorResponseModel

from fastapi.exceptions import RequestValidationError
from app.core.exceptions.http_exceptions import NotFoundError

from app.api.v1.endpoints import user_router, role_router


app = FastAPI()

configure_middlewares(app)

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    logger.error(f"Validation error: {exc.errors()}")
    error_response = ErrorResponseModel(
        status_code=422,
        error_code="VALIDATION_ERROR",
        message="Validation failed.",
        detail=exc.errors()
    )
    return JSONResponse(
        status_code=422,
        content=error_response.model_dump()
    )

app.include_router(role_router.router, tags=["Roles"], prefix="/api/v1/roles")
app.include_router(user_router.router, tags=["Admin User"], prefix="/api/v1/users")


@app.get("/")
def read_root():
    return {"msg": "Hello World"}

@app.get("/users/{user_id}")
async def read_user(user_id: int, session: AsyncSession = Depends(get_async_session)):
    stmt = select(User).where(User.id == user_id)
    result = await session.execute(stmt)
    user = result.scalars().first()

    if not user:
        raise NotFoundError(detail=f"User with id {user_id} not found")
     
    return user