import yaml, sys

# Retrieve arguments
yaml_filename = sys.argv[1]

# Retrieve template
template_file = open('template.dot', 'r')
template = template_file.read()
template_file.close()

# Retrieve yaml data
with open(yaml_filename) as yaml_file: data = yaml.load(yaml_file.read())

# Retrieves classes
CLASS_FORMAT = """  %s [
    label = "{%s
    |%s|%s}"
  ]

"""
class_string = ''
for entity in data:
    if 'class' in entity:
        class_name = entity['class']
    else:
        raise ValueError, 'Class name is mandatory'
    attributes = ''
    if 'attributes' in entity:
        for attribute in entity['attributes']:
            attributes += '%s\\l' % attribute
    else:
        attributes += '\\l'
    methods = ''
    if 'methods' in entity:
        for method in entity['methods']:
            methods += '%s\\l' % method
    else:
        methods += '\\l'
    class_string += CLASS_FORMAT % (class_name, class_name, attributes, methods)

# Retrieves relations
RELATION_FORMAT = "  %s -> %s;\n"
# Inheritance
inheritances = ''
for entity in data:
    if 'inherits' in entity:
        for parent in entity['inherits']:
            inheritances += RELATION_FORMAT % (parent, entity['class'])
# Is-part-of
ispartofs = ''
for entity in data:
    if 'ispartof' in entity:
        for parent in entity['ispartof']:
            ispartofs += RELATION_FORMAT % (parent, entity['class'])

print template % (class_string, inheritances, ispartofs)
