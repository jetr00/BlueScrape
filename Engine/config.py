from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache
import os

engine_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(engine_dir)
env_path = os.path.join(project_root, 'apis', 'apis.env')

class APIS(BaseSettings):
    news_api_key: str
        
    model_config = SettingsConfigDict(
        env_file = env_path,
        env_file_encoding = 'utf-8',
        case_sensitive = False,
        extra = 'ignore'
    )

@lru_cache()
def get_settings():
    return APIS()