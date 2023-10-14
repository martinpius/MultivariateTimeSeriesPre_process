### In this project we write a simple modules to read and preprocess multiple time series files from a folder using Pandas.
###### We are employing a multivariate time series dataset from UCI. This data can be freely downloaded at
 <https://archive.ics.uci.edu/dataset/34/diabetes>


## Specifically we:-:ghost:
- Read multiple files from a folder
- Combining the datasets into one big dataframe
- Grouping and extracting individual time series
- Processing, resampling, and plotting the series

### For this tutorial we will only use some selected time series
 To load the datasets from a folder we run write the following module :cd::cd:

 ``` python
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

```
To preprocess the data we use Groupby from Pandas to group the data of similar time-series object, Pandas date_time to process the date column and indexing the result by date :cd::cd:
```python
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

```
To obtain an individual series from our grouped dataset we use the follwing codes snippest. Also we clean the Value columns and converted to a proper format :cd:

```python

def get_TimeSeries(codes):

    TS = []
    for k,_ in codes.items():

        ts = processTimeSeries(k)
        ts[codes[k]] = (ts[codes[k]].astype(str).str.extract(r'^(\d{1})', expand=False)).astype(float) # Review REGX
        TS.append(ts)

    return TS
'''
```
Finally we resample 10 days time-stamps and plot the values using the following codes :cd:

```python

def resampleTS():
    TS = get_TimeSeries(codes)
    for ts in TS:
        ts.resample("10D").mean().plot()
        plt.show()

if __name__ == "__main__":
    TS = get_TimeSeries(codes)
    print(TS[0].head(100))

    resampleTS()
```
Thank you:dog::wink::smile:!!!! 
##### For more on this project and others, follow my **GitHub** at : <https://github.com/martinpius> 



