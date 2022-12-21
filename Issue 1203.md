# Issue 1203: 2.8.13.alpha0: flint doctest failures

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2007-11-18 23:12:10

Assignee: failure


```
sage -t  devel/sage-main/sage/libs/flint/fmpz_poly.pyx      **********************************************************************
File "fmpz_poly.pyx", line 271:
    sage: g / f
Exception raised:
    Traceback (most recent call last):
      File "/tmp/Work-mabshoff/release-cycles/sage-2.8.13.alpha0/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_13[3]>", line 1, in <module>
        g / f###line 271:
    sage: g / f
    TypeError: unsupported operand type(s) for /: 'sage.libs.flint.fmpz_poly.Fmpz_poly' and 'sage.libs.flint.fmpz_poly.Fmpz_poly'
**********************************************************************
```



---

Attachment

fix doctest failure


---

Comment by mabshoff created at 2007-11-20 09:41:19

Nobody complained about the patch. I also updated the description to reflect the "//". With the updated flint.spkg from 

http://sage.math.washington.edu/home/mabshoff/flint-0.9-r1072.spkg

it compiles on OSX 10.5 and passes testall on OSX 10.5 and sage.math.

Cheers,

Michael


---

Comment by mabshoff created at 2007-11-20 09:41:30

Resolution: fixed


---

Comment by mabshoff created at 2007-11-20 09:41:30

Merged in 2.8.13.rc0.
