# ============================================
# Scripts generated using ChatGPT by Yeran Kods
# ============================================
#
# This script is open for modifications
# Feel free to enhance and customize!
#
# Date: 27th January 2024
# ============================================

from lxml import etree

def extract_column_info(xml_file, output_file):
    try:
        tree = etree.parse(xml_file)
        root = tree.getroot()

        with open(output_file, 'w') as output:
            for change_set in root.xpath('//lb:changeSet', namespaces={'lb': 'http://www.liquibase.org/xml/ns/dbchangelog'}):
                change_set_id = change_set.get('id')
                for add_column in change_set.xpath('.//lb:addColumn', namespaces={'lb': 'http://www.liquibase.org/xml/ns/dbchangelog'}):
                    table_name = add_column.get('tableName')
                    column_name = add_column.find('lb:column', namespaces={'lb': 'http://www.liquibase.org/xml/ns/dbchangelog'}).get('name')
                    column_type = add_column.find('lb:column', namespaces={'lb': 'http://www.liquibase.org/xml/ns/dbchangelog'}).get('type')

                    if column_type.startswith("VARCHAR") and column_type != "VARCHAR(255)":
                        output.write(f"ChangeSet ID: {change_set_id}, Table: {table_name}, Column: {column_name}, Type: {column_type}\n")

        print(f"Output saved to {output_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Specify the input XML file
input_file = ""

# Specify the output text file
output_file = "varchar_diff.txt"

# Call the function to extract column information
extract_column_info(input_file, output_file)

