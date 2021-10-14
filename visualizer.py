import numpy as np
from matplotlib import pyplot as plt

def cadence (path):
    Reading_One = np.load(path)
    figure = plt.figure(figsize=(18, 12))
    for i in range(6):
        plt.subplot(6, 1, i + 1)
        plt.imshow(Reading_One[i].astype(float), interpolation='nearest', aspect='auto')
        plt.text(5, 100, ["ON", "OFF"][i % 2], bbox={'facecolor': 'green'})
        plt.colorbar()
    plt.show()