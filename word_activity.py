from lib import discordjson, plotdict


class _WordActivityPlot:

    def __init__(self, messages: list, proportional=True):
        self._plotmax = 0  # The largest value on the graph
        self._plotbuffer = []
        self.proportional = proportional
        self.messages = messages
        self.month_words = {}

        for message in self.messages:  # Calculate all the words over the months
            message: discordjson.DiscordMessage
            wordcount = len(message.get_content().split(' '))

            month = str(message.get_datetime().date())[:-3]
            try:
                self.month_words[month] += wordcount
            except KeyError:
                self.month_words[month] = wordcount

    def recalc_plotmax(self, months: dict = None):
        """Get plotmax or with 1arg calculate plotmax"""
        if months is None:
            return self._plotmax  # Can just be used to get plotmax but not reccomended

        self._plotmax = max(self._plotmax, *list(months.values()))
        return self._plotmax

    def show(self):
        """Display the data gathered as a graph.
        You can have the graph proportional to the total words in the month or just as total hits"""
        plot_data = []

        plotdict.plt.ylim(0, self._plotmax * 1.1)  # If not proportional

        plotdict.plt.title("Word Hits")
        plotdict.plt.xlabel("Month")
        plotdict.plt.ylabel("Hits")

        if self.proportional:
            self._plotmax = 0
            plotdict.plt.ylabel("% of max value")
            plotdict.plt.ylim(0, 100)

            for target_word, months in self._plotbuffer:
                for month in months:
                    months[month] = float(months[month]) / self.month_words[month]
                self.recalc_plotmax(months)

            for target_word, months in self._plotbuffer:
                if max(months.values()) != 0:
                    scaling = 100 / self._plotmax  # if the number is too small matplotlib freaks out
                else:
                    scaling = 1

                plot_data.append((target_word, {k: v * scaling for k, v in months.items()}))
        else:
            plot_data = self._plotbuffer

        for target_word, months in plot_data:
            plotdict.plot_dict(months, False, False, label=target_word, autoscale=False)

        plotdict.plt.legend()
        plotdict.plt.show()

    def word_activity_plot(self, target_word):
        """Plots the activity over months of the target word and saves it to plot with the show function"""
        months = {}

        for message in self.messages:
            # messages.values["content"]
            words = message.get_content().split(' ')

            message_hits = sum(word == target_word for word in words)
            month = str(message.get_datetime().date())[:-3]

            try:
                months[month] += message_hits
            except KeyError:
                months[month] = message_hits

        self._plotbuffer.append((target_word, months))
        self.recalc_plotmax(months)


if __name__ == '__main__':
    messages = discordjson.json_to_messages("messages.json")

    grapher = _WordActivityPlot(messages)

    target_word = None
    while True:
        target_word = input("(submit nothing to plot) Add a word to search for: ")
        if target_word == '':
            break
        grapher.word_activity_plot(target_word)

    grapher.proportional = \
        True if input("(y/n) Should the count be a precentage of the months total words: ") == 'y' else False
    grapher.show()
    input()
