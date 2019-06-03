from json import loads
import pandas as pd
from requests import get


class TeamConnection:
    """
    Connection to https://fantasy.premierleague.com/drf/teams/
    """

    def __init__(self):
        self.url = "https://fantasy.premierleague.com/drf/teams/"
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
