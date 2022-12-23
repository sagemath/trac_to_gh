# Issue 6530: methods not shown in documentation search

Issue created by migration from https://trac.sagemath.org/ticket/6530

Original creator: gpannwitz

Original creation time: 2009-07-14 07:39:42

Assignee: schilly

I did a search, on www.sagemath.org, for "gram schmidt".  In the Documentation section, there was no link returned for the documentation of the method "gram_schmidt", although this was exactly what I was looking for:

http://www.sagemath.org/doc/reference/sage/matrix/matrix2.html#sage.matrix.matrix2.Matrix.gram_schmidt

Perhaps our custom Google search can be tweaked?


---

Comment by schilly created at 2009-07-14 08:09:06

technically, it is all set so that it should work. I've added some redundant sites:

```
	http://www.sagemath.org/doc/numerical_sage    doc 
	http://www.sagemath.org/doc/a_tour_of_sage/    doc 
	http://www.sagemath.org/doc/installation/    doc 
	http://www.sagemath.org/doc/reference/    doc 
	http://www.sagemath.org/doc/developer/    developer 
	http://www.sagemath.org/doc/constructions    doc 
	http://www.sagemath.org/doc/tutorial/    doc 
```

(label "doc" is for used for documentation)

and a master page for the reference to point to all pages

```
http://www.sagemath.org/doc/reference/genindex-all.html [extract linked partial sites]   doc   
```


maybe it works now better, but i'm not sure.


---

Comment by schilly created at 2009-11-19 22:03:29

Resolution: fixed


---

Comment by schilly created at 2009-11-19 22:03:29

tested again, it finds "gram_schmidt" now. only "gram schmidt" seems to be too vague. ticket can be closed.
