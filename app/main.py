from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import (
    balance_token,
    balanced_pool,
    balanced_dividends,
    balanced_dollars,
    balanced_rewards,
    balanced_tvl,
    balanced_users
)

app = FastAPI(
    title="Balanced Stats API",
)
api_version = "2"

origins = [
    "http://localhost:1313",
    "https://brianli.com"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(balance_token.router, prefix=f"/api/v{api_version}")
app.include_router(balanced_dividends.router, prefix=f"/api/v{api_version}")
app.include_router(balanced_dollars.router, prefix=f"/api/v{api_version}")
app.include_router(balanced_pool.router, prefix=f"/api/v{api_version}")
app.include_router(balanced_rewards.router, prefix=f"/api/v{api_version}")
app.include_router(balanced_tvl.router, prefix=f"/api/v{api_version}")
app.include_router(balanced_users.router, prefix=f"/api/v{api_version}")
