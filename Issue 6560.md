# Issue 6560: docstring formatting issue from ticket #6332

Issue created by migration from https://trac.sagemath.org/ticket/6560

Original creator: mvngu

Original creation time: 2009-07-19 16:37:27

Assignee: tbd

CC:  fwclarke

The patch `trac_6332.patch` at #6332 contains docstrings that aren't formatted properly:

```
164	        -  ``var'' - the name used for the generator of the number fields (default 'a').
203	        -  ``var'' - the name used for the generator of the number fields (default 'a').
246	        -  ``var'' - the name used for the generator of the number fields (default 'a').
```

These results in 3 warnings when building the HTML version of the reference manual.


---

Comment by mvngu created at 2009-07-21 10:06:23

Resolution: duplicate


---

Comment by mvngu created at 2009-07-21 10:06:23

This is a duplicate of #6577.
