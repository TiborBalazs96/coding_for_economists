#1.Find headers/idxs for relevant vars:
f = open('data/raw/european_commission/ted-sample.csv')

#Grab headers
headers = f.readline().strip().split(',')

#Make sure to cloye the file
f.close()

for index,value in enumerate(headers):
  print(index,value)

#2.Initiate an empty list called data
data=[]
#3.Use the context manager open() and
#3.1.Iterate through each row in ted-sample.csv and
#3.2.Append each row to the data list using (in the loop body)
with open('data/raw/european_commission/ted-sample.csv') as f:
  for line in f:
    data.append(line.strip().split(','))

print(data[0])
#Output should look like: data = [[row0],[row1],[row2]]
data=data[1:]
#or data.pop(0)

#4.Count the number of wins by country
#Output should look like: d = {'Canada':1,'France':2,'Germany':3}

d = {}
for row in data:
  country = row[61]
  countries=country.split('---')
  for winning_country in countries:
    if country in d:  
      d[winning_country] = 0
      d[winning_country] += 1  

print(d)