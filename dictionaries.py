# List - ordered (indexed) collection of items - mutable - can have duplicates

# Dictionary (dict) - collection of items - mutable - unordered - not indexed
# keyed - key/value pairs - keys cannot have duplicates

person1 = {
    "name": "Matt",
    "last_name": "Flynn",
    "age": 52
}

print(person1.get('foo', 'Key not found'))

person1['address'] = { 'state': 'QLD', 'postcode': 4000, 'city': 'Brisbane' }
print(person1['address']['postcode'])

print(person1)
person1.update({ 'name': 'Kate', 'age': 21, 'height': 170 })
print(person1)

# Loop
for key, val in person1.items():
    print(f'Key: {key}')
    print(f'Value: {val}')
