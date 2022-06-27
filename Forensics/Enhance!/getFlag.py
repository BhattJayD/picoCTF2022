file=open('drawing.flag.svg','r')
flag=''
for i in file:
	#print(i.index('<?xml'))
	if ('id="tspan' in i):
		flag+=i[24:].replace('</tspan><tspan','')
print(flag.replace('\n','').replace(' ','').replace('</tspan></text>',''))
