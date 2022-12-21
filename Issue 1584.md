# Issue 1584: calculus.py doctest failure on Fermat

Issue created by migration from Trac.

Original creator: rlm

Original creation time: 2007-12-21 20:38:26

Assignee: was

FERMAT -- OSX 10.4 PowerPC


```
sage -t  devel/sage-main/sage/calculus/calculus.py
**********************************************************************
File "calculus.py", line 2005:
    sage: f = f.nintegral(x,0,1,1e-14)
Expected:
    Traceback (most recent call last):
    ...
    ValueError: Maxima (via quadpack) cannot compute the integral to
that precision
Got:
    Traceback (most recent call last):
      File "/Users/was/build/sage-2.9.1.alpha2/local/lib/python2.5/doctest.py",
line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_40[1]>", line 1, in <module>
        f = f.nintegral(x,Integer(0),Integer(1),RealNumber('1e-14'))###line
2005:
    sage: f = f.nintegral(x,0,1,1e-14)
      File "/Users/was/build/sage-2.9.1.alpha2/local/lib/python2.5/site-packages/sage/calculus/calculus.py",
line 2068, in nintegral
        raise TypeError, err
    TypeError: Error executing code in Maxima
    CODE:
        sage356 : quad_qags(sage6,sage6,sage352,sage353,sage354,sage355)$
    Maxima ERROR:
        ^M
    Maxima encountered a Lisp error:^M
    ^M
     ^M
    WRITE-CHAR on #<CLOSED OUTPUT BUFFERED FILE-STREAM CHARACTER
#P"/dev/fd/1"> is illegal^M
    ^M
    Automatically continuing.^M
    To reenable the Lisp debugger set *debugger-hook* to nil.^M
    <BLANKLINE>
**********************************************************************
1 items had failures:
   1 of  14 in __main__.example_40
***Test Failed*** 1 failures.
For whitespace errors, see the file .doctest_calculus.py
         [61.0 s]
```

----- This is related to Mike Hansen's precision detection patch -- it
doesn't work right on
OSX PPC, evidently. 


---

Attachment

+1


---

Comment by rlm created at 2007-12-21 22:09:07

merged in 2.9.1 alpha3


---

Comment by rlm created at 2007-12-21 22:09:07

Resolution: fixed
