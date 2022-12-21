# Issue 3970: MaximaElements should not coerce into SR.

Issue created by migration from Trac.

Original creator: mhansen

Original creation time: 2008-08-27 22:48:14

Assignee: burcin




---

Comment by mhansen created at 2008-08-27 22:49:51

After:


```
sage: f = maxima.function('x','sin(x)')
sage: f+x
sin(x)+x
sage: x+f
sin(x)+x
sage: type(_)
<class 'sage.interfaces.maxima.MaximaFunction'>
```



---

Comment by mhansen created at 2008-08-27 22:51:20

Patch added which fixes the issue.  This depends on #132.


---

Comment by mhansen created at 2008-08-29 00:47:11

This patch actually breaks everything in calculus.py.  I must have ran the tests without having it actually applied.


---

Comment by jason created at 2009-05-30 08:05:34

What is the status of this now?  Apparently it still is a problem in 4.0:


```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: f = maxima.function('x','sin(x)')
sage: f + x  #correct
sin(x)+x
sage: x+f    #wrong
sage0 + x
sage: 
| Sage Version 4.0, Release Date: 2009-05-29                         |
| Type notebook() for the GUI, and license() for information.        |
```



---

Comment by awebb created at 2009-10-06 12:58:15

I get an error with sage -t -long sage/symbolic/ring.pyx. I am not sure that I understand the patch as it seems to apply for both maxima and pari. Is this by intention? 


```
sage -t -long "devel/sage-myver/sage/symbolic/ring.pyx"
**********************************************************************
File "/home/adamwebb/local/sage/devel/sage-myver/sage/symbolic/ring.pyx", line 97:
    sage: SR.coerce(pari(2/5))
Exception raised:
    Traceback (most recent call last):
      File "/home/adamwebb/local/sage/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/adamwebb/local/sage/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/adamwebb/local/sage/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_7[3]>", line 1, in <module>
        SR.coerce(pari(Integer(2)/Integer(5)))###line 97:
    sage: SR.coerce(pari(2/5))
      File "parent.pyx", line 402, in sage.structure.parent.Parent.coerce (sage/structure/parent.c:4859)
      File "parent.pyx", line 429, in sage.structure.parent.Parent.coerce (sage/structure/parent.c:4806)
    TypeError: no canonical coercion from Interface to the PARI C library to Symbolic Ring
**********************************************************************
1 items had failures:
   1 of  12 in __main__.example_7
***Test Failed*** 1 failures.
```


if I put back the Pari stuff:

```
from sage.libs.pari.gen import PariInstance

elif isinstance(R, (PariInstance)): 
    return True
```

Then everything works.

Cheers,
Adam


---

Attachment

I forgot to remove the pari doctest.  It should also be removed since these parents should not have coercions going in both directions.

This is taken care of in the new patch.


---

Comment by awebb created at 2009-10-07 08:25:11

Changing status from needs_review to positive_review.


---

Comment by awebb created at 2009-10-07 08:25:11

In that case, everything looks good. A quick retest also passes. ~ Adam


---

Comment by mhansen created at 2009-10-15 05:49:38

Resolution: fixed
