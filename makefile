all:
	python process.py diagramme.yaml | dot -Tpng -o diagramme.png
