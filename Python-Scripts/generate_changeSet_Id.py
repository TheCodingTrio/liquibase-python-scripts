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

def update_changeset_ids(input_file, output_file):
    try:
        # Load the XML file with the namespace
        ns = {'lb': 'http://www.liquibase.org/xml/ns/dbchangelog'}
        tree = etree.parse(input_file)
        root = tree.getroot()

        # Find all <changeSet> elements
        change_set_elements = root.xpath('//lb:changeSet', namespaces=ns)

        # Loop through each <changeSet> element and update the id attribute
        for i, change_set in enumerate(change_set_elements):
            new_id = f"EHR-ORBOOK_v3.0.{i}"
            change_set.set('id', new_id)

        # Save the modified XML to the output file
        tree.write(output_file, pretty_print=True)
        print(f"ChangeSet ids updated successfully! Output saved to {output_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Specify the input XML file without preconditions
input_file = ""

# Specify the output file where the new changesets with updated ids will be saved
output_file = ""

# Call the function to update changeSet ids
update_changeset_ids(input_file, output_file)

