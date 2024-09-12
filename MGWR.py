import arcpy
import sys
sys.setrecursionlimit(3000)
arcpy.ImportToolbox(r"C:\Program Files\ArcGIS\Pro\Resources\ArcToolBox\Toolboxes\Spatial Statistics Tools.tbx")
#arcpy.ImportToolbox(r"@\Spatial Statistics Tools.tbx")
#Path to the workspace
arcpy.env.workspace = r"C:\Users\chuan\OneDrive\桌面\MGWR"

arcpy.stats.MGWR(
    in_features="main4.shp",
    dependent_variable="convenienc",
    model_type="CONTINUOUS",
    explanatory_variables="busC;metroC;bikeC;roadC;popDenC",
    #path to output (Known bug)
    output_features= r"C:\Users\chuan\OneDrive\桌面\MGWR\gis2023.gdb\main5_MGWR",
    neighborhood_type="NUMBER_OF_NEIGHBORS",
    neighborhood_selection_method="GOLDEN_SEARCH",
    distance_unit="METERS",
    robust_prediction="ROBUST",
    local_weighting_scheme="BISQUARE",
    scale="SCALE_DATA"
)

