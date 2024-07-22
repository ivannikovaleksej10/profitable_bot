from app.database.models import async_session
from app.database.models import User
from sqlalchemy import select, update, delete


async def set_user(tg_id: int) -> None:
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))

        if not user:
            session.add(User(tg_id=tg_id))
            await session.commit()


# async def set_all_money(all_money: int) -> None:
#     async with async_session() as session:
#         await session.scalar(select(User).where(User.all_money == all_money))
#         session.add(User(all_money=all_money))
#         await session.commit()