# Issue 6130: README about documentation is outdated.

Issue created by migration from https://trac.sagemath.org/ticket/6130

Original creator: malb

Original creation time: 2009-05-26 14:32:56

Assignee: tba


```
8. OPTIONAL: Documentation: If you want to (try to) build the
   documentation, change into SAGE_ROOT/devel/doc and type "make
   html" or "make pdf".  This requires having latex and latex2html
   installed, and there are some issues with the \url macro.  Note
   that the latex
```



---

Comment by mhansen created at 2009-05-28 07:37:02

Changing assignee from tba to mhansen.


---

Comment by mhansen created at 2009-05-28 07:37:02

I've changed the text to:


```
    8. OPTIONAL: Documentation: If you want to (try to) build the
       documentation, run "sage -docbuild help" for instructions.
       This requires having latex installed (if you want to build PDFs
       or HTML with PNG images for the math).  Note that the latex
       docs come *pre-built* with Sage, and are in
       SAGE_ROOT/devel/sage/doc/output/html.
```



---

Comment by mhansen created at 2009-05-28 07:37:02

Changing status from new to assigned.


---

Comment by mhansen created at 2009-05-28 07:44:14

Merged in 4.0.rc1.


---

Comment by mhansen created at 2009-05-28 07:44:14

Resolution: fixed
