from json import loads
import pandas as pd
from requests import get


class EventConnection:
    """
    Connection to https://fantasy.premierleague.com/drf/events/
    """

    def __init__(self):
        self.url = "https://fantasy.premierleague.com/drf/events/"
        self.response = get(self.url)
        if self.response.status_code != 200:
            raise AssertionError("API connection was unsuccessful")

    def get_content(self, as_pandas=False):
        """
        Gets the content of an API request
        :return: Content of API requests
        """
        if as_pandas:
            return pd.DataFrame(loads(self.response.content))
        else:
            return loads(self.response.content)
