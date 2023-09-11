"""The main file for the application"""
from typing import Dict

from fastapi import FastAPI

app = FastAPI(
        title="Github Actions",
        description="A simple application to run some github actions"
    )


@app.get("/")
async def root() -> Dict[str, str]:
    """The root endpoint for the application

    Returns:
        Dict[str, str]: The message
    """
    return {"Message": "The API works"}