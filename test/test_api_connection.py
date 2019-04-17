from pandas import DataFrame
from pytest import raises

from src.fantasyprem.api_connectors.event import EventConnection
from src.fantasyprem.api_connectors.player import PlayerConnection
from src.fantasyprem.api_connectors.player_summary import PlayerSummaryConnection


def test_get_player_summary_content():
    """
    Tests that the API returns a list of dictionaries
    """
    con = PlayerSummaryConnection()
    content = con.get_content()
    assert all(isinstance(item, dict) for item in content)


def test_get_player_ids():
    """
    Tests that the API returns a list of player ids
    """
    con = PlayerSummaryConnection()
    player_id_list = con.get_player_ids()
    assert type(player_id_list) is list
    assert all(isinstance(item, int) for item in player_id_list)


def test_get_history():
    """
    Tests that the API returns a list of dictionaries, and that an invalid player returns an
    assertion error
    """
    with raises(AssertionError):
        PlayerConnection(0)
    con = PlayerConnection(1)
    player_history = con.get_history()
    assert all(isinstance(item, dict) for item in player_history)


def test_get_event_content():
    """
    Tests that the API returns a list of dictionaries
    """
    con = EventConnection()
    content = con.get_content()
    assert all(isinstance(item, dict) for item in content)
    content = con.get_content(as_pandas=True)
    assert type(content) is DataFrame
