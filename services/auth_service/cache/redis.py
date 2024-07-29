from fastapi import HTTPException

import redis

from utils.base.config import settings


class RedisRepository:
    def __init__(self):
        setting = settings.radis

        self.redis = redis.Redis(
            host=setting.host,
            port=setting.port,
            db=0,
            decode_responses=True
            # protocol=3
        )

    async def is_key_exit(self, key):
        if not self.redis.exists(key):
            raise HTTPException(status_code=404, detail="Key not found")

    async def create(self, key: str, value: any) -> bool:
        try:
            self.redis.set(key, value)
            return True
        except Exception as error:
            raise HTTPException(status_code=400, detail=str(error))

    async def update(self, key: str, value: any) -> bool:
        try:
            await self.is_key_exit(key)
            self.redis.set(key, value)
            return True
        except Exception as error:
            raise HTTPException(status_code=400, detail=str(error))

    async def get(self, key: str) -> any:
        try:
            data = self.redis.get(key)
            return data
        except Exception as error:
            raise HTTPException(status_code=400, detail=str(error))

    async def delete(self, key: str) -> bool:
        try:
            await self.is_key_exit(key)
            return self.redis.delete(key)
        except Exception as error:
            raise HTTPException(status_code=400, detail=str(error))


RedisRepository = RedisRepository()
