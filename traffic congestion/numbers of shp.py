





success  numbers of shp
>>> import os
... import glob
... from arcpy import env
... env.workspace = "G:/7gaodetraffic/"
... # Open one of the files,
... folder_path = 'G:/7gaodetraffic/4delete duplicate/'
... road= glob.glob(r'G:/7gaodetraffic/4delete duplicate/*.shp')
... print len(road)
...
96



numbers of fields  success
 import arcpy.da
... import time,os
... import arcpy
... arcpy.env.workspace = "G:/7gaodetraffic/7poitsjoin"
... inFeatures = "2422.shp"
... fieldObjList = arcpy.ListFields(inFeatures)
... print fieldObjList
... print len(fieldObjList)
...
...



list filed
import arcpy.da
... import time,os
... import arcpy
... arcpy.env.workspace = "G:/7gaodetraffic/7poitsjoin"
... fields = arcpy.ListFields("2422.shp")
... print fields
...
...


import arcpy.da
... import time,os
... import arcpy
...  def getFieldNames(shp):
...     fieldnames = [f.name for f in arcpy.ListFields(shp)]
...     return fieldnames
...  fieldnames = getFieldNames("country.shp")












