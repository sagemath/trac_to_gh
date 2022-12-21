# Issue 1292: bug in polynomial root finding mod n

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-11-27 15:18:21

Assignee: somebody

This was reported by michael to sage-devel on Nov 27, 2007.   It's a genuine
bug which gives incorrect mathematical results (hence the critical marking). 


```
R=IntegerModRing(3^2)
A=PolynomialRing(R,'y')
y=A.gen()
f=10*y^2 - y^3 - 9;
f.roots(multiplicities=false)
///
[1, 0]
```



```
print [k for k in R if f(k) == 0]
///
[0, 1, 3, 6]
```




---

Comment by cwitty created at 2007-11-27 15:54:15

In this case, the roots method tries to factor f and extract roots from the factorization:

```
sage: factor(f)
(8) * (y + 8) * y^2
```

I'm told that we need to check that the coefficient ring forms a unique factorization domain before using this strategy, but I don't know how to check that in Sage.


---

Comment by was created at 2007-11-27 16:19:40

In this particular case, roots() is done by factoring modulo n then extracting
the roots from the linear factors.  That algorithm makes no sense directly
in case of a non-integral domain (unique factorization is irrelevant -- what
matters if that a product is 0 then at least 1 factor is). Use {{{R.is_integral_domain()}.



```
sage: f.factor()
(8) * (y + 8) * y^2
```


There is presumably another algorithm for finding roots that works given
a factorization even over a non-integral domain.  Probably we should
list all zero-divisor products a*b = 0, then for each factor `g_i(x)` of the
polynomial, find all y such `g_1(y) = a, g_2(y) = b`.   Also, worry about the
8 factor out front!

For now a quick hack would be to just do a stupid for loop to find all roots
in the non-integral-domain case -- at least that would be mathematically correct.


---

Comment by cwitty created at 2007-11-27 16:37:44

Changing assignee from somebody to cwitty.


---

Comment by mhansen created at 2007-11-27 20:50:45

For the IntegerModRing case, we could probably do something with http://www.shoup.net/ntl/doc/ZZ_pXFactoring.txt .


---

Attachment

I've attached a patch that only does root finding by factorization if the coefficient ring is an integral domain; so for this problem, it uses enumeration instead, and does find all four roots.  I think that using a non-stupid root-finding algorithm here should be a separate ticket; that's an enhancement request, instead of a critical bug fix.

NOTE THAT THIS PATCH REQUIRES THAT PATCHES FROM #1270 AND #1273 ARE ALREADY APPLIED.  This is just because #1273 happens to touch the same paragraph in the docstring of roots() that I needed to change for this patch, so I had to choose between depending on #1273 or conflicting with #1273.  Since I hope and expect that #1273 will be applied for 2.8.15, I chose to depend on it; if #1273 is rejected, I'll upload a modified patch that doesn't depend on #1273.


---

Comment by mhansen created at 2007-12-02 05:10:25

Looks good to me.


---

Comment by mabshoff created at 2007-12-02 05:57:42

Resolution: fixed


---

Comment by mabshoff created at 2007-12-02 05:57:42

Merged in 2.8.15.alpha2.
