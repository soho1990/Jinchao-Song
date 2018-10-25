
success
>>> import os
... import glob
... from arcpy import env
... env.workspace = r"G:\7gaodetraffic\4delete duplicate"
... # Open one of the files, ### batch clip
... folder_path = r'G:\7gaodetraffic\4delete duplicate'
... road= glob.glob(r'G:\7gaodetraffic\4delete duplicate/*.shp')
... i=1
... for i in range(0,200):
...      # Set input feature class
...     in_dataset = road[i]
...     # Set the field upon which the identicals are found
...     fields = ["direction"]

...     # Set the XY tolerance within which to identical records to be deleted
...     xy_tol = ""

...     # Set the Z tolerance to default
...     z_tol = ""

...     # Execute Delete Identical
...     arcpy.DeleteIdentical_management(in_dataset, fields, xy_tol, z_tol)
...


