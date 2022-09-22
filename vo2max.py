#  Copyright (c) 2022. JAMA Softwares company has reserved all rights to this code.
#  Copying is allowed only when source is mentioned in the context.
#  The respect belongs to the following persons and institutes:
#  Developer Jarno Matarmaa, Finland, Tampere
#  Institute of Ural Federal University, City of Yekaterinburg, Russian Federation.
#  Names have to be mentioned when the project will be presented

import pandas as pd
import numpy as np

data = pd.read_csv('CSVDATA/HMdata.csv', delimiter=";")
hr_mean = np.mean(data["HeartRate"])
hr_max = np.max(data["HeartRate"])
vo2_max = hr_max/58 * 15.3  # ml/min/kg
print("MaxHr = " + str(hr_max))
print("MeanHr = " + str(hr_mean))
print("Approximated VO2-max = " + str(vo2_max))
