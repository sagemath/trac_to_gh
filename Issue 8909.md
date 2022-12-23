# Issue 8909: Coercion from Gap to cyclotomic fields; usage of GAP to improve computation of invariant rings

Issue created by migration from https://trac.sagemath.org/ticket/8909

Original creator: SimonKing

Original creation time: 2010-05-07 10:58:12

Assignee: was

CC:  wdj

Keywords: gap, cyclotomic fields, invariant rings

When coercing from GAP to a cyclotomic field, it was assumed that the generator of a cyclotomic field is _always_ called ``E(n)``. But this is not necessarily the case, in particular when the object in GAP was created from Sage.

Moreover, GAP prints an additional exclamation mark in front of numbers if they are part of a matrix defined over a cyclotomic field.

For these two reasons, the following example used to fail, but now works with the patch:

```
            sage: F=CyclotomicField(8)
            sage: z=F.gen()
            sage: a=gap(z+1/z); a
            -zeta8^3+zeta8
            sage: F(a)
            -zeta8^3 + zeta8
            sage: b=gap(Matrix(F,[[z^2,1],[0,a+1]])); b
            [ [ zeta8^2, !1 ], [ !0, -zeta8^3+zeta8+1 ] ]
            sage: b[1,2]
            !1
            sage: F(b[1,2])
            1
            sage: Matrix(b,F)
            [             zeta8^2                    1]
            [                   0 -zeta8^3 + zeta8 + 1]
```


The idea was
 * to remove the exclamation mark when it is attempted to coerce into the rationals
 * to test whether the generator name in GAP happens to coincide with the generator name in Sage (here: ``zeta8``).

The motivation for working on it is my attempt to improve the computation of non-modular invariant rings of finite groups: There is a doc test using a finite matrix group over a cyclotomic field.

One massive bottle neck for the computation of invariant rings with Singular is the computation of the Reynolds operator. It requires to enumerate the group elements, and Singular is not good at this task.

The patch uses GAP to enumerate the group elements and uses this to construct the Reynolds operator in Singular. For complicated groups, this should save a massive amount of resources.

With the patch, the enumeration of group elements in Singular has the status of a backup: If the transformation of the matrix group into GAP fails or if the transformation of the resulting GAP matrices back into Sage fails, then the old algorithm is used.

I think this ticket is about "interfaces". I hope this labelling is correct.


---

Comment by SimonKing created at 2010-05-07 11:00:50

Improve coercion from GAP into cyclotomic fields; use GAP to compute Reynolds operators for Singular


---

Comment by SimonKing created at 2010-05-08 12:16:57

Changing status from new to needs_review.


---

Attachment

Sorry, I forgot to label it "needs review"


---

Comment by davidloeffler created at 2010-07-03 08:15:45

When this is merged we can probably close #5618 too.


---

Comment by davidloeffler created at 2010-07-03 10:28:16

Changing status from needs_review to positive_review.


---

Comment by davidloeffler created at 2010-07-03 10:28:16

Patch applies fine to 4.5.alpha1, code looks plausible, and all doctests pass. Contrary to my earlier hope, however, it does not fix #5618 which seems to be a separate problem.


---

Comment by mhansen created at 2010-07-04 18:39:43

Changing status from positive_review to needs_work.


---

Comment by mhansen created at 2010-07-04 18:39:43

There's a bare except clause at 6767 which should be fixed.


---

Comment by SimonKing created at 2010-07-04 19:00:06

Replying to [comment:4 mhansen]:
> There's a bare except clause at 6767 which should be fixed.

By 'bare', you mean that it is not specified what error is raised? So, `except TypeError:` instead of `except:`? Well this would be easy enough to fix.


---

Comment by SimonKing created at 2010-07-04 19:10:44

Specify an exception to be caught


---

Comment by SimonKing created at 2010-07-04 19:12:30

Changing status from needs_work to needs_review.


---

Attachment

Replying to [comment:5 SimonKing]:
> Replying to [comment:4 mhansen]:
> > There's a bare except clause at 6767 which should be fixed.
> 
> By 'bare', you mean that it is not specified what error is raised? So, `except TypeError:` instead of `except:`? Well this would be easy enough to fix.
> 

Under the assumption that I understood you correctly, I provided a second patch that specifies that we only want to catch a `TypeError`, and return to needs_review.


---

Comment by mhansen created at 2010-07-04 19:20:35

Yep, looks good to me.  If you didn't specify that, the except clause would also catch things like KeyboardInterrupt (Ctrl-C) which probably isn't intended.

Apply both patches.


---

Comment by mhansen created at 2010-07-04 19:20:35

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-07-21 03:31:55

Resolution: fixed
