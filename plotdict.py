from matplotlib import pyplot as plt

plt.xticks(rotation="vertical")


def plot_dict(vals: dict, sort=False, show=False, min_index=0, max_index=None):
    displaydict = vals.copy()

    if max_index is None:
        max_index = len(displaydict)

    if sort:
        displaydict = {k: v for k, v in sorted(displaydict.items(), key=lambda item: item[1], reverse=True)}

    plt.plot([str(a) for a in displaydict.keys()][min_index:max_index],
             [int(a) for a in displaydict.values()][min_index:max_index])
    if show:
        plt.show()
