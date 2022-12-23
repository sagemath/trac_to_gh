# Issue 9820: problems with infinite polynomial rings

Issue created by migration from https://trac.sagemath.org/ticket/9821

Original creator: fwclarke

Original creation time: 2010-08-27 11:53:35

Assignee: malb

Keywords: infinite polynomial ring

The functions `is_field` and `is_integral_domain` for infinite polynomial rings lack the keyword `proof`.  This can give rise to errors.  For example,

```
sage: R.<x> = InfinitePolynomialRing(ZZ)
sage: A.<t> = R[[]]
```



---

Attachment


---

Comment by fwclarke created at 2010-08-27 12:02:47

Changing status from new to needs_review.


---

Comment by fwclarke created at 2010-08-27 12:02:47

The patch fixes the problem.  There were actually two definitions of `is_field` in the file.  One has been deleted and the other modified.


---

Comment by mhansen created at 2010-08-27 17:05:05

Could you add a doctest testing the proof parameter.

(Note that this is a duplicate of #9589, but I think this one can get resolved quicker.)


---

Comment by fwclarke created at 2010-08-31 20:40:31

Replying to [comment:2 mhansen]:

> Could you add a doctest testing the proof parameter.

This has turned out to be more difficult than expected, but I do now have a replacement patch.  In order to create a reasonable doctest I had to correct a bug in `sage.rings.quotient_rings.QuotientRing_generic.is_integral_domain`

At the same time I have eliminated the `Integer(8)` example from that function's doctests, since that ring uses code from `sage/rings/finite_rings/integer_mod_ring.pyx` rather than from `quotient_rings`.

I didn't think it worth including an example of the use of `proof` in `is_field` because the parameter is ignored.

> (Note that this is a duplicate of #9589, but I think this one can get resolved quicker.)

(You must have meant #9549)


---

Comment by fwclarke created at 2010-08-31 20:41:00

replaces previous patch


---

Attachment

This has been fixed by #9443.  This ticket was actually a triplicate!

The bug in `is_integral_domain` for generic quotient rings is now the subject of #10219.


---

Comment by fwclarke created at 2010-11-05 12:22:45

Resolution: duplicate
