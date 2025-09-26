import csv

with open('exported_contacts4.csv', 'w', newline='') as csvfile:
    # The last argument called quoting, specifies what values should be quoted.
    # The default value QUOTE_MINIMAL means that only values with special characters such as separator or quotechar will be quoted.
    writer = csv.writer(csvfile, delimiter=',',  quoting=csv.QUOTE_ALL)
    # writer = csv.writer(csvfile, delimiter=',', quotechar='"')

    writer.writerow(['Name', 'Phone'])
    writer.writerow(['mother', '222-555-101'])
    writer.writerow(['father', '222-555-102'])
    writer.writerow(['wife"', '222-555-103'])
    writer.writerow(['mother-in-law', '222-555-104'])

    writer.writerow(['grandmother, grandfather and auntie', '222-555-105'])
    # csv.QUOTE_ALL – quotes all values
    # csv.QUOTE_NONNUMERIC – quotes only non-numeric values
    # csv.QUOTE_NONE – doesn't quote any values. It's not a good idea to set this value if you have special characters that require quoting, because this will raise an error
    # NOTE: The quotechar and quoting parameters can also be used in the reader function. See the documentation for more information.