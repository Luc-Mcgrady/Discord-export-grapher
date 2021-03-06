from lib import discordjson, plotdict

if __name__ == '__main__':
    messages = discordjson.json_to_messages()

    months = {}
    plotted_authors = []

    for message in messages:
        author = message.values["author"]["name"]
        month = str(message.get_datetime().date())[:-3]

        if author not in plotted_authors:
            plotted_authors.append(author)

        if month not in months.keys():
            months[month] = {}

        if author not in months[month].keys():
            months[month][author] = 0

        months[month][author] += 1

    maxval = 0

    for val in months.values():
        for author in plotted_authors:
            if author not in val.keys():
                val[author] = 0
        maxval = max(maxval, *list(val.values()))

    for author in plotted_authors:
        plotdict.plot_dict({k: v[author] for k, v in months.items() if author in v.keys()}, label=author)

    plotdict.plt.ylim(0, maxval)
    plotdict.plt.legend(prop={'size': 6})

    plotdict.plt.xlabel("month")
    plotdict.plt.ylabel("messages")
    plotdict.plt.title("user activity")

    plotdict.plt.show()

    print(months)
