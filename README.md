# Rename Images with Date Photo Taken

Purpose: Renames image files in a folder based on date photo taken from EXIF metadata

Author: Matthew Renze, modified by David Heereman

Usage: python.exe Rename.py input-folder
  - input-folder = the directory containing the image files to be renamed
  - naming_pattern: input_folder_YYYYMMDD_hhmmss.[jpg,png]


Example:
`python3 Rename.py /path/to/your/folder`

Behavior:  
 - Given a photo named "whatever.jpg"  
 - with EXIF date taken of "4/1/2018 5:54:17 PM"  
 - when you run this script on its parent folder
 - then it will be renamed "paren_folder_20180401_175417.jpg"

Notes:
  - For safety, please make a backup before running this script
  - Currently only designed to work with `.jpg`, `jpeg`, `.JPG`and `.png`  files
  - EXIF metadate must exist or an error will occur


Prerequisites:
  - [pillow (PIL) library](https://pillow.readthedocs.io/en/stable/installation.html)
    * `python3 -m pip install --upgrade Pillow --user`
