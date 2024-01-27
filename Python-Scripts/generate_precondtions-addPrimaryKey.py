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

def add_primary_key_preconditions(input_file, output_file):
    try:
        # Load the XML file with the namespace
        ns = {'lb': 'http://www.liquibase.org/xml/ns/dbchangelog'}
        tree = etree.parse(input_file)
        root = tree.getroot()

        # Find all <addPrimaryKey> elements
        add_primary_key_elements = root.xpath('//lb:addPrimaryKey', namespaces=ns)

        # Loop through each <addPrimaryKey> element
        for add_primary_key in add_primary_key_elements:
            # Create a new <preConditions> element
            preconditions = etree.Element('preConditions', onFail="MARK_RAN")
            not_element = etree.SubElement(preconditions, 'not')
            primary_key_exists_element = etree.SubElement(
                not_element, 'primaryKeyExists',
                tableName=add_primary_key.get('tableName'),
                primaryKeyName=add_primary_key.get('constraintName')  # Add primaryKeyName attribute
            )

            # Insert the <preConditions> before the <addPrimaryKey>
            add_primary_key_index = add_primary_key.getparent().index(add_primary_key)
            add_primary_key.getparent().insert(add_primary_key_index, preconditions)

        # Save the modified XML to the output file
        tree.write(output_file, pretty_print=True)
        print(f"Preconditions for addPrimaryKey added successfully! Output saved to {output_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Specify the input XML file without preconditions
input_file = ""

# Specify the output file where the new changesets with preconditions will be saved
output_file = ""

# Call the function to add preconditions to addPrimaryKey elements
add_primary_key_preconditions(input_file, output_file)

