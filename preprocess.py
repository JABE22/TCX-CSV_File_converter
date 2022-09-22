#  Copyright (c) 2022. JAMA Softwares company has reserved all rights to this code.
#  Copying is allowed only when source is mentioned in the context.
#  The respect belongs to the following persons and institutes:
#  Developer Jarno Matarmaa, Finland, Tampere
#  Institute of Ural Federal University, City of Yekaterinburg, Russian Federation.
#  Names have to be mentioned when the project will be presented

import pandas as pd
import seaborn as sns  # library for visualization
import matplotlib.pyplot as plt  # library for visualization
import numpy as np


def zone(hr):
    if 120 <= hr <= 136:  # Warm up
        return 1
    elif 136 <= hr <= 149:  # Easy
        return 2
    elif 150 <= hr <= 164:  # Aerobic
        return 3
    elif 165 <= hr <= 177:  # Threshold
        return 4
    elif hr >= 178:  # Maximum
        return 5
    else:
        return 0

# DATA IMPORT
DF_1 = pd.read_csv('CSVDATA/RUN_11112021_6km.csv', delimiter=';')[['Datetime', 'Altitude', 'HeartRate', 'Speed']]
DF_2 = pd.read_csv('CSVDATA/RUN_04112021_9km.csv', delimiter=';')[['Datetime', 'Altitude', 'HeartRate', 'Speed']]
# DATA INFO
print(DF_1.info())
print(DF_2.info())
# DIFFERENTIALS
DF_1_diff = DF_1[['Altitude', 'HeartRate', 'Speed']].diff()
DF_2_diff = DF_2[['Altitude', 'HeartRate', 'Speed']].diff()
#DF_1_diff.to_csv(path_or_buf='CSVDATA/DIFF.csv', index=False, sep=';')
# CATHEGORIZING by HR-zones
zones = [0, 121, 136, 150, 165, 178, np.inf]
lbls = ['Low', 'Zone 1', 'Zone 2', 'Zone 3', 'Zone 4', 'Zone 5']
DF_1['HRZone'] = pd.cut(DF_1['HeartRate'], bins=zones, labels=lbls)


#print(DF_1)
# DATA PREPROCESSING
#print(DF_1.isna().sum()/DF_1.shape[0])

hr_spd_1 = DF_1[['HeartRate', 'Speed']]
hr_spd_2 = DF_2[['HeartRate', 'Speed']]

# Scatter plots for HR and Speed correlation
figure1, (ax1, ax2) = plt.subplots(1, 2)
ax1.scatter(hr_spd_1['Speed'], hr_spd_1['HeartRate'], s=5)
ax1.set_title('Exercise 1')
ax2.scatter(hr_spd_2['Speed'], hr_spd_2['HeartRate'], s=5)
ax2.set_title('Exercise 2')
# Line plots for differential data
figure2, (ax3, ax4, ax5) = plt.subplots(1, 3)
ax3.plot(DF_1_diff['Altitude'], linewidth=1, c='g')
ax3.set(xlabel='Measurement', ylabel='Difference to previous value')
ax4.plot(DF_1_diff['HeartRate'], linewidth=1, c='r')
ax4.set(xlabel='Measurement', ylabel='Difference to previous value')
ax5.plot(DF_1_diff['Speed'], linewidth=1, c='b')
ax5.set(xlabel='Measurement', ylabel='Difference to previous value')
plt.show()
# Seaborn plots
plt.figure(figsize=(15,8))
sns.scatterplot(x='Speed', y='HeartRate', data=DF_1, hue='HRZone', palette=sns.color_palette("hls",6), alpha=0.7, size='Speed');
plt.show()