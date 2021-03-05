from lib import discordjson
from collections import Counter

# import matplotlib.pyplot as plt

if __name__ == '__main__':
    messages = discordjson.json_to_messages("messages.json")

    startday = messages[0].get_datetime().date()

    message_days = {}  # Messages seperated into days

    lastday = -1
    for message in messages:
        currentday = (message.get_datetime().date() - startday).days
        if currentday != lastday:
            message_days[currentday] = []
        message_days[currentday].append(message)
        lastday = currentday

    messagesent = []
    total_days = max(message_days)

    for day in range(total_days):
        if day not in message_days:
            messagesent.append(())
            continue

        todays_authors = []
        for message in message_days[day]:
            author = message.values["author"]["name"]
            if author not in todays_authors:
                todays_authors.append(author)

        messagesent.append(tuple(sorted(todays_authors)))

    outstring = "Who messaged on how many days:\n"  # The string that will be printed

    for authors, count in Counter(messagesent).items():
        if len(authors) == 0:
            outstring += "Nobody"
        else:
            outstring += ", ".join(authors)  # This is probably bad practice but to make it worse I wont explain why

        outstring += ": %r\n" % count

    print(outstring)
