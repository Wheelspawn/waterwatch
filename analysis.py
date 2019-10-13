
import zipfile
import gdal
import numpy
driver = gdal.GetDriverByName("JP2OpenJPEG")

fn1 = 'data/S2A_MSIL1C_20160109T173132_N0201_R012_T15TUJ_20160109T173131.zip'
archive = zipfile.ZipFile(fn1, 'r',zipfile.ZIP_DEFLATED)
fn_list = archive.namelist()
fn_list = [archive.getinfo(file).filename for file in fn_list]
jp2_list = [fn for fn in fn_list if fn[-3:]=='jp2']

loc = {}
loc['band8'] = [d for d in jp2_list if 'B08' in d][0]
loc['band3'] = [d for d in jp2_list if 'B03' in d][0]
# print(loc)
data = {}
ds = gdal.Open('/vsizip/%s/%s' %(fn1,loc['band3']))
data['band3'] = gdal.Open('/vsizip/%s/%s' %(fn1,loc['band3'])).ReadAsArray()
data['band8'] = gdal.Open('/vsizip/%s/%s' %(fn1,loc['band8'])).ReadAsArray()

[cols, rows] = data['band3'].shape
print(cols, rows)
ndwi = (data['band3'] - data['band8']) / (data['band3'] + data['band8'])
driver = gdal.GetDriverByName("GTiff")
outdata = driver.Create('test.tif', rows, cols, 1, gdal.GDT_UInt16)
outdata.SetGeoTransform(ds.GetGeoTransform())##sets same geotransform as input
outdata.SetProjection(ds.GetProjection())##sets same projection as input
outdata.GetRasterBand(1).WriteArray(ndwi)
outdata.GetRasterBand(1).SetNoDataValue(-9999)##if you want these values transparent
outdata.FlushCache() ##saves to disk!!
outdata = None
band=None
ds=None
# data['band8'] = ds.ReadAsArray()

# gdal.Warp(output_raster,input_raster,dstSRS='EPSG:4326')



