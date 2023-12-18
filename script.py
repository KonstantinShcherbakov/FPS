import requests
import xml.etree.ElementTree as ET

def process_xml_from_url(url, output_file):
    response = requests.get(url)
    
    if response.status_code == 200:
        root = ET.fromstring(response.content)
        
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

        tree = ET.ElementTree(root)
        tree.write(output_file, encoding='utf-8', xml_declaration=True)
        print(f"Файл '{output_file}' успешно сохранен.")
    else:
        print("Не удалось загрузить файл.")

url = 'https://logicfox.info/Price/LogicFox_UT_logic-house_test.xml'
output_filename = 'output.xml'

process_xml_from_url(url, output_filename)
