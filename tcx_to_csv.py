# THIS CODE READS A SET OF GARMIN TCX FILES
from filelocations import Dir
from datetime import datetime
from activityparser import save_tcx_to_csv, save_tcxset_to_csv
import sys
from pathlib import Path

# Run this program using syntax
# console> python tcx_to_csv.py s VO2-max_testrun.tcx

def main():
    args = sys.argv
    args = args[1:]  # First element of args is the python.py file name to run

    if len(args) < 1:
        print('Exactly two command line arguments or "--help" are required!')
        print("--Also, only two first arguments are noticed, others are ignored")
    elif len(args) == 1:
        if args[0] == '--help':
            printInfo()
        else:
            print("Unknown command!")
    elif len(args) == 2:
        c_type = args[0]
        if c_type == 's':
            # Saving single TCX activity to CSV file
            filename = args[1]
            time_stamp = datetime.now()
            save_tcx_to_csv("." + Dir.TCX_PATH.value + filename, Dir.CSV_PATH.value + filename,
                            Dir.COLUMN_TYPES_SINGLE.value, Dir.NAMES_SINGLE.value)
            print("Single TCXExercise processing time: " + str(datetime.now() - time_stamp))
        elif c_type == 'm':
            # Saving set of TCX activities to CSV file
            root_path = args[1]
            time_stamp = datetime.now()
            # File paths
            print(root_path)
            print(Dir.TCX_PATH_SET1.value)
            print(Dir.CSV_PATH_SET1.value)
            #
            save_tcxset_to_csv(root_path, Dir.TCX_PATH_SET1.value, Dir.CSV_PATH_SET1.value,
                               Dir.COLUMN_TYPES_SET.value, Dir.NAMES_SET.value, 10)
            print("\nSet of TCXExercises processing time: " + str(datetime.now() - time_stamp))

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


# RUNS THE Main method
if __name__ == '__main__':
    main()

def printInfo():
    print("* To convert one .TCX file, give arguments: [s] [filename.tcx]")
    print("* To convert set of .TCX files, give arguments: [m] [folder_to_read]")
    print("  -- Set of TCX files will be saved with name of reading folder")
    print("Default data locations are:")
    print("  --Read from: ../PythonProject/TCXDATA/")
    print("  --Save to: ../PythonProject/CSVDATA/")
'''
PRINTS NUMPY ARRAY (attributes separated by semicolon)
 for i in range(len(tp_array)):
     for j in range(8):
         print(tp_array[i][j], end=";")
     print("")
'''
