# Generates PDF for Set 3

# python executable
CC = python2

# all plots
PLOTS = explicit.eps explicit_error.eps bigh.eps smallh.eps explicit_E.eps explicit_E_log.eps implicit.eps implicit_error.eps implicit_E.eps explicit_xv.eps implicit_xv.eps symplectic.eps combined_xv.eps symplectic_E.eps symplectic_error.eps

pdf: set4.tex $(PLOTS)
	pdflatex set4.tex

$(PLOTS): %.eps: autoplots.py spring.py
	$(CC) autoplots.py $*

clean:
	rm -f *-eps-converted-to.pdf
	rm -f *.eps
