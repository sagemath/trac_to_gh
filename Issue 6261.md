# Issue 6261: Add multiplicative order for matrices over finite fields

Issue created by migration from https://trac.sagemath.org/ticket/6261

Original creator: ylchapuy

Original creation time: 2009-06-11 16:54:34

Assignee: was

For the algorithm used, see
Frank Celler and Charles R. Leedham-Green, "Calculating the Order of an Invertible Matrix".


---

Attachment


---

Comment by cremona created at 2009-06-14 16:33:15

This looks good to me.  One question:  in the line

```
ppart = p**Integer(a).exact_log(p)
```

do you really mean ppart to be the largest power of p which is <= a, rather than the pargest power which divides a?
If so, please change this to "positive review".

Remark:  I have a Magma implementation of an algorithm to determine when a polynomial over ZZ is cyclotomic (algorithm of Smyth and Beukers).  That could be used to extend this function to matrices over ZZ, at least.


---

Comment by ylchapuy created at 2009-06-16 20:07:37

Replying to [comment:2 cremona]:
> This looks good to me.  One question:  in the line
> {{{
> ppart = p**Integer(a).exact_log(p)
> }}}
> do you really mean ppart to be the largest power of p which is <= a, rather than the pargest power which divides a?
> If so, please change this to "positive review".

Yes, it's what I mean. Thanks for the review.


---

Comment by rlm created at 2009-06-24 10:10:33

Resolution: fixed


---

Comment by davidloeffler created at 2009-06-27 08:32:13

"Merged in: Yann Laigle-Chapuy"? Hang on a minute! Which version was this actually merged in?
