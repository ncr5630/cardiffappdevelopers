import re
import json
from datetime import datetime


class StoreData:
    def __init__(self):
        self.data = None

    def save_records(self, records):

        data = records.decode('utf-8')

        # checking data is malformed
        if self.check_malformed(data):
            return {"success": False}, 500
        # match pattern
        pattern = r'(\d+)\s+(\w+)\s+([\d.]+)'
        matches = re.findall(pattern, data)
        read_exit_data = self.read_exit_data()
        for match in matches:
            if match[0] != '':
                timestamp = match[0]
                name = match[1]
                value = match[2]
            # converting timestamp to ISO standard
            timestamp = int(timestamp)
            dt = datetime.utcfromtimestamp(timestamp)
            date_time = dt.strftime('%Y-%m-%dT%H:%M:%S.000Z')

            data_dict = {
                'time': date_time,
                'name': name,
                'Value': value
            }
            read_exit_data.append(data_dict)

        # Write the updated data to the JSON file
        with open('data/data.json', 'w') as file:
            unique_data = self.remove_duplicates(read_exit_data)
            json.dump(unique_data, file, indent=4)
        return {"success": True}, 200

    @staticmethod
    def check_malformed(data):
        lines = data.split("\n")
        for line in lines:
            pattern = r'(\d+)\s+([\d.]+)\s+(\w+)$'
            matches = re.match(pattern, line)
            if matches:
                return True
        return False

    @staticmethod
    def remove_duplicates(data_list):

        # Create a set of tuples representing unique records
        unique_records = set(tuple(d.items()) for d in data_list)

        # Convert the set back to a list of dictionaries
        unique_data_list = [dict(record) for record in unique_records]
        return unique_data_list

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
