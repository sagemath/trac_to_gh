# Issue 2225: sage-2.10.2.alpha1 -- genus2reduction is now completely broken (maybe caused by new spkg with makefile?)

Issue created by migration from https://trac.sagemath.org/ticket/2225

Original creator: was

Original creation time: 2008-02-20 06:58:10

Assignee: was

I think Tim (the Debian guy) wrote a makefile for genus2reduction.  He possibly messed something up, since now it's completely broken:


```
sage -t  devel/sage-main/sage/interfaces/genus2reduction.py **********************************************************************
File "genus2reduction.py", line 197:
    sage: R = genus2reduction(x^3 - 2*x^2 - 2*x + 1, -5*x^5)
Exception raised:
    Traceback (most recent call last):
      File "/Users/was/build/sage-2.10.2.alpha1/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_2[1]>", line 1, in <module>
        R = genus2reduction(x**Integer(3) - Integer(2)*x**Integer(2) - Integer(2)*x + Integer(1), -Integer(5)*x**Integer(5))###line 197:
    sage: R = genus2reduction(x^3 - 2*x^2 - 2*x + 1, -5*x^5)
      File "/Users/was/build/sage-2.10.2.alpha1/local/lib/python2.5/site-packages/sage/interfaces/genus2reduction.py", line 358, in __call__
        s, Q, P = self.raw(Q, P)
      File "/Users/was/build/sage-2.10.2.alpha1/local/lib/python2.5/site-packages/sage/interfaces/genus2reduction.py", line 349, in raw
        raise ValueError, "error in input; possibly singular curve? (Q=%s, P=%s)"%(Q,P)
    ValueError: error in input; possibly singular curve? (Q=x^3 - 2*x^2 - 2*x + 1, P=-5*x^5)
**********************************************************************
File "genus2reduction.py", line 198:
    sage: R.conductor
Exception raised:
    Traceback (most recent call last):
      File "/Users/was/build/sage-2.10.2.alpha1/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_2[2]>", line 1, in <module>
        R.conductor###line 198:
    sage: R.conductor
    NameError: name 'R' is not defined
**********************************************************************
File "genus2reduction.py", line 200:
    sage: factor(R.conductor)
Exception raised:
    Traceback (most recent call last):
      File "/Users/was/build/sage-2.10.2.alpha1/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_2[3]>", line 1, in <module>
        factor(R.conductor)###line 200:
    sage: factor(R.conductor)
    NameError: name 'R' is not defined
*
...
```



---

Comment by mabshoff created at 2008-02-20 14:11:26

Changing assignee from was to mabshoff.


---

Comment by mabshoff created at 2008-02-20 14:11:26

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-02-20 14:11:26

I will look into this. Make sure to close #2175 once we have resolved this issue.

Cheers,

Michael


---

Comment by mabshoff created at 2008-02-21 19:10:04

New, working spkg by was at

http://sage.math.washington.edu/home/was/patches/genus2reduction-0.3.p2.spkg

Cheers,

Michael


---

Comment by mabshoff created at 2008-02-21 19:16:50

The spkg looks good. I added a `.hgignore` and also corrected some small issues in SPKG.txt

Cheers,

Michael


---

Comment by mabshoff created at 2008-02-21 19:18:19

Resolution: fixed


---

Comment by mabshoff created at 2008-02-21 19:18:19

Merged in Sage 2.10.2.rc0
