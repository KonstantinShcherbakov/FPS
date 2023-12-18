import xml.etree.ElementTree as ET

def process_xml(input_file, output_file):
    tree = ET.parse(input_file)
    root = tree.getroot()

    # Обработка тега item_id для удаления нулей в начале
    for item in root.findall(".//item"):
        item_id = item.get('id')
        if item_id:
            item_id = item_id.lstrip('0')
            item.set('id', item_id)

    # Замена значений тега <available>
    for available in root.findall(".//available"):
        if available.text == 'true':
            available.text = 'В наличии'
        else:
            available.text = 'Нет в наличии'

    tree.write(output_file, encoding='utf-8', xml_declaration=True)

input_filename = 'input.xml'
output_filename = 'output.xml'

process_xml(input_filename, output_filename)
