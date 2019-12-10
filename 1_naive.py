total = 0
with open('1.in', 'r') as file:
	for line in file:
		module = int(line)
		mass = module // 3 - 2
		while mass > 0:
			total += mass
			mass = mass // 3 - 2
print(total)