# Generates PDF for Set 3

# python executable
CC = python2

# all plots
PLOTS = explicit explicit_error explicit_error_v_h explicit_E explicit_E_log implicit implicit_error implicit_E xv symplectic combined_xv symplectic_E symplectic_error

pdf: set4.tex $(PLOTS)
	pdflatex set4.tex

$(PLOTS): %: autoplots.py spring.py
	$(CC) autoplots.py $@

clean:
	rm -f *-eps-converted-to.pdf
	rm -f *.eps
