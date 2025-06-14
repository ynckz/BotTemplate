from dataclasses import dataclass
from environs import Env

@dataclass
class DbConfig:
    host:str
    password:str
    login:str
    database:str
    port:str

@dataclass
class Bot:
    token:str
    payments_token:str
    admin_ids: list[int]

@dataclass
class Miscellaneous:
    other_params: str = None

@dataclass
class Config:
    bot: Bot
    db:DbConfig
    misc : Miscellaneous

def load_db_config(path:str = None):
    env = Env()
    env.read_env(path)

    return DbConfig(
        login = env.str('DB_LOGIN'),
        password = env.str('DB_PASSWORD'),
        host = env.str('DB_HOST'),
        port  = env.str('DB_PORT'),
        database  = env.str('DB_NAME')
        
    )


def load_config(path:str = None):
    env = Env()
    env.read_env(path)
    return Config(
        bot = Bot(token = env.str('BOT_TOKEN'),
                  payments_token = env.str('PAYMENT_TOKEN'),
                  admin_ids = list(map(int, env.list("ADMINS")))),
        db = DbConfig(
            login=env.str('DB_LOGIN'),
            password=env.str('DB_PASSWORD'),
            host = env.str('DB_HOST'),
            port = env.str('DB_PORT'),
            database=env.str('DB_NAME')),

        misc=Miscellaneous()              
    
    )
