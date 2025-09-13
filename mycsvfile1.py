# The Python Standard Library offers a module called csv that provides functions for reading and writing data in CSV format.
import csv
# Reading data is done using the reader object, while writing is done using the writer object.

# open is a built-in function
#  with statement
# - This is a context manager that ensures the file is properly opened and closed.
# - Even if an error occurs while reading the file, Python will automatically close it when the block ends—no need to call csvfile.close() manually.
# 🔹 open('contacts.csv', newline='')
# - open() is the built-in function to access a file.
# - 'contacts.csv' is the filename you're trying to read.
# - newline='' - disables automatic newline translation.
# • 	Ensures that the  module can correctly parse rows without inserting extra blank lines (which is a common issue on Windows).
# • 	Prevents Python from converting \n to \r\n or vice versa, which can mess up CSV formatting.
# 🔹 as csvfile - This assigns the opened file object to the variable csvfile, which you can then use to read or process the file.
# Using with open(...) is cleaner and safer than manually opening and closing files. It’s especially useful in QA automation or data processing scripts where reliability matters.
with open('contacts.csv', newline='') as csvfile:

    # The reader function returns an object that allows you to iterate over each line in the CSV file.
    # To create it, we need to pass a file object to the reader function and a separator used to separate the data in the file
    # this can be omitted if our file uses the default separator, which is a comma
    # Note that a single line is returned as a list of strings. However, more readable results can be obtained, e.g., by using the join method.
    # reader = csv.reader(csvfile, delimiter=',')
    # for row in reader:
    #     # print(row)
    #     print(','.join(row))

    # csv.DictReader maps each line to an OrderedDict object, To achieve this, we must use the DictReader class
    # NOTE: If you define more column names than the values in the file, the missing values will be None.
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['Name'], ':', row['Phone'])

# NOTE: If you define more column names than the values in the file, the missing values will be None.
# import csv
#
# with open('example.csv', newline='') as f:
#     reader = csv.DictReader(f, fieldnames=['Name', 'Age', 'City'])
#     for row in reader:
#         print(row)
# If example.csv contains:
# Alice,30
# Bob,25,New York
# Charlie
# You’ll get:

# OrderedDict([('Name', 'Alice'), ('Age', '30'), ('City', None)])
# OrderedDict([('Name', 'Bob'), ('Age', '25'), ('City', 'New York')])
# OrderedDict([('Name', 'Charlie'), ('Age', None), ('City', None)])