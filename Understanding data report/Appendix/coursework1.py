import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import time
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn import svm
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier
import matplotlib.image as mpimg

rawData = pd.read_csv('data.csv')
data = pd.read_csv('data.csv')
data=data.rename(columns={'vhigh':'buyingPrice',
                          'vhigh.1':'maintenanceCost',
                          '2':'doors',
                          '2.1':'capacity',
                          'small':'luggageSpace',
                          'low':'safety',
                          'unacc':'acceptability'})
data.to_csv('test.csv')
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



f1=data['buyingPrice'].value_counts().sort_index()
f2=data['maintenanceCost'].value_counts().sort_index()
f3=data['doors'].value_counts().sort_index()
f4=data['capacity'].value_counts().sort_index()
f5=data['luggageSpace'].value_counts().sort_index()
f6=data['safety'].value_counts().sort_index()

invCat  = {v: k for k, v in categories.items()}
invCat1 = {v: k for k, v in categories1.items()}
invCat2 = {v: k for k, v in categories2.items()}
invCat3 = {v: k for k, v in accTransform.items()}

fig1 ,axs = plt.subplots(3,2,figsize=(10,15))
fig1.suptitle('Feature Value Distribution')
axs[0,0].bar(f1.index.map(invCat),f1)
axs[0,0].set_title('Buying Price')
axs[0,1].bar(f2.index.map(invCat),f2)
axs[0,1].set_title('maintenance Cost')
axs[1,0].bar(f3.index.map(invCat1),f3)
axs[1,0].set_title('Doors')
axs[1,1].bar(f4.index.map(invCat1),f4)
axs[1,1].set_title('Capacity')
axs[2,0].bar(f5.index.map(invCat2),f5)
axs[2,0].set_title('Luggage Space')
axs[2,1].bar(f6.index.map(invCat),f6)
axs[0,0].set_ylabel('Frequency')
axs[1,0].set_ylabel('Frequency')
axs[2,0].set_ylabel('Frequency')
axs[2,1].set_title('Safety')

img1 = mpimg.imread('Figures/Boxplot/buyingprice.png')
img2 = mpimg.imread('Figures/Boxplot/maintaincost.png')
img3 = mpimg.imread('Figures/Boxplot/doors.png')
img4 = mpimg.imread('Figures/Boxplot/luggagespace.png')
img5 = mpimg.imread('Figures/Boxplot/capacity.png')
img6 = mpimg.imread('Figures/Boxplot/safety.png')
imgs =[];imgs.extend((img1,img2,img3,img4,img5,img6))
fig = plt.figure(figsize = (20,20))
ax1 = fig.add_subplot(6,1,1)
ax1.imshow(img1)
plt.xticks([])
plt.yticks([])
ax1.set_xlabel('Buying price')
ax2 = fig.add_subplot(6,1,2)
ax2.imshow(img2)
ax2.set_xlabel('Maintenance Cost')
plt.xticks([])
plt.yticks([])
ax3 = fig.add_subplot(6,1,3)
ax3.imshow(img3)
ax3.set_xlabel('Doors')
plt.xticks([])
plt.yticks([])
ax4 = fig.add_subplot(6,1,4)
ax4.imshow(img4)
ax4.set_xlabel('Luggage Space')
plt.xticks([])
plt.yticks([])
ax5 = fig.add_subplot(6,1,5)
ax5.imshow(img5)
ax5.set_xlabel('Capacity')
plt.xticks([])
plt.yticks([])
ax6 = fig.add_subplot(6,1,6)
ax6.imshow(img6)
ax6.set_xlabel('Safety')
plt.xticks([])
plt.yticks([])
plt.show()

fig3=plt.figure()
classes = data['acceptability'].value_counts().sort_index()
plt.bar(classes.index.map(invCat3),classes)
plt.title('Classes Distribution')
plt.ylabel('Frequency')


xData = data.drop('acceptability',axis=1).astype(float)
yData = data.acceptability.astype(float)
xTrain,xTest,yTrain,yTest = train_test_split(xData, yData,
                                             test_size=0.15,
                                             random_state=int(time.time()))



lgModel = LogisticRegression()
lgModel.max_iter=500
lgModel.fit(xTrain,yTrain)
print(lgModel.score(xTest,yTest))
yPred = lgModel.predict(xTest)
cm=confusion_matrix(yTest, yPred)
plt.figure(figsize = (9,6))
importance = lgModel.coef_[0]
for i,v in enumerate(importance):
 	print('Feature: %0d, Score: %.5f' % (i,v))
columns = list(data.columns)
columns.remove('acceptability')
plt.bar(columns, importance)
plt.ylabel('Importance Score')
plt.title('Analysing important features')
plt.show()

