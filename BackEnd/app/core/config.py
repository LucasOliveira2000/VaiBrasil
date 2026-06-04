from pydantic_settings import BaseSettings

class Config(BaseSettings):
    
    # Local ou produção
    APP_ENV: bool
    
    # Configurações de banco de dados
    DATABASE_URL: str
    
    # Configurações de autenticação
    SECRET_KEY: str
    
    model_config = {
        "env_file": ".env",
        "env_file_encoding": "utf-8",
        "extra": "ignore"
    }
    
config = Config()