def read(f_name):
	table={}
	fin = open(f_name) #input file name is the first arg in the command line
	var=fin.read().split('\n')
	var =filter(lambda x:x!='',var)
	var =list(map(lambda y :y.split('\t'), var))
	fin.close()

	final_state = var[-1]
	alphabets = var[0]

	for val in alphabets:
		table[val]=[]

	for n in range(len(alphabets)):
		temp=map(lambda x:x[n], var[1:-1])	
		for m in temp:
			table[alphabets[n]].append(m)

	return (table, alphabets, final_state)


def process(input_str,table,alphabets,final_state):
	curr_state=0
	for alpha in input_str:
		if alpha in alphabets:
			curr_state=table[alpha][int(curr_state)]
		else:
			return False  
	if curr_state in final_state:
		return True
	else:
		return False

if __name__=='__main__':
	file_name= input('Enter file name: ')
	table, alphabets, final_state = read(file_name)
	while(True):
		x = input("Enter string ")
		print(process(x,table,alphabets,final_state))