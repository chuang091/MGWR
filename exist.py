import arcpy

# 指定要檢查的要素類別的路徑
feature_class = r"C:\Users\chuan\OneDrive\桌面\MGWR\gis2023.gdb\main5_MGWR"

# 檢查要素類別是否存在
if arcpy.Exists(feature_class):
    print(f"{feature_class} 存在")
    # 列出要素類別中的所有欄位
    fields = arcpy.ListFields(feature_class)
    
    # 輸出欄位名稱 (header)
    print(f"Feature Class '{feature_class}' 的欄位：")
    for field in fields:
        print(field.name)
else:
    print(f"{feature_class} 不存在")