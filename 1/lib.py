def spikegraph_of_points(points):
    from collections import Counter

    counts = Counter(points)
    spikegraph_of_counts(counts)

def spikegraph_of_counts(counts):
    import numpy as np
    import matplotlib.pyplot as plt

    x = counts.keys()
    y = np.array(list(counts.values())) / sum(counts.values())
    plt.bar(left=x, height=y, width=0.1)
    plt.show()
