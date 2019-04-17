from json import loads
import pandas as pd
from requests import get


class PlayerConnection:
    """
    Connection to https://fantasy.premierleague.com/drf/element-summary/{element_id}
    """

    def __init__(self, element_id):
        self.url = "https://fantasy.premierleague.com/drf/element-summary/"
        self.element_id = element_id
        self.url = "{url}{element}".format(url=self.url, element=self.element_id)
        self.response = get(self.url)
        if self.response.status_code != 200:
            raise AssertionError("API connection was unsuccessful")

    def get_history(self, as_pandas=False):
        """
        Gets the content of an API request
        :return: Content of API requests
        """
        if as_pandas:
            return pd.DataFrame(loads(self.response.content)["history"])
        else:
            return loads(self.response.content)["history"]
