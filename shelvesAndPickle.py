import shelve

shelve_name = 'first_shelve.shlv'

my_shelve = shelve.open(shelve_name, flag='c')
my_shelve['EUR'] = {'code':'Euro', 'symbol': '€'}
my_shelve['GBP'] = {'code':'Pounds sterling', 'symbol': '£'}
my_shelve['USD'] = {'code':'US dollar', 'symbol': '$'}
my_shelve['JPY'] = {'code':'Japanese yen', 'symbol': '¥'}
my_shelve.close()
new_shelve1 = shelve.open(shelve_name)
usddata = new_shelve1['USD']
usddata['value'] = 123
new_shelve1['USD']=usddata
new_shelve1.close()
new_shelve2 = shelve.open(shelve_name)
new_shelve2['EUR2'] = {'code':'Euro2', 'symbol': '€2'}
new_shelve2.close()
new_shelve3 = shelve.open(shelve_name)
print("Contents of the shelve:")
for key in new_shelve3:
    print(f"{key}: {new_shelve3[key]}")  # Access and print each key-value pair

new_shelve3.update({'AUD': {'code': 'Australian dollar', 'symbol': 'A$'}})

print("Keys in shelve after the addition:", list(new_shelve3.keys()))

for key, value in new_shelve3.items():
    print(f"{key}: {value}")

del new_shelve3['JPY']

print("Keys in shelve after deelting JPY:", list(new_shelve3.keys()))

for key, value in new_shelve3.items():
    print(f"{key}: {value}")


import pickle

data_dict = dict(new_shelve3)  # Convert shelve contents to a dictionary
pickle_file_name = 'shelve_backup.pkl'
# Serialize (pickle) the dictionary
with open(pickle_file_name, 'wb') as backup_file:
    pickle.dump(data_dict, backup_file)
print("Shelve data has been pickled and saved as 'shelve_backup.pkl'")

# Unpickle the data
with open(pickle_file_name, 'rb') as backup_file:
    restored_data = pickle.load(backup_file)

# Create a new shelve and populate it with the restored data
new_shelve_name = 'restored_shelve.shlv'
with shelve.open(new_shelve_name, flag='c') as restored_shelve:
    restored_shelve.update(restored_data)  # Add all unpickled data to the shelve

    print(f"Data has been successfully unpickled and saved to a new shelve: {new_shelve_name}")
    for key, value in restored_shelve.items():
        print(f"{key}: {value}")
