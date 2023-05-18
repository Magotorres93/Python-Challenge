import csv
import os
url= 'budget_data.csv'
csvpath = os.path.join("c:/Users/magot/OneDrive/Desktop/Repositorio1", "budget_data.csv")
print(csvpath)
with open(csvpath,'r')as budgetdata:
    #lines= budgetdata.read()
    #print(lines)
    csvreader=csv.reader(budgetdata,delimiter=',')
    next(csvreader,None)
    

    
    #The total number of months included in the dataset
    i=0
    for row in csvreader:
        i=i+1
    print("total number of months: ",i)
     
   # The net total amount of "Profit/Losses" over the entire period

amount=[]
with open(csvpath,'r')as budgetdata:
    csvreader1=csv.reader(budgetdata,delimiter=',')
    next(csvreader1,None)

    
    for row in csvreader1:
        amount.append(int(row[1]))
                      
        
    print("total amount: ",sum(amount))

#The changes in "Profit/Losses" over the entire period, and then the average of those changes

x=0
Change=[]    
j=i-1
for x in range (j):
    Change.append(amount[x+1]-amount[x])

print("Average Change: ",sum(Change)/j)

#The greatest increase in profits (date and amount) over the entire period
month=[]


with open(csvpath,'r')as budgetdata:
    csvreader2=csv.reader(budgetdata,delimiter=',')
    next(csvreader2,None)

    for row in csvreader2:
        month.append(row[0])



decrease=0
Indexm=0



m=0
for ind,m in enumerate(Change):
  if m<0:
      if decrease>m:
          decrease=m
          Indexm=ind
         
      
print("Greates decrease in profits: ",month[Indexm+1],decrease)
         
                      

Increase=0
Indexm=0



m=0
for ind,m in enumerate(Change):
  if m>0:
      if Increase<m:
          Increase=m
          Indexm=ind
         
      
print("Greates Increase in profits: ",month[Indexm+1],Increase)
    
text=f"""
Financial Analysis
----------------------------
total number of months:{i}
total amount: {sum(amount)}   
Average Change: {sum(Change)/j:.2f}
Greates decrease in profits: {month[Indexm+1]}, {decrease}
""" 
print(text)    
   
text_path=os.path.join("c:/Users/magot/OneDrive/Desktop/Repositorio1", "Financial Analisis.txt")

with open(text_path, "w") as file:
    file.write(text)  


