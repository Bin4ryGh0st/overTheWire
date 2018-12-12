import os
#print(os.getcwd())

def getDirElements():
	os.system('ls > .pipe')
	pipe = open('.pipe','r')
	pipeData=[]
	tempPipeData = pipe.readline().strip()
	while tempPipeData:
		pipeData.append(tempPipeData)
		tempPipeData = pipe.readline().strip()
	pipe.close()
	print(pipeData)
	return pipeData

data = open('data.txt','r')
os.system('xxd -r data.txt > inhere')
data.close()

inhere='inhere'
previous=''
decompress = 1
while decompress:
	os.system('file '+inhere+' > .pipe')
	pipe = open('.pipe','r')
	pipeData = pipe.readline().strip()
	pipe.close()
	if 'gzip compressed data' in pipeData:
		print('gz')
		os.system('mv '+inhere+' '+inhere+'.gz')
		dirElements = getDirElements()
		os.system('gunzip '+inhere+'.gz')
		inhere = list(set(getDirElements()).difference(dirElements))[0]
	elif 'bzip2 compressed data' in pipeData:
		print('bz2')
		os.system('mv '+inhere+' '+inhere+'.bz2')
		dirElements = getDirElements()
		os.system('bunzip2 '+inhere+'.bz2')
		inhere = list(set(getDirElements()).difference(dirElements))[0]
	elif 'POSIX tar archive' in pipeData:
		print('tar')
		os.system('mv '+inhere+' '+inhere+'.tar') 
		dirElements = getDirElements()
		os.system('tar -xf '+inhere+'.tar')
		previous = inhere
		inhere = list(set(getDirElements()).difference(dirElements))[0]
		if inhere==set():
			inhere=previous
		else:
			os.system('rm '+previous+'.tar')
	else:
		print(pipeData)
		decompress = 0
		if 'ASCII text' in pipeData:
			os.system('mv '+inhere+' ./.flag.txt')
flag = open('.flag.txt','r')
print("\n"+flag.readline().strip())
flag.close()
os.remove('.pipe')
os.remove('.flag.txt')
