





SUCCESS ADD FIELD
>>> import os
... import glob
... from arcpy import env
... env.workspace = "F:/7gaodetraffic/4delete duplicate/"
... # Open one of the files,
... folder_path = "F:/7gaodetraffic/4delete duplicate/"
... road= glob.glob(r'F:/7gaodetraffic/4delete duplicate/*.shp')
... i=1
... for i in range(1,200):
...		line=road[i]
...		arcpy.AddField_management(line,"length","DOUBLE",6,"","","length","NULLABLE","REQUIRED")



>>> import os
... import glob
... from arcpy import env
... env.workspace = "F:/10LST25cities/H and area of building/"
... # Open one of the files,
... folder_path = "F:/10LST25cities/H and area of building/"
... road= glob.glob(r'F:/10LST25cities/H and area of building/*.shp')
... i=1
... for i in range(1,200):
...		line=road[i]
...		arcpy.AddField_management(line,"a","DOUBLE",6,"","","a","NULLABLE","REQUIRED")
