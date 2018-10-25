





success
>>> import os
... import glob
... from arcpy import env
... env.workspace = "G:/7gaodetraffic/"
... # Open one of the files,
... folder_path = 'G:/7gaodetraffic/4delete duplicate/'
... road= glob.glob(r'G:/7gaodetraffic/4delete duplicate/*.shp')
... i=1
... for i in range(0,200):
...     target_features = "G:/7gaodetraffic/5topoint/0000POI.shp"
...     join_features = road[i]
...     out_feature_class = "G:/7gaodetraffic/5joinlinetopoint/"+ os.path.basename(road[i])
...     arcpy.SpatialJoin_analysis(target_features, join_features, out_feature_class)
...     print out_feature_class


import os
... import glob
... from arcpy import env
... env.workspace = "G:/7gaodetraffic/"
... road= glob.glob(r'G:/7gaodetraffic/4delete duplicate/2422.shp')
... i=1
... for i in range(0,200):
...     target_features = "G:/7gaodetraffic/5topoint/0000POI.shp"
...     join_features = road[i]
...     out_feature_class = "F:/7gaodetraffic/8/"+ os.path.basename(road[i])
...     arcpy.SpatialJoin_analysis(target_features, join_features, out_feature_class)
...     print out_feature_class



success
>>> import os
... import glob
... from arcpy import env
... env.workspace = "G:/7gaodetraffic/"
... target_features = "F:/7gaodetraffic/8/0000POI.shp"
... join_features = "F:/7gaodetraffic/8/2422.shp"
... out_feature_class = "F:/7gaodetraffic/8/SPEED"
... arcpy.SpatialJoin_analysis(target_features, join_features, out_feature_class)
... print out_feature_class
... 
F:/7gaodetraffic/8/SPEED
>>> import os
... import glob
... from arcpy import env
... env.workspace = "G:/7gaodetraffic/"
... target_features = "F:/7gaodetraffic/8/0000POI.shp"
... join_features = "F:/7gaodetraffic/7poitsjoin/1010status.shp"
... out_feature_class = "F:/7gaodetraffic/8/STATUS"
... arcpy.SpatialJoin_analysis(target_features, join_features, out_feature_class)
... print out_feature_class
... 
F:/7gaodetraffic/8/STATUS