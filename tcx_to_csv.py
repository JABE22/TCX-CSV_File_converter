#  Copyright (c) 2022. JAMA Softwares company has reserved all rights to this code.
#  Copying is allowed only when source is mentioned in the context.
#  The respect belongs to the following persons and institutes:
#  Developer Jarno Matarmaa, Finland, Tampere
#  Institute of Ural Federal University, City of Yekaterinburg, Russian Federation.
#  Names have to be mentioned when the project will be presented

# THIS CODE READS A SET OF GARMIN TCX FILES
import os
from filelocations import Dir
from datetime import datetime
from activityparser import save_tcx_to_csv, save_tcxset_to_csv
import sys
from pathlib import Path

'''
Run this program using one of the following scripts:
console> python tcx_to_csv.py -s VO2-max_testrun.tcx
console> python tcx_to_csv.py -m DATA/

Or check instructions by typing --help
console> python tcx_to_csv.py --help
'''

def main():
    args = sys.argv
    args = args[1:]  # First element of args is the python.py file name to run
    c_type = ''
    activity_number = 0

    if len(args) < 1:
        print('At least one command line argument or "--help" required!')
        print("--Two first arguments are noticed (for command '-m' three), others are ignored")
    else:
        c_type = args[0]

        if c_type == '--help':
            printInfo()

        elif c_type == '-s':
            if len(args) > 1:
                # Saving single TCX activity to CSV file
                filename = args[1]
                time_stamp = datetime.now()
                save_tcx_to_csv(Dir.TCX_PATH.value + filename, Dir.CSV_PATH.value + os.path.basename(filename),
                                Dir.COLUMN_TYPES_SINGLE.value, Dir.NAMES_SINGLE.value)
                print("Single TCXExercise processing time: " + str(datetime.now() - time_stamp))
            else:
                print("Missing argument: [filename].tcx")

        elif c_type == '-m':
            if len(args) == 1:
                print("Missing argument: [read_from_path]...)")
                print("Using default path: " + Dir.ROOT_PATH.value)
                root_path = Dir.ROOT_PATH.value
                activity_number = 2
            elif len(args) == 2:
                root_path = str(args[1])
                activity_number = 2
            else:
                root_path = str(args[1])
                activity_number = int(args[2])
            # Saving set of TCX activities to CSV file
            time_stamp = datetime.now()
            # File paths
            print("File path setup:")
            print("Root: " + root_path)
            print("Read: " + Dir.TCX_PATH_SET1.value)
            print("Write: " + Dir.CSV_PATH_SET1.value)
            save_tcxset_to_csv(root_path, Dir.TCX_PATH_SET1.value, Dir.CSV_PATH_SET1.value,
                               Dir.COLUMN_TYPES_SET.value, Dir.NAMES_SET.value, activity_number)
            print("\nSet of TCXExercises processing time: " + str(datetime.now() - time_stamp))
        else:
            print("Unknown command: " + str(c_type))


def printInfo():
    print("* To convert one .TCX file, give arguments: [-s] [filename].tcx")
    print("  -- File will be read from the location DATA/TCXDATA/[path_filename].tcx")
    print("  -- File will be written to the location DATA/CSVDATA/TEST/[filename].csv")
    print("* To convert set of .TCX files, give arguments: [-m] [read_from_path]")
    print("  -- Set of TCX files will be saved with same name as tcx files (except .tcx -> .csv)")
    print("     Default data locations are:")
    print("     --Read from: DATA/TCXDATA/SET1/")
    print("     --Save to: DATA/CSVDATA/SET1/")


# RUNS THE Main method
if __name__ == '__main__':
    main()


# SOME DIAGNOSIS SCRIPTS
'''
# Saving single TCX activity to CSV file
time_stamp = datetime.now()
save_tcx_to_csv(Dir.FILE_TCX_HALF_MARATHON.value, Dir.FILE_CSV_HALF_MARATHON.value,
                Dir.COLUMN_TYPES_SINGLE.value, Dir.NAMES_SINGLE.value)
print("Single TCXExercise processing time: " + str(datetime.now() - time_stamp))
# Saving set of TCX activities to CSV file
time_stamp = datetime.now()
save_tcxset_to_csv(Dir.TCX_PATH.value + "SET1/", Dir.FILE_CSV_ACTIVITIES.value,
                   Dir.COLUMN_TYPES_SET.value, Dir.NAMES_SET.value, 20)
print("Set of TCXExercises processing time: " + str(datetime.now() - time_stamp))
'''

'''
PRINTS NUMPY ARRAY (attributes separated by semicolon)
 for i in range(len(tp_array)):
     for j in range(8):
         print(tp_array[i][j], end=";")
     print("")
'''
