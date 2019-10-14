import pandas as pd, matplotlib.pyplot as plt, random
def read_data(df, minCharge, maxCharge):
    """
    In read_data we have 3 arguments
    df = the data frame we created from the file
    minCharge = the lowest charge of the group we want
    maxCharge = the highest charge of the group we want
    """
    #getting the data for the mincharge
    charge = df[df.power_level == minCharge]
    #seeing how many rows of data are in the min charge
    minChargeCount = len(charge.index)
    #adding the min charge with the max charge to make one full dataframe of the group needed
    fullArray = charge.append(df[df.power_level == maxCharge])
    # using the min count to subtract it from the full array rows to get the max charge rows
    maxChargeCount = len(fullArray.index) - minChargeCount
    #returing the data we grouped based off of the min charge and max charge arguments and how many of each
    return(charge, minChargeCount, maxChargeCount)
def scatter_plot(low, med, high):
    """
    In scatter_plot we have 3 arguments

    low = data of the low charge group (0 , 1)
    med = data of the medium charge group (2 , 3)
    high = data of the high charge group (4, 5)
    """
    # these are locations where scooters are centered around there are 6 locations
    locations = {0: {"x1": -.35, "x2": -.05, "y1": -.3, "y2": .1}, 1: {"x1": .1, "x2": .45, "y1": -.3, "y2": .2}, 2: {"x1": -.18, "x2": -.08, "y1": .225, "y2": .425}, 3: {"x1": .55, "x2": 1, "y1": .4, "y2": 1.2}, 4: {"x1": .9, "x2": 1.25, "y1": 1.25, "y2": 1.4}, 5: {"x1": 1.28, "x2": 1.4, "y1": .825, "y2": .925}}
    counter = 0
    # using counter so we only get certian plots at a time 
    while counter <=3:
        plt.figure(figsize=(10,10))
        if counter == 0:
            # this will get a scatter plot of all the data including the bus location
            title = "(plt1) Bus and Scooter Locations"
            plt.scatter(x=high['xcoordinate'], y=high['ycoordinate'], alpha=.2, facecolors = 'None', edgecolors="Blue", label="High")
            plt.scatter(x=med['xcoordinate'], y=med['ycoordinate'], alpha=.3, facecolors = 'None', edgecolors="Orange", label = "Medium")
            plt.scatter(x=low['xcoordinate'], y=low['ycoordinate'], alpha=.5, facecolors = 'None', edgecolors="Red", label = "Low")
            plt.scatter(x=20.19, y=20.19, edgecolors='black', marker='^', label = "Bus")
            plt.grid(True)
        elif counter == 1:
            # this will only get the low battery locations
            title = "(plt2) Scooters with low Battery Location"
            plt.scatter(x=low['xcoordinate'], y=low['ycoordinate'], alpha=.5, facecolors = 'None', edgecolors="Red", label = "Low")
        elif counter == 2:
            # here we get a scatter plot of all the scooters and we can finally see all the 6 locations
            title = "(plt3) All scooter locations compared with charge"
            plt.scatter(x=high['xcoordinate'], y=high['ycoordinate'], alpha=.2, facecolors = 'None', edgecolors="Blue", label = "High")
            plt.scatter(x=med['xcoordinate'], y=med['ycoordinate'], alpha=.3, facecolors = 'None', edgecolors="Orange", label = "Medium")
            plt.scatter(x=low['xcoordinate'], y=low['ycoordinate'], alpha=.5, facecolors = 'None', edgecolors="Red", label = "Low")
        else:
            # using the dictionary for the locations we are able to see certian locations at a time and analyze them 
            for index in range(6):
                title = "(plt"+str(index+4)+") Focusing on Location "+str(index)+" with all scooters"
                plt.figure(figsize=(10,10))
                location = locations[index]
                plt.xlim(location["x1"], location["x2"])
                plt.ylim(location["y1"], location["y2"])
                plt.scatter(x=high['xcoordinate'], y=high['ycoordinate'], alpha=.2, facecolors = 'None', edgecolors="Blue", label="High")
                plt.scatter(x=med['xcoordinate'], y=med['ycoordinate'], alpha=.3, facecolors = 'None', edgecolors="Orange", label = "Medium")
                plt.scatter(x=low['xcoordinate'], y=low['ycoordinate'], alpha=.5, facecolors = 'None', edgecolors="Red", label = "Low")
                plt.title(title)
                plt.xlabel("xcoordinate")
                plt.ylabel("ycoordinate")
                plt.legend()
                plt.show()
            return locations
        counter += 1
        plt.title(title)
        plt.xlabel("xcoordinate")
        plt.ylabel("ycoordinate")
        plt.legend()
        plt.show()
#using pandas to get a dataframe 
df = pd.read_csv('2019-XTern- Work Sample Assessment Data Science-DS.csv', index_col='scooter_id')
# reading the csv file to only get scooters based off of their charge and grouping them.
lowCharge, zeroCount, oneCount = read_data(df, 0, 1)
medCharge, twoCount, threeCount = read_data(df, 2,3)
highCharge, fourCount, fiveCount = read_data(df,4,5)
#then running scatter plots to compare the charges and scooter locations 
scatter_plot(lowCharge, medCharge, highCharge)
#analysis based off of the counts made in the read_data function 
print("The number of scooters for each power level are. 0:",zeroCount,"1:",oneCount,"2:",twoCount,"3:",threeCount,"4:",fourCount,"5:",fiveCount,".")
print("We classifyed those that are 0 or 1 as low Charge that need immediate charge.")
print("We classifyed the scooters that are 2 or 3 as medium charge. We classifyed the high Charge as scooters with power level of 4 or 5.")
