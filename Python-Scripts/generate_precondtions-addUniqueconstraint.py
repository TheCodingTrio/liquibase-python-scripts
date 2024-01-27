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

def add_unique_constraint_preconditions(input_file, output_file):
    try:
        # Load the XML file with the namespace
        ns = {'lb': 'http://www.liquibase.org/xml/ns/dbchangelog'}
        tree = etree.parse(input_file)
        root = tree.getroot()

        # Find all <addUniqueConstraint> elements
        add_unique_constraint_elements = root.xpath('//lb:addUniqueConstraint', namespaces=ns)

        # Loop through each <addUniqueConstraint> element
        for add_unique_constraint in add_unique_constraint_elements:
            # Create a new <preConditions> element
            preconditions = etree.Element('preConditions', onFail="MARK_RAN")
            not_element = etree.SubElement(preconditions, 'not')
            unique_constraint_exists_element = etree.SubElement(
                not_element, 'uniqueConstraintExists',
                tableName=add_unique_constraint.get('tableName'),
                columnNames=add_unique_constraint.get('columnNames'),
                constraintName=add_unique_constraint.get('constraintName')
            )

            # Insert the <preConditions> before the <addUniqueConstraint>
            add_unique_constraint_index = add_unique_constraint.getparent().index(add_unique_constraint)
            add_unique_constraint.getparent().insert(add_unique_constraint_index, preconditions)

        # Save the modified XML to the output file
        tree.write(output_file, pretty_print=True)
        print(f"Preconditions for addUniqueConstraint added successfully! Output saved to {output_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Specify the input XML file without preconditions
input_file = ""

# Specify the output file where the new changesets with preconditions will be saved
output_file = ""

# Call the function to add preconditions to addUniqueConstraint elements
add_unique_constraint_preconditions(input_file, output_file)
