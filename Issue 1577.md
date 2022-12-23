# Issue 1577: .coefficients() and .monomials() differ in order in multivariate polynomial rings

Issue created by migration from https://trac.sagemath.org/ticket/1577

Original creator: ncalexan

Original creation time: 2007-12-21 01:34:55

Assignee: malb

CC:  jbmohler

Keywords: multi polynomial rings coefficients monomials

A small annoyance -- the ordering on the lists below is different:

```
sage: R.<fx,fy,gx,gy> = ZZ[]
sage: F = ((fx*gy - fy*gx)^3)
sage: F
-1*fy^3*gx^3 + 3*fx*fy^2*gx^2*gy - 3*fx^2*fy*gx*gy^2 + fx^3*gy^3
sage: F.monomials()
[fx^2*fy*gx*gy^2, fy^3*gx^3, fx*fy^2*gx^2*gy, fx^3*gy^3]
sage: F.coefficients()
[-3, -1, 3, 1]
```


`F.coefficients?` says
"The order the coefficients appear in depends on the ordering used on self's parent."
`F.monomials?` says
"Returns list of all monomials which occure in this multivariate polynomial."

I think the latter should be changed.


---

Comment by rlm created at 2007-12-21 01:47:26

Looks like monomials and coefficients line up, but it's not in the same order as they print?


---

Comment by ncalexan created at 2007-12-21 04:19:14

While we're here:

The elements of list() don't have the correct types -- the final line should be a libsingular poly as well:

```
sage: R.<x, y> = QQ[]
sage: (x + y).monomials()
[x, y]
sage: type((x + y).monomials()[0])
<type 'sage.rings.polynomial.multi_polynomial_libsingular.MPolynomial_libsingular'>
sage: list(x + y)[0]
(1, x)
sage: type(list(x + y)[0][-1])
<class 'sage.rings.polynomial.multi_polynomial_element.MPolynomial_polydict'>
```



---

Attachment


---

Comment by malb created at 2008-01-06 17:09:58

Changing status from new to assigned.


---

Comment by jbmohler created at 2008-01-10 10:45:19

I entirely agree with the actual code of this patch.  One of the doc-string changes is not representative though -- we are not sorting largest to smallest (whatever that might mean for a monomial).

I think that ZZ mpolys doc-string for monomials should read 

```
        Return the list of monomials in self. The returned list is
        ordered by the term ordering of self.parent().
```

just like for QQ mpolys.


---

Comment by jbmohler created at 2008-01-10 10:47:52

Oh, perhaps I should add that I doc-tested 'sage/rings' and verified that the patch fixes the original bug as well as the bug mentioned in the comments.


---

Comment by malb created at 2008-01-10 10:51:45

I am okay with changing the docstring but want to point out that "from largest to smallest" is well defined for a multivariate polynomial in a given ring. It means to sort according to the monomial ordering of the ring (which is a property of that ring) but in _descending_ order. This fact is not clear -- though probably 'natural' -- when writing "The returned list is ordered by the term ordering of self.parent()"


---

Attachment

Joel's suggested change is in `trac_1577_comment_4.patch`.


---

Comment by malb created at 2008-01-16 15:40:49

jbmohler can you verify this is correct now?


---

Comment by ncalexan created at 2008-01-20 06:48:20

I reported this bug, and I approved this patch!  Apply.


---

Comment by mabshoff created at 2008-01-21 05:47:04

Merged both patches in Sage 2.10.1.alpha1


---

Comment by mabshoff created at 2008-01-21 05:47:04

Resolution: fixed
