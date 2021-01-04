# SIRS model on Barabasi Albert random model (without isolation)
This is a simulation of SIRS model, which I computed for my coursework submission.<br/>
This algorithm does not only work for BA model, but any simple(undirected, no multi-link, no self-link) network.<br/>
<br/>
There are three status in SIRS mode:<br/>
-Susceptible.<br/>
-Infected: A node is infected.
It can passes disease to a susceptible with probability alpha.<br/>
Recover and being removed from the network with probability beta.<br/>
Recover but become susceptible again with probability gamma.<br/>
-Removed: A node is removed from the network, meaning that it cannot be infected anymore, but there is a chance for it to join back the network with probability delta.<br/>
<br/>
At time step 0, all nodes are susceptible, and one node is chosen at random to become the first infected.<br/>
<br/>
Other parameters' explaination:<br/>
-experimentTime: Number of experiments you want the algorithms to carry out. At the end, all counts will be averaged.<br/>
-numberOfNodes: Number of nodes in the network, compulsory in generating the BA model. If you want to use your own network. Try: numberOfNodes=len(G.nodes) after the network being initiated.<br/>
-numberOfSteps: Number of steps of each experiment. There is no converging criteria in this algorithm but a limit number of time steps.<br/>

After the network intialisation, a pandas dataframe will be created, contains three columns:<br/>
 - Node ID<br/>
 - It's status; 0,1,2. Correpsonding to susceptible, infected and removed.<br/>
 - It's neighbours<br/>
 <br/>
Three arrays are initiated, they are used to store counts of nodes in each status.<br/>

## Main Loop:
1. For every experiment:</br>
 -Chooses a inital node to infect.<br/>
 -Changes its status to 1.<br/>
2. Seperates all nodes into three list: susceptibleList, infectedList, removedList with different status <br/>
3. Carrying out tasks on infectedList:<br/>
 -Trying to infect all of its neighbours<br/>
 -Trying to be removed<br/>
 -Trying to recover but become susceptible again<br/>
4. Carrying out tasks on removedList:<br/>
 -Trying to become susceptible
5. Stores number of nodes in each list in the arrays.
6. Repeats step 2 - step 5 for expected number of steps.
7. Repeats step 1 - step 6 for expected number of expreiment times.
8. Averages results and plot the results.
<br/>
A plot of preset parameters is also uploaded.


# SIRS model on Barabasi Albert random model (with isolation)
The methodology is similar, while a new appraoch for all nodes is introduced: isolation.<br/>
Any node can choose to isolate itself with probability q, so it will become completely seperated from the others.<br/>
The difference between removed and isolated is that an isolated node will not be able to join back in. Additionally, a removed node can only be changed from an infected node. However, any node with any status can become isolated. Also, since we are assuming that isolation period is long enough that an infected node can be categorized as a recover/removed node eventually.<br/>
A new array will be initated at the start to store all isolated nodes. Also new arrays are created to store the count of isolated nodes for each experiment and time step.<br/>
The only difference in the main loop besides storing results is that: an additional for loop is created. For all nodes in the nodeList, every node can decide to seperate itself with probability q.<br/>
This algorithm can be simplified. A node can be simply removed from the network when it decides to isolate itself and making the algorithm much faster.
A plot of preset parameters is also uploaded.
