# DesignWorkshopProject
Garmin TCX data to CSV data parser algorithm

## Description

Scripts can be used to transform certain features from Garmin TCX activity data format to CSV for further processing and analysis.

## How to use

In order to successfully run the code there are some pre-requisitions:

1. Data to read have to be available on the specific folder path (Folder names are defined in the source code)
2. Syntax for the commandline:
  - To convert one .TCX file, give arguments: **[s] [filename.tcx]**
    -- Data (single file) will be read from the location ./TCXDATA/[filename.tcx]
  - To convert a set of .TCX files, give arguments: **[m] [read_from]**
    -- TCX files will be read from the path [read_from]/TCXDATA/SET1/
    -- Default data locations are:
      Read from: [read_from]/TCXDATA/SET1/
      Save to: [read_from]/CSVDATA/SET1/
    -- Transformed data will be saved to the same root folder given as parameter
    -- Set of TCX files will be saved to CSV with the same original file names (except .tcx -> .csv)
