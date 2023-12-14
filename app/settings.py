from typing import Optional

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    db_user: str = "postgres"
    db_password: str
    db_host: str = "localhost"
    db_port: int = 5432
    db_db: str
    secret_key: str
    attachment_bucket_name: str = "caas-attachments"
    gcp_key_file_path: str
    print_sql_queries: bool = False
    disable_docs: bool = True
    sentry_dsn: Optional[bool] = None


settings = Settings()
