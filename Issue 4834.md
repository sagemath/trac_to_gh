# Issue 4834: Return eigenvectors as members of a "normal" space instead of as members of an eigenspace

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2008-12-19 22:29:12

Assignee: was

CC:  robertwb

From sage-support:


```

> It looks like eigenvectors are returned as the basis vectors of the
> > eigenspace.  Should they be returned as just plain old vectors instead?

Yes, definitely.  Then we don't have create a whole bunch of different
vector spaces for no reason too.

 -- William
```




---

Comment by jason created at 2009-10-16 18:05:59

Changing assignee from was to jason.


---

Attachment

Attached worksheet does a better job of illustrating the problem.  I plan to attack this at Bug Days if it is still open.

Can we naturally coerce vectors from lower-dimensional subspaces into the obvious ambient vector space (the one with same degree, same ring or a common super-ring)?  That might be one other solution.


---

Comment by rbeezer created at 2010-12-10 02:14:37

Changing status from new to needs_info.


---

Comment by jason created at 2010-12-10 02:43:44

I fiddled with this a bit, and thought I posted a patch.  I can help at the Bug Days with this, if it's still open.


---

Comment by rbeezer created at 2011-01-11 21:54:14

Following looks to me like the essence of the complaint.  Eigenvectors are assigned to their eigenspaces, which I think is useful and informative, and not worth throwing away.  Simple operations seem to work properly, in that computations proceed and parents are assigned accordingly.

However, when a symbolic element is introduced, then addition fails with incompatible parents.  It would seem that the vector over the rationals could get promoted to be over the symbolic ring?  Similar behavior occurs for an element of a number field.



```
sage: B=matrix([[1,2],[2,1]])
sage: spec=B.eigenvectors_right()
sage: v=spec[0][1][0]
sage: z=spec[1][1][0]
sage: v,z
((1, 1), (1, -1))
sage: v.parent()
Vector space of degree 2 and dimension 1 over Rational Field
User basis matrix:
[1 1]
sage: z.parent()
Vector space of degree 2 and dimension 1 over Rational Field
User basis matrix:
[ 1 -1]
sage: u=3*v
sage: u.parent()
Vector space of degree 2 and dimension 1 over Rational Field
User basis matrix:
[1 1]
sage: w = v + z
sage: w.parent()
Vector space of degree 2 and dimension 2 over Rational Field
User basis matrix:
[ 1 -1]
[ 1  1]

sage: var('t')
t
sage: v + t*z
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/sage/sage-4.6.1.rc1/devel/sage-main/<ipython console> in <module>()

/sage/sage-4.6.1.rc1/local/lib/python2.6/site-packages/sage/structure/element.so in sage.structure.element.ModuleElement.__add__ (sage/structure/element.c:7627)()

/sage/sage-4.6.1.rc1/local/lib/python2.6/site-packages/sage/structure/coerce.so in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:6995)()

TypeError: unsupported operand parent(s) for '+': 'Vector space of degree 2 and dimension 1 over Rational Field
User basis matrix:
[1 1]' and 'Vector space of degree 2 and dimension 1 over Symbolic Ring
User basis matrix:
[ 1 -1]'

sage: R.<a>=QuadraticField(-5)
sage: v + a*z
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/sage/sage-4.6.1.rc1/devel/sage-main/<ipython console> in <module>()

/sage/sage-4.6.1.rc1/local/lib/python2.6/site-packages/sage/structure/element.so in sage.structure.element.ModuleElement.__add__ (sage/structure/element.c:7627)()

/sage/sage-4.6.1.rc1/local/lib/python2.6/site-packages/sage/structure/coerce.so in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:6995)()

TypeError: unsupported operand parent(s) for '+': 'Vector space of degree 2 and dimension 1 over Rational Field
User basis matrix:
[1 1]' and 'Vector space of degree 2 and dimension 1 over Number Field in a with defining polynomial x^2 + 5
User basis matrix:
[ 1 -1]'
```



---

Comment by rbeezer created at 2011-01-12 18:03:31

I spent some time trying to see where to add this to the coercion system, but it was beyond me. I could probably review a fix.


---

Comment by rbeezer created at 2011-01-22 21:43:45

A workaround is to begin with symbolic matrices, which are now amenable to eigenvector computations (albeit slowly).  See #6934, #10346 (coming soon to an official release).  Then results (eigenvectors) are symbolic for starters, so they play nicely with a symbolic expression like the variable t.


```
sage: B=matrix(SR, [[1,2],[2,1]])
sage: spec=B.eigenvectors_left()
sage: spec
[(3, [(1, 1)], 1), (-1, [(1, -1)], 1)]
sage: v = spec[0][1][0]
sage: z = spec[1][1][0]
sage: z.parent()
Vector space of dimension 2 over Symbolic Ring
sage: var('t')
t
sage: v + t*z
(t + 1, -t + 1)
```


But I think an addition to the coercion system is still the best long-term solution, since these symbolic eigenvalue computations are not real robust.
