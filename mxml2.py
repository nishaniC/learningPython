import xml.etree.ElementTree as ET
xml_data="""<?xml version="1.0"?>
<data>
    <book title="The Little Prince">
        <author>Antoine de Saint-Exupéry</author>
        <year>1943</year>
    </book>
    <book title="Hamlet">
        <author>William Shakespeare</author>
        <year>1603</year>
    </book>
</data>"""
# To create a tree (an ElementTree object) from an existing XML document, pass it to the parse method
tree = ET.parse('books.xml')


# The getroot method returns the root element
root = tree.getroot()
print("root",root)
# tag – this returns the tag name as a string
# attrib – this returns all attributes in the tag as a dictionary. To retrieve the value of a single attribute, use its key, e.g., child.attrib ['title'].
print('The root tag is:', root.tag)
print('The root has the following children:')
for child in root:
    print(child.tag, child.attrib)
# root <Element 'data' at 0x0000015071E7F150>
# The root tag is: data
# The root has the following children:
# book {'title': 'The Little Prince'}
# book {'title': 'Hamlet'}

#  With access to the root element, we can reach any elements in the document.
#  Each of these elements is represented by a class called Element.

# we can use the method called fromstring, which, as an argument, takes XML as a string
# The fromstring method doesn't return the ElementTree object, but instead returns the root element represented by the Element class
root2 = ET.fromstring(xml_data)
print("root2",root2)
print('The root2 tag is:', root2.tag)
print('The root2 has the following children:')
for child in root2:
    print(child.tag, child.attrib)
# root2 <Element 'data' at 0x0000015071E7F100>
# The root2 tag is: data
# The root2 has the following children:
# book {'title': 'The Little Prince'}
# book {'title': 'Hamlet'}

# In addition to iterating over tree elements, we can access them directly using indexes
# Displaying text is possible thanks to the text property, available in the Element object.
print("My books:\n")
for book in root:
    print('Title: ', book.attrib['title'])
    print('Author:', book[0].text)
    print('Year: ', book[1].text, '\n')
# My books:
#
# Title:  The Little Prince
# Author: Antoine de Saint-Exupéry
# Year:  1943
#
# Title:  Hamlet
# Author: William Shakespeare
# Year:  1603

# Indexes are also used in deeper nesting, e.g., root [0] [0] .text returns the first book element, and then displays the text placed in its first child.

# The iter method returns all elements by having the tag passed as an argument.
# The element that calls it is treated as the main element from which the search starts.
# In order to find all matches, the iterator iterates recursively through all child elements and their nested elements.
for author in root.iter('author'):
    print(author.text)
# Antoine de Saint-Exupéry
# William Shakespeare
print()

# the findall method search for direct child elements (the findall method can only iterate over the book elements that are the closest children of the root element. )
#  The findall method also accepts an XPath expression
#  — `findall()` in Python’s `xml.etree.ElementTree` module does accept a limited form of **XPath expressions**, which makes it super handy for navigating XML trees.
#
# ### 🔍 How `findall()` Uses XPath
#
# While it doesn’t support full XPath syntax like `lxml` does, it handles a useful subset:
#
# #### ✅ Supported XPath Patterns
#
# | Expression             | Meaning                                      |
# |------------------------|----------------------------------------------|
# | `'tag'`                | Finds all child elements with that tag       |
# | `'./tag'`              | Finds direct children with that tag          |
# | `'.//tag'`             | Finds all descendants with that tag          |
# | `'tag[@attr="value"]'` | Finds elements with a specific attribute     |
#
# ### 🧪 Example
#
# ```python
# import xml.etree.ElementTree as ET
#
# xml_data = '''
# <library>
#     <book genre="fiction">
#         <title>Python 101</title>
#     </book>
#     <book genre="non-fiction">
#         <title>Data Science</title>
#     </book>
# </library>
# '''
#
# root = ET.fromstring(xml_data)
#
# # Find all book elements
# books = root.findall('.//book')
#
# # Find books with genre="fiction"
# fiction_books = root.findall('.//book[@genre="fiction"]')
#
# for book in fiction_books:
#     print(book.find('title').text)  # Output: Python 101
# ```
#
# ### ⚠️ Limitations
#
# - No support for complex XPath like `position()`, `contains()`, or `or`
# - If you need full XPath power, consider switching to `lxml.etree`
#
for book in root.findall('book'):
    print(book.get('title'))
# The Little Prince
# Hamlet

# The find method returns the first child element containing the specified tag or matching XPath expression.
# Note that the element from which we start the search is the root element.
print(root.find('book').get('title'))
# The Little Prince