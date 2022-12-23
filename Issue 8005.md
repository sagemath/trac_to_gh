# Issue 8005: powers of elements in a QuotientRing

Issue created by migration from https://trac.sagemath.org/ticket/8005

Original creator: wjp

Original creation time: 2010-01-19 23:56:52

Assignee: AlexGhitza

Reported by Ronald van Luijk:

The following seems inconsistent:


```
sage: F = GF(5)
sage: R.<x,y>=F[]
sage: I=Ideal(R, [x, y])
sage: S.<x1,y1>=QuotientRing(R,I)
sage: print x1^2
x1^2
sage: print x1^3
x1^3
sage: print (x1^2)^2
x1^4
sage: print x1^4
NotImplementedError
```


The traceback is:


```
NotImplementedError                       Traceback (most recent call last)

/home/wjp/.sage/<ipython console> in <module>()

/data/sage/sage-4.3.1.rc1/local/lib/python2.6/site-packages/sage/structure/element.so in sage.structure.element.RingElement.__pow__ (sage/structure/element.c:10708)()

/data/sage/sage-4.3.1.rc1/local/lib/python2.6/site-packages/sage/structure/element.so in sage.structure.element.generic_power_c (sage/structure/element.c:22501)()

/data/sage/sage-4.3.1.rc1/local/lib/python2.6/site-packages/sage/structure/element.so in sage.structure.element.Element.__richcmp__ (sage/structure/element.c:6516)()

/data/sage/sage-4.3.1.rc1/local/lib/python2.6/site-packages/sage/structure/element.so in sage.structure.element.Element._richcmp (sage/structure/element.c:6398)()

/data/sage/sage-4.3.1.rc1/local/lib/python2.6/site-packages/sage/rings/quotient_ring_element.pyc in __cmp__(self, other)
    463             1
    464         """
--> 465         if self.__rep == other.__rep or ((self.__rep - other.__rep) in self.parent().defining_ideal()):
    466             return 0
    467         return cmp(self.__rep, other.__rep)

/data/sage/sage-4.3.1.rc1/local/lib/python2.6/site-packages/sage/rings/ideal.pyc in __contains__(self, x)
    260     def __contains__(self, x):
    261         try:
--> 262             return self._contains_(self.__ring(x))
    263         except TypeError:
    264             return False

/data/sage/sage-4.3.1.rc1/local/lib/python2.6/site-packages/sage/rings/ideal.pyc in _contains_(self, x)
    266     def _contains_(self, x):
    267         # check if x, which is assumed to be in the ambient ring, is actually in this ideal.
--> 268         raise NotImplementedError
    269 
    270     def __nonzero__(self):
```



---

Comment by Bouillaguet created at 2013-01-27 08:14:17

This bug no longer exists. Let's close this ticket


---

Comment by Bouillaguet created at 2013-01-27 08:14:17

Changing status from new to needs_review.


---

Comment by cnassau created at 2013-01-27 09:57:54

This is with Sage 5.7beta0 where everything seems to work as expected:

```
sage: F = GF(5)
sage: R.<x,y>=F[]
sage: I=Ideal(R, [x, y])
sage: S.<x1,y1>=QuotientRing(R,I)
sage: print x1^2
0
sage: print (x1^2)^2
0
sage: print x1^4
0
sage: print x1
0
sage: S
Quotient of Multivariate Polynomial Ring in x, y over Finite Field of size 5 by the ideal (x, y)
```

I wouldn't know how to create a meaningful doctest for this problem, so I'm giving the 'wontfix' a positive review.


---

Comment by cnassau created at 2013-01-27 09:57:54

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2013-01-31 20:39:13

Resolution: worksforme


---

Comment by mjo created at 2014-10-28 13:27:11

Changing assignee from AlexGhitza to mjo.


---

Comment by mjo created at 2014-10-28 13:27:11

Huh. This has been on my TODO list for quite a while I guess! It looks like this was fixed as part of #9138.

I've added a doctest for it, and cleaned up a little.
----
New commits:


---

Comment by mjo created at 2014-10-28 14:18:59

Aaaannd I can't reopen the ticket. Sorry for the noise.
