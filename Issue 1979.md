# Issue 1979: doctest fall out from #740 in tut.tex

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-01-30 05:10:33

Assignee: failure

The following happens while doctesting `tut.tex`:

```
sage -t  tut.tex
**********************************************************************
File "tut.py", line 1676:
    : EllipticCurve(5)
Expected:
    Elliptic Curve defined by y^2 + x*y  = x^3 + 36/1723*x + 1/1723
                over Rational Field
Got:
    Elliptic Curve defined by y^2  = x^3 + 25845*x - 29687290 over Rational Field
**********************************************************************
File "tut.py", line 1722:
    : factor(F.conductor())
Expected:
    2^6 * 37
Got:
    2^6 * 3^2 * 37^2
**********************************************************************
File "tut.py", line 1730:
    : G = F.quadratic_twist(2); G
Expected:
    Elliptic Curve defined by y^2 + y = x^3 - x over Rational Field
Got:
    Elliptic Curve defined by y^2 + y = x^3 - 12321*x - 341908 over Rational Field
**********************************************************************
File "tut.py", line 1732:
    : G.conductor()
Expected:
    37
Got:
    12321
**********************************************************************
```

William says:

```
[04:56] <mabshoff> william_stein: #740 seems to create different results in various places, i.e. doc test failures.
[04:56] <william_stein> hmmm
[04:57] <mabshoff> File "tut.py", line 1676:
[04:57] <mabshoff>     : EllipticCurve(5)
[04:57] <mabshoff> Expected:
[04:57] <mabshoff>     Elliptic Curve defined by y^2 + x*y  = x^3 + 36/1723*x + 1/1723
[04:57] <mabshoff>                 over Rational Field
[04:57] <mabshoff> Got:
[04:57] <mabshoff>     Elliptic Curve defined by y^2  = x^3 + 25845*x - 29687290 over Rational Field
[04:57] <william_stein> mabshoff -- not surprising.
[04:57] <william_stein> NOBODY has doctested testall after applying that.
[04:57] <mabshoff> ok
[04:57] <william_stein> The new output in tut.py is right, by the way.
[04:57] <mabshoff> :)
[04:57] <william_stein> It's a different curve with that j-invariant -- a better one.
```

Patch coming up.

Cheers,

Michael


---

Attachment


---

Comment by mabshoff created at 2008-01-30 09:42:09

Merged in Sage 2.10.1.rc3. This ticket should be reopened if it turns out that the fix is incorrect.


---

Comment by mabshoff created at 2008-01-30 09:42:09

Resolution: fixed


---

Comment by was created at 2008-01-30 13:05:11

Looks good to me (and Cremona said the same in email).


---

Attachment

This is a corrected patch of my patch, so I am reverting my patch an applying this one


---

Comment by mabshoff created at 2008-01-30 15:25:47

Merged ec740.patch in Sage 2.10.1.rc4 after reverting the original patch
