from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.jobstores.mongodb import MongoDBJobStore
from pymongo import MongoClient

from services import GlobalConfigService
from helpers import singleton


@singleton
class JobsService(AsyncIOScheduler):
    def __init__(self, config: GlobalConfigService):
        self.__client = MongoClient(config.mongo_connstring)
        self.__jobstore = MongoDBJobStore(
            database='apscheduler', collection='jobs', client=self.__client)

        super().__init__()
        self.add_jobstore(self.__jobstore)
        self.start()
