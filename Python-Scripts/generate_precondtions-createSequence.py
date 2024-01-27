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

def add_sequence_preconditions(input_file, output_file):
    try:
        # Load the XML file with the namespace
        ns = {'lb': 'http://www.liquibase.org/xml/ns/dbchangelog'}
        tree = etree.parse(input_file)
        root = tree.getroot()

        # Find all <createSequence> elements
        create_sequence_elements = root.xpath('//lb:createSequence', namespaces=ns)

        # Loop through each <createSequence> element
        for create_sequence in create_sequence_elements:
            # Create a new <preConditions> element
            preconditions = etree.Element('preConditions', onFail="MARK_RAN")
            not_element = etree.SubElement(preconditions, 'not')
            sequence_exists_element = etree.SubElement(
                not_element, 'sequenceExists',
                sequenceName=create_sequence.get('sequenceName')
            )

            # Insert the <preConditions> before the <createSequence>
            create_sequence_index = create_sequence.getparent().index(create_sequence)
            create_sequence.getparent().insert(create_sequence_index, preconditions)

        # Save the modified XML to the output file
        tree.write(output_file, pretty_print=True)
        print(f"Preconditions for createSequence added successfully! Output saved to {output_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Specify the input XML file without preconditions
input_file = ""

# Specify the output file where the new changesets with preconditions will be saved
output_file = ""

# Call the function to add preconditions to createSequence elements
add_sequence_preconditions(input_file, output_file)


