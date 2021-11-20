import csv
with open("C:/Users/Hp/Desktop/White HAt Junior/PYTHON/C104/SOCR-HeightWeight.csv")as f:
    reader=csv.reader(f)
    filedata=list(reader)
filedata.pop(0)
Newdata=[]
for i in range(len(filedata)):
    nnum=filedata[i][1]
    Newdata.append(float(nnum))
n=len(Newdata)
Newdata.sort()
#median 
if n %2==0:
    median1=float(Newdata[n//2])
    median2=float(Newdata[n//2-1])
    median=(median1+median2)/2
else:
    median=Newdata[n//2]
    print(n)
print("Median is "+ str(median))        
