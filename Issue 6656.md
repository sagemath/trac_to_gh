# Issue 6656: [with patch, needs review] fix latex method for laurent series element

Issue created by migration from Trac.

Original creator: jhpalmieri

Original creation time: 2009-07-29 19:05:01

Assignee: jhpalmieri

In the [Sage Notebook Bugreports](http://spreadsheets.google.com/pub?key=pCwvGVwSMxTzT6E2xNdo5fA), there is a report of an error with typesetting Laurent series elements:

```
sage: R.<a,b>=PolynomialRing(QQ)
sage: T.<x>=LaurentSeriesRing(R)
sage: latex(a*x+b*x)
'a + bx'
```

It ought to be (a+b)x, but the parentheses are missing.  The attached patch should fix this.



---

Attachment

reviewer patch


---

Comment by mvngu created at 2009-08-03 01:47:56

Before the patch:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: R.<a,b> = PolynomialRing(QQ)
sage: T.<x> = LaurentSeriesRing(R)
sage: y = a*x + b*x
sage: y._latex_()
'a + bx'
sage: latex(y)
a + bx
```

After the patch:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
**********************************************************************
*                                                                    *
* Warning: this is a prerelease version, and it may be unstable.     *
*                                                                    *
**********************************************************************
sage: R.<a,b> = PolynomialRing(QQ)
sage: T.<x> = LaurentSeriesRing(R)
sage: y = a*x + b*x
sage: y._latex_()
'\\left(a + b\\right)x'
sage: latex(y)
\left(a + b\right)x
```

Note that one can also obtain the LaTeX representation of an object through the `latex()` function. So I'm attaching a patch on top of John's that also calls that function. If John is OK with the patch `trac_6656-reviewer.patch`, then the ticket has positive review from me.


---

Comment by jhpalmieri created at 2009-08-03 02:13:12

Sure, looks fine to me. Tests still pass with the reviewer patch.


---

Comment by mvngu created at 2009-08-03 02:32:03

Resolution: fixed


---

Comment by mvngu created at 2009-08-03 02:32:03

Merged both patches.
