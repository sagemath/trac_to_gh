# Issue 4701: magma/sage interface -- coercion for single variable polynomials broken in some cases

Issue created by migration from https://trac.sagemath.org/ticket/4701

Original creator: was

Original creation time: 2008-12-05 00:32:30

Assignee: was

Fix this:

```
sage: R.<x> = GF(9,'a')[]
sage: magma(x)
boom
```



---

Comment by was created at 2008-12-05 01:29:18

The attached patch fixes the problem by using _ref instead of name in the polynomial ring conversion function, just like in the multivariate case.   It also fixes a bunch of spots in the output of doctests where the magma variable names _sage_[n] were hard coded, by replacing them by _sage_[...].  Finally I updated the docstring of _ref to more clearly explain what it does.  So it's basically two lines of code followed by a bunch of doctest fixes/improvements.


---

Attachment


---

Attachment

There are problems.  My referee patch includes a few failing doctests.


```
sage: R = GF(3^5, 'a') # optional - magma
sage: a = magma(R.gen()) # optional - magma
sage: a^3 # optional - magma
a^3
sage: a^3 + a # optional - magma
a^47
sage: a.sage()
a
sage: a.sage().parent()
Finite Field in a of size 3^5
sage: a.Eltseq()
[ 0, 1, 0, 0, 0 ]
sage: a.Sage()
GF(243, 'a'.replace('$.', 'x').replace('.', ''), modulus=GF(3)['a'.replace('$.', 'x').replace('.', '')]([ 1, 2, 0, 0, 0, 1 ]))(GF(3)['a'.replace('$.', 'x').replace('.', '')]([ 0, 1 ]))
```



---

Attachment

After some discussion on IRC, wstein and I decided to review this positive and open a new ticket for the referee comments.  Apply trac_4701.patch and trac_4701_part2.patch only.


---

Comment by was created at 2008-12-06 23:18:05

See #4730 -- for dealing with conversions of finite field elements.


---

Comment by mabshoff created at 2008-12-07 09:15:46

Resolution: fixed


---

Comment by mabshoff created at 2008-12-07 09:15:46

Merged trac_4701.patch and trac_4701_part2.patch only in Sage 3.2.2.alpha1.

Nick: The issues I reported stem from the referee patch which I did apply accidentally [well, I didn't read the ticket in as much detail as I should have :(] and those are already #4730 as wstein pointed out on the last comment.

Cheers,

Michael
