import pandas as pd
from getData_FromFolder import read_fromFolder, codes, names, folder_path
import warnings
warnings.filterwarnings("ignore")
import matplotlib.pyplot as plt

def processTimeSeries(group):

    dfm = read_fromFolder(folder_path, names)
    groups = dfm.groupby(by = "Code")
    ts = groups.get_group(group)
    ts["Date_"] = ts["Date"] +' '+ ts["Time"]
    ts["Date_"] = pd.to_datetime(ts["Date_"], format = "%m-%d-%Y %H:%M", errors = "coerce")
    ts.drop(columns = ["Date", "Time", "Code"], inplace = True)
    ts.rename(columns = {"Values": codes[group], "Date_": "Date"}, inplace = True)
    ts = ts.set_index("Date")
    return ts



def get_TimeSeries(codes):

    TS = []
    for k,_ in codes.items():

        ts = processTimeSeries(k)
        ts[codes[k]] = (ts[codes[k]].astype(str).str.extract(r'^(\d{1})', expand=False)).astype(float) # Review REGX
        TS.append(ts)

    return TS

def resampleTS():
    TS = get_TimeSeries(codes)
    for ts in TS:
        ts.resample("10D").mean().plot()
        plt.show()

if __name__ == "__main__":
    TS = get_TimeSeries(codes)
    print(TS[0].head(100))

    resampleTS()