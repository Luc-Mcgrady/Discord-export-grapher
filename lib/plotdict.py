from matplotlib import pyplot as plt

plt.xticks(rotation="vertical")

def plot_dict(vals: dict, sort=False, show=False, min_index=0, max_index=None, label: str = None,
              autoscale: bool = True):
    """Plots the given dictionary to the "plt" variable of this import"""
    displaydict = vals.copy()

    if max_index is None:
        max_index = len(displaydict)

    if sort:
        displaydict = {k: v for k, v in sorted(displaydict.items(), key=lambda item: item[1], reverse=True)}

    displaydict = {k: v for k, v in list(displaydict.items())[min_index:max_index]}
    if autoscale:
        plt.ylim(0, max(displaydict.values()))
    plt.plot([str(a) for a in displaydict.keys()],
             [int(a) for a in displaydict.values()], label=label)
    if show:
        plt.show()
