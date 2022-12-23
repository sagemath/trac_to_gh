# Issue 6337: bug in jorder form over symbolic ring

Issue created by migration from https://trac.sagemath.org/ticket/6337

Original creator: was

Original creation time: 2009-06-16 16:58:27

Assignee: was


```
sage: version()
'Sage Version 4.0.1, Release Date: 2009-06-06'
sage: var('a d')
(a, d)
sage: A = matrix([[a,0],[1,d]])
sage: A.eigenvalues()
[d, a]
sage: A.jordan_form()
---------------------------------------------------------------------------
RuntimeError                              Traceback (most recent call
last)

/home/bo198214/.sage/temp/darkdepth/6404/
_home_bo198214__sage_init_sage_0.py in <module>()

/usr/src/sage-4.0.1-linux-Debian_GNU_Linux_5.0_lenny-sse2-x86_64-Linux/
local/lib/python2.5/site-packages/sage/matrix/matrix2.so in
sage.matrix.matrix2.Matrix.jordan_form (sage/matrix/matrix2.c:27915)()

RuntimeError: Some eigenvalue does not exist in Symbolic Ring.
```



---

Comment by mhampton created at 2009-06-16 17:12:52

Things are failing early on, with the roots command.  E.g.:

sage: var('a, d')
sage: ((d - x)*(a - x)).roots()
[(x, 1)]

While the eigenvalues method works, it doesn't compute multiplicities, so I am not sure what the easiest fix is.


---

Comment by darij created at 2013-06-22 23:04:09

This one looks different now:

```
sage: sage: var('a d')
(a, d)
sage: sage: A = matrix([[a,0],[1,d]])
sage: sage: A.eigenvalues()
[d, a]
sage: sage: A.jordan_form()
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-8-708dc91119f4> in <module>()
----> 1 A.jordan_form()

/home/darij/sage-5.11.beta3/local/lib/python2.7/site-packages/sage/matrix/matrix2.so in sage.matrix.matrix2.Matrix.jordan_form (sage/matrix/matrix2.c:44267)()

ValueError: Jordan normal form not implemented over inexact rings.
```


I agree that the symbolic ring is inexact, and that Jordan normal form requires exactness...


---

Comment by rws created at 2015-07-31 13:51:37

Changing status from new to needs_review.


---

Comment by rws created at 2015-07-31 13:51:37

Replying to [comment:3 darij]:
> I agree that the symbolic ring is inexact, and that Jordan normal form requires exactness...
So this would be invalid now?


---

Comment by darij created at 2015-07-31 13:54:10

I think someone who understands symbolic better should weigh in.


---

Comment by vdelecroix created at 2015-08-09 14:20:16

Replying to [comment:1 mhampton]:
> Things are failing early on, with the roots command.  E.g.:
> 
> sage: var('a, d')
> sage: ((d - x)*(a - x)).roots()
> [(x, 1)]

What is failing here? In order to get the expected answer you need of course to specify the variable

```
sage: var('a d')
(a, d)
sage:  ((d - x)*(a - x)).roots()
[(x, 1)]
sage:  ((d - x)*(a - x)).roots(x)
[(d, 1), (a, 1)]
sage:  ((d - x)**2).roots()
[(x, 2)]
```



---

Comment by pbruin created at 2015-08-31 18:13:28

Here is a straightforward implementation of `jordan_form()` for symbolic matrices using Maxima.  Even though the "symbolic ring" is considered to be inexact, it still seems useful to have a working `jordan_form()` method for it.


---

Comment by cpernet created at 2015-09-15 16:09:31

This looks fine to me.


Replying to [comment:8 rws]:
> Replying to [comment:3 darij]:
> > I agree that the symbolic ring is inexact, and that Jordan normal form requires exactness...
> So this would be invalid now?
The Jordan normal form does not require more "exactness" from the ring as do the eigenvalues which are already implemented for symbolic matrices (calling maxima). Hence I see no point in discussing whether or not we should offer a jordan_form method for symbolic matrices, it seems natural to do it as what is proposed here.

Just one thing: to be consistent with what is returned over other coefficient domains, the Jordan form should display the subdivision of the block matrix.
  {{{#!python
  sage: a = matrix(QQ,3,[1,0,1,0,2,0,0,0,1])
  sage: a.jordan_form()
  [2|0 0]
  [-+---]
  [0|1 1]
  [0|0 1]
  }}}


---

Comment by cpernet created at 2015-09-15 16:09:31

Changing status from needs_review to needs_work.


---

Comment by git created at 2015-09-17 15:56:49

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by pbruin created at 2015-09-17 15:59:04

Changing status from needs_work to needs_review.


---

Comment by pbruin created at 2015-09-17 15:59:04

Replying to [comment:12 cpernet]:
> Just one thing: to be consistent with what is returned over other coefficient domains, the Jordan form should display the subdivision of the block matrix.
Thanks for noticing, I added this in the latest commit.


---

Comment by cpernet created at 2015-09-18 05:29:21

Thanks, this is all good to me.


---

Comment by cpernet created at 2015-09-18 05:29:21

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2015-09-18 07:36:37

Changing status from positive_review to needs_work.


---

Comment by vbraun created at 2015-09-18 07:36:37

Reviewer name missing


---

Comment by cpernet created at 2015-09-18 11:41:23

Changing status from needs_work to positive_review.


---

Comment by vbraun created at 2015-09-18 19:10:48

Resolution: fixed
