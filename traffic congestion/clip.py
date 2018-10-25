

sucess
...import os
... # This is the path where all the files are stored.
... folder_path = 'G:/7gaodetraffic/1010'
... # Open one of the files,
... for data_file in sorted(os.listdir(folder_path)):
...     print data_file

sucess
>>> import glob
... print glob.glob(r'G:/7gaodetraffic/1010/*.shp')
...
...





import os
import glob
from arcpy import env
env.workspace = "G:/7gaodetraffic/1010/"
... # This is the path where all the files are stored.
... folder_path = 'G:/7gaodetraffic/1010'
... # Open one of the files, ### batch clip
... for road in sorted(os.listdir(folder_path)):
        input_feature=road
        clip_feature= "research_area.shp"
        output_feature = "'G:/7gaodetraffic/2clip' + os.path.basename(road) + 'clip'"
        xy_tolerance = ""
        arcpy.Clip_analysis(input_feature, clip_feature, output_feature, xy_tolerance)
        print road+"  has done"



try clip success
>>> # Import system modules
... import arcpy
... from arcpy import env
... # Set workspace
... env.workspace = "G:/7gaodetraffic/1010/"
... # Set local variables
... in_features = "0000.shp"
... clip_features = "research_area.shp"
... out_feature_class = "G:/7gaodetraffic/2clip/0000clip.shp"
... xy_tolerance = ""
... # Execute Clip
... arcpy.Clip_analysis(in_features, clip_features, out_feature_class, xy_tolerance)
...

import os
import glob
from arcpy import env
env.workspace = "G:/7gaodetraffic/1010/"
... # Open one of the files, ### batch clip
... folder_path = 'G:/7gaodetraffic/1010'
for road in sorted(os.listdir(folder_path)):
    print road
    if road.split(".")[1]=='shp':
        input_feature=road
        clip_feature= "research_area.shp"
        output_feature = r"G:/7gaodetraffic/2clip_ "+os.path.basename(road)+"_clip.shp"
        xy_tolerance = ""
        arcpy.Clip_analysis(input_feature, clip_feature, output_feature, xy_tolerance)
        print output_feature

>>> import os
... import glob
... from arcpy import env
... env.workspace = "G:/7gaodetraffic/1010/"
... # Open one of the files, ### batch clip
... folder_path = 'G:/7gaodetraffic/1010'
... for road in sorted(os.listdir(folder_path)):
...     if road.split(".")[1]=='shp':
...         input_feature=road
...         clip_feature= "research_area.shp"
...         output_feature = r（"G:/7gaodetraffic/2clip_ ”+"_clip.shp"+ road.split（'.'）[1]）
...         xy_tolerance = ""
...         arcpy.Clip_analysis(input_feature, clip_feature, output_feature, xy_tolerance)
...         print output_feature


>>> import os
... import glob
... from arcpy import env
... env.workspace = "G:/7gaodetraffic/1010/"
... # Open one of the files, ### batch clip
... folder_path = 'G:/7gaodetraffic/1010'
... for road in sorted(os.listdir(folder_path)):
...     if road.split(".")[1]=='shp':
...         input_feature=road
...         clip_feature= "research_area.shp"
...         output_feature = "G:/7gaodetraffic/2clip/"+"_clip.shp"+os.path.basename(road)"
...         xy_tolerance = ""
...         arcpy.Clip_analysis(input_feature, clip_feature, output_feature, xy_tolerance)
...         print output_feature


>>> import os
... import glob
... from arcpy import env
... env.workspace = "G:/7gaodetraffic/1010/"
... # Open one of the files, ### batch clip
... folder_path = 'G:/7gaodetraffic/1010'
... for road in sorted(os.listdir(folder_path)):
...     if road.split(".")[1]=='shp':
...         input_feature=road
...         clip_feature= "research_area.shp"
...         output_feature = "G:/7gaodetraffic/2clip”+road.split（"."）[1]+"_clip.shp"
...         xy_tolerance = ""
...         arcpy.Clip_analysis(input_feature, clip_feature, output_feature, xy_tolerance)
...         print output_feature

success one
>>> import os
... import glob
... from arcpy import env
... env.workspace = "G:/7gaodetraffic/1010/"
... # Open one of the files, ### batch clip
... folder_path = 'G:/7gaodetraffic/1010'
        if road.split(".")[1]=='shp':
...         input_feature=road
...         clip_feature= "research_area.shp"
...         output_feature = "G:/7gaodetraffic/2clip/ "+"_clip"+ os.path.basename(road)
...         xy_tolerance = ""
...         arcpy.Clip_analysis(input_feature, clip_feature, output_feature, xy_tolerance)
...         print output_feature

>>> import os
... import glob
... from arcpy import env
... env.workspace = "G:/7gaodetraffic/1010/"
... # Open one of the files, ### batch clip
... folder_path = 'G:/7gaodetraffic/1010'
... road= glob.glob(r'G:/7gaodetraffic/1010/*.shp')
... years = np.arange(0000,2400)
... for yr in years:
... for road in sorted(os.listdir(folder_path)):
...         input_features=road
...         clip_features= "research_area.shp"
...         output_features = "G:/7gaodetraffic/2clip/"+ os.path.basename(road)
...         xy_tolerance = ""
...         arcpy.Clip_analysis(input_features, clip_features, output_features, xy_tolerance)
...         print output_features

Yuhang
>>> import os
... import glob
... from arcpy import env
... env.workspace = "G:/7gaodetraffic/1010/"
... # Open one of the files, ### batch clip
... folder_path = 'G:/7gaodetraffic/1010'
... road= glob.glob(r'G:/7gaodetraffic/1010/*.shp')
... i=1
... for i in range(0,200):
...     input_features = road[i]
...     clip_features= "research_area.shp"
...     output_features = "G:/7gaodetraffic/2clip/"+ os.path.basename(road[i])
...     xy_tolerance = ""
...     arcpy.Clip_analysis(input_features, clip_features, output_features, xy_tolerance)
...     print output_features
...


