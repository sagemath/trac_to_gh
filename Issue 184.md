# Issue 184: negation of RealDouble broken

Issue created by migration from Trac.

Original creator: boothby

Original creation time: 2006-12-17 19:36:55

Assignee: somebody


```
sage: -RDF(1)
///
Traceback (most recent call last):
  File "", line 1, in 
  File "/home/server2/sage_notebook/worksheets/bugs_/code/12.py", line 4, in 
    -RDF(Integer(1))
  File "/sage/local/lib/python2.5/", line 1, in 
    
  File "element.pyx", line 511, in element.ModuleElement.__neg__
  File "element.pyx", line 525, in element.ModuleElement._neg_c
  File "element.pyx", line 535, in element.ModuleElement._neg_c_impl
TypeError: 'NoneType' object is not callable
```



---

Comment by dmharvey created at 2006-12-17 22:28:28

Resolution: fixed


---

Comment by dmharvey created at 2006-12-17 22:28:28

Fixed, patch =

http://sage.math.washington.edu/home/dmharvey/patches/rdf-negative.hg
