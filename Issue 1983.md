# Issue 1983: [with patch; needs review] change 0^0, for 0 a Sage integer, to evaluate to 1 for consistency with Python, PARI, Magma, Maple, MPFR, GMP, etc.

Issue created by migration from https://trac.sagemath.org/ticket/1983

Original creator: was

Original creation time: 2008-01-30 13:35:24

Assignee: somebody

As justification that this is for *consistency*, everybody defines 0^0 to be 1, except Mathematica:


```

sage: gp('0^0')
1
sage: magma('0^0')
1
sage: mathematica('0^0')
...
Mathematica ERROR:
	                                        0
Power::indet: Indeterminate expression 0  encountered.
sage: maple('0^0')
1
sage: int(0)^int(0)
1
sage: float(0)^float(0)
1.0
sage: 0.0^0.0
1.00000000000000
```



---

Attachment


---

Comment by jkantor created at 2008-02-01 05:00:14

This works as described.


---

Comment by mabshoff created at 2008-02-01 05:02:43

Resolution: fixed


---

Comment by mabshoff created at 2008-02-01 05:02:43

Merged in Sage 2.10.1.rc4
