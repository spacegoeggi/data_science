def single(list):
	for x in range(len(list)):
		check = False
		for y in range(x+1,len(list)): 
			if list[x] == list[y]:
				check = True
		if check == False:
			return list[x]

def test_answer():
	assert 