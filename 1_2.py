with open('1.in', 'r') as input_file:
	masses = [int(line) for line in input_file]

def fuel(mass):
	return mass // 3 - 2

def all_fuels(mass):
	while (mass := fuel(mass)) > 0:
		yield mass

total_fuel = sum(sum(all_fuels(mass)) for mass in masses)

print('Total fuel is', total_fuel)
