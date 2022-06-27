import re
file=open('anthem.flag.txt','r')
print(re.findall('picoCTF{.*}',file.read())[0])
file.close()
