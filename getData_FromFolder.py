import pandas as pd
import os

names = ["Date", "Time", "Code", "Values"]
folder_path = "/Users/martin/Desktop/Diabetes-Data/diabetes/Diabetes-Data"
codes =  {
33 : 'RID',
34 : 'NPHID',
48: 'UBGID',
58: 'PBBGM',
60: 'PRLBBGM'}


def read_fromFolder(path, names):
    files = [i for i in (os.path.join(path, f) for f in os.listdir(path)) if os.path.isfile(i)]

    dfs = []
    for file in files:
        df = pd.read_csv(file, names = names, sep = "\t", encoding = "utf-8")
        dfs.append(df)
    return pd.concat(dfs)

if __name__ == "__main__":
    df = read_fromFolder(folder_path, names)
    print(df.head(50))