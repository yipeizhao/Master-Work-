import networkx as nx
import pandas as pd
import random
import matplotlib.pyplot as plt
import numpy as np

# Initiating parameters
alpha=0.1
beta=0.01
gamma=0.005
delta=0.001
experimentTime = 2
numberOfNodes = 500
numberOfSteps=500
# Creating the BA Graph
G=nx.barabasi_albert_graph(numberOfNodes,2)
#Creating a pandas dataframe which has three features:
#Index of a node
#Status of a node
#Nodes' Neighbours
#Status description:
#0:This person is susceptible
#1:This peron is infected
#2:This person is removed
nodeList = list(G.nodes())
status=[0]*len(nodeList)
neighbors=[]
for item in nodeList:
    nodeNeighbors=list(G.neighbors(item))
    neighbors.append(nodeNeighbors)
data = {'Nodes':nodeList,'Status':status,'Neighbours':neighbors}
df=pd.DataFrame(data=data)
originaldf=pd.DataFrame(data=data)

#Return a boolean with the given probability
def decision(probability):
    return random.random() < probability

#Change the status of a person
def changeStatus(node,resultant):
    df.loc[df['Nodes']==node,'Status']=resultant
    
#Turn susceptible neighbours into infected
def infection(node,neighbours):
    for neighbour in neighbours:
        if list(df.loc[df['Nodes']==neighbour,'Status'])[0]==0:
            if decision(alpha):
                changeStatus(neighbour,1)

#Getting the neighbours of a node
def getNeighbors(node):
    return list(df.loc[df['Nodes']==node,'Neighbours'])[0]
    
#Turn an infected person into removed
def removed(node):
    if decision(beta):
        changeStatus(node,2)

#Turn an infected person into susceptible again
def recover(node):
    if decision(gamma):
        changeStatus(node,0)

#Turn an removed person into susceptible again
def join(node):
    if decision(delta):
        changeStatus(node,0)

sumSusceptibleResult=[]
sumRemovedResult=[]
sumInfectedResult=[]
for experimentCount in range (0,experimentTime):
# Main Loop
    df=pd.DataFrame(data=data)
    initialInfected = random.choice(nodeList)
    changeStatus(initialInfected,1)
    susceptibleResult,infectedResult,removedResult=[],[],[]
    for stepCount in range(0,numberOfSteps):
      susceptibleCount=0;infectedCount=0;removedCount=0
      infectedList,susceptibleList,removedList=[],[],[]
      for node in nodeList:
          if list(df.loc[df['Nodes']==node,'Status'])[0]==0:
              susceptibleList.append(node)
              susceptibleCount+=1
          elif list(df.loc[df['Nodes']==node,'Status'])[0]==1:
              infectedList.append(node)
              infectedCount+=1
          elif list(df.loc[df['Nodes']==node,'Status'])[0]==2:
              removedList.append(node)
              removedCount+=1
          else:
              print('Error')
      susceptibleResult.append(susceptibleCount)
      infectedResult.append(infectedCount)
      removedResult.append(removedCount)
      for node in infectedList:
          infection(node,getNeighbors(node))
          removed(node)
          recover(node)
      for node in removedList:
          join(node)
    sumSusceptibleResult.append(susceptibleResult)
    sumInfectedResult.append(infectedResult)
    sumRemovedResult.append(removedResult)      

def averageResult(result):
    averagedResult = [0]*len(result[0])
    for i in range(len(result)):
        for j in range(len(result[0])):
            averagedResult[j] +=result[i][j]
    averagedResult[:] = [(x /len(result))/numberOfNodes for x in averagedResult]
    return averagedResult
averagedSusceptible=averageResult(sumSusceptibleResult)
averagedInfected=averageResult(sumInfectedResult)
averagedRemoved=averageResult(sumRemovedResult)

xlinspace=np.linspace(1,len(removedResult),len(removedResult))
plt.plot(xlinspace,averagedSusceptible,color='red',label='Suspectible Count')
plt.plot(xlinspace,averagedInfected,color='blue',label='Infected Count')
plt.plot(xlinspace,averagedRemoved,color='green',label='Removed Count')
plt.legend()
plt.xlabel('Time step')
plt.ylabel('Fraction nodes')
plt.title('SIRS model on a BA model')
