# https://github.com/Tyrrrz/DiscordChatExporter as json
import json
import datetime


class DiscordMessage:
    """Holds the json values of a message exported by https://github.com/Tyrrrz/DiscordChatExporter as json"""
    def __init__(self, jsondict: dict):
        assert type(jsondict) == dict
        self.values = jsondict

    def get_datetime(self, time_string: str = None):
        """Gets a datetime class based on the messages timestamp"""
        if time_string is None:
            time_string = self.values["timestamp"]

        # print(time_string)
        time_string = time_string.split('T')

        year, month, day = [int(a) for a in time_string[0].split('-')]

        time_string = time_string[1].split('+')[0].split(':')

        hour, minute, second = [int(a.split('.')[0]) for a in time_string[:3]]

        # print(year, month, day, hour, minute, int(second))
        # print(second)

        return datetime.datetime(year, month, day, hour, minute, int(second))

    def get_content(self) -> str:
        """Neater optional get function for the message text"""
        return self.values["content"]


def json_to_messages(filename: str):
    """Gets a list of DiscordMessage objects containing the json of the file"""
    try:
        vals = json.load(open(filename, 'r', encoding="utf8"))["messages"]
    except FileNotFoundError as e:
        raise type(e)("Name your json file messages.json and put it in the directory with this file")

    return [DiscordMessage(a) for a in vals]


if __name__ == '__main__':
    for message in json_to_messages("../messages.json"):
        print(message.get_datetime())
