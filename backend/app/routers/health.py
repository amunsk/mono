from fastapi import APIRouter, status

router = APIRouter(prefix="/health", tags=["Health"])

@router.get("", status_code=status.HTTP_200_OK)
async def healthcheck() -> dict[str, str]:
    """Liveness probe."""
    return {"status": "ok"}
