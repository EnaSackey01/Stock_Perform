import csv
import statistics 

ADBE_Data = []
with open ("ADBE.csv", "r") as infile:
    reader = csv.DictReader(infile)
    #save the dictionary onject into a list of dictionaries to analyze 
    for row in reader:
        ADBE_Data.append(row)

print(ADBE_Data)

l = 0
ADBE_std_Data = []
while l < len(ADBE_Data):
    try:
        day1 = float(ADBE_Data[l]["Closing_Price"])
        day2 = float(ADBE_Data[l + 1]["Closing_Price"])
        day3 = float(ADBE_Data[l + 2]["Closing_Price"])
        day4 = float(ADBE_Data[l + 3]["Closing_Price"])
        day5 = float(ADBE_Data[l + 4]["Closing_Price"])

        pop_stdev = statistics.pstdev([day1, day2, day3, day4, day5])
        ADBE_std_Data.append(pop_stdev)
        l += 5
    except:
        break

print(ADBE_std_Data)

GOOGL_Data = []
with open ("GOOGL.csv", "r") as infile:
    reader = csv.DictReader(infile)
    #save the dictionary onject into a list of dictionaries to analyze 
    for row in reader:
        GOOGL_Data.append(row)

print(GOOGL_Data)

r = 0
GOOGL_std_Data = []
while r < len(GOOGL_Data):
    try:
        day1 = float(GOOGL_Data[r]["Closing_Price"])
        day2 = float(GOOGL_Data[r + 1]["Closing_Price"])
        day3 = float(GOOGL_Data[r + 2]["Closing_Price"])
        day4 = float(GOOGL_Data[r + 3]["Closing_Price"])
        day5 = float(GOOGL_Data[r + 4]["Closing_Price"])

        pop_stdev2 = statistics.pstdev([day1, day2, day3, day4, day5])
        GOOGL_std_Data.append(pop_stdev2)
        r += 5
    except:
        break

print(GOOGL_std_Data)


AMZN_Data = []
with open ("AMZN.csv", "r") as infile:
    reader = csv.DictReader(infile)
    #save the dictionary onject into a list of dictionaries to analyze 
    for row in reader:
        AMZN_Data.append(row)

print(AMZN_Data)

s = 0
AMZN_std_Data = []
while s < len(AMZN_Data):
    try:
        day1 = float(AMZN_Data[s]["Closing_Price"])
        day2 = float(AMZN_Data[s + 1]["Closing_Price"])
        day3 = float(AMZN_Data[s + 2]["Closing_Price"])
        day4 = float(AMZN_Data[s + 3]["Closing_Price"])
        day5 = float(AMZN_Data[s + 4]["Closing_Price"])

        pop_stdev3 = statistics.pstdev([day1, day2, day3, day4, day5])
        AMZN_std_Data.append(pop_stdev3)
        s += 5
    except:
        break
print(AMZN_std_Data)


CRM_Data = []
with open ("CRM.csv", "r") as infile:
    reader = csv.DictReader(infile)
    #save the dictionary onject into a list of dictionaries to analyze 
    for row in reader:
        CRM_Data.append(row)

print(CRM_Data)

p = 0
CRM_std_Data = []
while p < len(CRM_Data):
    try:
        day1 = float(CRM_Data[p]["Closing_Price"])
        day2 = float(CRM_Data[p + 1]["Closing_Price"])
        day3 = float(CRM_Data[p + 2]["Closing_Price"])
        day4 = float(CRM_Data[p + 3]["Closing_Price"])
        day5 = float(CRM_Data[p + 4]["Closing_Price"])

        pop_stdev4 = statistics.pstdev([day1, day2, day3, day4, day5])
        CRM_std_Data.append(pop_stdev4)
        p += 5
    except:
        break

print(CRM_std_Data)


COUR_Data = []
with open ("COUR.csv", "r") as infile:
    reader = csv.DictReader(infile)
    #save the dictionary onject into a list of dictionaries to analyze 
    for row in reader:
        COUR_Data.append(row)

print(COUR_Data)

v = 0
COUR_std_Data = []
while v < len(COUR_Data):
    try:
        day1 = float(COUR_Data[v]["Closing_Price"])
        day2 = float(COUR_Data[v + 1]["Closing_Price"])
        day3 = float(COUR_Data[v + 2]["Closing_Price"])
        day4 = float(COUR_Data[v + 3]["Closing_Price"])
        day5 = float(COUR_Data[v + 4]["Closing_Price"])

        pop_stdev = statistics.pstdev([day1, day2, day3, day4, day5])
        COUR_std_Data.append(pop_stdev)
        v += 5
    except:
        break

print(COUR_std_Data)
