import os
import xml.etree.ElementTree as ET
import maya
import datetime
'''
Use may also try libraries directly from the tcxreader (e.g.: pip install tcxreader) 
Here required functions are copy pasted in order to make some case specific modifications to tcxreader.
For example, some feature names may change and in the TCXExercise object of .tcx file by Garmin and tcxreader lacks support for changes.
'''
#from tcxreader.tcx_track_point import TCXTrackPoint
#from tcxreader.tcx_exercise import TCXExercise
from pathlib import Path

GARMIN_XML_SCHEMA = '{http://www.garmin.com/xmlschemas/TrainingCenterDatabase/v2}'
GARMIN_XML_EXTENSIONS = '{http://www.garmin.com/xmlschemas/ActivityExtension/v2}'

class TCXTrackPoint(object):
    def __init__(self, longitude: float = None, latitude: float = None, elevation: float = None, time=None,
                 distance=None, hr_value: int = None, cadence=None, TPX_speed: float = None, watts: float = None):
        '''
        :param longitude: Longitude of the trackpoint
        :param latitude: Latitude of the trackpoint
        :param elevation: Elevation of the trackpoint
        :param time: Datetime of the trackpoint
        :param distance: Total distance traveled at the current trackpoint
        :param hr_value: Heart rate value at the trackpoint
        :param cadence: Cadence at the trackpoint
        :param TPX_speed: Current speed (extension), not necessarily OK!
        :param watts: Watts usage at the trackpoint
        '''
        self.longitude = longitude
        self.latitude = latitude
        self.elevation = elevation
        self.time = time
        self.distance = distance
        self.hr_value = hr_value
        self.cadence = cadence
        self.watts = watts
        self.TPX_speed = TPX_speed

    def __str__(self):
        (longitude, latitude, elevation) = (self.longitude, self.latitude, self.elevation)
        time = self.time
        distance = self.distance
        (hr_value, cadence, watts) = (self.hr_value, self.cadence, self.watts)
        TPX_speed = self.TPX_speed

        return f'{time} | lat:{latitude}, lon:{longitude} elev:{elevation} | m:{distance} | ' \
               f'hr:{hr_value}, cadence:{cadence}, watt:{watts}, TPX_speed:{TPX_speed}'

    def __unicode__(self):
        return self.__str__()


class TCXExercise:
    def __init__(self, trackpoints: [TCXTrackPoint] = None, activity_type: str = None, calories: int = None,
                 hr_avg: float = None, hr_max: float = None, hr_min=None, max_speed: float = None,
                 avg_speed: float = None, start_time: datetime = None, end_time: datetime = None,
                 duration: float = None, cadence_avg: float = None, cadence_max: float = None, ascent: float = None,
                 descent: float = None, distance: float = None, altitude_avg: float = None, altitude_min: float = None,
                 altitude_max: float = None):
        """
        :param trackpoints: List of TCXTrackPoint objects
        :param activity_type: sport string
        :param calories: total calories used in an exercise
        :param hr_avg: maxiumum heartrate achieved during the exercise
        :param hr_max: average heartrate during the exercise
        :param hr_min: minimum heartrate achieved during the exercise
        :param avg_speed: average speed during the exercise (km/h)
        :param start_time: datetime of exercise start
        :param end_time: datetime of exercise end
        :param duration: duration of exercise in seconds
        :param cadence_avg: average cadence during the exercise
        :param cadence_max: maximum cadence during the exercise
        :param ascent: total meters of ascent during the exercise
        :param descent: total meters of descent during the exercise
        :param distance: total distance of exercise in meters
        :param altitude_avg: average altitude in meters
        :param altitude_min: minimum altitude during the exercise
        :param altitude_max: maxiumum altitude during the exersice
        """

        self.trackpoints = trackpoints
        self.activity_type = activity_type
        self.calories = calories
        self.hr_avg = hr_avg
        self.hr_max = hr_max
        self.hr_min = hr_min
        self.duration = duration
        self.max_speed = max_speed
        self.avg_speed = avg_speed
        self.start_time = start_time
        self.end_time = end_time
        self.cadence_avg = cadence_avg
        self.cadence_max = cadence_max
        self.ascent = ascent
        self.descent = descent
        self.distance = distance
        self.altitude_avg = altitude_avg
        self.altitude_min = altitude_min
        self.altitude_max = altitude_max



