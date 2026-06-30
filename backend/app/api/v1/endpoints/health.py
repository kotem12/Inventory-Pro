from fastapi import APIRouter

router = APIRouter(tags=["Health"])


@router.get("/health")
async def health_check():
    """
    Health check endpoint.

    Used by load balancers, monitoring systems,
    Docker health checks, and Kubernetes probes.
    """
    return {
        "status": "healthy",
    }
