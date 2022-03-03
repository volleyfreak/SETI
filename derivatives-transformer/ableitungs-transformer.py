import numpy as np
import pandas as pd

#
# train = pd.read_csv('./seti-breakthrough-listen/train_labels.csv')
# train['img_path']=train['id'].apply(lambda x:f'./seti-breakthrough-listen/train/{x[0]}/{x}.npy')
# print('start train')
# for i in range(len(train)):
#     entry = train.iloc[i]
#     cadence = np.take(np.load(entry['img_path']), [0,2,4], 0)
#     for i in range(3):
#         cadence = cadence.T
#         for j in range(len(cadence)-1):
#             for k in range(len(cadence[j])-1):
#                 cadence[j][k] = abs(cadence[j][k] - cadence[j][k+1])
#         for j in range(len(cadence)-1):
#             for k in range(len(cadence[j])):
#                 cadence[j][k] = abs(cadence[j][k] - cadence[j+1][k])
#         cadence =cadence.T
#     np.save('./output/train/'+entry['id']+'.npy', cadence)
#     if (i%100 == 0):
#         print('iteration: '+ i)
# print('finished train')
print('start train')
import os
for item in os.listdir('./seti-breakthrough-listen/test'):
    for entry in os.listdir('./seti-breakthrough-listen/test/'+item):
        cadence = np.take(np.load('./seti-breakthrough-listen/test/'+item+'/'+entry), [0,2,4], 0)
        for i in range(3):
            cadence = cadence.T
            for j in range(len(cadence)-1):
                for k in range(len(cadence[j])-1):
                    cadence[j][k] = abs(cadence[j][k] - cadence[j][k+1])
            for j in range(len(cadence)-1):
                for k in range(len(cadence[j])):
                    cadence[j][k] = abs(cadence[j][k] - cadence[j+1][k])
            cadence =cadence.T
            np.save('./output/test/'+entry, cadence)

print('finished test')