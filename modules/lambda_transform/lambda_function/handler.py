import json
import xml.etree.ElementTree as ET

def json_to_xml(json_obj):
    root = ET.Element("root")
    for key, val in json_obj.items():
        child = ET.SubElement(root, key)
        child.text = str(val)
    return ET.tostring(root, encoding='unicode')

def lambda_handler(event, context):
    try:
        data = event.get("body")
        if isinstance(data, str):
            data = json.loads(data)

        xml_result = json_to_xml(data)
        return {
            'statusCode': 200,
            'body': xml_result,
            'headers': {
                'Content-Type': 'application/xml'
            }
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': str(e)
        }
