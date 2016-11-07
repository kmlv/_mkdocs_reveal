# Notes for building documentation and slides with MkDocs

* Thanks to Eric Aldrich!

* Additions KLV


## Building static website documentation

* Make a new mkdocs directory with the command

  > mkdocs new dirName

* Place a file entitled mathjaxhelper.js in dirName/docs/js/ with the single
  line:

  > MathJax.Hub.Config({tex2jax: {inlineMath: [['$','$'], ['\\(','\\)']]}});

* Add the following line to mkdocs.yml:

  > extra_javascript: ["https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML","js/mathjaxhelper.js"]

--------------------------------------------
## Building slides

* Install reveal.js in the MkDocs docs directory with the command

  > git clone https://github.com/hakimel/reveal.js.git

* Copy the reveal.js and reveal.css files:

  > cp dirName/docs/reveal.js/js/reveal.js dirName/docs/reveal.js/js/reveal.min.js

  > cp dirName/docs/reveal.js/css/reveal.css dirName/docs/reveal.js/css/reveal.min.css

* Copy the pauseFilter.py script to the docs directory:

  > cp ~/Dropbox/Academics/Markdown/pauseFilter.py dirName/docs/

  All pauses should be written as .. raw:: <!--pause-->

* To access all TeX math environments, create a file
  dirName/docs/reveal.js/js/revealMathJax.js with the code snippet

  <script type="text/x-mathjax-config">
    MathJax.Hub.Config({
      tex2jax: {
  	  inlineMath: [ ['$','$'], ["\\(","\\)"] ],
	  displayMath: [ ['$$','$$'], ["\\[","\\]"] ],	
	  processEscapes: true,
	  displaystyle: true
      },
      "HTML-CSS": { availableFonts: ["TeX"] }
    });
  </script><script type="text/javascript"
    src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML-full">
  </script>

* Copy the file myMoon.css (or another custom CSS file) the css/theme directory:

  > cp ~/Dropbox/Academics/Markdown/myMoon.css dirName/docs/reveal.js/css/theme/

* Build reveal.js slides with the command in the docs directory (or
  where file.md is located). This requires you have pandoc installed previously. 
  There is a pkg download in pandoc github for OSX. 

  > pandoc --filter pauseFilter.py -t revealjs -V revealjs-url=reveal.js --css=reveal.js/css/theme/myMoon.css -H reveal.js/js/revealMathJax.js -s file.md -o file.html

* If using MkDocs, issue this command in the directory where file.md
  resides

* Temporary note: KLV Nov 16 could not get filter to work 

    > mkdocs serve

--------------------------------------------
## Building an academic article

* Kieran Healy has a nice blog post describing how to use pandoc to
  build an academic article:

> http://kieranhealy.org/blog/archives/2014/01/23/plain-text/

* The general command is

> pandoc -r markdown+simple_tables+table_captions+yaml_metadata_block
  -s -S --latex-engine=pdflatex
  --template=$(PREFIX)/templates/latex.template --filter
  pandoc-citeproc --csl=$(PREFIX)/csl/$(CSL).csl --bibliography=$(BIB)

* In his specific case takes the form

> pandoc -r markdown+simple_tables+table_captions+yaml_metadata_block -s -S --latex-engine=pdflatex --template=/Users/kjhealy/.pandoc/templates/latex.template --filter pandoc-citeproc --csl=/Users/kjhealy/.pandoc/csl/apsr.csl --bibliography=/Users/kjhealy/Documents/bibs/socbib-pandoc.bib

* The command depends on a .csl file for bibliography formatting and a
  latex.template file.

## Add ReadTheDocs themes to Sphinx

* Add the lines to conf.py

> import sphinx_rtd_theme
> html_theme = 'sphinx_rtd_theme'
> html_theme_path = ['_themes/sphinx_rtd_theme/']

* Make a directory called _themes in the root reStructuredText
  directory.

* Clone the sphinx_rtd_theme in the _themes directory:

> git clone https://github.com/snide/sphinx_rtd_theme.git
