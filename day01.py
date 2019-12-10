with open('day1.in') as input_file:
	masses = [int(line) for line in input_file]

def fuel(mass):
	return mass // 3 - 2

def all_fuels(mass):
	while (mass := fuel(mass)) > 0:
		yield mass

fuel_simple = sum(fuel(mass) for mass in masses)
fuel_recursive = sum(sum(all_fuels(mass)) for mass in masses)

print('Part 1:', fuel_simple)
print('Part 2:', fuel_recursive)
