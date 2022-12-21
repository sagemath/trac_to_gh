# Issue 6886: Elliptic curve isogeny checking can be expensive

Issue created by migration from Trac.

Original creator: cremona

Original creation time: 2009-09-04 08:58:56

Assignee: davidloeffler

CC:  wuthrich shumow

Keywords: elliptic curve isogeny

In #6384, code was introduced to check whether the kernel polynomial provided by the user was valid, by checking that it divides the appropriate division polynomial.

This can be too expensive!  I have been working with isogenies of degree 163 over QQ, for which computing the 163-division polynomial takes many hours.  So I want to introduce a check parameter to the isogeny construction, default True, so that users (or other code) can switch off this check (when they "know" they are right!).



---

Attachment

An optional argument 'check' is added to isogenies for elliptic curves.


---

Comment by wuthrich created at 2009-10-08 21:55:38

Changing status from new to needs_review.


---

Comment by cremona created at 2009-10-08 22:07:47

Thanks, Chris -- I will test the patch when I can.  Another situation where this will help is for curves over QQbar, where (at present) the order of points cannot be obtained.  [I was thinking of adding this by coercing everything into a suitable number field, though I fear it would be quite expensive.]


---

Comment by wuthrich created at 2009-10-09 09:01:22

documentation for it; to be applied after the first


---

Attachment

I forgot to add the documentation. The second patch (to be applied after the first) fixes that.

If check is false and a (or several) presumably-torsion points are given, the algorithm does not check if they are really torsion anymore. But it still needs the function .order(). I think we should open another ticket for this.

Chris.


---

Comment by davidloeffler created at 2009-10-09 09:13:53

Remove assignee davidloeffler.


---

Comment by cremona created at 2009-10-11 11:04:45

The patches look good, apply to 4.1.2.rc0 and all elliptic curves tests pass.  Even better, the patch I am currently working on for #6887 applies fine on top of these, and I will make anything I post at #6887 depend on this one.  It may happen that I further develop the checking code on that ticket, but this is good to go in now -- it can get into 4.1.2 while the new stuff in #6887 had better wait since it does a lot of new stuff.

I have been thinking of a better way of testing the validity of a kernel polynomial, and currently have an idea (not implemented ) which would work in the case of a cyclic kernel.


---

Comment by cremona created at 2009-10-11 11:04:45

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2009-10-19 06:12:27

Resolution: fixed
