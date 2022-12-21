# Issue 6888: sage-env complain about bad SAGE_ROOT environment variable with no reason

Issue created by migration from Trac.

Original creator: sbarthelemy

Original creation time: 2009-09-04 12:59:01

Assignee: tbd

the $SAGE_ROOT/local/bin/sage-env has 2 small flaws.

1) the script prints the following message: 

```
    You must set the SAGE_ROOT environment variable or
    run this script from the SAGE_ROOT or
    SAGE_ROOT/local/bin/ directory.
```

even if SAGE_ROOT is set correctly.

2) if SAGE_ROOT is set to a wrong path, it doesn't stop,

The attached patch fixes them. 

I am not a shell expert, so please test it.




---

Attachment


---

Comment by timdumol created at 2009-09-22 13:30:06

Looks good. Good job.


---

Comment by mhansen created at 2009-10-15 09:40:32

Resolution: fixed


---

Comment by chapoton created at 2017-07-19 09:06:12

full author name
