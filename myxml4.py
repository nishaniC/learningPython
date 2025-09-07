import xml.etree.ElementTree as ET

tree = ET.parse('books.xml')
root = tree.getroot()
for child in root:
    # To change the tag of the Element object, we must assign a new value to its tag property
    child.tag = 'movie'
    # The remove method removes the child element passed as its argument, which must be an Element object.
    child.remove(child.find('author'))
    child.remove(child.find('year'))
    # The Element object has a method called set, which allows you to set any attribute
    child.set('rate', '5')
    print(child.tag, child.attrib)
    for sub_child in child:
        print(sub_child.tag, ':', sub_child.text)

#  To save all the changes we’ve made to the tree, we have to use the method called write.
# The write method has only one required argument, which is a file name of the output XML file, or a file object opened for writing.
# In addition, we can define character encoding by using the second argument (the default is US-ASCII).
# To add a prolog(e.g. <?xml version='1.0' encoding='UTF-8'?>) to our document, we must pass True in the third argument.
tree.write('movies.xml', 'UTF-8', True)