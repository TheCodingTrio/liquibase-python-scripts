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

def extract_table_structure(changelog_file):
    ns = {'lb': 'http://www.liquibase.org/xml/ns/dbchangelog'}
    tree = etree.parse(changelog_file)
    root = tree.getroot()

    table_structures = {}

    for create_table in root.xpath('//lb:createTable', namespaces=ns):
        table_name = create_table.get('tableName')
        columns = {}

        for column in create_table.xpath('./lb:column', namespaces=ns):
            column_name = column.get('name')
            column_type = column.get('type')
            columns[column_name] = column_type

        table_structures[table_name] = columns

    return table_structures

def compare_table_structures(old_changelog, new_changelog):
    old_structure = extract_table_structure(old_changelog)
    new_structure = extract_table_structure(new_changelog)

    diff_results = []

    for table, old_columns in old_structure.items():
        if table in new_structure:
            new_columns = new_structure[table]

            for column, old_type in old_columns.items():
                if column in new_columns:
                    new_type = new_columns[column]
                    if old_type != new_type:
                        diff_results.append(f"Table: {table}, Column: {column}, Old Type: {old_type}, New Type: {new_type}")

    return diff_results

def save_diff_to_file(diff_results, output_file):
    with open(output_file, 'w') as file:
        for diff in diff_results:
            file.write(f"{diff}\n")

if __name__ == "__main__":
    old_changelog_file = ""

    new_changelog_file = ""

    output_diff_file = "table_structure_diff.txt"

    differences = compare_table_structures(old_changelog_file, new_changelog_file)
    save_diff_to_file(differences, output_diff_file)

    print(f"Table structure differences saved to {output_diff_file}")






