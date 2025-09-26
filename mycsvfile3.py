import csv
# saving data to a CSV file is done using the writer object provided by the csv module
# To create it, we need to use a function called writer, which takes the same set of arguments as the reader function(a file object and a separator used to separate the data in the file
#     # this can be omitted if we want our file to use the default separator, which is a comma)
with open('exported_contacts.csv', 'w', newline='') as csvfile:
    # we create a writer object
    writer = csv.writer(csvfile, delimiter=',')
    # The writerow method takes a list of values as an argument, and then saves them as one line in a CSV file.p
    writer.writerow(['Name', 'Phone'])
    writer.writerow(['mother', '222-555-101'])
    writer.writerow(['father', '222-555-102'])
    writer.writerow(['wife', '222-555-103'])
    writer.writerow(['mother-in-law', '222-555-104'])

