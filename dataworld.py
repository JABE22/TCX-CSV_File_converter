import datadotworld as dw
import numpy as np

# SEEKS Data from data.world
results = dw.query('jarnoma/half-marathon',
                   'SELECT * FROM HMdata')
results_df = results.dataframe
hr_mean = np.mean(results_df["heartrate"])
hr_max = np.max(results_df["heartrate"])
vo2_max = hr_max/59 * 15.3  # ml/min/kg
print(results_df)
print("MaxHr = " + str(hr_max))
print("MeanHr = " + str(hr_mean))
print("Approximated VO2-max = " + str(vo2_max))
