# Issue 2627: Integer(abs(gamma(n+1))) is not always equal to factorial(n) for n a positive integer

Issue created by migration from Trac.

Original creator: ddrake

Original creation time: 2008-03-21 06:59:01

Assignee: cwitty

Keywords: gamma function, factorial

`Integer(abs(gamma(n+1))) - factorial(n)` should be zero for all positive integers, but on 2.10.3, I get:


```
sage: [ Integer(abs(gamma(n+1))) - factorial(n) for n in range(20, 30) ]

[0,
 0,
 0,
 1572864,
 -29360128,
 71303168,
 14738784256,
 -220528115712,
 11417398804480,
 -55923527647232]
```


I'm guessing this is due to some numerical noise. There should be some type-checking done in the gamma function.

I would also like to see, for instance, gamma(1/2) return sqrt(pi) instead of a floating point number, although I think the above issue is more pressing and easier to deal with.


---

Comment by mhansen created at 2008-03-21 07:04:54

The right fix would probably be to add a .gamma() method to the integers, and then also make the generic gamma use interval arithmetic.


---

Attachment


```
sage: sage: [ Integer(abs(gamma(n+1))) - factorial(n) for n in range(20, 30) ]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
sage: gamma(1/2)
sqrt(pi)
sage: gamma(-101/2)
-2251799813685248*sqrt(pi)/275264606114823679801052037785492781962370429385126144787167211167753726318359375
```



---

Comment by ddrake created at 2008-03-27 08:29:09

The patch applies cleanly and works as advertised. I tested with integers as large as 500000 and had no troubles. The half-integer and multifactorial stuff works too. Positive review for functionality; I'm not familiar enough with the Pyrex code to review that, although it looks pretty straightforward.

The doctests also pass for me.


---

Comment by mabshoff created at 2008-03-27 08:59:31

I looked at the Cython code.  Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-03-27 09:00:29

Merged in Sage 2.11.alpha2


---

Comment by mabshoff created at 2008-03-27 09:00:29

Resolution: fixed


---

Comment by mabshoff created at 2008-03-27 09:32:40

The is one doctest failure:

```
sage -t  devel/sage-main/sage/functions/transcendental.py
**********************************************************************
File "transcendental.py", line 102:
    sage: gamma(6)
Expected:
    120.000000000000
Got:
    120
**********************************************************************
```

Trivial fix coming up.

Cheers,

Michael


---

Attachment

Merged trac_2627_doctest-fix.patch in Sage 2.11.alpha2
