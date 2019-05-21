SHELL=/bin/bash
DOC=diplom

all:
	latexmk -synctex=1 -interaction=nonstopmode -file-line-error -pdf -outdir=./ $(DOC).tex

clean:
	rm *.aux *.log *.out *.toc *.pdf *.fls *.gz *.fdb_latexmk