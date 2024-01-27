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

def add_foreign_key_preconditions(input_file, output_file):
    try:
        # Load the XML file with the namespace
        ns = {'lb': 'http://www.liquibase.org/xml/ns/dbchangelog'}
        tree = etree.parse(input_file)
        root = tree.getroot()

        # Find all <addForeignKeyConstraint> elements
        add_foreign_key_elements = root.xpath('//lb:addForeignKeyConstraint', namespaces=ns)

        # Loop through each <addForeignKeyConstraint> element
        for add_foreign_key in add_foreign_key_elements:
            # Create a new <preConditions> element
            preconditions = etree.Element('preConditions', onFail="MARK_RAN")
            not_element = etree.SubElement(preconditions, 'not')
            foreign_key_constraint_exists_element = etree.SubElement(
                not_element, 'foreignKeyConstraintExists',
                foreignKeyName=add_foreign_key.get('constraintName'),
                foreignKeyTableName=add_foreign_key.get('baseTableName')
            )

            # Insert the <preConditions> before the <addForeignKeyConstraint>
            add_foreign_key_index = add_foreign_key.getparent().index(add_foreign_key)
            add_foreign_key.getparent().insert(add_foreign_key_index, preconditions)

        # Save the modified XML to the output file
        tree.write(output_file, pretty_print=True)
        print(f"Preconditions for addForeignKeyConstraint added successfully! Output saved to {output_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Specify the input XML file without preconditions
input_file = ""

# Specify the output file where the new changesets with preconditions will be saved
output_file = ""

# Call the function to add preconditions to addForeignKeyConstraint elements
add_foreign_key_preconditions(input_file, output_file)

