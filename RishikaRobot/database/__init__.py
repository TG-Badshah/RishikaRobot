

from async_pymongo import AsyncClient

from RishikaRobot import MONGO_DB_URI

DBNAME = "RishikaRobot"

mongo = AsyncClient(MONGO_DB_URI)
dbname = mongo[DBNAME]
