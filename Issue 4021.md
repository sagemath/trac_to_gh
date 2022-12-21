# Issue 4021: [with patch, needs review] MPolynomial_libsingular over ZZ

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2008-08-31 17:08:10

Assignee: malb

CC:  was

Keywords: libsingular, singular, ZZ, multivariate

There it is.


---

Attachment

the attached patch depends on #686


---

Comment by malb created at 2008-09-01 12:40:07

On [sage-devel] Oliver Wienand (author of the upcoming Singular implementation for GBs over rings) wrote:

> I have just glimpsed over the code. But maybe it is worth stating in
> the comments, that the reduce impl. only returns unqiue answer against
> strong Gröbner basis.

> Gröbner basis G of I <=> the leading ideal of G generates all leading
> terms of I
> strong % of I <=> for every leading term t of I there exists an
> element g of G, such that the leading term of g divides t.

> (leading terms means coef * product of variables)

> Otherwise the reduce code shown in
> http://trac.sagemath.org/sage_trac/attachment/ticket/4021/mpolynomial_libsingular_zz.patch
> looks fine.


---

Comment by malb created at 2008-09-20 15:46:54

Changing status from new to assigned.


---

Attachment

The second patch addresses the review of Oliver Wienand on [sage-devel]:

```
I have just glimpsed over the code. But maybe it is worth stating in
the comments, that the reduce impl. only returns unqiue answer against
strong Gröbner basis.

Gröbner basis G of I <=> the leading ideal of G generates all leading
terms of I
strong % of I <=> for every leading term t of I there exists an
element g of G, such that the leading term of g divides t.

(leading terms meaans coef * product of variables)

Otherwise the reduce code shown in
http://trac.sagemath.org/sage_trac/attachment/ticket/4021/mpolynomial_libsingular_zz.patch
looks fine.
```



---

Attachment

Applies cleanly on 3.1.3.alpha1 + the patch at #686, except for a reject in rings/polynomial/multi_polynomial_libsingular.pyx, which can be ignored.

There is a tiny doctest failure in rings/polynomial/multi_polynomial_element.py which is fixed by the attached patch.


---

Comment by mabshoff created at 2008-09-28 18:15:30

Merged all three patches in Sage 3.1.3.alpha2


---

Comment by mabshoff created at 2008-09-28 19:22:43

Resolution: fixed


---

Comment by mabshoff created at 2008-09-28 19:22:43

Merged all three patches in Sage 3.1.3.alpha2 and this time I closed the ticket :)
