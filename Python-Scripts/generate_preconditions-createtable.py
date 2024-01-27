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

def add_preconditions(input_file, output_file):
    try:
        # Load the XML file with the namespace
        ns = {'lb': 'http://www.liquibase.org/xml/ns/dbchangelog'}
        tree = etree.parse(input_file)
        root = tree.getroot()

        # Find all <createTable> elements
        create_table_elements = root.xpath('//lb:createTable', namespaces=ns)

        # Loop through each <createTable> element
        for create_table in create_table_elements:
            # Create a new <preConditions> element
            preconditions = etree.Element('preConditions', onFail="MARK_RAN")
            not_element = etree.SubElement(preconditions, 'not')
            table_exists_element = etree.SubElement(not_element, 'tableExists', tableName=create_table.get('tableName'))

            # Insert the <preConditions> before the <createTable>
            create_table_index = create_table.getparent().index(create_table)
            create_table.getparent().insert(create_table_index, preconditions)

        # Save the modified XML to the output file
        tree.write(output_file, pretty_print=True)
        print(f"Preconditions for createTable added successfully! Output saved to {output_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Specify the input XML file without preconditions
input_file = ""

# Specify the output file where the new changesets with preconditions will be saved
output_file = ""

# Call the function to add preconditions
add_preconditions(input_file, output_file)

