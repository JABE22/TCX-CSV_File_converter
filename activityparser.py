#  Copyright (c) 2022. JAMA Softwares company has reserved all rights to this code.
#  Copying is allowed only when source is mentioned in the context.
#  The respect belongs to the following persons and institutes:
#  Developer Jarno Matarmaa, Finland, Tampere
#  Institute of Ural Federal University, City of Yekaterinburg, Russian Federation.
#  Names have to be mentioned when the project will be presented

# tcxreader instructions: https://pypi.org/project/tcxreader/
import datetime
import numpy as np
from tcxread import TCXReader, TCXTrackPoint, TCXExercise
from filelocations import Dir
from pathlib import Path
# from tabulate import tabulate # For data visualization in console

def tcx_trackpoints_to_numpy(file_path: str, column_types: [(str,type)]) -> tuple:
    """
    TCX Reader - Reading a single .tcx file to NumPy array

    @param file_path: File path for tcx file to read
    @param column_types: Column/Variable types and/or names. Will be directly stored as a value of numpy array function 'dtype' parameter
    @return: Two dimensional NumPy array containing all the rows and columns from 'file_path'
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


def tcx_exercises_to_csv(tcx_folder: str, csv_folder: str, column_types: [(str,type)], column_names: str, exers: int) -> list:
    """
    TCX Reader - Reads a set of .tcx files from the given path and writes them to file using function save_tcx_to_csv()

    @param tcx_folder: Tcx file folder path to read from
    @param csv_folder: Csv file folder path to write to
    @param column_types: Data variable types (float, int, datetime, str). Will be only fed to a function save_tcx_to_csv() as a parameters
    @param column_names: Data variable names for .csv header row. Values separated by semicolon. Feature/column names. Will be only fed to a function save_tcx_to_csv() as a parameters
    @param exers: Number of activities/exercises to read from .tcx file set
    @return: Activity types as list of strings in a size of given function parameter "exers" for classification tasks
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


def save_tcx_to_csv(read: str, write: str, types: [(str,type)], names: str) -> str:
    """
    Converts garmin .tcx file to .csv.

    @param read: Tcx file path to read from
    @param write: Csv file path to write to
    @param types: Data variable types (float, int, datetime, str).
    @param names: Data variable names for .csv header row. Values separated by semicolon.
    @return: String/Name of the saved sport activity
    """
    sport, tp_array = tcx_trackpoints_to_numpy(read, types)
    write = str(Path(write).with_suffix('.csv'))
    print("Read from: " + read + "\nWrite to: " + write)
    np.savetxt(write, tp_array, delimiter=";", fmt='% s', header=names, comments="")

    # Let's return activity type since we won't handle it here
    return sport


def save_tcxset_to_csv(root: str, read: str, write: str, types: [(str,type)], names: str, exers: int = 0) -> object:
    """
    Converts set of garmin .tcx files to one single .csv file.

    @param root: Root folder for all the data (read and write)
    @param read: Tcx folder path to read
    @param write: Csv file path/name to write
    @param types: Data variable types (float, int, datetime, str).
    @param names: Data variable names for .csv header row. Values separated by semicolon.
    @param exers: Number of activities to read from .tcx set
    """
    activity_types = tcx_exercises_to_csv(root + read, root + write, types, names, exers)
    print(activity_types)
    write = str(Path(root + write + "activity_types.csv"))
    print("\nSaving activity types to: " + write)
    np.savetxt(write, activity_types, delimiter=";", fmt='% s', header="activity_name", comments="")

