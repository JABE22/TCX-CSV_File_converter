**Design Workshop Project 2022**
# TCX to CSV data parcer

Garmin TCX data to CSV data parser algorithm

Implemented as an independent study work in Data Science at Ural Federal University. 
The project is for learning or study purposes only and not intended to be used without deep understanding about the Python code. However, you may save some time to have it as a sceleton to start your own project.

## Description

Scripts can be used to transform certain features from Garmin TCX activity data format to CSV for further processing and analysis.

## TCXReader
Actual parcer for .tcx files is copied from the source. (However, project is not dependent on that library since it includes necessary code)
https://github.com/alenrajsp/tcxreader

## How to use

In order to successfully run the code there are some pre-requisitions:

1. Data to read have to be available on the specific folder path (Folder names are defined in the source code)
2. Syntax for the commandline:
  - To convert one .TCX file, give arguments: **[s] [filename.tcx]**
    - Data (single file) will be read from the location **./TCXDATA/[filename.tcx]**
  - To convert a set of .TCX files, give arguments: **[m] [read_from]**
    - TCX files will be read from the path **[read_from]/TCXDATA/SET1/**
    - Default data locations are:
      - Read from: [read_from]/TCXDATA/SET1/
      - Save to: [read_from]/CSVDATA/SET1/
    - The amount of files (at maximum) to read is hard coded and set to 10 (can be easily changed according to your needs)
    - Transformed data will be saved to the same root folder given as parameter
    - Set of TCX files will be saved to CSV with the same original file names (except .tcx -> .csv)
 
 Feel free to copy the code and modify it according to your needs or will
