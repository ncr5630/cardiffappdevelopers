from abc import ABC, abstractmethod

class ApplicationMain(ABC):

    @abstractmethod
    def get_records_data(self, from_date, to_date):
        pass

    @abstractmethod
    def save_recorded_data(self, body):
        pass
