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

def extract_foreign_key_constraints(changelog_file):
    ns = {'lb': 'http://www.liquibase.org/xml/ns/dbchangelog'}
    tree = etree.parse(changelog_file)
    root = tree.getroot()

    foreign_key_constraints = {}

    for change_set in root.xpath('//lb:changeSet', namespaces=ns):
        change_set_id = change_set.get('id')

        old_constraint = change_set.find('.//lb:preConditions/lb:foreignKeyConstraintExists', namespaces=ns)
        new_constraint = change_set.find('.//lb:addForeignKeyConstraint', namespaces=ns)

        if old_constraint is not None and new_constraint is not None:
            old_table_name = old_constraint.get('foreignKeyTableName')
            new_table_name = new_constraint.get('baseTableName')

            old_constraint_name = old_constraint.get('foreignKeyName')
            new_constraint_name = new_constraint.get('constraintName')

            if old_constraint_name != new_constraint_name and old_table_name == new_table_name:
                foreign_key_constraints[change_set_id] = {
                    'table_name': old_table_name,
                    'old_constraint_name': old_constraint_name,
                    'new_constraint_name': new_constraint_name
                }

    return foreign_key_constraints

def save_diff_to_file(diff_results, output_file):
    with open(output_file, 'w') as file:
        for change_set_id, diff in diff_results.items():
            file.write(f"ChangeSet ID: {change_set_id}\n")
            file.write(f"Table Name: {diff['table_name']}\n")
            file.write(f"Old Constraint Name: {diff['old_constraint_name']}\n")
            file.write(f"New Constraint Name: {diff['new_constraint_name']}\n")
            file.write("\n")

if __name__ == "__main__":
    old_changelog_file = ""
    new_changelog_file = ""
    output_diff_file = "foreign_key_constraints_diff.txt"

    differences = extract_foreign_key_constraints(old_changelog_file)
    save_diff_to_file(differences, output_diff_file)

    print(f"Foreign Key Constraints differences saved to {output_diff_file}")
