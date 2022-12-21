# Issue 7458: [with patch, needs review] Sylvester matrix for polynomials

Issue created by migration from Trac.

Original creator: carlohamalainen

Original creation time: 2009-11-14 13:00:01

Assignee: malb

Small patch to add Sylvester matrix calculation for univariate and multivariate polynomials.

I think that my patch is a bit more general (and has doctests) compared to didier deshommes' patch here, which seems to have never been merged:

http://sage.math.washington.edu/home/dfdeshom/custom/patches/sylveste...



---

Attachment


---

Comment by lftabera created at 2010-11-06 12:06:38

Changing status from new to needs_work.


---

Attachment

This is a very basic feature that has to be in Sage.

I have rebased Carlo patch to 4.6  but have not touched the code.

I have some concerns that makes me mark the patch as needs work:

- The univariate case should accept the same syntax as the multivariate case. In the univariate case, the preferred call is f.sylvester_matrix(g), but I do not want Sage to throw an error if I wrote f.sylvester_matrix(g, x)

- Corner cases must be well documented. 


```
sage: K.<x>=QQ[]
sage: K(1).sylvester_matrix(K(1))
[]
```


In particular, I am not sure how to deal with the sylvester matrix of 0 and constant or 0 and 0
Curretly it throws an error. My opinion is that this is not defined but  should throw a more meaningful error.

Maple for instance return the empty matrix. So in maple:

Determinant(Sylvester_Matrix)  != Resultant 

In this corner cases.

I will  try to check what other CAS do to get a wider picture.

- An example explicitly relating Sylvester matrix and resultant should be added.


---

Comment by lftabera created at 2010-11-06 12:06:38

Changing keywords from "" to "Sylvester matrix".


---

Comment by lftabera created at 2010-11-06 17:30:59

- I have added more documentation and doctest.

- The variable argument is now optional in both univariate and multivariate. If it is not used, the first variable of the polynomial ring is used.

- I have added coercion to be able to compute the Sylvester matrix of polynomials in different rings, for ex. ZZ[x] and QQ[x] 

- solved an issue for the dimension of the matrix of the sylvester matrix of (x**n, 0)

It is not ready for review because the sylvester matrix of (0,0) is not implemented.


---

Comment by lftabera created at 2010-11-12 13:36:54

Changing status from needs_work to needs_review.


---

Attachment

Finally, if one of the polynomials is zero, the code raises a ValueError.


---

Comment by lftabera created at 2010-12-04 12:51:46

Apply trac-7458-sylvester-rebase-4.6.patch, trac-7458-sylvester-improvements.patch


---

Comment by davidloeffler created at 2010-12-16 11:38:48

Very nice. I am impressed with the thoroughness of the testing of corner cases here. All doctests in sage/rings pass, and the reference manual builds OK.


---

Comment by davidloeffler created at 2010-12-16 11:38:48

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2011-01-26 22:26:11

Resolution: fixed
