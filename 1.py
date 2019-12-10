with open('1.in', 'r') as input_file:
	masses = [int(l.rstrip()) for l in input_file]

def fuel(mass):
	f = mass // 3 - 2
	return f if f > 0 else 0

total_fuel = sum(fuel(mass) for mass in masses)

print('Total fuel is', total_fuel)