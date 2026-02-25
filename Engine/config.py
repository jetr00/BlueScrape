from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache
import os

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
env_path = os.path.join(project_root, '.env')

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