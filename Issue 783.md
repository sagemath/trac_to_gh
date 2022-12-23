# Issue 783: dilog is lame

Issue created by migration from https://trac.sagemath.org/ticket/783

Original creator: was

Original creation time: 2007-10-02 13:26:29

Assignee: somebody

dilog on almost all input gives NotImplementedError:


```
sage: dilog(-1)
---------------------------------------------------------------------------
<type 'exceptions.NotImplementedError'>   Traceback (most recent call last)

/home/was/Desktop/<ipython console> in <module>()

/home/was/s/local/lib/python2.5/site-packages/sage/functions/special.py in dilog(t)
    743         return t.dilog()
    744     except AttributeError:
--> 745         raise NotImplementedError
    746
    747 def lngamma(t):

<type 'exceptions.NotImplementedError'>:
sage:                                     
```


Should add dilog to RDF, RR, CDF, CC elements, when it makes sense.

This does work:

```
sage: dilog(pari(2))
2.4674011002723396547086227499690377838 - 2.1775860903036021305006888982376139473*I
```


See also this from pari-dev (which I don't agree with):



---

Comment by was created at 2007-10-02 13:26:45


```
Vincent Lefevre <vincent@vinc17.org> 	
to pari-dev
	
show details
	 1:08 am (5 hours ago) 
Hi,

With Pari 2.3.2:

? dilog(-1)
%1 = -0.8224670334241132182362075834 + 9.136285398175292265776793780 E-29*I

but the value should be a real number. I suppose that the imaginary
term is due to a rounding error, in which case it should be zeroed
if one knows that the mathematical result is a real number.

Note that due to this problem, the plot function fails with:
 *** plot: impossible assignment t_COMPLEX --> t_REAL.
```



---

Attachment

But polylog is implemented to a more serious extent, in calculus.py.  I think we should just have dilog(z) be an alias for polylog(2, z).

I've put up a patch making this change.


---

Comment by mhansen created at 2008-04-26 01:47:14

Looks good to me.


---

Comment by mabshoff created at 2008-04-26 02:07:15

The hunk

```
diff -r 631bb7b11fe9 -r 2829ba5e615e sage/functions/all.py
--- a/sage/functions/all.py     Tue Apr 15 04:19:13 2008 -0700
+++ b/sage/functions/all.py     Sat Apr 19 10:33:01 2008 -0400
@@ -16,7 +16,7 @@ from special    import (bessel_I, bessel
                         spherical_bessel_J, spherical_bessel_Y,
                         spherical_hankel1, spherical_hankel2,
                         spherical_harmonic, jacobi,
-                        inverse_jacobi, dilog,
+                        inverse_jacobi,
                         lngamma, exp_int, error_fcn)

 from orthogonal_polys import (chebyshev_T,
```

conflicts with one of the other patches in 3.0.1.alpha0, so I am merging that one manually.

Cheers,

Michael


---

Comment by mabshoff created at 2008-04-26 03:35:00

Resolution: fixed


---

Comment by mabshoff created at 2008-04-26 03:35:00

Merged in Sage 3.0.1.alpha0


---

Comment by zimmerma created at 2010-02-07 10:44:24

Resolution changed from fixed to 


---

Comment by zimmerma created at 2010-02-07 10:44:24

Changing status from closed to new.


---

Comment by zimmerma created at 2010-02-07 10:44:24

I'd like to reopen this ticket, since the fix only corrected integer input (here with Sage 4.3.1):

```
sage: dilog(-1.1)
ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (2251, 0))

---------------------------------------------------------------------------
NotImplementedError                       Traceback (most recent call last
```

Pari knows how to compute this:

```
sage: gp.dilog(-1.1)
-0.89083809026228267332015894927022713036
```



---

Comment by mhansen created at 2010-08-26 21:48:48

Changing status from new to needs_review.


---

Comment by zimmerma created at 2010-08-30 12:19:52

Changing status from needs_review to needs_info.


---

Comment by zimmerma created at 2010-08-30 12:19:52

There is something strange in the examples added:

```
sage: from sage.symbolic.pynac import py_li2_for_doctests as py_li2 
sage: py_li2(-1.1)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/users/caramel/zimmerma/Adm/Stages/10/Prest/<ipython console> in <module>()

/usr/local/sage-core2/local/lib/python2.6/site-packages/sage/symbolic/pynac.so in sage.symbolic.pynac.py_li2_for_doctests (sage/symbolic/pynac.cpp:15450)()

TypeError: py_li2_for_doctests() takes exactly 2 positional arguments (1 given)
```

Shouldn't `py_li2` take two arguments?

Also I've noticed the following, which maybe should be in a different ticket:

```
sage: dilog(+Infinity)
dilog(+Infinity)
sage: dilog(-Infinity)
dilog(-Infinity)
sage: limit(dilog(x),x=+Infinity)
Infinity
sage: limit(dilog(x),x=-Infinity)
-Infinity
```

Maybe `dilog(+Infinity)` and `dilog(-Infinity)` should return the corresponding limits?


---

Comment by mhansen created at 2010-08-30 18:12:37

The patch had some typos so I uploaded a correct version.  The +Infinity/-Infinity thing should probably be a new ticket as it's something that should be done in a manner consistent for all functions.


---

Comment by mhansen created at 2010-08-30 18:12:37

Changing status from needs_info to needs_review.


---

Comment by zimmerma created at 2010-09-01 14:54:54

Changing status from needs_review to positive_review.


---

Comment by zimmerma created at 2010-09-01 14:54:54

good work, Mike!


---

Comment by burcin created at 2010-09-12 12:05:39

The function `syntactically_equal()` in attachment:trac_783.patch doesn't contain doctests. I don't see how the changes to `sage/symbolic/expression.pyx` in that patch are relevant to this ticket. Perhaps these should be on a different ticket.


---

Comment by burcin created at 2010-09-12 12:05:39

Changing status from positive_review to needs_work.


---

Comment by zimmerma created at 2010-09-12 12:33:35

Replying to [comment:12 burcin]:
> The function `syntactically_equal()` in attachment:trac_783.patch doesn't contain doctests. I don't see how the changes to `sage/symbolic/expression.pyx` in that patch are relevant to this ticket. Perhaps these should be on a different ticket.

you are perfectly right, Burcin. Mike, please could you remove that unused code from the patch?
Paul


---

Attachment


---

Comment by mhansen created at 2010-09-12 17:00:42

Changing status from needs_work to positive_review.


---

Comment by mhansen created at 2010-09-12 17:00:42

Sorry about that -- I'm not sure how those changes snuck into that patch.


---

Comment by zimmerma created at 2010-09-13 10:13:15

> Sorry about that -- I'm not sure how those changes snuck into that patch. 

I'm sorry I didn't see that during my review. Anyway I confirm all doctests still pass
(tested with Sage 4.5.2).

Paul


---

Comment by mpatel created at 2010-09-15 11:13:45

Resolution: fixed
