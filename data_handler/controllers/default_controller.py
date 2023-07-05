import connexion
# import six
#
# from utils import util
from solution.data_adapter_main import ApplicationService

service_obj = ApplicationService()


def create_records(body):  # noqa: E501
    """Save data

    Save data with timestamp, metric_name, and metric_value # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = str.from_dict(connexion.request.get_json())  # noqa: E501
    return service_obj.save_recorded_data(body)


def get_data(from_date, to_date):  # noqa: E501
    """Get data

    Retrieve data within a specified time range # noqa: E501

    :param _from: Start date (yyyy-mm-dd)
    :type _from: str
    :param to: End date (yyyy-mm-dd)
    :type to: str

    :rtype: None
    """
    return service_obj.get_records_data(from_date, to_date)
