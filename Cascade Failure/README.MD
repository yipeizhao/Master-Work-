# A cascade failure simulation on a real network.

The network is downloaded from http://networkrepository.com/soc-hamsterster.php. <br/>
Reference: {nr,<br/>
     title={The Network Data Repository with Interactive Graph Analytics and Visualization},<br/>
     author={Ryan A. Rossi and Nesreen K. Ahmed},<br/>
     booktitle={AAAI},<br/>
     url={http://networkrepository.com},<br/>
     year={2015}<br/>
}<br/>

This is a cascade failure propagation model for any simple graph. For every nodes, if the fraction of it's failed neighbours over all neighbours is larger than a preset parameter phi, fail the node.
By varying phi, we can evaluate the performance of the network on defending against cascade failure.<br/>
The basic logic for every single experiment is as follows:<br/>
For all nodes in the graph, check the number of its failed neighbours, if the number divided by neighbour number is larger than phi, remove the node from the network.<br/>
Initially, I was thinking abot using the similar appraoch for SIRS model. However, the algorithm takes a deadly amount of time to compute the result. Removing the failed nodes increase the amount of time ran by the algorithm.
A plot of the result is uploaded.
