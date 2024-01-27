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

def add_index_preconditions(input_file, output_file):
    try:
        # Load the XML file with the namespace
        ns = {'lb': 'http://www.liquibase.org/xml/ns/dbchangelog'}
        tree = etree.parse(input_file)
        root = tree.getroot()

        # Find all <createIndex> elements
        create_index_elements = root.xpath('//lb:createIndex', namespaces=ns)

        # Loop through each <createIndex> element
        for create_index in create_index_elements:
            # Create a new <preConditions> element
            preconditions = etree.Element('preConditions', onFail="MARK_RAN")
            not_element = etree.SubElement(preconditions, 'not')
            index_exists_element = etree.SubElement(
                not_element, 'indexExists',
                indexName=create_index.get('indexName'),
                tableName=create_index.get('tableName')
            )

            # Insert the <preConditions> before the <createIndex>
            create_index_index = create_index.getparent().index(create_index)
            create_index.getparent().insert(create_index_index, preconditions)

        # Save the modified XML to the output file
        tree.write(output_file, pretty_print=True)
        print(f"Preconditions added successfully! Output saved to {output_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Specify the input XML file without preconditions
input_file = ""

# Specify the output file where the new changesets with preconditions will be saved
output_file = ""

# Call the function to add preconditions to createIndex elements
add_index_preconditions(input_file, output_file)

