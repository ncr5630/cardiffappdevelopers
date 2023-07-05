import re

from solution.abstract_adapter_main import ApplicationMain
from solution.data_store_adapter import StoreData
from solution.get_data_adapter import GetData


class ApplicationService(ApplicationMain):
    def __init__(self):
        self.save_data_obj = StoreData()
        self.get_data_obj = GetData()

    def get_records_data(self, from_date, to_date):
        return self.get_data_obj.search_data_by_date_range(from_date, to_date)

    def save_recorded_data(self, records):
        return self.save_data_obj.save_records(records)




