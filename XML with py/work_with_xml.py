import os
import xml.etree.ElementTree as et

base_path = os.path.dirname(os.path.realpath(__file__))
xml_file = os.path.join(base_path, "tut.xml")
# print(xml_file)

tree = et.parse(xml_file)
root = tree.getroot()

print(len(root[0])) # print how many elements exist in this file:

for child in root:
    print(child.tag)

'''
# chnage value for an exisitng element :

for child in root:
    for element in child:
        if(element.text == "Apple"):
            element.text = "Orange"
        # print(element.tag , " : ", element.text)
'''

'''
# add new element to the file :

new_food = et.SubElement(root, "food", attrib={"id" : "Added"})
new_food_name = et.SubElement(new_food, "name")
new_food_price = et.SubElement(new_food, "price")
new_food_description = et.SubElement(new_food, "description")
new_food_calories = et.SubElement(new_food, "calories")

new_food_name.text = "Apple"
new_food_price.text = "1$"
new_food_description.text = "delicious"
new_food_calories.text = "100"
'''

# write to the old xml file
tree.write(xml_file)  
