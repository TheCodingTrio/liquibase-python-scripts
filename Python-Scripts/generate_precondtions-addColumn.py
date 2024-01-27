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

def add_column_preconditions(input_file, output_file):
    try:
        # Load the XML file with the namespace
        ns = {'lb': 'http://www.liquibase.org/xml/ns/dbchangelog'}
        tree = etree.parse(input_file)
        root = tree.getroot()

        # Find all <addColumn> elements
        add_column_elements = root.xpath('//lb:addColumn', namespaces=ns)

        # Loop through each <addColumn> element
        for add_column in add_column_elements:
            # Extract tableName, columnName, and type attributes
            table_name = add_column.get('tableName')
            column_name = add_column.xpath('lb:column/@name', namespaces=ns)[0]
            column_type = add_column.xpath('lb:column/@type', namespaces=ns)[0]

            # Create a new <preConditions> element
            preconditions = etree.Element('preConditions', onFail="MARK_RAN")
            not_element = etree.SubElement(preconditions, 'not')

            # Create <columnExists> element for each column
            column_exists_element = etree.SubElement(
                not_element, 'columnExists',
                tableName=table_name,
                columnName=column_name
            )

            # Insert the <preConditions> before the <addColumn>
            add_column_index = add_column.getparent().index(add_column)
            add_column.getparent().insert(add_column_index, preconditions)

        # Save the modified XML to the output file
        tree.write(output_file, pretty_print=True)
        print(f"Preconditions for addColumn added successfully! Output saved to {output_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Specify the input XML file without preconditions
input_file = ""

# Specify the output file where the new changesets with preconditions will be saved
output_file = ""

# Call the function to add preconditions to addColumn elements
add_column_preconditions(input_file, output_file)
