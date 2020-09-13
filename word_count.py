import discordexport
import plotdict

if __name__ == '__main__':
    messages = discordexport.json_to_messages("messages.json")

    words = ' '.join([message.values["content"] for message in messages]).split(' ')

    word_counts = {}

    for word in words:
        try:
            word_counts[word] += 1
        except KeyError:
            word_counts[word] = 0

    for range_min in range(0, len(word_counts), 50):
        range_max = range_min + 50

        plotdict.plot_dict(word_counts, True, True, range_min, range_max)
