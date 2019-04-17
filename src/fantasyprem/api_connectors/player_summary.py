from json import loads
import pandas as pd
from requests import get


class PlayerSummaryConnection:
    """
    Connection to https://fantasy.premierleague.com/drf/elements/
    """

    def __init__(self):
        self.url = "https://fantasy.premierleague.com/drf/elements/"
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

    def get_player_ids(self):
        """
        Extracts all player ID values from the summary
        :return: a list of player ids
        """
        return [i["id"] for i in self.get_content()]
