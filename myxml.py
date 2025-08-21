import xml.etree.ElementTree
# The xml.etree.ElementTree module may be also used to create, modify and write XML files.

# the parse() function reads the XML document, builds the tree, and returns it; we use the tree object to invoke its fundamental method named getroot()
# which returns what it promises – the root element of the tree;
cars_for_sale = xml.etree.ElementTree.parse('cars.xml').getroot()

# each tree element (i.e., each object containing the element) has a property named tag which stores the textual representation of the element's name –
# we use it to print the root element's name;
print(cars_for_sale.tag)

# now we start to traverse the tree using the findall() method of the root object; the method's arguments name the elements we are interested in;
for car in cars_for_sale.findall('car'):
    print('\t', car.tag)

    #  we initiate the iterations which should reveal all car's components
    for prop in car:
        print('\t\t', prop.tag, end='')
        if prop.tag == 'price':
            # we make use of the attrib property which is, in fact, a Python dictionary grouping all of tag's attributes (as attributes occur in pairs, a dictionary is the best tool to store them)
            print(prop.attrib, end='')
        # we print tag's content – it is available as a value returned from the text property.
        print(' =', prop.text)


# here we are  using xml.etree.ElementTree to remove one car from our offer (theFord Mustang) and add a new car to it

# parses the file and fetch an object storing all elements – we’ll name it tree
tree = xml.etree.ElementTree.parse('cars.xml')
# find the root of the tree and store it in cars_for_sale
cars_for_sale = tree.getroot()
for car in cars_for_sale.findall('car'):
    if car.find('brand').text == 'Ford' and car.find('model').text == 'Mustang':
        cars_for_sale.remove(car)
        break
#the Element() method requires one argument: a string containing the element's (tag's) name;
new_car = xml.etree.ElementTree.Element('car')
# we call the SubElement() method as many times as the number of sub-elements (the inner tags) we need; each invocation needs two arguments:
# a parent element object (new_car here) and a sub-element name (as a string); note: the function returns an object for the newly created element; in fact, we need it only once,
# for a very specific purpose: we use it to set the text associated with the tag – this is why we access the text property and set it with the desired value;
xml.etree.ElementTree.SubElement(new_car, 'id').text = '4'
xml.etree.ElementTree.SubElement(new_car, 'brand').text = 'Maserati'
xml.etree.ElementTree.SubElement(new_car, 'model').text = 'Mexico'
xml.etree.ElementTree.SubElement(new_car, 'production_year').text = '1970'
# The invocation contains one more argument: a dictionary; the function will use is to embed an attribute inside the sub-element
xml.etree.ElementTree.SubElement(new_car, 'price', {'currency': 'EUR'}).text = '61800'
cars_for_sale.append(new_car)
# method invoked from within the tree object creates a new file and fills it with the modified XML document.
# The method parameter should specify the output format. For standard XML, it should be 'xml'
tree.write('newcars.xml', method='xml')
