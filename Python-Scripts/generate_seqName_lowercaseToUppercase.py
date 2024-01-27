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

def update_sequence_names(input_file, output_file):
    try:
        # Load the XML file with the namespace
        ns = {'lb': 'http://www.liquibase.org/xml/ns/dbchangelog'}
        tree = etree.parse(input_file)
        root = tree.getroot()

        # Find all <sequenceExists> and <createSequence> elements
        sequence_elements = root.xpath('//lb:sequenceExists|//lb:createSequence', namespaces=ns)

        # Loop through each <sequenceExists> and <createSequence> element
        for sequence_element in sequence_elements:
            # Get the sequenceName attribute
            sequence_name = sequence_element.get('sequenceName')

            # Update the sequenceName attribute to uppercase
            sequence_element.set('sequenceName', sequence_name.upper())

        # Save the modified XML to the output file
        tree.write(output_file, pretty_print=True)
        print(f"Sequence names updated successfully! Output saved to {output_file}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Specify the input XML file with lowercase sequence names
input_file = ""

# Specify the output file where the updated XML will be saved
output_file = "/home/yeranKods/My-Projects/Python-Scripts/output.xml"

# Call the function to update sequence names
update_sequence_names(input_file, output_file)
