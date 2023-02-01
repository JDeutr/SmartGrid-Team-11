# SmartGrid-Team-11
SmartGrid case for Algoritmen en Heuristieken from The Voltage Visionairs(Team11)

Many homes today have solar panels to produce their own energy. Fortunately, those installations often produce more than is needed for their own consumption. The surplus could be sold back to the supplier, but the infrastructure (the grid) is often not up to the task. To manage the peaks in consumption and production, batteries need to be installed. For this case different algorihms where tested to find the best solution and the lowest cost for three different neighbourhouds/districts. The lowest cost can be generated by laying as less cables as needed to connect the houses with the batteries. 

<br/>To run:
<br/> python main.py (district) (amount of times) (algorithm) (type of cost calculation)
<br/> python main.py 1 1 random own

district:
- 1
- 2
- 3

amount of times:
- number of runs 

algorithms:
- random
- nearest
- prim
- sa (simulated annealing)

types of cost calculation:
- own
- shared

Results can be found in output.json
