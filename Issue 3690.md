# Issue 3690: trivial problems in the doc spkg

Issue created by migration from Trac.

Original creator: tabbott

Original creation time: 2008-07-21 05:50:06

Assignee: mabshoff

Below are some trivial problems in the doc spkg found using Debian's automated package quality checking tools:

# Empty files in doc-3.0.5.spkg

```
const/.doctest/err
const/tut.toc
doc/.doctest/err
doc/.doctest/out
html/const/images.idx
html/inst/images.idx
html/inst/index.dat
html/prog/images.idx
html/prog/index.dat
html/ref/images.idx
html/whatsnew/index.dat
inst/inst.idx
overviews/.doctest/err
overviews/.doctest/out
prog/.doctest/err
prog/.doctest/out
prog/prog.idx
ref/ref.idx
ref/ref10.syn
ref/ref11.syn
ref/ref12.syn
ref/ref13.syn
ref/ref14.syn
ref/ref15.syn
ref/ref16.syn
ref/ref17.syn
ref/ref18.syn
ref/ref19.syn
ref/ref2.syn
ref/ref20.syn
ref/ref21.syn
ref/ref22.syn
ref/ref23.syn
ref/ref24.syn
ref/ref25.syn
ref/ref26.syn
ref/ref27.syn
ref/ref28.syn
ref/ref29.syn
ref/ref3.syn
ref/ref30.syn
ref/ref31.syn
ref/ref32.syn
ref/ref33.syn
ref/ref34.syn
ref/ref35.syn
ref/ref36.syn
ref/ref37.syn
ref/ref38.syn
ref/ref39.syn
ref/ref4.syn
ref/ref40.syn
ref/ref41.syn
ref/ref42.syn
ref/ref43.syn
ref/ref5.syn
ref/ref6.syn
ref/ref7.syn
ref/ref8.syn
ref/ref9.syn
ref/rings.py
texinputs/python.
tut/.doctest/err
tut/glossary.tex
version
```


# Empty directories in doc-3.0.5.spkg

```
auto/
overviews/a_tour_of_sage/sage_notebook/worksheets/root/0/cells/0/
overviews/a_tour_of_sage/sage_notebook/worksheets/root/0/cells/1/
overviews/a_tour_of_sage/sage_notebook/worksheets/root/0/cells/2/
overviews/a_tour_of_sage/sage_notebook/worksheets/root/0/cells/3/
overviews/a_tour_of_sage/sage_notebook/worksheets/root/0/cells/4/
overviews/a_tour_of_sage/sage_notebook/worksheets/root/0/cells/6/
overviews/a_tour_of_sage/sage_notebook/worksheets/root/0/cells/7/
overviews/a_tour_of_sage/sage_notebook/worksheets/root/0/cells/9/
overviews/a_tour_of_sage/sage_notebook/worksheets/root/0/cells/10/
overviews/a_tour_of_sage/sage_notebook/worksheets/root/0/cells/11/
overviews/a_tour_of_sage/sage_notebook/worksheets/root/0/cells/14/
overviews/a_tour_of_sage/sage_notebook/worksheets/root/0/cells/21/
overviews/a_tour_of_sage/sage_notebook/worksheets/root/0/data/
overviews/a_tour_of_sage/sage_notebook/objects/
```



---

Comment by mvngu created at 2009-08-13 19:41:44

Resolution: invalid


---

Comment by mvngu created at 2009-08-13 19:41:44

The issue is no longer relevant since we have switched to using Sphinx and ReST for the documentation.
