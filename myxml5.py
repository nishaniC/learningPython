import xml.etree.ElementTree as ET

# The Element class constructor takes two arguments.
# The first is the name of the tag to be created, while the second (optional) is the attribute dictionary.
root = ET.Element('data')
# The SubElement function takes three arguments.
#
# The first one defines the parent element, the second one defines the tag name,
# and the third (optional) defines the attributes of the element.
# The created elements are objects of the Element class, so we can use all the methods that we learned about during this course.
movie_1 = ET.SubElement(root, 'movie', {'title': 'The Little Prince', 'rate': '5'})
movie_2 = ET.SubElement(root, 'movie', {'title': 'Hamlet', 'rate': '5'})

# dump method allows us to debug either the whole tree or a single element.
ET.dump(root)

# NOTE: To save a document using the write method, we need to have an ElementTree object.
# To do this, pass our root element to its constructor:
tree = ET.ElementTree(root)
tree.write('movies2.xml', 'UTF-8', True)