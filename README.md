This is a slightly modified version of Trench's source available here:

http://digitalcommons.trinity.edu/mono/7/

The figures have been converted to .png format (from .eps) and the
corresponding LaTeX source has been adapted to use the .png files instead
of the .eps files.

The main LaTeX file can be compiled from the command line using:

	pdflatex trench.tex

which will produce a viewable .pdf file of the text.

trench_real_analysis.tex is the original .eps based LaTeX source, to
compile this, copy it to the eps directory and use:

	latex trench_real_analysis.tex

	dvips trench_real_analysis.dvi

trench.tex is the modified .png based LaTeX source.

Directories:
	Python:  a couple of Python scripts that I used to make some
	modifications.

	eps:  the original eps formatted figures

	png:  png versions of the figures, created with ImageMagick's
	"convert" command, i.e.
		convert -density 300 fig010101.eps fig010101.png
