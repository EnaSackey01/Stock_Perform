import matplotlib.pyplot as plt

fig,(S1, S2, S3, S4, S5) = plt.subplots()

S1.plot(COUR_std_Data)
plt.show(COUR_std_Data)
plt.savefig(COUR_std_Data)

S2.plot(CRM_std_Data)
plt.show(CRM_std_Data)
plt.savefig(CRMStockData)

S3.plot(AMZN_std_Data)
plt.show(AMZN_std_Data)
plt.savefig(AMZN_std_Data)

S4.plot(ADBE_std_Data)
plt.show(ADBE_std_Data)
plt.savefig(ADBE_std_Data)

S5.plot(GOOGL_std_Data)
plt.show(GOOGL_std_Data)
plt.savefig(GOOGL_std_Data)


#fig,ax= plt.subplots()
#ax.plot(cvs_stdev)
#ax.set_ylabel(“STDEV of price”)
#ax.set_xlabel(“weeks since March29”)
#ax.set_title(“STANDARD DEVIATION OF STOCKS”)
#plt.savefig(f”data{file}.png”)