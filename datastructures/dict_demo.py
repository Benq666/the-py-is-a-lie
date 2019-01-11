# store key:value pairs
# {}
# not sequenced and no indexing

fruit = {'form': 'round', 'color': 'red', 'name': 'cherry'}
print(fruit)
print(fruit['form'])

fruit_color = fruit['color']
print(fruit_color)

fruit['price'] = 12
print(fruit)

price_increase = fruit['price'] + 8
print(price_increase)

fruit['price'] += 8
print(fruit['price'])
