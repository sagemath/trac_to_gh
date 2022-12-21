# Issue 5782: Failure of __pow__ in RDF for noninteger powers of  zero

Issue created by migration from Trac.

Original creator: kbaker

Original creation time: 2009-04-14 00:00:05

Assignee: somebody

Keywords: RDF, __pow__, zero

Positive noninteger powers of RDF(0) give nan rather than zero:

```
  sage: RDF(0)^.5
  nan

  sage: RDF(0)^(1/2)
  nan
```


In contrast, noninteger powers of CDF(0) have the correct value:

```
  sage: CDF(0)^.5
  0

  sage: CDF(0)^(1/2)
  0
```



---

Comment by mabshoff created at 2009-04-16 03:04:54

Hmm, we have some trivial doctest failures:

```
sage -t -long "devel/sage/sage/rings/real_double.pyx"       
**********************************************************************
File "/scratch/mabshoff/sage-3.4.1.rc3/devel/sage/sage/rings/real_double.pyx", line 1543:
    sage: RDF(0)^.5
Expected:
    0
Got:
    0.0
**********************************************************************
File "/scratch/mabshoff/sage-3.4.1.rc3/devel/sage/sage/rings/real_double.pyx", line 1545:
    sage: RDF(0)^(1/2)
Expected:
    0
Got:
    0.0
**********************************************************************
```


I think other than that this is good to go.

Cheers,

Michael


---

Attachment


---

Comment by robertwb created at 2009-04-16 04:59:10

Doh! Patch updated.


---

Comment by mabshoff created at 2009-04-16 07:24:34

Second patch looks good to me. Positive review. It also passes doctests :)

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-16 07:24:49

Merged in Sage 3.4.1.rc3.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-16 07:24:49

Resolution: fixed


---

Comment by jason created at 2009-04-16 17:33:35

Does this fix #5785?


---

Comment by mabshoff created at 2009-04-16 21:20:13

Replying to [comment:6 jason]:
> Does this fix #5785?

Yes.

Cheers,

Michael
