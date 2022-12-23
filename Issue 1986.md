# Issue 1986: Numerical noise in fast evaluation code.

Issue created by migration from https://trac.sagemath.org/ticket/1986

Original creator: jsp

Original creation time: 2008-01-30 18:16:24

Assignee: failure

Tested on Fedora 7 and 8 32 bits:

```
sage -t  devel/sage-main/sage/ext/fast_eval.pyx             **********************************************************************
File "fast_eval.pyx", line 919:
     sage: f(pi/4)
Expected:
     1.00000000000000...
Got:
     1.0
**********************************************************************
File "fast_eval.pyx", line 1013:
     sage: f(tanh(0.5))
Expected:
     0.5
Got:
     0.49999999999999994
**********************************************************************
2 items had failures:
    1 of   3 in __main__.example_29
    1 of   3 in __main__.example_38
***Test Failed*** 2 failures.
For whitespace errors, see the file .doctest_fast_eval.pyx
          [2.0 s]
exit code: 256

----------------------------------------------------------------------
The following tests failed:


         sage -t  devel/sage-main/sage/ext/fast_eval.pyx
```




---

Comment by robertwb created at 2008-01-31 07:02:14

For the 

```
Expected:
     1.00000000000000...
Got:
     1.0
```

I thought the ... would take care of it. I'd be happy to make a patch, if someone could explain how the anti-numerical noise ... works in the doctests.


---

Attachment


---

Comment by mabshoff created at 2008-02-02 08:22:32

The patch looks good to me.

Cheers,

Michael


---

Comment by mabshoff created at 2008-02-02 08:23:42

Resolution: fixed


---

Comment by mabshoff created at 2008-02-02 08:23:42

Merged in Sage 2.10.1.rc5
