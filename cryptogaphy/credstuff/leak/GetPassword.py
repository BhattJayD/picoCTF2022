import codecs
username=open('usernames.txt','r',encoding='utf-8')
password=open('passwords.txt','r',encoding='utf-8')
atoz="".join([chr(i) for i in range(97,97+26)])
user=[]
for i in username:
	user.append(str(i))
passwd=[]
for i in password:
        passwd.append(i)
res=passwd[user.index('cultiris\n')] # got password of cultiris
#print(res)

#performing rot 13

for i in res:
	if(i!='{' and i!='}'):
		print(codecs.encode(i,'rot_13'),end='')
	else:
		print(i,end='')
username.close()
password.close()
