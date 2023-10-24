from pathlib import Path

from dotenv import load_dotenv, find_dotenv
from pydantic import BaseSettings


def _build_path(file_name):
    path = Path(__file__).absolute().parent.parent.parent / file_name
    return path


class EnvConfig(BaseSettings):
    """
    Variables contained in this model will attempt to load from .env or environment and if variable is missing,
    it will throw an exception.
    """

    USER_NAME: str
    PASSWORD: str

    BASE_URL: str


load_dotenv(find_dotenv(_build_path('.env')))
config = EnvConfig()
