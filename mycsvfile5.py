import csv

with open('exported_contacts5.csv', 'w', newline='') as csvfile:
    fieldnames = ['Name', 'Phone']
    # Unlike the DictReader object, when creating the DictWriter object, we must define fieldnames parameter.
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # adds the header(comma seperated column names) as the first line of the file, calling writeheader() is not required
    writer.writeheader()
    writer.writerow({'Name': 'mother', 'Phone': '222-555-101'})
    writer.writerow({'Name': 'father', 'Phone': '222-555-102'})
    writer.writerow({'Name': 'wife', 'Phone': '222-555-103'})
    writer.writerow({'Name': 'mother-in-law', 'Phone': '222-555-104'})
    writer.writerow({'Name': 'grandmother, grandfather and auntie', 'Phone': '222-555-105'})