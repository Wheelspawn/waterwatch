# connect to the API
from sentinelsat import SentinelAPI, read_geojson, geojson_to_wkt
import datetime
from datetime import timedelta
api = SentinelAPI('navidj', 'smaptest123', 'https://scihub.copernicus.eu/dhus')
# search by polygon, time, and SciHub query keywords
footprint = geojson_to_wkt(read_geojson('data/extentIowa.geojson'))
maxCloudCov = 20 #%
deltaT = 10# days

# convert to Pandas DataFrame
def getData(dtInput):
    #
    dtData = datetime.datetime.strptime(dtInput, '%Y%m%d').date() + timedelta(days=deltaT)
    products = api.query(footprint,
                         date=(dtInput, dtData),
                         platformname='Sentinel-2')
    products_df = api.to_dataframe(products)

    # sort and limit to first 5 sorted products
    products_df_sorted = products_df.sort_values(['cloudcoverpercentage', 'ingestiondate'], ascending=[True, True])
    cloudMasked = products_df['cloudcoverpercentage']<20
    # download sorted and reduced products
    api.download_all(cloudMasked.index)

start = datetime.datetime.strptime("01-01-2016", "%d-%m-%Y").date()
end = datetime.datetime.strptime("10-01-2017", "%d-%m-%Y").date()
date_generated = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days, 10)]

for _dt in date_generated:
    dtInput = _dt.strftime('%Y%m%d')
    print(dtInput)
    # getData(dtInput)