# Issue 3575: [with patch; needs review] delete random crap from the bottom of complex_double.pyx

Issue created by migration from https://trac.sagemath.org/ticket/3575

Original creator: was

Original creation time: 2008-07-06 22:04:22

Assignee: cwitty




---

Attachment


---

Comment by mabshoff created at 2008-07-07 01:45:22

In my merge tree somebody else already beat you to it and deleted the random crap:

```
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.0.4.alpha2/devel/sage$ tail -n 10 sage/rings/complex_double.pyx
        True    
    """
    return _CDF   

from sage.misc.parser import Parser
cdef cdf_parser = Parser(float, float,  {"I" : _CDF.gen(), "i" : _CDF.gen()})



#####
```


Cheers,

Michael


---

Comment by mabshoff created at 2008-07-07 01:45:22

Resolution: fixed
