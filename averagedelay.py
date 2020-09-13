from discordexport import json_to_messages

if __name__ == '__main__':

    try:

        messages = json_to_messages("messages.json")
        last_author_ID = messages[0].values["author"]["id"]
        last_time = messages[0].get_datetime().timestamp()
        delays = []

        for message in messages[1:]:
            if last_author_ID != message.values["author"]["id"]:
                last_author_ID = message.values["author"]["id"]

                current_time = message.get_datetime().timestamp()
                delays.append(current_time - last_time)
                last_time = current_time

        print(sum(delays)/len(delays))

    except FileNotFoundError:
        input("Name your csv file messages.csv and put it in the directory with this file")
