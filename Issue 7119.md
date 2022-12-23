# Issue 7119: Redundant minus sign in PolyDict polynomial

Issue created by migration from https://trac.sagemath.org/ticket/7119

Original creator: klee

Original creation time: 2009-10-05 04:49:57

Assignee: Kwankyu Lee

There is a tiny bug in the polydict implementation of multivariate
polynomial ring. 


```
sage: from sage.rings.polynomial.multi_polynomial_ring import MPolynomialRing_polydict
sage: R.<x,y>=MPolynomialRing_polydict(GF(2),2,order='lex')
sage: R
Multivariate Polynomial Ring in x, y over Finite Field of size 2
sage: f=x+y
sage: f.lt()
-x
sage: f.lm()
-x
```


The minus sign in "-x" is redundant



---

Comment by klee created at 2009-10-05 04:59:59

Changing status from new to assigned.


---

Attachment

The patch corrects the bug.


---

Comment by klee created at 2009-10-05 04:59:59

Changing assignee from Kwankyu Lee to klee.


---

Comment by awebb created at 2009-10-10 10:19:29

I think a doctest should be added for the case that the patch fixes. ~ adam


---

Attachment

The new patch includes doctests and a bugfix of the patch itself.

Martin says:

Alex Ghitza wrote a patch to fix printing of multivariate polynomials in
general

  http://trac.sagemath.org/sage_trac/ticket/6551

which might contain your fix. However, it needs some work before it can go in.


However, it seems to me that Alex Ghitza's patch is independent with the current patch.


---

Comment by klee created at 2009-10-12 08:12:32

The present bug results from the class PolyDict in sage/rings/polynomial/
polydict.pyx rests upon "zero" optional parameter, which defaults to
integer 0, to decide the characteristic of the parent ring when its
object is printed. On the other hand, f.lt() does not set the "zero"
parameter in sage/rings/polynomial/multi_polynomial_element.py. 

I think patching the polydict.pyx so as not to rely on the "zero" paramter might be better way to correct the bug. But this is out of my reach.


---

Comment by awebb created at 2009-10-12 11:25:28

What does the TESTS: label do? When I build the reference the Test section is also included. In which case, why not just add to the Examples section (separated by a line with a :: to start a new section)?

I think it would be easier to use something like:

```
sage: R.<x,y>=PolynomialRing(GF(2),2,order='lex')
sage: f=x+y
sage: f.lt()
x
```


Then you don't need the long import statement.  What do you think?

Adam


---

Comment by awebb created at 2009-10-12 11:42:10

suggested changes


---

Attachment

I added a "suggested changes" patch just to clarify. ~ Adam


---

Comment by klee created at 2009-10-13 02:14:49

Hi Adam,

The bug is in the polydict engine of multivariate polynomial rings. So your doctest does not check the bug.

About the tests section in the docstring, see this thread in sage-devel: http://groups.google.com/group/sage-devel/browse_frm/thread/2c86e8b59d670502

To summarize, your "suggested changes" should be reverted.

Kwankyu


---

Comment by awebb created at 2009-10-13 06:18:26

Changing status from needs_review to positive_review.


---

Comment by awebb created at 2009-10-13 06:18:26

Hi,

That all sounds fine to me. In that case my suggested patch can be ignored. If you know how, you can delete it. In any case, trac_#7119.patch would be the correct patch to apply.

Cheers,

Adam


---

Comment by mhansen created at 2009-10-15 15:33:32

Resolution: fixed
