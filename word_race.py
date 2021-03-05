from lib import discordjson
import pandas as pd
import datetime
import copy
import bar_chart_race as bcr

if __name__ == '__main__':

    messages = discordjson.json_to_messages("messages.json")

    word_counts = {}
    date_period_words = {}
    date_total_words = {}

    # Config start

    data_distance = datetime.timedelta(days=14)
    periods_shown = 3
    bar_count = 40
    blacklist_words = ['']

    # Config end

    last_day_record = messages[0].get_datetime()
    used_words = []
    for message in messages[:]:
        message_words = message.get_content().split(' ')

        for word in message_words:  # Count the words in the message and add them to the
            word = word.lower()

            if word in blacklist_words:
                continue

            if word in word_counts:
                word_counts[word] += 1
            else:
                word_counts[word] = 1

        if message.get_datetime() >= last_day_record + data_distance:

            period_word_counts = copy.copy(word_counts)

            if len(date_total_words) >= periods_shown:
                sub_dict = list(date_total_words.values())[-periods_shown]
                for word in sub_dict:
                    period_word_counts[word] -= sub_dict[word]

            date_period_words[message.get_datetime()] = copy.copy(period_word_counts)
            date_total_words[message.get_datetime()] = copy.copy(word_counts)
            sorted_word_counts = {k: v for k, v in sorted(period_word_counts.items(), key=lambda a: a[1], reverse=True)}

            for key in list(sorted_word_counts.keys())[:bar_count]:
                if key not in used_words:
                    used_words.append(key)  # used for removing words that don't appear in the animation

            last_day_record = message.get_datetime()

    # used_words = [key for key, val in word_counts.items() if val > used_threshold]
    used_date_words = {}

    for key in date_period_words.keys():
        used_date_words[key] = {}
        for word in used_words:
            if word in date_period_words[key]:
                used_date_words[key][word] = date_period_words[key][word]
            else:
                used_date_words[key][word] = 0

    index = ["%s - %s" % ((key - data_distance * periods_shown).date(), key.date()) for key in used_date_words.keys()]
    plot = pd.DataFrame(used_date_words.values(), index=index)
    print(plot)
    print(used_words)

    bcr.bar_chart_race(plot,
                       title="Words in messages between...",
                       filename="newstuff.mpeg",
                       sort="desc",
                       n_bars=bar_count,
                       period_length=750,
                       steps_per_period=30)
