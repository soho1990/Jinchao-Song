





success
>>> import os
... arcpy.env.workspace= r'F:/7gaodetraffic/7poitsjoin'
... inFeatures="2422.shp"
... fieldObjList= arcpy.ListFields(inFeatures)
... # Create an empty list that will be populated with field names          
... fieldNameList = []  
... # For each field in the object list, add the field name to the  
... #  name list.  If the field is required, exclude it, to prevent errors  
... for field in fieldObjList:  
...     if not field.required:  
...         fieldNameList.append(field.name)  
... print fieldNameList



