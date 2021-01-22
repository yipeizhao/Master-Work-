import pandas as pd

import numpy as np
rawData = pd.read_csv('data.csv')
data = pd.read_csv('data.csv')
data=data.rename(columns={'vhigh':'buyingPrice',
                          'vhigh.1':'maintenanceCost',
                          '2':'doors',
                          '2.1':'capacity',
                          'small':'luggageSpace',
                          'low':'safety',
                          'unacc':'acceptability'})

categories = {'low':0,'med':1,'high':2,'vhigh':3}
categories1 = {'1':1,'2':2,'3':3,'4':4,'5more':5,'more':5}
categories2 = {'small':0,'med':1,'big':2}
accTransform = {'unacc':0,'acc':1,'good':2,'vgood':3}
data.buyingPrice=data.buyingPrice.map(categories)
data.maintenanceCost = data.maintenanceCost.map(categories)
data.safety = data.safety.map(categories)
data.luggageSpace = data.luggageSpace.map(categories2)
data.doors = data.doors.map(categories1)
data.capacity= data.capacity.map(categories1)
data.acceptability = data.acceptability.map(accTransform)

costDictionary={(0,0):0,(0,1):1,(0,2):2,(0,3):3,
            (1,0):4,(1,1):5,(1,2):6,(1,3):7,
            (2,0):8,(2,1):9,(2,2):10,(2,3):11,
            (3,0):12,(3,1):13,(3,2):14,(3,3):15,
    }
costList = []
for i in range(0,len(data.buyingPrice)):
    tempTuple=(data.iloc[i].buyingPrice,data.iloc[i].maintenanceCost)
    value = costDictionary[tempTuple]
    costList.append(value)
    

doorsList = set(data.doors)
capacityList = set(data.capacity)
luggageList = set(data.luggageSpace)
import itertools
product = list(itertools.product(doorsList,capacityList,luggageList))
spaceIndex = np.linspace(0,len(product)-1,len(product))

spaceList=[]
spaceDictionary=dict(zip(product, spaceIndex))
for i in range(0,len(data.buyingPrice)):
    tempTuple=(data.iloc[i].doors,data.iloc[i].capacity,data.iloc[i].luggageSpace)
    value = spaceDictionary[tempTuple]
    spaceList.append(value)
    
dataset={'Cost':costList,'Space':spaceList,'Safety':list(data.safety),
      'Acceptability':data.acceptability
      }
df=pd.DataFrame(dataset)
df.to_csv('TransformedData.csv')

from sklearn.decomposition import PCA
pca=PCA(n_components=3)
pca.fit(data)
x_pca=pca.transform(data)
print(x_pca.shape)
x_pca3=pd.DataFrame(data=x_pca)
x_pca3['Acceptability']= data.acceptability
x_pca3.to_csv('PCAData.csv')