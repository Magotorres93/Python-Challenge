import csv
import os
url= 'election_data.csv'
csvpath = os.path.join("c:/Users/magot/OneDrive/Desktop/Repositorio1", "election_data.csv")
print(csvpath)
with open(csvpath,'r')as electiondata:

    csvreader=csv.reader(electiondata,delimiter=',')
    next(csvreader,None)

 #The total number of votes cast
    i=0
    Candidate=[] 
    for row in csvreader:
        i=i+1
        Candidate.append(row[2])
    print("total number of votes cast: ",i)


#A complete list of candidates who received votes
#The percentage of votes each candidate won
#The total number of votes each candidate won

c1=0
c2=0
c3=0
m1='Charles Casper Stockham'
m2='Diana DeGette'
m3='Raymon Anthony Doane'

for w in range (i):
  if m1==Candidate[w]:
     c1=c1+1 
    
  elif m2==Candidate[w]:
     c2=c2+1
  else :
     c3=c3+1

print(m1,": ",round(c1/i*100,3),"%  (",c1,")")
print(m2,": ",round(c2/i*100,3),"%  (",c2,")")
print(m3,": ",round(c3/i*100,3),"%  (",c3,")")

#The winner of the election based on popular vote

if c1 > c2 and c1>c3:
   print("Winner: ",m1)
elif c2>c1 and c2>c3:
   print("Winner: ",m2)    
else: 
   print("Winner: ",m3)  

     
text=f"""
Election Results
-------------------------
total number of votes cast:{i}
-------------------------
'Charles Casper Stockham' {round(c1/i*100,3)}%  ({c1})
'Diana DeGette' {round(c2/i*100,3)}%  ({c2})
'Raymon Anthony Doane'{round(c3/i*100,3)}%  ({c3})

"""
print(text)    
   
text_path=os.path.join("c:/Users/magot/OneDrive/Desktop/Repositorio1", "Candidate_votes.txt")

with open(text_path, "w") as file:
    file.write(text)  




  


        
