# Issue 6934: Fix eigenvectors (and a lot of other stuff) for symbolic matrices

Issue created by migration from https://trac.sagemath.org/ticket/6934

Original creator: kcrisman

Original creation time: 2009-09-15 13:46:05

Assignee: was

CC:  jason rbeezer

Keywords: symbolics, matrices, polynomials

From sage-devel [http://groups.google.com/group/sage-devel/browse_thread/thread/4f39037d7fd17133](http://groups.google.com/group/sage-devel/browse_thread/thread/4f39037d7fd17133) we have the following:

```
sage: A=matrix(SR,[[1,2,3],[4,5,6],[7,8,9]]) 
sage: A.eigenvectors_right() 
Traceback (most recent call last): 
... 
TypeError: degree() takes exactly one argument (0 given)
```

As it turns out, there are a HOST of things you can't do with A because of the new symbolics, which no one has yet implemented.  Another example:

```
sage: A = matrix(SR, [[1,2,3],[4,5,6],[7,8,9]])
sage: A.charpoly()
(x - 1)*((x - 9)*(x - 5) - 48) - 29*x - 3
sage: type(_)
<type 'sage.symbolic.expression.Expression'>
sage: B = matrix(QQ, [[1,2,3],[4,5,6],[7,8,9]])
sage: B.charpoly()
x^3 - 15*x^2 - 18*x
sage: type(_)
<class 'sage.rings.polynomial.polynomial_element_generic.Polynomial_rational_dense'>
```

which means minpoly does not work (because it requires a polynomial, not an expression) and so on. 

These were not caught before because these things were not tested, since they weren't actually implemented in the dense symbolic matrix file.


---

Comment by kcrisman created at 2009-09-15 13:47:10

Changing priority from major to critical.


---

Comment by kcrisman created at 2009-09-15 18:29:51

Note that #6936 will help make this ticket more specific.


---

Comment by mhansen created at 2009-11-10 04:17:44

See also #5639 which needs a review -- wink, wink.


---

Comment by jason created at 2009-11-10 05:32:24

I've attached an initial cut.  This needs doctests and testing in general.


---

Comment by jason created at 2009-11-10 05:32:24

Changing status from new to needs_work.


---

Comment by matthiasr created at 2010-05-25 16:10:35

friendly reminder … will this be ready soon? can I do anything to speed this up? (i.e., what exactly still needs to be done here? where do I even have to apply this?)


---

Comment by jason created at 2010-05-25 16:32:35

Several things need to be done:

1. Documentation for the function needs to be written.

2. doctests need to be run in Sage to check to make sure something didn't break.

To apply the patch, you can follow the instructions in the Sage Developer's guide.


---

Comment by jason created at 2010-05-25 17:02:55

Changing status from needs_work to needs_review.


---

Attachment

Okay, I fixed everything and this should be ready for review now.  Doctests pass on 4.4.1 in matrix/*.py[x]


---

Comment by rbeezer created at 2010-05-28 17:16:50

Hi Jason,

I can't get this to finish on a non-trivial 3x3 matrix.

9 different variables:  100 minutes, 2 GB memory used, killed my system

3x3 `VanderMonde` matrix, with one variable per row (each row is the 0, 1, 2 powers of the variable).  I killed it after 5 minutes.

So, yes, this would be nice for completeness, but seems of very limited value.  Do you (or anybody reading this) have any bigger, more interesting examples that actually finish?

The characteristic polynomial of a symbolic matrix can be computed quite quickly.  I don't imagine there is a good way to factor such a thing, though?

Rob


---

Comment by jason created at 2010-05-28 18:14:52

Well, once nice thing is that the eigenvectors/eigenvalues of a numeric matrix (like in the description) return root symbols instead of QQbar elements.  There have been lots of people complaining that the eigenvalues of a 2x2 matrix should just have square root signs.  With this patch, eigenvectors works too.


---

Comment by jason created at 2010-05-28 18:18:11

I might add that mathematica is fast (almost instantaneous) because they just punt to saying "roots of this huge symbolic characteristic polynomial".

It's too bad that we don't have a generic RootOf construct (I don't believe maxima has one either).  The closest we get is QQbar, but that only works for rational polynomials.


---

Attachment

OK, I see.  For example, this does a nice job with eigenvalues of graphs.  I've attached some doctests along these lines - if you want to include them, then go ahead and provide the review for the reviewer patch.  I'm clear for a positive review on the rest.


---

Attachment

apply on top of previous patches


---

Comment by jason created at 2010-09-03 21:54:27

Okay, back to you Rob.  I fixed one small problem with your docstring, but then realized that the file isn't included in the manual anyway.  So I added it to the manual and fixed two other small documentation problems.

If you think my changes are good, please set the ticket to positive review.


---

Comment by rbeezer created at 2010-09-04 02:31:43

Builds, passes all tests (-testall on 4.5.2) and the docs (the newly included module anyway) look good.  Thanks for the corrections on my additions.  I think this one is done.


---

Comment by rbeezer created at 2010-09-04 02:31:43

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-09-05 04:01:34

Could someone please prepend the ticket number to the commit string for [attachment:trac-6934-more-doctest-issues.patch] (and restore the status to "positive review")?


---

Comment by mpatel created at 2010-09-05 04:01:34

Changing status from positive_review to needs_work.


---

Attachment


---

Comment by rbeezer created at 2010-09-05 06:34:25

Changing status from needs_work to positive_review.


---

Comment by rbeezer created at 2010-09-05 06:34:25

Fixed the patch, tried to replace the existing one, but a stray "S" came into the filename.

So the third patch to apply for this ticket is the fourth one present at the moment, with "doctests" in the middle of the filename.


---

Comment by mpatel created at 2010-09-15 09:55:05

Thanks!


---

Comment by mpatel created at 2010-09-15 09:55:05

Resolution: fixed
