# Issue 9636: Catch output from PARI in Sage

Issue created by migration from https://trac.sagemath.org/ticket/9636

Original creator: jdemeyer

Original creation time: 2010-07-29 07:56:00

Assignee: was

CC:  leif robertwb

The output from print() functions in libpari is directly written to stdout and is not caught by Sage.  For example, the following doctest fails:

```
def printhello():
    """
    sage: printhello()
    hello
    """
    pari('print("hello")')
```

It gives

```
File "/home/jdemeyer/paritest.sage", line 3:
    sage: printhello()
Expected:
    hello
Got nothing
```


Luckily, libpari provides ways to redirect the output.  There should a small Cython wrapper to direct the PARI output to sys.stdout.write().

I will try to implement this (using #9343 as starting point). -- Jeroen Demeyer


---

Comment by jdemeyer created at 2010-08-14 20:25:53

Changing status from new to needs_review.


---

Attachment


```
cdef extern: 
    PariOUT defaultOut 
    PariOUT defaultErr 

```

should perhaps migrate to `sage/libs/pari/decl.pxi`, too.

*Positive review* from me though. Robert, anything to complain about?

----

I wonder when Cython will support `const`...


---

Comment by leif created at 2010-09-07 11:18:23

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-09-10 10:44:51

Resolution: fixed
