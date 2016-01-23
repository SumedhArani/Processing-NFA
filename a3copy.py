from a2 import process, read

def subsetDFA(table, alphabets, final_state):
	n_states=['0'] #starting state considered by default
	n_table={} #new table i.e dfa representing the nfa

	#create a new table storing the new dfa
	for x in alphabets: # language is the same as in nfa
		if x not in n_table:
			n_table[x]=[] #initialise the new table

	for curr_state in n_states:
		arr_nstr=[]
		for y in alphabets:
			n_str=''
			p_state = curr_state.split(',')
			for state in p_state:
				if '-' not in state and table[y][int(state)]!='-' and table[y][int(state)] not in n_str:
					n_str = n_str +','+table[y][int(state)]
					if len(table[y][int(state)])>1 and 'lambda' in table:
						temp_arr = table[y][int(state)].split(',')
						for temp in temp_arr:
							if temp!='' and temp!='-':
								t_attr=table['lambda'][int(temp)]
								'''
								if t_attr!='' and t_attr!='-':
									print(temp_arr)
									temp_arr.append(table['lambda'][int(t_attr)])
									print('change: ',temp_arr)
								'''
								while(t_attr!='' and t_attr!='-'):									
									n_str = n_str +','+t_attr
									t_attr = table['lambda'][int(t_attr)]

			n_str = n_str.strip()
			if n_str!='' and ','==n_str[0]:
				n_str = n_str[1:]	

			if n_str != '':# and y!='lambda':
				n_table[y].append(n_str)
				arr_nstr.append(n_str)

			if y=='lambda':
				n_table[y].append(n_str)

		for s in arr_nstr:
			if s not in n_states:
				n_states.append(s)

	xb=True
	for x in table:
		if x!='lambda':
			x1 = table[x][0]
			if x1=='-':
				xb=xb and True
	if(xb):
		n_states.pop(0)

	for y in alphabets:
		for z in range(len(n_table[y])):
			if y!='lambda':
				n_table[y][z]=n_states.index(n_table[y][z])

	n_fstates=[]
	for f in final_state:
		if f != '' :
			for n in range(len(n_states)):
				if f in n_states[n]:
					n_fstates.append(n)

	return n_table, alphabets, n_fstates	


if __name__ == '__main__':
	#file_name = input("Enter input file name: ")
	file_name='inputA3.txt'
	table, alphabets, final_state = read(file_name)
	n_table, alphabets, n_fstates= subsetDFA(table, alphabets, final_state)
	while(True):
		test_str = input('Enter test string: ')
		print(process(test_str,n_table, alphabets, n_fstates))



