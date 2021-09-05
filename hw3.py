import time
from math import pi
import csv
import tempfile
import pandas as pd

#In class participation work - Sangwha Lee
#create list 
List = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(List)
#reverse the list
List.reverse()
print(List)
#print except 3 and 7
print(List[:3] + List[4:7] + List[8:])
#convert list to set
listToset = set(List)
print(listToset)
#remove 8 from set
listToset.remove(8)
print(listToset)
#print set in ascending order
print(sorted(listToset))

#HW3 - 1
start_time = time.time()
for i in range(1, 101):
  if i%3==0 and i%5==0:
    print(i, " FizzBuzz", end ="\n")   
  elif i%3==0:
    print(i," Fizz", end ="\n") 
  elif i%5==0:
    print(i," Buzz", end ="\n")
  else:
    print(i, end ="\n")
end_time = time.time()
print(end_time - start_time, " seconds")

#HW3 - 2 
r = int(input("Enter the value of the radius: "))
print("The volume of the sphere of radius ", str(r), " is: ",str(4/3*pi *r**3))

#csv file data
data = {
  'Title': ['1984', 'Animal Farm', 'Brave New World', 'Fahrenheit 451', 'Jane Eyre'],
  'Author': ['George Orwell', 'George Orwell', 'Aldous Huxley', 'Ray Bradbury', 'Charlotte Bronte'], 
  'ISBN13': ['978-0451524935', '978-0451526342', '978-0060929879', '978-0345342966', '978-0142437209'], 
  'Pages': [268, 144, 288, 208, 532]
}

header = data.keys()

#HW3 - 3
#create csv file and open as write mode
with open('hw3.csv', 'w') as csvfile:
  #create writer obj
  writer = csv.writer(csvfile)
  #insert column names 
  writer.writerow(header)

  #insert values according to columns
  for row in range(len(data[list(header)[0]])):
    writer.writerow([data[key][row] for key in header])
  
  #return name of csv file
  print(csvfile.name)

#HW3 - 4
#open csv file as read mode
with open('hw3.csv', 'r') as csvfile:
  #create reader obj
  reader = csv.DictReader(csvfile)
  #create dictionary structure
  dict = {column : [] for column in reader.fieldnames}

  #go into each rows then look every element in that row
  for row in reader:
    for column in reader.fieldnames:
      #insert each element into specific columns
      dict[column].append(row[column])

  #print values in dictionary
  for key, value in dict.items():
    print(key, ': ', value)

#HW3 - 5
#create tempfile
with tempfile.NamedTemporaryFile(mode = 'r+') as temp:
  #create dataframe, convert it into csv using temp
  tempdf = pd.DataFrame(data, columns=header)
  tempdf.to_csv(temp.name, index=False)

  #create reader obj based on temp
  reader = csv.DictReader(temp)
  #create dictionary, insert values
  dict = {column : [] for column in reader.fieldnames}
  for row in reader:
    for column in reader.fieldnames:
      dict[column].append(row[column])
  #print values
  for key, value in dict.items():
    print(key, ': ', value)
#temp is closed


#resources
#https://stackoverflow.com/questions/1557571/how-do-i-get-time-of-a-python-programs-execution
#https://stackoverflow.com/questions/45198869/create-dictionary-from-csv-with-headers
#https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html
#https://docs.python.org/3/tutorial/datastructures.html