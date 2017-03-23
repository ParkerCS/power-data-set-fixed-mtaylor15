'''
Use the power_data.csv file AND the zipcode database
to answer the questions below.  Make sure all answers
are printed in a readable format. (i.e. "The city with the highest electricity cost in Illinois is XXXXX."

The power_data dataset, compiled by NREL using data from ABB,
the Velocity Suite and the U.S. Energy Information
Administration dataset 861, provides average residential,
commercial and industrial electricity rates by zip code for
both investor owned utilities (IOU) and non-investor owned
utilities. Note: the file includes average rates for each
utility, but not the detailed rate structure data found in the
OpenEI U.S. Utility Rate Database.

This is a big dataset.
Below are some questions that you likely would not be able
to answer without some help from a programming language.
It's good geeky fun.  Enjoy

FOR ALL THE RATES, ONLY USE THE BUNDLED VALUES (NOT DELIVERY).  This rate includes transmission fees and grid fees that are part of the true rate.
'''


import csv
from operator import itemgetter
import re
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import statistics


#1  What is the average residential rate for YOUR zipcode? You will need to read the power_data into your program to answer this.  (7pts)
power_data = []
file = open("power_data.csv", "r")
reader = csv.reader(file)
for line in reader:
    power_data.append(line)
power_data = power_data[1:]

for i in range(len(power_data)):
    power_data[i][-1] = float(power_data[i][-1])

power_data.sort(key=itemgetter(-1))
print("The average of all of them is", power_data[len(power_data)//2][-1])


for i in range(len(power_data)):
    if power_data[i][0] == "60615" and power_data[i][4] == "Bundled":
        print("Average bundled  rate for my zipcode(60615) is: " , power_data[i][-1],)

file.close()
#2 What is the MEDIAN rate for all BUNDLED RESIDENTIAL rates in Illinois? Use the data you extracted to check all "IL" zipcodes to answer this. (10pts)

illinois_bund_res = []

for i in range(len(power_data)):
    if power_data[i][4] == "Bundled" and power_data[i][3] == "IL":
        illinois_bund_res.append(power_data[i][8])
print("The median is", statistics.median(illinois_bund_res))


#power_data.sort(key=itemgetter(-2))
#print(power_data[len(power_data[-2]))




#3 What city in Illinois has the lowest residential rate?  Which has the highest?  You will need to go through the database and compare each value for this one. Then you will need to reference the zipcode dataset to get the city.  (15pts)

illonois_res_rate = []
for i in range(len(power_data)):
    if power_data[i][4] == "Bundled" and power_data[i][3] == "IL":
        illonois_res_rate.append(power_data[i][-1])
print(illonois_res_rate)


for i in range(len(power_data)):
    power_data[i][-1] = float(power_data[i][-1])
power_data.sort(key=itemgetter(-1))



#FOR #4  CHOOSE ONE OF THE FOLLOWING TWO PROBLEMS. The first one is easier than the second.
#4  (Easier) USING ONLY THE ZIP CODE DATA... Make a scatterplot of all the zip codes in Illinois according to their Lat/Long.  Make the marker size vary depending on the population contained in that zip code.  Add an alpha value to the marker so that you can see overlapping markers.

def split_line(line):
    return re.findall('[A-Za-z0-9]+(?:\'[A-Za-a0-9]+)?', line)
zip_data = []
file = open("free-zipcode-database-Primary.csv", "r")

lat = []
long = []
zipcode = []







#4 (Harder) USING BOTH THE ZIP CODE DATA AND THE POWER DATA... Make a scatterplot of all zip codes in Illinois according to their Lat/Long.  Make the marker red for the top 25% in residential power rate.  Make the marker yellow for the middle 25 to 50 percentile. Make the marker green if customers pay a rate in the bottom 50% of residential power cost.  This one is very challenging.  You are using data from two different datasets and merging them into one.  There are many ways to solve. (20pts)

