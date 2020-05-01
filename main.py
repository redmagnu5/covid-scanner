import torchxrayvision as xrv


d_covid19 = xrv.datasets.COVID19_Dataset(imgpath="covid-chestxray-dataset/images", csvpath="covid-chestxray-dataset/metadata.csv")
