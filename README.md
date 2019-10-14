# XternDataScience
This is my code and analysis for the Data Science portion.
The code (xtern.py) has two main functions read_data and scatter_plot.

	Read_data function will read the data and group the data based on the power level

	Scatter_plot function will make scatter plots based on what we are trying to analyze

Also grouped the scooters based on their power level in 3 groups

	low = power_levels of 0 or 1

	med = power_levels of 2 or 3

	high = power_levels of 4 or 5

Based on the code there are some things we are able to clearly see
	We can see from plt 1 - 3 that there are certain locations that the scooters are centered around.
	There are 19 hubs of scooters that are spread throughout the map (seen on plt 2, 3).
	We can label these hubs A - S. Image_labeled shows the hubs and their names. 

We can also look at precise locations to get a better understanding of the hubs.
	These are plts 4- 9.
The locations we are focusing on are: 

plt 4:

x = -.35, -.05
y = -.3, .1

plt 5:

x = .1, .45
y = -.3, .2

plt 6:

x = -.18, -.08
y = .225, .425 

plt 7:

x = .6, 1
y = .4, 1.2 

plt 8:

x = .9, 1.25 
y= 1.25, 1.4 

plt 9:

x = 1.28, 1.4 
y = .825, .925

Each of the plots have the hubs labeled.

From these points and graphs here are the conclusions:

	There are 19 hubs or locations that are popular for the scooters to be around

To fully charge each of the scooters it would take:

The number of scooters for each power level are. 0: 4388 1: 4248 2: 4245 3: 4160 4: 4284 5: 4343 
(4388*5)+(4248*4)+(4245*3)+(4160*2)+(4284*1)+(4343*0)
21940 + 16992 + 12735 + 8320 + 4284 + 0 = 64271 hours

	It would take a total of 64,271 hours to charge all scooters to 5 hours if you are only charging one scooter each time 

The most efficient scooter charging strategy:

Assumptions I am making: 

	The bus can hold 500 scooters. 
	The bus doesn’t have to go all the way to 20.19, 20.19 to charge them. 
	power_level of 4 is a fine power level and we don't need to charge them immediately
	We are charging these scooters during the day when they are still being used
	Each grid is 1 mile. bus can go directly to hubs

Based on plt1 we can see how far the bus is from all the hubs. 
We would first start the bus and head to hubs A,B,C,G,D,E,F,H,I,J,K,N,M,L,O,P,Q,R,S.
This pass we would only focus on the low powered and medium powered scooters (0-3).
These scooters need immediate charge so we would focus them over scooters with 4 power level.

On average each of these hubs will have ~900 scooters in both of these groups. About 450 will be ones of low power and the rest(450 scooters) are medium power.
Each hub we would need to charge them for 8 hours before we are done with that hub and then we can move on to the next hub.
	This would take a total of 8 hours of charge time per hub 
	72 hours of total charge
	Picking up and dropping off the scooters will be .5 minutes per scooter or 142 hours total
	Traveling will take a total of 2 hours 
	Making the total hours of charging the scooters 72+142+2 = 216
	
When we are done with this pass we can then make a returning trip and charge any scooters that dropped further. We would start at s then do the opposite pathing… S,R,Q,P,O…
	We will say that scooters only dropped to 3 hours
	19*2+2 = 40
	N = number of scooters
Picking up scooters would be X = (N*.5)/60
	40 + X hours total 
	Total hours of 256+X hours 

scenario 2:

If this mega bus can hold a large sum of scooters (5k) and can only charge at 20.19, 20.19:

Pick up all scooters that are at power_level 0 in this order A,B,C,G,D,E,F,H,I,J,K,N,M,L,O,P,Q,R,S. Then drive back to 20.19, 20.19.
Charge them for 5 hours.
Return each of the scooters and pick up the power_level 1 scooters while dropping off the new fully charged ones.
Doing this each time for each of the power levels 
	5+4+3+2+1 = 15 hours of charge time 
Traveling to all hubs and picking up each scooter at a rate of .5 minutes per scooter:
	~ 40 hours for scooter pick up and drop off per group
	40 * 5 = 200 hours of picking up 
	2 hour of traveling from each hub and base location per power_level group
	2*5 = 10
10+15+200 
	225 hours of total charging and traveling
