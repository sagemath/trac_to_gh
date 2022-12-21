# Issue 6643: vector function changes the ring of a vector for ZZ when possible

Issue created by migration from Trac.

Original creator: slabbe

Original creation time: 2009-07-27 19:40:35

Assignee: slabbe

The following works fine, i.e vector function doesn't change the ring of the input vector :


```
sage: K.<sqrt3> = QuadraticField(3); K
Number Field in sqrt3 with defining polynomial x^2 - 3
sage: v = vector(K, (1/2, sqrt3/2) ); v
(1/2, 1/2*sqrt3)
sage: v.parent()
Vector space of dimension 2 over Number Field in sqrt3 with defining polynomial x^2 - 3
sage: vector(v).parent()
Vector space of dimension 2 over Number Field in sqrt3 with defining polynomial x^2 - 3
```


For rationals coordinates, it is also OK :


```
sage: v2 = vector(K, (1/2, 3/2) ); v2
(1/2, 3/2)
sage: v2.parent()
Vector space of dimension 2 over Number Field in sqrt3 with defining polynomial x^2 - 3
sage: vector(v2).parent()
Vector space of dimension 2 over Number Field in sqrt3 with defining polynomial x^2 - 3
```


But, for integers, it changes the ring for ZZ :


```
sage: v3 = vector(K, (0, 1) )
sage: v3.parent()
Vector space of dimension 2 over Number Field in sqrt3 with defining polynomial x^2 - 3
sage: vector(v3).parent()
Ambient free module of rank 2 over the principal ideal domain Integer Ring
```


which I doesn't like because I want to be able to add them (the addition of those vector appears to be unsupported yet by the coercion system...this could be another ticket...) :


```
sage: v + v3
(1/2, 1/2*sqrt3 + 1)
sage: vector(v) + vector(v3)
ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (1052, 0))

Traceback (most recent call last):
...
/home/slabbe/sage-4.1/local/lib/python2.6/site-packages/sage/modules/free_module.pyc in __cmp__(self, other)
   3806             if not c: return c
   3807             try:
-> 3808                 if self.base_ring().is_subring(other.base_ring()):
   3809                     return -1
   3810                 elif other.base_ring().is_subring(self.base_ring()):

/home/slabbe/sage-4.1/local/lib/python2.6/site-packages/sage/rings/ring.so in sage.rings.ring.Ring.is_subring (sage/rings/ring.c:4724)()

AttributeError: 'NotImplementedType' object has no attribute 'natural_map'
```


I will also ask on sage-devel if there is a reason why the vector function changes the ring of a vector for ZZ when possible.


---

Attachment

Applies on sage-4.1


---

Comment by slabbe created at 2009-07-27 20:15:33

I posted my question on sage-devel :

http://groups.google.com/group/sage-devel/browse_thread/thread/dc142746f1aa8175


---

Comment by slabbe created at 2009-07-27 20:16:38

Changing status from new to assigned.


---

Comment by slabbe created at 2009-07-27 20:16:38

Changing keywords from "" to "vector".


---

Comment by rbeezer created at 2009-08-17 06:23:17

Performs as advertised, passes all tests, documentation builds without warnings.

Positive review.


---

Comment by mvngu created at 2009-08-25 01:40:51

Resolution: fixed
