from typing import Optional

from pydantic import BaseSettings, EmailStr

SECRET = 'SECRET'
FOUNDATION_KYTTI = 'Кошачий благотворительный фонд'
DISCRIPTION_APP = 'Сервис для поддержки котиков!'
DB_URL = 'sqlite+aiosqlite:///./charity_project_donation.db'
ENV = '.env'


class Settings(BaseSettings):
    app_title: str = FOUNDATION_KYTTI
    app_description: str = DISCRIPTION_APP
    database_url: str = DB_URL
    secret: str = SECRET
    first_superuser_email: Optional[EmailStr] = None
    first_superuser_password: Optional[str] = None

    class Config:
        env_file = ENV


settings = Settings()
