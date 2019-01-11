# methods for a dictionary data structure

countries = {'Norge': {'size': 'large enough', 'people': 'happy', 'food': 'very tasty'},
             'Russland': {'size': 'large', 'people': '100+ mil', 'food': 'tasty'}}
fruit = {'form': 'round', 'color': 'red', 'name': 'cherry'}

print(countries.keys(), fruit.keys(), sep='\n' + '--' * 20 + '\n')
print('--' * 20)

print(countries.values(), fruit.values(), sep='\n' + '--' * 20 + '\n')
print('--' * 20)

print(countries.items(), fruit.items(), sep='\n' + '--' * 20 + '\n')
print('--' * 20)

removed_item = countries.pop('Russland')
print(removed_item)

countries.clear()
fruit.clear()
