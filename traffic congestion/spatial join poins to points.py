


















success
import os
... import glob
... from arcpy import env
... env.workspace = "G:/7gaodetraffic/6deletefields/"
... # Open one of the files,
... folder_path = 'G:/7gaodetraffic/6deletefields/'
... road= glob.glob(r'G:\7gaodetraffic\6deletefields/*.shp')
... output= glob.glob('G:/7gaodetraffic/7poitsjoin/*.shp')
... i=1
... a=1
... for i in range(0,3):
...     target_features = road[i+1]
...     for a in range(0,3):
...         join_features = output[a]
...         out_feature_class = "G:/7gaodetraffic/7poitsjoin/"+ os.path.basename(road[i+1])
...         arcpy.SpatialJoin_analysis(target_features, join_features, out_feature_class)
...         print out_feature_class




import os
... import glob
... from arcpy import env
... env.workspace = "G:/7gaodetraffic/6deletefields/"
... # Open one of the files,
... folder_path = 'G:/7gaodetraffic/6deletefields/'
... road= glob.glob(r'G:\7gaodetraffic\6deletefields/*.shp')
... output= glob.glob('G:/7gaodetraffic/7poitsjoin/*.shp')
... i=1
... a=1
... for i in range(0,3):
...     output= glob.glob('G:/7gaodetraffic/7poitsjoin/*.shp')
...     # Set local parameters
...     inFeatures = output[i]
...         for a in range(0,3):
...             idFeatures = road[a]
...             outFeatures = "G:/7gaodetraffic/7poitsjoin/"+ os.path.basename(road[i+1])
...     # Process: Use the Identity function
...     arcpy.Identity_analysis (inFeatures, idFeatures, outFeatures)


import os
... import glob
... from arcpy import env
... env.workspace = "G:/7gaodetraffic/"
... # Open one of the files,
... folder_path = 'G:/7gaodetraffic/6deletefields/'
... road= glob.glob(r'G:\7gaodetraffic\6deletefields/*.shp')
... output= glob.glob('G:/7gaodetraffic/7poitsjoin/*.shp')
... i=1
... a=1
... for i in range(0,4):
...     output= glob.glob('G:/7gaodetraffic/7poitsjoin/*.shp')
...     # Set local parameters
...     inFeatures = output[i]
...     a=1
...     for a in range(0,7):
...         idFeatures = road[a+1]
...         outFeatures = "G:/7gaodetraffic/7poitsjoin/"+ os.path.basename(road[a+1])
...         # Process: Use the Identity function
...         arcpy.Identity_analysis (inFeatures, idFeatures, outFeatures)
...     print outFeatures


identity  success
import os
... import os
... import glob
... from arcpy import env
... env.workspace = "G:/7gaodetraffic/"
... # Open one of the files,
... folder_path = 'G:/7gaodetraffic/6deletefields/'
... road= glob.glob(r'G:\7gaodetraffic\6deletefields/*.shp')
... output= glob.glob('G:/7gaodetraffic/7poitsjoin/*.shp')
... i=1
... for i in range(0,7):
...     output= glob.glob('G:/7gaodetraffic/7poitsjoin/*.shp')
...     # Set local parameters
...     inFeatures = output[i]
...     idFeatures = road[i+1]
...     outFeatures = "G:/7gaodetraffic/7poitsjoin/"+ os.path.basename(road[i+1])
...     # Process: Use the Identity function
...     arcpy.Identity_analysis (inFeatures, idFeatures, outFeatures)
...     print outFeatures




