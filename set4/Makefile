# Generates PDF for Set 3

# python executable
CC=python2

pdf: set4.tex plots
	pdflatex set4.tex

plots: autoplots.py spring.py
	$(CC) autoplots.py

clean:
	rm -f *-eps-converted-to.pdf
	rm -f *.eps
