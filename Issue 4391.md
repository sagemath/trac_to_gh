# Issue 4391: [with patch, needs review] Sage 3.1.4: optional doctest failure in sage/schemes/elliptic_curves/ell_finite_field.py

Issue created by migration from https://trac.sagemath.org/ticket/4391

Original creator: mabshoff

Original creation time: 2008-10-30 06:41:42

Assignee: mabshoff


```
sage -t -long -optional devel/sage/sage/schemes/elliptic_curves/ell_finite_field.py
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.1.3.final/tmp/ell_finite_field.py", line 102:
    sage: magma(E) # optional -- requires Magma
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/release-cycle/sage-3.1.3.final/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_4[3]>", line 1, in <module>
        magma(E) # optional -- requires Magma###line 102:
    sage: magma(E) # optional -- requires Magma
    NameError: name 'E' is not defined
**********************************************************************
```



---

Comment by mabshoff created at 2008-10-30 06:41:53

Changing status from new to assigned.


---

Comment by craigcitro created at 2008-10-30 07:26:31

Looks good.


---

Comment by mabshoff created at 2008-10-30 07:39:13

I had to rebase t my own patch for Saeg 3.2.alpha1, oh well :)

Cheers,

Michael


---

Attachment


---

Comment by mabshoff created at 2008-10-30 07:42:54

Resolution: fixed


---

Comment by mabshoff created at 2008-10-30 07:42:54

Merged in Sage 3.2.alpha2
