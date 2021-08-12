import plotly.express as px
import csv
import numpy as np

def getdatasource(datapath):
    icecream=[]
    temperature=[]
    with open (datapath) as csvfile:
        cvsreader=csv.DictReader(csvfile)
        for row in cvsreader:
            icecream.append(float(row['Ice-cream Sales( ₹ )']))
            temperature.append(float(row['Temperature']))
    return {'x':icecream,'y':temperature}

def findcorealation(datasource):
    corelation=np.corrcoef(datasource['x'],datasource['y'])
    print('corelation between temperature and icecream is --> ',corelation[0,1])

def setup():
    datapath='Ice-Cream vs Cold-Drink vs Temperature - Ice Cream Sale vs Temperature data.csv'
    datasource=getdatasource(datapath)
    findcorealation(datasource)

setup()