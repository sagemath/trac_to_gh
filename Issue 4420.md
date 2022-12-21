# Issue 4420: [with patch, needs review] sort Gröbner bases

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2008-11-02 01:41:57

Assignee: malb

To make the answer returned by `Ideal.groebner_basis` truely canonical, sort it. The attach patch also fixes some doctest failures in `rings/polynomial` and replaces #4035.


---

Attachment


---

Comment by mabshoff created at 2008-11-02 01:45:24

The hunk from sage/rings/polynomial/multi_polynomial.pyx will conflict since it was already patched in #4385.

I am reviewing the remainder of the patch now.

Cheers,

Michael


---

Comment by mabshoff created at 2008-11-02 02:12:53

The patch needs fixes for doc.text, const.tex and tut.tex:

```
sage -t -long devel/doc/tut/tut.tex
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.2.alpha3/tmp/tut.py", line 2240:
    : V.irreducible_components()
Expected:
        [
        Closed subscheme of Affine Space of dimension 2 over Rational Field defined by:
          y
          x - 1,
        Closed subscheme of Affine Space of dimension 2 over Rational Field defined by:
          y - 1
          x,
        Closed subscheme of Affine Space of dimension 2 over Rational Field defined by:
          x + y + 2
          2*y^2 + 4*y + 3
        ]
Got:
    [
    Closed subscheme of Affine Space of dimension 2 over Rational Field defined by:
      y - 1
      x,
    Closed subscheme of Affine Space of dimension 2 over Rational Field defined by:
      y
      x - 1,
    Closed subscheme of Affine Space of dimension 2 over Rational Field defined by:
      x + y + 2
      2*y^2 + 4*y + 3
    ]
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.2.alpha3/tmp/tut.py", line 1654:
    : B = I.groebner_basis(); B
Expected:
    [x^2*y^2, x^6]
Got:
    [x^6, x^2*y^2]
**********************************************************************
2 items had failures:
   1 of  10 in __main__.example_100
   1 of  12 in __main__.example_78
***Test Failed*** 2 failures.
For whitespace errors, see the file /scratch/mabshoff/release-cycle/sage-3.2.alpha3/tmp/.doctest_tut.py

	 [23.2 s]
sage -t -long devel/doc/const/const.tex
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.2.alpha3/tmp/const.py", line 2847:
    : B = I.groebner_basis(); B
Expected:
    [b^2 - 1, a - 2*b]
Got:
    [a - 2*b, b^2 - 1]
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.2.alpha3/tmp/const.py", line 2864:
    : B = I.groebner_basis(); B
Expected:
    [c^2*d^6 - c^2*d^2 - d^4 + 1,
     c^3*d^2 + c^2*d^3 - c - d,
     b*d^4 - b + d^5 - d,
     b*c - b*d + c^2*d^4 + c*d - 2*d^2,
     b^2 + 2*b*d + d^2,
     a + b + c + d]
Got:
    [a + b + c + d, b^2 + 2*b*d + d^2, b*c - b*d + c^2*d^4 + c*d - 2*d^2, b*d^4 - b + d^5 - d, c^3*d^2 + c^2*d^3 - c - d, c^2*d^6 - c^2*d^2 - d^4 + 1]
**********************************************************************
2 items had failures:
   1 of   6 in __main__.example_95
   1 of   6 in __main__.example_96
***Test Failed*** 2 failures.
For whitespace errors, see the file /scratch/mabshoff/release-cycle/sage-3.2.alpha3/tmp/.doctest_const.py

	 [30.0 s]
```

Trivial patch coming up unless malb beats me to it :)

Cheers,

Michael


---

Comment by mabshoff created at 2008-11-02 02:18:33

Another odd thing: With -t -long the tests pass after applying this patch, but with -t -long -optional I reproducibly get the following failure:

```
sage -t -optional -long devel/sage/sage/rings/polynomial/multi_polynomial_ideal.py
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.1.3.final/tmp/multi_polynomial_ideal.py", line 144:
    sage: I.groebner_basis()
Expected:
    [x + y + z, y^2 + y + 23234, y*z + y + 26532, 2*y + 158864, z^2 + 17223, 2*z + 41856, 164878]
Got:
    [x + y + z, y^2 + y + 23234, y*z + y + 26532, 2*y - 6014, z^2 + 17223, 2*z + 41856, 164878]
```

Also: the surf doctests fail since surf was removed from the singular.spkg. We might want to package the surf jars into an optinonal spkg.

Cheers,

Michael


---

Comment by malb created at 2008-11-02 02:31:58

Replying to [comment:3 mabshoff]:
> Expected:
>     [x + y + z, y^2 + y + 23234, y*z + y + 26532, 2*y + 158864, z^2 + 17223, 2*z + 41856, 164878]
> Got:
>     [x + y + z, y^2 + y + 23234, y*z + y + 26532, 2*y - 6014, z^2 + 17223, 2*z + 41856, 164878]

That's the difference between M2 and the native/naive GB implementation of ZZ. IIRC the patch does not improve or worsen the situation (i.e. the same doctest failed before). Both answers are correct and that mess should be dealt with eventually.


---

Comment by mabshoff created at 2008-11-02 02:36:32

The ticket for the new optional surf.spkg is now #4421. I am also not working on fixing the documentation doctests since I am getting distracted by something else :(

Cheers,

Michael


---

Comment by mabshoff created at 2008-11-02 02:38:34

Replying to [comment:4 malb]:

> That's the difference between M2 and the native/naive GB implementation of ZZ. IIRC the patch does not improve or worsen the situation (i.e. the same doctest failed before). Both answers are correct and that mess should be dealt with eventually.

Does the GB computation over ZZ default to M2 if it is available? I guess in that case we should use some optional parameter to select the default one and make the one selecting the M2 engine optional. Once the documentation is fixed I will give this patch a positive review despite the M2 issue since as is due to the missing surf bits for Singular we have optional doctest failures. As you pointed out we can deal with that later.

Cheers,

Michael


---

Attachment

The attached patch fixes the doctest failures in `tut.tex` and `const.tex`


---

Comment by mabshoff created at 2008-11-02 16:14:36

Positive review.

Mike: Note that sort_gb_doc.patch fixes doctests in the documentation.

Cheers,

Michael


---

Comment by mabshoff created at 2008-11-02 16:15:05

Resolution: fixed


---

Comment by mabshoff created at 2008-11-02 16:15:05

Merged in Sage 3.2.alpha3
