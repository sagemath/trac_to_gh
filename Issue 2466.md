# Issue 2466: 2.10.3: doctest failure in const.tex

Issue created by migration from https://trac.sagemath.org/ticket/2466

Original creator: mabshoff

Original creation time: 2008-03-11 01:47:54

Assignee: failure


```
sage -t -long devel/doc-main/const/const.tex
**********************************************************************
File "const.py", line 1544:
    : A.eigenspaces() #random output
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/release-cycle/sage-2.10.3.rc4/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_47[5]>", line 1, in <module>
        print "ignore this";  A.eigenspaces() #random output###line 1544:
    : A.eigenspaces() #random output
      File "matrix2.pyx", line 2198, in sage.matrix.matrix2.Matrix.eigenspaces
    NotImplementedError: won't use generic algorithm for inexact base rings, pass the option even_if_inexact=True if you really want this.
**********************************************************************
```



---

Attachment


---

Comment by was created at 2008-03-11 02:24:36

Resolution: fixed


---

Comment by mabshoff created at 2008-03-11 02:36:35

Patch looks good to me. Positive review.


---

Comment by mabshoff created at 2008-03-11 02:36:50

Merged in Sage 2.10.3.rc5
