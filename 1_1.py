with open('1.in', 'r') as input_file:
	masses = [int(line) for line in input_file]

def fuel(mass):
	return mass // 3 - 2

total_fuel = sum(fuel(mass) for mass in masses)

print('Total fuel is', total_fuel)
