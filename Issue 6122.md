# Issue 6122: [with patch, needs review] strip 'nodetex' from docstrings

Issue created by migration from Trac.

Original creator: jhpalmieri

Original creation time: 2009-05-23 20:00:22

Assignee: jhpalmieri

It bothers me that when you ask for a docstring with a 'nodetex' directive, that directive is printed as part of the docstring.  This patch strips it out.

Before (note the line after "Docstring:"):

```
sage: view?
Base Class:       <type 'function'>
String Form:   <function view at 0x102a230>
Namespace:        Interactive
File:             /Applications/sage/local/lib/python2.5/site-packages/sage/misc/latex.py
Definition:       view(objects, title='SAGE', debug=False, sep='', tiny=False, **kwds)
Docstring:
    nodetex
        Compute a latex representation of each object in objects, compile,
        and display typeset. If used from the command line, this requires
        that latex be installed.
```


After:

```
sage: view?
Base Class:       <type 'function'>
String Form:   <function view at 0x102b770>
Namespace:        Interactive
File:             /Applications/sage/local/lib/python2.5/site-packages/sage/misc/latex.py
Definition:       view(objects, title='SAGE', debug=False, sep='', tiny=False, pdflatex=None, **kwds)
Docstring:
    
        Compute a latex representation of each object in objects, compile,
        and display typeset. If used from the command line, this requires
        that latex be installed.
```



---

Attachment

Applies cleanly to 4.0, works as advertised at command-line and in the notebook.

Passes  sage -t -rand sage/misc/sagedoc.py

It would be nice if these directives were cleaned out prior to building the PDF and HTML versions of the documentation.  This patch seems to only apply to the "interactive" documentation.   I'm still seeing nodetex directives in the PDF anyway, and in a sense they are worse, as they lead off a line and then the real beginning follows with no line break (as it used to look in the ASCII versions).  

Positive review.


---

Comment by jhpalmieri created at 2009-05-31 04:59:57

> It would be nice if these directives were cleaned out prior to building the PDF and HTML versions of the documentation.

See #6166.


---

Comment by mhansen created at 2009-06-01 05:04:23

Resolution: fixed


---

Comment by mhansen created at 2009-06-01 05:04:23

Merged in 4.0.1.alpha0.
