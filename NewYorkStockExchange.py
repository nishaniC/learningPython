import xml.etree.ElementTree

try:
    stocks =  xml.etree.ElementTree.parse('nyse.xml').getroot()
except xml.etree.ElementTree.ParseError:
    print('XML parse error')
    exit(1)
except FileNotFoundError:
    print('File not found')
    exit(1)

headers=["COMPANY", "LAST", "CHANGE", "MIN","MAX"]
# for header in headers:
#     print(header, end='\t\t\t')
# print('')

key_widths = [40,15, 15, 15, 15]
key_width = [ 15, 10, 20, 15]

def show_head():
    for (n, w) in zip(headers, key_widths):
        print(n.ljust(w), end='')
    print('')
    print("--------------------------------------------------------------------------------------------")

def show_quote(quot):
    for w in quot.attrib.values():
        print(str(w).ljust(15), end='')
    print()

show_head()
for quote in stocks.findall('quote'):
    print(quote.text.ljust(key_widths[0]), end='')
    show_quote(quote)