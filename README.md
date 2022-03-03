# SETI - Searching for Extraterestial Intelligence

A collection of notebooks that try to detect artificially inserted alien signals in a large data set.
The challenge was taken from: https://www.kaggle.com/c/seti-breakthrough-listen. The dataset is also available on the kaggle website.

## Table of contents
- [SETI](#seti---searching-for-extraterestial-intelligence)
    - [Table of contents](#table-of-contents)
    - [conservative approach](#conservative-approach)
      - [Finding clusters](#finding-clusters)
      - [Exploiting the data leak](#exploiting-the-data-leak)
    - [neural network approach](#neural-network-approach)
    - [results](#results)

## Conversavative approach
<img src="https://raw.githubusercontent.com/volleyfreak/SETI/main/screenshots/Sample%200029a35de92941d%20%2B%20Boxes.png" alt="Your image title" width="500"/> </br>

Different approaches were tried out to reliably increase the SNR of alien signals (red boxes) in noisy images.
Results  can be found in [/source/conservative-approach](https://github.com/volleyfreak/SETI/tree/main/source/conservative-approach). The most promising preprocessing step: Derivation images was also applied on the whole dataset. But the results were not useful as input for a neural networks.

### Finding clusters
If the right preprocessing steps were applied it is possible to automatically detect clusters in images with good SNR. That algorithm is implemented in [/source/conservative-approach/derivatives+cluster.ipynb](https://github.com/volleyfreak/SETI/blob/main/source/conservative-approach/derivatives%2Bcluster.ipynb)

### Exploiting the data leak
It seems like the creators of the challenge shifted the frequency and reused part of the backgroind noise. 
That means if a perfect match is found, shifted and subtracted, the result would be an image without background noise. 
That process is shown in the notebook [/source/remote-notebooks/magic-2-an-explanation.ipynb](https://github.com/volleyfreak/SETI/blob/main/source/remote-notebooks/magic-2-an-explanation.ipynb)

## Neural network approach
Two different neural networks were trained on the task and then fine-tuned to deliver good results. A ResNet18 and an EfficientNet.
The corresponding notebooks can be found in [/source/remote-notebooks/](https://github.com/volleyfreak/SETI/tree/main/source/remote-notebooks). 
Their architectures can be viewed in [/net architectures/](https://github.com/volleyfreak/SETI/tree/main/net%20architectures).

## Results
ResNet delievered poor results which were not better than a no skill model..
But EfficientNet achieved good results. The initial implementation with an AUC score of 0.753 could be improved to a score of 0.800.
This was achieved by using only ON measurements and applying a 1x1 Convolutional Layer as first layer.\
<img src="https://github.com/volleyfreak/SETI/blob/main/screenshots/deep%20runs/pretraining_+1x1conv+more_runs.png?raw=true" alt="Your image title" width="500"/>
