# Issue 2717: maxima expect interface synchronization not sufficiently robust

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-03-29 16:27:36

Assignee: was

It is still possible to very occassionaly throw off the Maxima synchronization, maybe during parallel doctesting (?).  E.g.,

```
sage -t  devel/sage-main/sage/calculus/functional.py        **********************************************************************
File "functional.py", line 301:
    sage: limit((tan(sin(x)) - sin(tan(x)))/x^7, taylor=True, x=0)
Expected:
    1/30
Got:
    1820214126
**********************************************************************
1 items had failures:
   1 of   7 in __main__.example_4
***Test Failed*** 1 failures.
For whitespace errors
```


The above is particularly bad since you can't tell something went wrong -- you just
get a wrong number out.  The point of this ticket isn't to fix the whole problem.
Instead, change the synchronization marker in maxima.py from being a single number
to a string such as 

    __SAGE_SYNCHRO_MARKER_1820214126

so that instead of people being confused by a wrong answer, it will be
crystal clear that something went wrong. 

This will likely be nearly trivial to implement. 


---

Attachment


---

Comment by mabshoff created at 2008-03-29 19:28:57

Looks good to me. Second review appreciated.

Cheers,

Michael


---

Comment by mhansen created at 2008-03-29 20:38:48

Looks good to me.


---

Comment by mabshoff created at 2008-03-29 20:50:57

Merged in Sage 2.11.rc0


---

Comment by mabshoff created at 2008-03-29 20:50:57

Resolution: fixed
