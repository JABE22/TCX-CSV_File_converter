# DesignWorkshopProject
Garmin TCX data to CSV data parser algorithm

## Description

Scripts can be used to transform certain features from Garmin TCX activity data format to CSV for further processing and analysis.

## How to use

In order to successfully run the code there are some pre-requisitions:

1. Data to read have to be available on the specific folder path (Folder names are defined in the source code)
2. Syntax for the commandline:
  A. To convert one .TCX file, give arguments: **[s] [filename.tcx]**
    
  B. To convert set of .TCX files, give arguments: **[m] [folder_to_read]**
    - Set of TCX files will be saved to CSV with the same original file names")
    - Default data locations are:
      --Read from: [commandline_parameter]/TCXDATA/SET1/
      --Save to: [commandline_parameter]/CSVDATA/SET1/
