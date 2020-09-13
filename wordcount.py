import discordexport
from matplotlib import pyplot as plt

if __name__ == '__main__':
    messages = discordexport.json_to_messages("messages.json")

    words = ' '.join([message.values["content"] for message in messages]).split(' ')

    word_counts = {}

    for word in words:
        try:
            word_counts[word] += 1
        except KeyError:
            word_counts[word] = 0

    word_counts = {k: v for k, v in sorted(word_counts.items(), key=lambda item: item[1], reverse=True)}

    for range_min in range(0, len(word_counts), 50):
        range_max = range_min + 50

        plt.plot([str(a) for a in word_counts.keys()][range_min:range_max],
                 [int(a) for a in word_counts.values()][range_min:range_max])
        plt.show()
        plt.get_current_fig_manager().frame.Maximise = True
