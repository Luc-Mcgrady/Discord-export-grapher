from lib import discordjson
import pandas as pd
import datetime
import copy
import bar_chart_race as bcr

if __name__ == '__main__':
    messages = discordjson.json_to_messages("messages.json")

    word_counts = {}
    date_words = {}

    # Config start

    data_distance = datetime.timedelta(days=14)
    bar_count = 30

    # Config end

    last_day_record = datetime.datetime.fromordinal(1)
    used_words = []
    for message in messages[:]:
        message_words = message.get_content().split(' ')

        for word in message_words:  # Count the words in the message and add them to the

            if word in word_counts:
                word_counts[word] += 1
            else:
                word_counts[word] = 1

        if message.get_datetime() >= last_day_record + data_distance:
            sorted_word_counts = {k: v for k, v in sorted(word_counts.items(), key=lambda a: a[1], reverse=True)}
            date_words[message.get_datetime()] = copy.copy(word_counts)

            for key in list(sorted_word_counts.keys())[:bar_count]:
                if key not in used_words:
                    used_words.append(key)  # used for removing words that don't appear in the animation

            last_day_record = message.get_datetime()

    # used_words = [key for key, val in word_counts.items() if val > used_threshold]
    used_date_words = {}

    for key in date_words.keys():
        used_date_words[key] = {}
        for word in used_words:
            if word in date_words[key]:
                used_date_words[key][word] = date_words[key][word]
            else:
                used_date_words[key][word] = 0

    plot = pd.DataFrame(used_date_words.values(), index=used_date_words.keys())
    print(plot)
    print(used_words)

    bcr.bar_chart_race(plot,
                       filename="newstuff.mpeg",
                       sort="desc",
                       n_bars=bar_count,
                       period_length=500,
                       steps_per_period=20)
