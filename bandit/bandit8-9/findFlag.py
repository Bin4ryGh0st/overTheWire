data = open('data.txt','r')
count = dict()
tempData=data.readline().strip()

while tempData:
	try:
		count[tempData]+=1
	except KeyError:
		count[tempData]=1
	tempData=data.readline().strip()
	
for flag in count:
	if count[flag]==1:
		print(flag)
		break
		
data.close()
