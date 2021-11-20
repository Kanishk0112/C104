import csv
with open("C:/Users/Hp/Desktop/White HAt Junior/PYTHON/C104/SOCR-HeightWeight.csv")as f:
    reader=csv.reader(f)
    filedata=list(reader)
filedata.pop(0)
Newdata=[]
for i in range(len(filedata)):
    nnum=filedata[i][1]
    Newdata.append(float(nnum))
#getting the mean
n=len(Newdata)
total=0
for x in Newdata:
    total=total+x
mean=total/n
print("mean is"+ str(mean))        