class TCXReader:
    def __init__(self):
        self = self

    def read(self, fileLocation: str, only_gps: bool = True) -> TCXExercise:
        """
        :param only_gps: If set to True erases any Trackpoints at the start and end of the exercise without GPS data.
        :param fileLocation: location of the tcx file
        :return: A list of TCXTrackPoint objects.
        """

        tcx_exercise = TCXExercise(calories=0, distance=0)

        tree = ET.parse(fileLocation)
        root = tree.getroot()
        trackpoints = []
        for activities in root:
            if activities.tag == GARMIN_XML_SCHEMA + 'Activities':
                for activity in activities:
                    if activity.tag == GARMIN_XML_SCHEMA + 'Activity':
                        tcx_exercise.activity_type = activity.attrib['Sport']
                        for lap in activity:
                            if lap.tag == GARMIN_XML_SCHEMA + 'Lap':
                                for track in lap:
                                    if track.tag == GARMIN_XML_SCHEMA + 'Calories':
                                        tcx_exercise.calories += int(track.text)
                                    if track.tag == GARMIN_XML_SCHEMA + 'DistanceMeters':
                                        tcx_exercise.distance += float(track.text)
                                    if track.tag == GARMIN_XML_SCHEMA + 'Track':
                                        for trackpoint in track:
                                            tcx_point = TCXTrackPoint()
                                            if trackpoint.tag == GARMIN_XML_SCHEMA + 'Trackpoint':
                                                for trackpoint_data in trackpoint:
                                                    if trackpoint_data.tag == GARMIN_XML_SCHEMA + 'Time':
                                                        tcx_point.time = maya.parse(trackpoint_data.text,
                                                                                    '%Y-%m-%d %H:%M:%S.%f').datetime()
                                                    elif trackpoint_data.tag == GARMIN_XML_SCHEMA + 'Position':
                                                        for position in trackpoint_data:
                                                            if position.tag == GARMIN_XML_SCHEMA + "LatitudeDegrees":
                                                                tcx_point.latitude = float(position.text)
                                                            elif position.tag == GARMIN_XML_SCHEMA + "LongitudeDegrees":
                                                                tcx_point.longitude = float(position.text)
                                                    elif trackpoint_data.tag == GARMIN_XML_SCHEMA + 'AltitudeMeters':
                                                        tcx_point.elevation = float(trackpoint_data.text)
                                                    elif trackpoint_data.tag == GARMIN_XML_SCHEMA + 'DistanceMeters':
                                                        tcx_point.distance = float(trackpoint_data.text)
                                                    elif trackpoint_data.tag == GARMIN_XML_SCHEMA + 'HeartRateBpm':
                                                        for heart_rate in trackpoint_data:
                                                            tcx_point.hr_value = int(heart_rate.text)
                                                    elif trackpoint_data.tag == GARMIN_XML_SCHEMA + 'Cadence':
                                                        tcx_point.cadence = int(trackpoint_data.text)
                                                    elif trackpoint_data.tag == GARMIN_XML_SCHEMA + 'Extensions':
                                                        for extension in trackpoint_data:
                                                            if extension.tag == GARMIN_XML_EXTENSIONS + 'TPX':
                                                                for tpx_extension in extension:
                                                                    if tpx_extension.tag == GARMIN_XML_EXTENSIONS + 'Speed':
                                                                        tcx_point.TPX_speed = float(tpx_extension.text)
                                                                    elif tpx_extension.tag == GARMIN_XML_EXTENSIONS + 'Watts':
                                                                        tcx_point.watts = float(tpx_extension.text)
                                            trackpoints.append(tcx_point)
        # remove_data_at_start_and_end_without_gps. Those stats are not taken for distance and hr measurements!
        if only_gps == True:
            removalList = []
            for index in range(len(trackpoints)):
                if trackpoints[index].longitude is None:
                    removalList.append(index)

            for removal in sorted(removalList, reverse=True):
                del trackpoints[removal]

        tcx_exercise.trackpoints = trackpoints

        tcx_exercise = self.__find_hi_lo_avg(tcx_exercise)
        return tcx_exercise

    def __find_hi_lo_avg(self, tcx: TCXExercise) -> TCXExercise:
        trackpoints = tcx.trackpoints
        hr = []
        altitude = []
        cadence = []
        for trackpoint in tcx.trackpoints:
            if trackpoint.hr_value != None:
                hr.append(trackpoint.hr_value)
            if trackpoint.elevation != None:
                altitude.append(trackpoint.elevation)
            if trackpoint.cadence != None:
                cadence.append(trackpoint.cadence)

        if len(altitude) > 0:
            (tcx.altitude_max, tcx.altitude_min) = (max(altitude), min(altitude))
            tcx.altitude_avg = sum(altitude) / len(altitude)

        (ascent, descent) = (0, 0)
        previous_altitude = -100
        for alt in altitude:
            if isinstance(alt, float):
                if previous_altitude == -100:
                    pass
                elif alt > previous_altitude:
                    ascent += alt - previous_altitude
                elif alt < previous_altitude:
                    descent += previous_altitude - alt
                previous_altitude = alt

        (tcx.ascent, tcx.descent) = (ascent, descent)

        if len(hr) > 0:
            (tcx.al, tcx.hr_min) = (max(hr), min(hr))
            tcx.hr_avg = sum(hr) / len(hr)

        if len(cadence) > 0:
            tcx.cadence_max = max(cadence)
            tcx.cadence_avg = sum(cadence) / len(cadence)

        if len(trackpoints) > 2:
            tcx.start_time = trackpoints[0].time
            tcx.end_time = trackpoints[-1].time
            tcx.duration = abs((tcx.start_time - tcx.end_time).total_seconds())
            tcx.avg_speed = tcx.distance / tcx.duration * 3.6

        return tcx