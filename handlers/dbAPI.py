from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy import Column, Integer, String, update
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.future import select

# залупа базовая для класса
Base = declarative_base()

# Короче таблицу для sqlalchemy представляю чтобы он понял
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    TGid = Column(Integer, unique=True, nullable=False)
    username = Column(String, unique=True)
    fName = Column(String)

# асинхронный движок и сессию
engine = create_async_engine("sqlite+aiosqlite:///xddDB.db", echo=True)
Session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

# Асинхронная функция для добавления нового пользователя
async def getUserInfo(TGid, username, fName):
    async with Session() as session:
          async with session.begin():
               # Проверка на существование пользователя
               isUser = select(User).where(User.TGid == TGid)
               result = await session.execute(isUser)
               user = result.scalars().first()
               #   if user is not None and (User.username != username or User.fName != fName):
               if user:
                    if user.username != username or user.fName != fName:
                         newUser = update(User).where(User.id == user.id).values(username=username, fName=fName)
                         await session.execute(newUser)
                         await session.commit()
                    return user
               else:
                    # Создаем нового пользователя
                    newUser = User(TGid=TGid, username=username, fName=fName)
                    session.add(newUser)
                    await session.commit()
                    return newUser

# Пример использования
import asyncio

async def main():
    user = await getUserInfo(12345, "testuser", "Test")
    print(f"User: {user.username}, First Name: {user.fName}")

asyncio.run(main())
