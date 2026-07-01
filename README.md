[excel_reader.py](https://github.com/user-attachments/files/29562101/excel_reader.py)
import pandas as pd


def read_excel(file_path):

    df = pd.read_excel(file_path, header=1)

    # 去掉空行
    df = df.dropna(subset=["设备型号"])

    result = {}

    for _, row in df.iterrows():

        model = str(row["设备型号"]).strip()

        install = row["安装数量（台）"]
        remove = row["拆除数量（台）"]

        if pd.isna(install):
            install = 0

        if pd.isna(remove):
            remove = 0

        if model not in result:
            result[model] = {
                "安装": 0,
                "拆除": 0
            }

        result[model]["安装"] += int(install)
        result[model]["拆除"] += int(remove)

    print("==========统计结果==========")

    for k, v in result.items():
        print(k, v)

    return result
