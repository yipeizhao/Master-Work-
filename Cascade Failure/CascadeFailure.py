import networkx as nx
import csv
import random
import numpy as np
import matplotlib.pyplot as plt
#Import the network
f=open('Hamsterster.csv','r')
Ef=csv.reader(f)
next(f)
E=[(row[0],row[1]) for row in Ef]
originalG=nx.Graph()
originalG.add_edges_from(E)
#Chooose the giant component to work with
Gcc = sorted(nx.connected_components(originalG), key=len, reverse=True)
Gc=nx.Graph()
Gc = originalG.subgraph(Gcc[0]);
GcSize=len(Gc.nodes)
#Creating a node list and number of its neighbours
nodeList=list(Gc.nodes())
neighbors=[]
for item in nodeList:
    nodeNeighbors=list(Gc.neighbors(item))
    neighbors.append(len(nodeNeighbors))
neighbourNumber=dict(zip(nodeList,neighbors))
#Returning a list, which contains neighbours of a ndoe
def getNeighbours(node):
    neighbourList=list(G.neighbors(node))
    return neighbourList

#Trying to fail a node, return true if successfully failed, false otherwise
def failNode(node):
    currentNeighbourNumber=len(getNeighbours(node))
    initialNeighbourNumber=neighbourNumber[node]
    if (initialNeighbourNumber-currentNeighbourNumber)/initialNeighbourNumber>phi:
        return True
    else:
        return False
phiSpace=np.linspace(0,1,100)
#Storing the results of different phi
phiResult=[]
#Main loop
for phi in phiSpace:
#SumResult store the summation of the result of a single experiment
    sumResult = []
    for experimentTime in range(0,500):
        #Creating a copy of the giant component
        G=nx.Graph(Gc)
        #Failing the first victim
        initialFailed=random.choice(nodeList)
        #Creating a check list which stores the neighbours of a failed node
        #Since not all nodes have failing neighbours
        checkList=[]
        #Stores the neighbour of the first failed node
        for item in getNeighbours(initialFailed):
            checkList.append(item)    
        #Remove the first failed node
        G.remove_node(initialFailed)
        #Iterate until the check list becomes empty
        while len(checkList)!=0:
            #For every node in the node list, try to fail it
            #If it fail, append all of its current neighbours into the check list
            #And remove it from the check list
            #If it didn't fail, still remove it from the checklist
            for node in checkList:
                if failNode(node):
                    for item in getNeighbours(node):
                        if item not in checkList:
                            checkList.append(item)
                    G.remove_node(node)
                    checkList.remove(node)
                else:
                    checkList.remove(node)
        #When the checklist becomes empty, append it into the sumResult list
        sumResult.append((len(Gc.nodes)-len(G.nodes))/len(Gc.nodes))
    #After 500 experiment, append results of all 00 experiments into the phiResult list
    phiResult.append(sumResult)
#Find the average result by different phi
averageResult=[]
for result in phiResult:
    averageResult.append(sum(result)/len(result))
plt.plot(phiSpace,averageResult)
plt.xlabel('phi')
plt.ylabel('Fraction of nodes remain in the giant component')
plt.title('Cascade Failing')