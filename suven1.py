from operator import itemgetter

myfile=open(r"C:\Users\abc\Documents\Estimated_Population_2015.csv")
mydict={}

for line in myfile.readlines():
	try:
		mydict[line.split(",")[0]]=int(line.rstrip("\n").split(",")[1])
	
	except ValueError:
		pass
		
myfile.close()
sorted_list=sorted(mydict.items(), key=itemgetter(1), reverse=True)

for i in sorted_list:
	print(i)