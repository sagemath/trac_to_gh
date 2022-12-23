# Issue 3755: [with patch; needs review] finance -- improve implementation of hurst exponent

Issue created by migration from https://trac.sagemath.org/ticket/3755

Original creator: was

Original creation time: 2008-08-01 16:07:13

Assignee: was

This improves the examples, documentation, and implementation of the code in
the finance package for computing the Hurst exponent.  The main core improvement
is that the algorithm is more sophisticated than the very naive one currently
in Sage. 


---

Attachment


---

Comment by brettnak created at 2008-08-02 01:10:20

REFEREE REPORT

* Patch installs and passes doctests.


```
sage -t --optional devel/sage-review-finance/sage/finance/time_series.pyx
         [15.7 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 15.7 seconds
```


* I found no coding errors or bugs while testing the modified functions in the notebook.


---

Comment by mabshoff created at 2008-08-03 08:59:23

So is this a positive review? It looks to me like it is.

Cheers,

Michael


---

Comment by mabshoff created at 2008-08-06 01:02:46

A positive review it is then.

Cheers,

Michael


---

Comment by mabshoff created at 2008-08-06 01:04:19

Merged in Sage 3.1.alpha1


---

Comment by mabshoff created at 2008-08-06 01:04:19

Resolution: fixed
