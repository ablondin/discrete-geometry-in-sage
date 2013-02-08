all:
	python process.py diagramme.yaml | dot -Tpdf -o diagramme.pdf
