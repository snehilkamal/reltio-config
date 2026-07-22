import csv

suffix = '_RDNB'

template_string_type = """<fields>
    <fullName>{name}{suffix}__c</fullName>
    <label>{label}</label>
    <type>Text</type>
    <length>255</length>
    <required>false</required>
    <externalId>false</externalId>
    <trackFeedHistory>false</trackFeedHistory>
    <trackHistory>false</trackHistory>
</fields>"""

template_number_type = """<fields>
    <fullName>{name}{suffix}__c</fullName>
    <label>{label}</label>
    <type>Number</type>
    <precision>18</precision>
    <scale>0</scale>
    <required>false</required>
    <externalId>false</externalId>
    <trackFeedHistory>false</trackFeedHistory>
    <trackHistory>false</trackHistory>
</fields>"""

template_boolean_type = """<fields>
    <fullName>{name}{suffix}__c</fullName>
    <label>{label}</label>
    <type>Checkbox</type>
    <defaultValue>false</defaultValue>
    <required>false</required>
    <externalId>false</externalId>
    <trackFeedHistory>false</trackFeedHistory>
    <trackHistory>false</trackHistory>
</fields>"""

template_date_type = """<fields>
    <fullName>{name}{suffix}__c</fullName>
    <label>{label}</label>
    <type>Date</type>
    <required>false</required>
    <externalId>false</externalId>
    <trackFeedHistory>false</trackFeedHistory>
    <trackHistory>false</trackHistory>
</fields>"""

default_template = """<fields>
    <fullName>{name}{suffix}__c</fullName>
    <label>{label}</label>
    <type>{type}</type>
    <required>false</required>
    <externalId>false</externalId>
    <trackFeedHistory>false</trackFeedHistory>
    <trackHistory>false</trackHistory>
</fields>"""

template_members = '<members>Account.{name}{suffix}__c</members>'

templates = {
    'Text': template_string_type,
    'Number': template_number_type,
    'Checkbox': template_boolean_type,
    'Date': template_date_type
}

admin_template = """<fieldPermissions>
    <field>Account.{name}{suffix}__c</field>
    <editable>true</editable>
    <readable>true</readable>
</fieldPermissions>
"""

layout_template = """<layoutItems>
    <behavior>Edit</behavior>
    <field>{name}{suffix}__c</field>
</layoutItems>
"""

mapping_template = '"{name}{suffix}__c": "{uri}",'

"""
"HasOptedOutOfEmail": "*/attributes/PrivacyPreferences/*/value/EmailOptOut/@@@ov@@@/@value",

configuration/entityTypes/Organization/attributes/Identifiers/attributes/ActivationDate
"""


def convert_uri(uri):
    return '*/attributes/' + uri.replace('configuration/entityTypes/Organization/attributes/', '')\
                .replace('attributes', '*/value', ) + '/@@@ov@@@/@value'


with open('reltio_fields.csv') as fin,\
    open('out_fields.txt', 'w') as out_fields_file,\
    open('out_package.txt', 'w') as out_pack_file,\
    open('out_layouts.txt', 'w') as out_layout_file,\
    open('out_mapping_r_s.txt', 'w') as out_mapping_file,\
    open('out_admin.txt', 'w') as out_admin_file:

    reader = csv.reader(fin)
    for row in reader:
        t = templates.get(row[1])
        out_fields_file.write(t.format(name=row[0], suffix=suffix, label=row[3]) + '\n')
        out_pack_file.write(template_members.format(name = row[0], suffix=suffix) + '\n')
        out_admin_file.write(admin_template.format(name = row[0], suffix=suffix))
        out_layout_file.write(layout_template.format(name = row[0], suffix=suffix))
        out_mapping_file.write(mapping_template.format(name = row[0], suffix=suffix, uri=convert_uri(row[2])) + '\n')