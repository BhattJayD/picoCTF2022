
atoz=[chr(i) for i in range(65,65+26)]
for i in range(0,10):
	atoz.append(i)
atoz.append('_')
print(len(atoz))

encodedmsg=[]
with open('message.txt','r') as f:
	lst=f.readline().split(' ')
	lst.remove('')
	encodedmsg=[int(lst[i])%37 for i in range(len(lst))]
	f.close()
op=[atoz[encodedmsg[i]] for i in range(len(encodedmsg))]
res="".join([str(i) for i in op])
print("picoCTF{"+res+"}")
