import xml.etree.ElementTree as parser

tree = parser.parse("store.xml")

#Получили корневой элемент дерева
root = tree.getroot()

for item in root:
    if item != None:
        for inner_item in item:
            if inner_item != None:
                print(inner_item.tag,inner_item.text)

