from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    SECRET_KEY: str
    ALGORITHM: str 
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    DATABASE_URL: str
    
    # class Config:
    #     env_file = ".env"
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()