






>>> import os
... import glob
... from arcpy import env
... env.workspace = "G:/7gaodetraffic/"
... # Open one of the files,
... folder_path = r'G:/7gaodetraffic/5joinlinetopoint/'
... road= glob.glob(r'G:/7gaodetraffic/5joinlinetopoint/*.shp')
... i=1
... for i in range(0,200):
... arcpy.CopyFeatures_management(road[i], "G:/7gaodetraffic/6deletefields/")
... road1= glob.glob(r'G:/7gaodetraffic/6deletefields/*.shp')
... for a in range(0,200):
... arcpy.DeleteField_management((road1[a]),
                             ["Join_Count", "TARGET_FID", "Id_1", "name","direction"])

import os
... import glob
... from arcpy import env
... env.workspace = "G:/7gaodetraffic/"
... # Open one of the files,
... folder_path = r'G:\7gaodetraffic\6deletefields\'
... road= glob.glob(r'G:\7gaodetraffic\6deletefields\*.shp')
... i=0
... for i in range(0,200):
... arcpy.DeleteField_management((road[i]),
...                              ["Join_Count", "TARGET_FID", "Id_1", "name","direction"])

success
import os
... import glob
... from arcpy import env
... env.workspace = "G:/7gaodetraffic/"
... # Open one of the files,
... folder_path = 'G:/7gaodetraffic/6deletefields/'
... road= glob.glob('G:/7gaodetraffic/5joinlinetopoint/*.shp')
... i=0
... for i in range(0,200):
... # Set local variables
...     inFeatures = road[i]
...     outFeatureClass = "G:/7gaodetraffic/6deletefields/"+ os.path.basename(road[i])
...     dropFields = ["Join_Count", "TARGET_FID", "Id_1", "name","direction"]
...     # Execute CopyFeatures to make a new copy of the feature class
...     #  Use CopyRows if you have a table
...     arcpy.CopyFeatures_management(inFeatures, outFeatureClass)
...     # Execute DeleteField
...     arcpy.DeleteField_management(outFeatureClass, dropFields)



delete multiple fields

import glob
... import os
... from arcpy import env
... env.workspace = "F:/7gaodetraffic/"
... # Open one of the files,
... folder_path = r'F:/7gaodetraffic/7poitsjoin/2422.shp'
... inFeatures = folder_path    
... outFeatureClass = "F:/7gaodetraffic/8/24223.shp"
... A=outFeatureClass
... fieldObjList= arcpy.ListFields(A)
... # Create an empty list that will be populated with field names          
... fieldNameList = []  
... # For each field in the object list, add the field name to the  
... #  name list.  If the field is required, exclude it, to prevent errors  
... for field in fieldObjList:  
...     if not field.required:  
...         fieldNameList.append(field.name) 
... print fieldNameList
... for FID in fieldNameList
...		FID="FID*"
...		dropFields = [FID]
... # Execute CopyFeatures to make a new copy of the feature class
... #  Use CopyRows if you have a table
... arcpy.CopyFeatures_management(inFeatures, outFeatureClass)


 

