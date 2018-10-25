





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

 
import arcpy

# Run the Copy Features tool, setting the output to the geometry object.
# geometries is returned as a list of geometry objects.
geometries = arcpy.CopyFeatures_management("c:/data/streets.shp",
                                           arcpy.Geometry())

# Walk through each geometry, totaling the length
length = 0
for geometry in geometries:
    length += geometry.length

print("Total length: {0}".format(length))



import arcpy
fc= "F:/7gaodetraffic/4delete duplicate/0130.shp"
cursor= arcpy.da.SearchCursor(inFc, "SHAPE@")
for geom in cursor:
    total_length= geom.length
print total_length