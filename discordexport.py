# https://github.com/Tyrrrz/DiscordChatExporter as csv
import json
import datetime


class DiscordMessage:
    def __init__(self, jsondict: dict):
        assert type(jsondict) == dict
        self.values = jsondict

    def get_datetime(self, time_string: str = None):
        if time_string is None:
            time_string = self.values["timestamp"]

        #print(time_string)
        time_string = time_string.split('T')

        year, month, day = [int(a) for a in time_string[0].split('-')]

        time_string = time_string[1].split('+')[0].split(':')

        hour, minute, second = [int(a.split('.')[0]) for a in time_string[:3]]

        # print(year, month, day, hour, minute, int(second))
        # print(second)

        return datetime.datetime(year, month, day, hour, minute, int(second))


def json_to_messages(filename: str):
    vals = json.load(open(filename, 'r', encoding="utf8"))["messages"]
    return [DiscordMessage(a) for a in vals]


if __name__ == '__main__':
    for message in json_to_messages("messages.json"):
        print(message.get_datetime())
