# Area coverage for campaign planning
This repository solves the area coverage problem for planning long term AUV missions.

The achieved maturity of autonomous underwater vehicles (AUVs) makes the deployment of multi-vehicle networks practical and cost-effective. Many scientific, civilian and military applications nowdays require the usage of AUVs. 
From an end user perspective the ability to scale from one asset to multiple vehicles able to coordinate their activities means maximising the benefits. 
To maximise their operational effectiveness, one critical decision variable that has a direct impact on both the cost and performance, lies in how to properly place the different sensors in the target environment.
The number of sensors, the dedicated communication networks, can contribute a significant portion of the overall cost. 
The placement of the vehicles determines the overall mission time and the associated coverage area.
In fact, one critical weakness of existing systems lies in the ability to plan multi-days, multi-vehicle missions over large areas. 
The ability to quickly allocate each vehicle to one specific area, to monitor the mission performance, and to understand the quality of the data gathered would represent a key capability to speed up the uptake of the technology even more.
This repository addresses the area coverage problem and aims at providing a solution to efficiently schedule AUV operations over multi-days and large areas.

## Table of content
-[01-knapsacking-the-area-coverage-problem.ipynb](01-knapsacking-the-area-coverage-problem.ipynb)
 Main notebook. Describes the problem and how to solve using convex optimisation.
 
-[02-cvxpy.ipynb](02-cvxpy.ipynb) 
 Playground on cvxpy applied to the area coverage problem.
 
# Dependencies
This repository uses cvxpy, available from [cvxpy.org](cvxpy.org)  
It is also suggested to install cvxopt to make sure all the solvers that come packaged with cvxpy can be used.

Some of this repository relies on the GLPK_MI solver. This is a special solver designed for IP problems.
To install GLPK (in /usr/local/):
- Download the latest version of GLPK from the gnu website.
- Untar it: `tar -xzf glpk-4.43.tar.gz`
- and run 
```
./configure -prefix=/usr/local
make
sudo make install
```
At this point, you should have GLPK installed. To verify run:
```
which glpsol
```
output: `/usr/local/bin/glpsol`

# How to run it
Open [01-knapsacking-the-area-coverage-problem.ipynb](01-knapsacking-the-area-coverage-problem.ipynb) and run each cell.
