from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routes.integration_conf import get_integration_config as intergration_route
from api.router import api_router
from core.config import settings

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#integration_route
app.include_router(intergration_route)

#app-route
app.include_router(api_router, prefix=settings.API_PREFIX)


@app.get("/healthcheck")
async def health_check():
    """Checks if server is active."""
    return {"status": "active"}
