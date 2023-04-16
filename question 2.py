'''Question - We would like you to learn the basics of python and data science to load a dataset, read it and perform some operations to find multiple mathematical metrics such as average, maximum, minimum and such. 
Here is a dataset for autos. 
https://drive.google.com/file/d/1QP21K5tiJAjt5NA7W2FxSe9Wam9-tIcQ/view?usp=sharing 
Flow: '''
#1.	Download this dataset. 
#2.	Write basic python script to load csv and read it as data frame 
import chardet
with open ('autos.csv','rb') as rawdata:
  result = chardet.detect(rawdata.read(100000))
result

pd.read_csv('autos.csv',encoding='Windows-1252')
autos_df=pd.read_csv('autos.csv',encoding='Windows-1252')
type(autos_df)

#3.Use the data frame to perform following: 
#a.Find Average price of autos ( using price column of dataset) 
mean1=autos_df['price'].mean()
mean1

#b. Print the list of different possible types of VehicleType found in dataset 
unique1=autos_df['vehicleType'].unique()
unique1

#c. Calculate and print lowest yearOfRegistration and highest yearOfRegistration
#minimum 
min1=autos_df['yearOfRegistration'].min()
min1
#maximun
max1=autos_df['yearOfRegistration'].max()
max1

# d. Find and print standard deviation of column kilometer
std1=autos_df['kilometer'].std()
std1

#e. Draw a bar graph to represent count of different type of column brand
brand_counts = autos['brand'].value_counts()
plt.bar(brand_counts.index, brand_counts.values)
plt.xlabel('Brand')
plt.ylabel('Count')
plt.title('Count of Different Brands')
plt.show()

#f. Find out which VehicleType is sold minimum and maximum
vehicle_type_counts = autos['vehicleType'].value_counts()
min_vehicle_type = vehicle_type_counts.idxmin()
max_vehicle_type = vehicle_type_counts.idxmax()
print(f"VehicleType sold minimum: {min_vehicle_type}")
print(f"VehicleType sold maximum: {max_vehicle_type}")

#g. Create a pie chart to represent different types of gearbox count
gearbox_counts = autos['gearbox'].value_counts()
plt.pie(gearbox_counts.values, labels=gearbox_counts.index, autopct='%1.1f%%')
plt.title('Gearbox Count')
plt.show()



