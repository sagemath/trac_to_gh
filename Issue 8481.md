# Issue 8481: lift doesn't work for vector space homomorphisms

Issue created by migration from https://trac.sagemath.org/ticket/8481

Original creator: jhpalmieri

Original creation time: 2010-03-07 22:49:07

Assignee: was


```
sage: V = QQ**2
sage: W = QQ**2
sage: f = V.hom([W.1, W.1])
sage: f.lift(W.1)
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)

/Users/palmieri/<ipython console> in <module>()

/Applications/sage/local/lib/python2.6/site-packages/sage/modules/free_module_morphism.pyc in lift(self, x)
    337         x = self.codomain()(x)
    338         A = self.matrix()
--> 339         H, U = A.hermite_form(transformation=True,include_zero_rows=False)
    340         Y = H.solve_left(vector(self.codomain().coordinates(x)))
    341         C = Y*U

...
```



---

Comment by jhpalmieri created at 2010-03-08 23:47:28

Changing status from new to needs_review.


---

Attachment


---

Comment by was created at 2010-04-05 02:55:23

Changing status from needs_review to needs_work.


---

Comment by was created at 2010-04-05 02:55:23

1. Can you change this to only do check=True when the base ring is *not* a field:

```
        5408	 	                    check=False, copy=False, coerce=False) 
 	5408	                    check=True, copy=False, coerce=False) 
```

Or, better yet, always do check=False unless the components of v are not all in the base ring.   The problem is that check=True could be *massively* expensive -- you could add hours to the runtimes of real-world computations with this one little change.  

2. I'm happy with all the other code.  

I'm running tests and will report in a moment.


---

Comment by was created at 2010-04-05 03:02:57

All doctests pass fine.


---

Attachment

Here's a new patch.  I hope the speed hit isn't too bad with this one.


---

Comment by jhpalmieri created at 2010-04-06 00:00:00

Changing status from needs_work to needs_review.


---

Comment by was created at 2010-04-06 05:46:21

OK, looks good!


---

Comment by was created at 2010-04-06 05:46:21

Changing status from needs_review to positive_review.


---

Comment by jhpalmieri created at 2010-04-15 23:54:05

Merged "trac_8481-lift.v2.patch" into 4.4.alpha0.


---

Comment by jhpalmieri created at 2010-04-15 23:54:05

Resolution: fixed
