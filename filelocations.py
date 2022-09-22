#  Copyright (c) 2022. JAMA Softwares company has reserved all rights to this code.
#  Copying is allowed only when source is mentioned in the context.
#  The respect belongs to the following persons and institutes:
#  Developer Jarno Matarmaa, Finland, Tampere
#  Institute of Ural Federal University, City of Yekaterinburg, Russian Federation.
#  Names have to be mentioned when the project will be presented

from datetime import datetime
from enum import Enum


class Dir(Enum):
    """
    This enum class stores file paths for specific data science project
    """
    # General dataset locations
    TCX_PATH = "/TCXDATA/"
    CSV_PATH = "/CSVDATA/"
    TCX_PATH_SET1 = "TCXDATA/SET1/"
    CSV_PATH_SET1 = "CSVDATA/SET1/"
    # Half Marathon activity locations and details
    FILE_TCX_HALF_MARATHON = "TCXDATA/activity_5657402449.tcx"
    FILE_CSV_HALF_MARATHON = "CSVDATA/HMdata.csv"
    COLUMN_TYPES_SINGLE = [("Datetime", datetime), ("Latitude", float), ("Longitude", float),
                    ("Altitude", float), ("Distance", float), ("Hr", int),
                    ("Speed", float), ("Cadence", float), ("Watts", float)]
    # COL_NAMES = ["Date", "Time", "Latitude", "Longitude", "Altitude", "Distance", "Hr", "Speed", "Cadence", "Watts"]
    NAMES_SINGLE = "Datetime;Latitude;Longitude;Altitude;Distance;HeartRate;Speed;Cadence;Watts"
    # Set of sport activities
    FILE_CSV_ACTIVITIES = "CSVDATA/ACTIVITIESdata.csv"
    NAMES_SET = "Datetime;Latitude;Longitude;Altitude;Distance;HeartRate;Speed;Cadence;Watts"
    COLUMN_TYPES_SET = [("Datetime", datetime), ("Latitude", float), ("Longitude", float),
                    ("Altitude", float), ("Distance", float), ("Hr", int),
                    ("Speed", float), ("Cadence", float), ("Watts", float)]

"""
INFO

data = {TCXExercise}
    activity_type = {str} 'Running'
    start_time = {datetime} 2020-10-10 10:01:56+00:00
    end_time = {datetime} 2020-10-10 11:40:09+00:00
    altitude_avg = {float} 95.3437700814951
    altitude_min = {float} 82.19999694824219
    altitude_max = {float} 120.80000305175781
    ascent = {float} 319.5998992919922
    descent = {float} 328.39990234375
    distance = {float} 21277.92
    duration = {float} 5893.0
    hr_avg = {float} 179.6028740490279
    hr_min = {int} 123
    hr_max = {int} 200
    calories = {int} 1703
    avg_speed = {float} 12.998559647038858
    cadence_avg = {NoneType} None
    cadence_max = {NoneType} None
    trackpoints = {list: 5915} [TCXTrackPoint]

    Data fields in the single TCXTracPoint object inside TCXExercise
    (in this case the file has 5915 trackpoints)
    One trackpoint represent a single row in my .csv file

    {TCXTrackPoint}
        TPX_speed = {float} 5.011000156402588
        cadence = {float} 80
        distance = {float} 514.0499877929688
        elevation = {float} 46.79999923706055
        hr_value = {int} 134
        latitude = {float} 45.5244944896549
        longitude = {float} 13.596355207264423
        time = {datetime} 2015-02-19 09:34:17+00:00
        watts = {float} 123
"""