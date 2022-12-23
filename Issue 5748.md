# Issue 5748: Sage 3.4.1.rc2: isinf() related doctest failure in sage/rings/infinity.py

Issue created by migration from https://trac.sagemath.org/ticket/5748

Original creator: mabshoff

Original creation time: 2009-04-11 08:13:38

Assignee: mabshoff

Notice the following on OSX and Solaris:

```
bsd:sage-3.4.1.rc2 mabshoff$ ./sage -t  devel/sage/sage/rings/infinity.py
sage -t  "devel/sage/sage/rings/infinity.py"                
**********************************************************************
File "/Users/mabshoff/sage-3.4.1.rc2/devel/sage/sage/rings/infinity.py", line 408:
    sage: CDF(-infinity)
Expected:
    -infinity
Got:
    +infinity
**********************************************************************
```

IIRC there was an analog problem in the GSL when using isinf() on OSX and Solaris due to the system's math library having a bug.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-15 04:09:42

We should use GSL to determine if the double is +infinity or -infinity. It fixes the problem on OSX for GSL's printing, etc:

```
int
gsl_isinf (const double x)
{
  int fpc = _fpclass(x);

  if (fpc == _FPCLASS_PINF)
    return +1;
  else if (fpc == _FPCLASS_NINF)
    return -1;
  else 
    return 0;
}
```

We should also take a look at sage/rings/real_double.pyx where cwitty does this clever thing:

```
        """
        cdef int isinf = gsl_isinf(self._value)
        cdef bint isnan = gsl_isnan(self._value)
```


Cheers,

Michael


---

Attachment


---

Comment by cwitty created at 2009-04-15 05:35:53

Code looks good, doctests pass.  Positive review.


---

Comment by mabshoff created at 2009-04-15 06:46:52

Resolution: fixed


---

Comment by mabshoff created at 2009-04-15 06:46:52

Merged in Sage 3.4.1.rc3.

Cheers,

Michael
