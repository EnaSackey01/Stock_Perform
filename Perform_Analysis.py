import csv
import statistics 
import matplotlib.pyplot as plt

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
        day1 = float(ADBE_Data[l]["Closing"])
        day2 = float(ADBE_Data[l + 1]["Closing"])
        day3 = float(ADBE_Data[l + 2]["Closing"])
        day4 = float(ADBE_Data[l + 3]["Closing"])
        day5 = float(ADBE_Data[l + 4]["Closing"])

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
        day1 = float(GOOGL_Data[r]["Closing"])
        day2 = float(GOOGL_Data[r + 1]["Closing"])
        day3 = float(GOOGL_Data[r + 2]["Closing"])
        day4 = float(GOOGL_Data[r + 3]["Closing"])
        day5 = float(GOOGL_Data[r + 4]["Closing"])

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
        day1 = float(AMZN_Data[s]["Closing"])
        day2 = float(AMZN_Data[s + 1]["Closing"])
        day3 = float(AMZN_Data[s + 2]["Closing"])
        day4 = float(AMZN_Data[s + 3]["Closing"])
        day5 = float(AMZN_Data[s + 4]["Closing"])

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
        day1 = float(CRM_Data[p]["Closing"])
        day2 = float(CRM_Data[p + 1]["Closing"])
        day3 = float(CRM_Data[p + 2]["Closing"])
        day4 = float(CRM_Data[p + 3]["Closing"])
        day5 = float(CRM_Data[p + 4]["Closing"])

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
        day1 = float(COUR_Data[v]["Closing"])
        day2 = float(COUR_Data[v + 1]["Closing"])
        day3 = float(COUR_Data[v + 2]["Closing"])
        day4 = float(COUR_Data[v + 3]["Closing"])
        day5 = float(COUR_Data[v + 4]["Closing"])

        pop_stdev = statistics.pstdev([day1, day2, day3, day4, day5])
        COUR_std_Data.append(pop_stdev)
        v += 5
    except:
        break

print(COUR_std_Data)

fig,S1 = plt.subplots()
S1.plot(COUR_std_Data)
S1.set_ylabel("Price's Standard Deviation")
S1.set_xlabel("Number Of Weeks")
S1.set_title("STANDARD DEVIATION OF COURSERA'S STOCK")
plt.savefig("Coursera's Std_Dev.png")

fig,S2 = plt.subplots()
S2.plot(CRM_std_Data)
S2.set_ylabel("Price's Standard Deviation")
S2.set_xlabel("Number Of Weeks")
S2.set_title("STANDARD DEVIATION OF SALESFORCE'S STOCK")
plt.savefig("Salesforce's Std_Dev.png")

fig,S3 = plt.subplots()
S3.plot(AMZN_std_Data)
S3.set_ylabel("Price's Standard Deviation")
S3.set_xlabel("Number Of Weeks")
S3.set_title("STANDARD DEVIATION OF AMAZONS' STOCK")
plt.savefig("Amazon's Std_Dev.png")

fig,S4 = plt.subplots()
S4.plot(ADBE_std_Data)
S4.set_ylabel("Price's Standard Deviation")
S4.set_xlabel("Number Of Weeks")
S4.set_title("STANDARD DEVIATION OF ADOBE'S STOCK")
plt.savefig("Adobe's Std_Dev.png")

fig,S5 = plt.subplots()
S5.plot(GOOGL_std_Data)
S5.set_ylabel("Price's Standard Deviation")
S5.set_xlabel("Number Of Weeks")
S5.set_title("STANDARD DEVIATION OF GOOGLE's STOCK")
plt.savefig("Google's Std_Dev.png")

#fig,(S1, S2, S3, S4, S5) = plt.subplots()
#fig,ax= plt.subplots()
#ax.plot(cvs_stdev)
#ax.set_ylabel(“STDEV of price”)
#ax.set_xlabel(“weeks since March29”)
#ax.set_title(“STANDARD DEVIATION OF STOCKS”)
#plt.savefig(f”data{file}.png”)

fig,(Ax1) = plt.subplots()
Ax1.plot(COUR_std_Data, label="Coursera")
Ax1.plot(CRM_std_Data, label="Salesforce")
Ax1.plot(AMZN_std_Data, label="Amazon")
Ax1.plot(ADBE_std_Data, label="Adobe")
Ax1.plot(GOOGL_std_Data, label="Google")
Ax1.set_ylabel("Price's Standard Deviation")
Ax1.set_xlabel("Number Of Weeks")
Ax1.set_title("STANDARD DEVIATION OF 5 STOCK")
plt.legend()
plt.savefig("5 Stock's Std_Dev.png")
