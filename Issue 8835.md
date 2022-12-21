# Issue 8835: mark some latex doctests optional

Issue created by migration from Trac.

Original creator: was

Original creation time: 2010-05-01 06:18:36

Assignee: tbd

On t2 we have some failures due to assumptions in doctests about the latex install.  As latex is not a prereq for sage, not having it shouldn't result in latex errors.  These should thus be marked


```
    # optional - latex
```


The failures:


```
sage -t  -long "devel/sage/sage/misc/latex.py"
**********************************************************************
File "/scratch/wstein/build/sage-4.4.1.alpha2/devel/sage/sage/misc/latex.py", line 1023:
    sage: latex.has_file("article.cls")
Expected:
    True
Got:
    False
**********************************************************************
File "/scratch/wstein/build/sage-4.4.1.alpha2/devel/sage/sage/misc/latex.py", line 1050:
    sage: latex.check_file("article.cls")
Expected nothing
Got:
    <BLANKLINE>
    Warning: `article.cls` is not part of this computer's TeX installation.
**********************************************************************
File "/scratch/wstein/build/sage-4.4.1.alpha2/devel/sage/sage/misc/latex.py", line 1207:
    sage: latex.extra_preamble()
Expected:
    '\\usepackage{xypic}\n'
Got:
    ''
**********************************************************************
3 items had failures:
   1 of   4 in __main__.example_28
   1 of   6 in __main__.example_29
   1 of   6 in __main__.example_35
***Test Failed*** 3 failures.
For whitespace errors, see the file /scratch/wstein/sage//tmp/.doctest_latex.py
```



---

Attachment


---

Comment by was created at 2010-05-01 06:22:41

Changing status from new to needs_review.


---

Comment by mvngu created at 2010-05-02 18:31:35

Yes, LaTeX is not a prerequisite. With the patch, the doctests under `sage/misc/latex.py` pass on t2.math.


---

Comment by mvngu created at 2010-05-02 18:31:35

Resolution: fixed
