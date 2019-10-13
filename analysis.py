import ZipFile

import zipfile
import pandas as pd

fn = 'data//S2A_MSIL1C_20160720T174112_N0204_R055_T14TPP_20160720T174112.zip'
archive = zipfile.ZipFile(fn, 'r',zipfile.ZIP_DEFLATED)
fn_list = archive.namelist()
fn_list = [archive.getinfo(file).filename for file in fn_list]
jp2_list = [fn for fn in fn_list if fn[-3:]=='jp2']

loc = {}
loc['band8'] = [d for d in jp2_list if 'B08' in d][0]
loc['band3'] = [d for d in jp2_list if 'B03' in d][0]

with zipfile.ZipFile(fn) as archive:
    for file in archive.namelist():
        file_info = archive.getinfo(file)
        print(file_info.filename)
list_one = [ fi for fi in fn_list if fi.endswith("*.jp2") ]
imgdata = archive.read('img_01.png')

S2A_MSIL1C_20160720T174112_N0204_R055_T14TPP_20160720T174112


filename='S2A_MSIL1C_20160720T174112_N0204_R055_T14TPP_20160720T174112.SAFE/GRANULE/L1C_T14TPP_A005629_20160720T174112/IMG_DATA/T14TPP_20160720T174112_B03.jp2'
