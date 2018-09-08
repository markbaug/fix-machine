def fix_machine(debris,product):
	integer=0
	while True:
		test=debris.find(product[integer])
		if test==-1:
			return "Not possible"
		else:
			integer=integer+1
			if integer>len(product)-1:
				return product