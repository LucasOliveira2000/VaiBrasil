from abc import ABC, abstractmethod


class BaseCrawler(ABC):
    def __init__(self, crawler_id: int, fonte_id: int):
        self.crawler_id = crawler_id
        self.fonte_id = fonte_id

    @abstractmethod
    def run(self):
        pass
