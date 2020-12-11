from lib import discordjson
# import matplotlib.pyplot as plt

if __name__ == '__main__':
    messages = discordjson.json_to_messages("messages.json")

    startday = messages[0].get_datetime().date()

    total_days = (messages[-1].get_datetime().date() - startday).days

    messagesent = []

    messagedates = [(message.get_datetime().date() - startday).days for message in messages]

    for day in range(total_days):
        messagesent.append(day in messagedates)

    # print(messagesent)
    print(
        """Days since first message sent = {days}
Days where messages were sent = {}/{days}
Days where messages were not sent = {}/{days}""".format(
            sum(messagesent), total_days - sum(messagesent), days=total_days))
