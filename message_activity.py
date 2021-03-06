from lib import discordjson
from lib.plotdict import plot_dict

if __name__ == '__main__':
    messages = discordjson.json_to_messages()

    months = {}

    for message in messages:
        # messages.values["content"]
        try:
            months[str(message.get_datetime().date())[:-3]] += 1
        except KeyError:
            months[str(message.get_datetime().date())[:-3]] = 0

    plot_dict(months, False, True)
