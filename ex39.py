states = {
    'oregon': 'or',
    'florida': 'fl',
    'califirnia': 'ca',
    'new york': 'ny',
    'michigan': 'mi'
}

cities = {
    'ca': 'san francisco',
    'mi': 'detroit',
    'fl': 'jacksonville',
}

cities['ny'] = 'new york'

print('-' * 20)
print("ny state has:", cities['ny'])
print('-' * 20)
# items()函数返回可遍历的元组数组
test = states.items()
print(test)

for state, abbrev in states.items():
    print("{} is abbreviated {}".format(state, abbrev))

# get函数返回字典中指定键的值
# 如果值不在字典中，默认返回none，或者返回在get函数中给予的该键的值
state = states.get('Texas')
if not state:
    print("Sorry, no Texas.")

city = cities.get('TX', 'does not exist')
print("The city for the state 'TX' is {}".format(city))
