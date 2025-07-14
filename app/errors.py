from fastapi import Request, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from sqlalchemy.exc import NoResultFound
from starlette.exceptions import HTTPException as StarletteHTTPException


def add_exception_handlers(app):
    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request: Request, exc: RequestValidationError):
        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            content={"error": "Validation Error", "details": exc.errors()},
        )

    @app.exception_handler(NoResultFound)
    async def not_found_handler(request: Request, exc: NoResultFound):
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"error": "Order not found"},
        )

    @app.exception_handler(StarletteHTTPException)
    async def http_exception_handler(request: Request, exc: StarletteHTTPException):
        return JSONResponse(
            status_code=exc.status_code,
            content={"error": exc.detail},
        )

    @app.exception_handler(Exception)
    async def general_exception_handler(request: Request, exc: Exception):
        return JSONResponse(
            status_code=500,
            content={"error": "Internal server error"},
        )
