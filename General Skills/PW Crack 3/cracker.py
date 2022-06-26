from os import system as s
pos_pw_list = ["f09e", "4dcf", "87ab", "dba8", "752e", "3961", "f159"]
for i in range(len(pos_pw_list)):
	s(f'echo {pos_pw_list[i]} | python3 level3.py')
