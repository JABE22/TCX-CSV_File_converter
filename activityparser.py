# tcxreader instructions: https://pypi.org/project/tcxreader/
import datetime
import numpy as np
from tcxread import TCXReader, TCXTrackPoint, TCXExercise
from filelocations import Dir
from pathlib import Path
# from tabulate import tabulate # For data visualization in console

def tcx_trackpoints_to_numpy(file_path, column_types):
    """
    TCX Reader - Reading a single .tcx file to NumPy array

    :param file_path: File path for tcx file to read
    :param column_types: Column/Variable types and/or names. Will be directly stored as a value of numpy array function 'dtype' parameter
    :return: Two dimensional NumPy array containing all the rows and columns from 'file_path'
    """
    tcx_reader = TCXReader()
    data: TCXExercise = tcx_reader.read(file_path)
    sport = data.activity_type
    print("Getting trackpoints for activity type: %s" % sport)
    trackpoints = data.trackpoints
    print("The file has " + str(len(trackpoints)) + " trackpoints")
    # Creates empty numpy array with 9 columns
    tp_array = np.empty((0, len(column_types)), dtype=column_types)
    # Constructing NumPy array
    for tp in trackpoints:
        datarow = [tp.time, tp.latitude, tp.longitude, tp.elevation,
                   tp.distance, tp.hr_value, tp.TPX_speed, tp.cadence, tp.watts]
        tp_array = np.append(tp_array, np.array([datarow]), axis=0)

    return (sport, tp_array)


def tcx_exercises_to_csv(tcx_folder, csv_folder, column_types, column_names, exers):
    """
    TCX Reader - Reading a set of .tcx files to NumPy array

    :param tcx_folder: Tcx file folder path ro read from.
    :param column_types: Data variable types (float, int, datetime, str). Directly placed as numpy array dtype value
    :param rows: Number of rows to read from .tcx set
    :return tp_array: Array of activities in a dimension based on the size of parameter column_types
    """
    tcx_files = Path(tcx_folder).glob('*.tcx')
    activity_types = np.array([])
    file_number = 1

    if exers == 0:
        exers = len(tcx_files)

    for child in tcx_files:  # In order to avoid reading errors
        if child.is_file() and file_number <= exers:
            print("\nFile number to process: " + str(file_number))
            print("Activity inserted: " + child.name + ", Activities = " + str(file_number))
            # Data instance
            r_path_filename = tcx_folder + child.name
            w_path_filename = csv_folder + child.name
            sport = save_tcx_to_csv(r_path_filename, w_path_filename, column_types, column_names)
            activity_types = np.append(activity_types, sport)
            file_number = file_number + 1
        else:
            break

    return activity_types

def save_tcx_to_csv(read, write, types, names):
    """
    Converts garmin .tcx file to .csv.

    :param read: Tcx file path to read
    :param write: Csv file path to write
    :param types: Data variable types (float, int, datetime, str).
    :param names: Data variable names for .csv header row. Values separated by semicolon.
    """
    sport, tp_array = tcx_trackpoints_to_numpy(read, types)
    write = str(Path(write).with_suffix('.csv'))
    print("Read from: " + read + "\nWrite to: " + write)
    np.savetxt(write, tp_array, delimiter=";", fmt='% s', header=names, comments="")

    # Let's return activity type since we cannot handle it here
    return sport


def save_tcxset_to_csv(root, read, write, types, names, exers=0):
    """
    Converts set of garmin .tcx files to one single .csv file.

    :param read: Tcx folder to read
    :param write: Csv file path/name to write
    :param types: Data variable types (float, int, datetime, str).
    :param names: Data variable names for .csv header row. Values separated by semicolon.
    :param rows: Number of rows to read from .tcx set
    """
    activity_types = tcx_exercises_to_csv(root + read, root + write, types, names, exers)
    print(activity_types)
    write = str(Path(root + write + "activity_types.csv"))
    print("\nSaving activity types to: " + write)
    np.savetxt(write, activity_types, delimiter=";", fmt='% s', header="activity_name", comments="")

