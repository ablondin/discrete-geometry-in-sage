YAUML
=====

Script for generating UML diagrams from
`YAML <http://www.yaml.org/>`__ files.

Dependencies
------------

To run the script, the following softwares are needed :

- Python
- `Graphviz <http://www.graphviz.org/>`__
- `PyYAML <https://bitbucket.org/xi/pyyaml>`__

Usage
-----

See file `diagramme.yaml <diagramme.yaml>`__ to see
an example of YAML syntax to be used for specifying
UML relations.

Then run::

    make

Currently, only inheritance and meronymy (is-part-of)
relations are supported
