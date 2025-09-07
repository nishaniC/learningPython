import xml.etree.ElementTree as ET
xml_data="""<?xml version="1.0"?>
<shop>
    <category name="Vegan Products">
        <product name="Good Morning Sunshine">
            <type>cereals</type>
            <producer>OpenEDG Testing Service</producer>
            <price>9.90</price>
            <currency>USD</currency>
        </product>
        <product name="Spaghetti Veganietto">
            <type>pasta</type>
            <producer>Programmers Eat Pasta</producer>
            <price>15.49</price>
            <currency>EUR</currency>
        </product>
        <product name="Fantastic Almond Milk">
            <type>beverages</type>
            <producer>Drinks4Coders Inc.</producer>
            <price>19.75</price>
            <currency>USD</currency>
        </product>
    </category>
</shop>"""

root = ET.fromstring(xml_data)

tree = ET.ElementTree(root)
tree.write('shop.xml', 'UTF-8', True)

def createxmlelement(root_tag,child_tag,attrib):
    item = ET.SubElement(root_tag, child_tag, attrib)

# second approach
root2 = ET.Element('shop')
tree2 = ET.ElementTree(root2)
category  = ET.SubElement(root2, 'category ', {'name': 'Vegan Products'})
product1 = ET.SubElement(category , 'product', {'name': 'Good Morning Sunshine'})
type1 = ET.SubElement(product1 , 'type')
type1.text='cereals'
producer1 = ET.SubElement(product1 , 'producer')
producer1.text='OpenEDG Testing Service'
price1 = ET.SubElement(product1 , 'price')
price1.text='9.90'
currency1 = ET.SubElement(product1 , 'currency')
currency1.text='USD'

product2 = ET.SubElement(category , 'product', {'name': 'Spaghetti Veganietto'})
type2 = ET.SubElement(product2 , 'type')
type2.text='pasta'
producer2 = ET.SubElement(product2 , 'producer')
producer2.text='Programmers Eat Pasta'
price2 = ET.SubElement(product2 , 'price')
price2.text='15.49'
currency2 = ET.SubElement(product2 , 'currency')
currency2.text='EUR'

product2 = ET.SubElement(category , 'product', {'name': 'Fantastic Almond Milk'})
type2 = ET.SubElement(product2 , 'type')
type2.text='beverages'
producer2 = ET.SubElement(product2 , 'producer')
producer2.text='Drinks4Coders Inc.'
price2 = ET.SubElement(product2 , 'price')
price2.text='19.75'
currency2 = ET.SubElement(product2 , 'currency')
currency2.text='USD'


tree2.write('shop2.xml', 'UTF-8', True)