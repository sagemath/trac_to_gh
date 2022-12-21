# Issue 1531: Sage 2.9.rc2: doctest failure sage/calculus/calculus.py

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2007-12-16 02:08:14

Assignee: mabshoff


```
File "calculus.py", line 6144:
    sage: maxima(f(sqrt(2), theta+3))
Expected:
    'Gamma(theta+3,sqrt(2))
Got:
    'Gamma(sqrt(2),theta+3)
```



---

Comment by mabshoff created at 2007-12-16 02:08:53


```
[02:58] <wstein|packing> 'Gamma(sqrt(2),theta+3) is right and 'Gamma(theta+3,sqrt(2)) is wrong!
[02:58] <wstein|packing> so change the doctest :-0
```



---

Comment by mabshoff created at 2007-12-16 02:09:07

Changing status from new to assigned.


---

Comment by mabshoff created at 2007-12-16 03:03:23

Resolution: fixed


---

Comment by mabshoff created at 2007-12-16 03:03:23

Merged in 2.9.rc3.
