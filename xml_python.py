import xml.etree.ElementTree as ET

xml_data = """
<user>
    <id>1</id>
    <first_name>John</first_name>
    <last_name>Doe</last_name>
    <email>jihn.doe@example.com</email>
</user>
"""

root = ET.fromstring(xml_data)
print("User ID:", root.find('id').text)
print("User email:", root.find('email').text)
print("User name:", root.find("first_name").text, root.find("last_name").text)
