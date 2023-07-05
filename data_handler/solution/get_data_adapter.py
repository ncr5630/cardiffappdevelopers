import json
from datetime import datetime


class GetData:
    def __init__(self):
        self.data = None

    def search_data_by_date_range(self, from_date, to_date):
        read_data = self.read_exit_data()
        from_date = datetime.strptime(from_date, '%Y-%m-%d').date()
        to_date = datetime.strptime(to_date, '%Y-%m-%d').date()
        search_results = []
        for record in read_data:
            time_str = record['time']
            time_format = '%Y-%m-%dT%H:%M:%S.%fZ'
            record_date = datetime.strptime(time_str, time_format).date()
            if from_date <= record_date <= to_date:
                search_results.append(record)
        return search_results, 200

    @staticmethod
    def read_exit_data():
        data_list = []
        # Read existing data from the JSON file
        try:
            with open('data/data.json', 'r') as file:
                data_list = json.load(file)
        except FileNotFoundError:
            pass

        return data_list
