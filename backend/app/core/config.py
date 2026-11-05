from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str = "Task Manager API"

    DEBUG: bool = False

    DATABASE_URL: str

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )


settings = Settings()


'''
What happens here?

BaseSettings reads configuration from environment variables and the .env file.

Instead of hardcoding database credentials throughout the application, we access them through:

settings.DATABASE_URL

This is important when moving between development, testing, and production environments.
'''