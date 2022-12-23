# Issue 2057: followup to #1983 -- 0^0 for 0 a rational

Issue created by migration from https://trac.sagemath.org/ticket/2057

Original creator: was

Original creation time: 2008-02-05 15:25:10

Assignee: somebody

Before patch:

```

sage: (0/1) ^ (0/1)

---------------------------------------------------------------------------
<type 'exceptions.ArithmeticError'>       Traceback (most recent call last)

/home/was/<ipython console> in <module>()

/home/was/rational.pyx in sage.rings.rational.Rational.__pow__()

<type 'exceptions.ArithmeticError'>: 0^0 is undefined.
```


After patch:

```
sage: (0/1) ^ (0/1)
1
sage: type(_)
<type 'sage.rings.rational.Rational'>
```



---

Attachment


---

Comment by mhansen created at 2008-02-06 04:03:10

Looks good to me.


---

Comment by mabshoff created at 2008-02-07 05:15:08

Merged in Sage 2.l0.2.alpha0


---

Comment by mabshoff created at 2008-02-07 05:15:08

Resolution: fixed
