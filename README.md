# SETI - Searching for Extraterestial Intelligence

A collection of notebooks that try to detect artificially inserted alien signals in large data set.
The challenge was taken from: https://www.kaggle.com/c/seti-breakthrough-listen. The dataset is also available on the kaggle website.

## Table of contents
- [SETI](#seti---searching-for-extraterestial-intelligence)
    - [Table of contents](#table-of-contents)
    - [conservative approach](#conservative-approach)
    - [neural network approach](#neural-network-approach)
    - [results](#results)

## Conversavative approach
Different approaches were tried out to reliably increase the SNR of alien signals (red boxes) in noisy images.
Results  can be found in .source/conservative-approach. \
<img src="https://raw.githubusercontent.com/volleyfreak/SETI/main/screenshots/Sample%200029a35de92941d%20%2B%20Boxes.png" alt="Your image title" width="700"/>

## Neural network approach
Two different neural networks were trained on the task and then fine-tuned to deliver good results. A ResNet18 and an EfficientNet.
The corresponding notebooks can be found in [/source/remote-notebooks/](https://github.com/volleyfreak/SETI/tree/main/source/remote-notebooks)
Their architectures can be viewed in [/net architectures](https://github.com/volleyfreak/SETI/tree/main/net%20architectures).

## Results
ResNet delievered poor results which were not better than a no skill model..
But EfficientNet achieved good results. The initial implementation with an AUC score of 0.753 could be improved to 0.800.
<img src="https://raw.githubusercontent.com/volleyfreak/SETI/main/screenshots/Sample%200029a35de92941d%20%2B%20Boxes.png" alt="Your image title" width="700"/>