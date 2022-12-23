# Issue 7191: is_primitive() for a Dirichlet character doesn't work when base ring is CC

Issue created by migration from https://trac.sagemath.org/ticket/7191

Original creator: bober

Original creation time: 2009-10-12 02:58:56

Assignee: was

CC:  wuthrich

See the following example:


```
sage: G = DirichletGroup(500, base_ring=CC)
sage: G[0].is_primitive()
False
sage: G[1].is_primitive()
---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)

/home/bober/.sage/temp/bober/24617/_home_bober__sage_init_sage_0.py in <module>()

/home/bober/sage/local/lib/python2.6/site-packages/sage/misc/cachefunc.pyc in __call__(self, *args, **kwds)
    240             return cache[key]
    241         else:
--> 242             cache[key] = self.f(self._instance, *args, **kwds)
    243             return cache[key]
    244 

/home/bober/sage/local/lib/python2.6/site-packages/sage/modular/dirichlet.pyc in is_primitive(self)
   1161             True
   1162         """
-> 1163         return (self.conductor() == self.modulus())
   1164 
   1165     @cached_method

/home/bober/sage/local/lib/python2.6/site-packages/sage/misc/cachefunc.pyc in __call__(self, *args, **kwds)
    240             return cache[key]
    241         else:
--> 242             cache[key] = self.f(self._instance, *args, **kwds)
    243             return cache[key]
    244 

/home/bober/sage/local/lib/python2.6/site-packages/sage/modular/dirichlet.pyc in conductor(self)
    624         F = arith.factor(self.modulus())
    625         if len(F) > 1:
--> 626             return misc.mul([d.conductor() for d in self.decomposition()])
    627         p = F[0][0]
    628         # When p is odd, and x =/= 1, the conductor is the smallest p**r such that

/home/bober/sage/local/lib/python2.6/site-packages/sage/misc/cachefunc.pyc in __call__(self, *args, **kwds)
    240             return cache[key]
    241         else:
--> 242             cache[key] = self.f(self._instance, *args, **kwds)
    243             return cache[key]
    244 

/home/bober/sage/local/lib/python2.6/site-packages/sage/modular/dirichlet.pyc in conductor(self)
    620             20
    621         """
--> 622         if self.modulus() == 1 or self.is_trivial():
    623             return 1
    624         F = arith.factor(self.modulus())

/home/bober/sage/local/lib/python2.6/site-packages/sage/misc/cachefunc.pyc in __call__(self, *args, **kwds)
    240             return cache[key]
    241         else:
--> 242             cache[key] = self.f(self._instance, *args, **kwds)
    243             return cache[key]
    244 

/home/bober/sage/local/lib/python2.6/site-packages/sage/modular/dirichlet.pyc in is_trivial(self)
   1177             True
   1178         """
-> 1179         return (self.element() == 0)
   1180 
   1181     def kernel(self):

/home/bober/sage/local/lib/python2.6/site-packages/sage/modular/dirichlet.pyc in element(self)
   1531             M    = P._module
   1532             dlog = P._zeta_dlog
-> 1533             v = M([dlog[x] for x in self.values_on_gens()])
   1534             self.__element = v
   1535             return v

KeyError: -1.00000000000000 - 2.63677968348475e-16*I
sage: G[3].is_primitive()
---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)

/home/bober/.sage/temp/bober/24617/_home_bober__sage_init_sage_0.py in <module>()

/home/bober/sage/local/lib/python2.6/site-packages/sage/misc/cachefunc.pyc in __call__(self, *args, **kwds)
    240             return cache[key]
    241         else:
--> 242             cache[key] = self.f(self._instance, *args, **kwds)
    243             return cache[key]
    244 

/home/bober/sage/local/lib/python2.6/site-packages/sage/modular/dirichlet.pyc in is_primitive(self)
   1161             True
   1162         """
-> 1163         return (self.conductor() == self.modulus())
   1164 
   1165     @cached_method

/home/bober/sage/local/lib/python2.6/site-packages/sage/misc/cachefunc.pyc in __call__(self, *args, **kwds)
    240             return cache[key]
    241         else:
--> 242             cache[key] = self.f(self._instance, *args, **kwds)
    243             return cache[key]
    244 

/home/bober/sage/local/lib/python2.6/site-packages/sage/modular/dirichlet.pyc in conductor(self)
    624         F = arith.factor(self.modulus())
    625         if len(F) > 1:
--> 626             return misc.mul([d.conductor() for d in self.decomposition()])
    627         p = F[0][0]
    628         # When p is odd, and x =/= 1, the conductor is the smallest p**r such that

/home/bober/sage/local/lib/python2.6/site-packages/sage/misc/cachefunc.pyc in __call__(self, *args, **kwds)
    240             return cache[key]
    241         else:
--> 242             cache[key] = self.f(self._instance, *args, **kwds)
    243             return cache[key]
    244 

/home/bober/sage/local/lib/python2.6/site-packages/sage/modular/dirichlet.pyc in conductor(self)
    620             20
    621         """
--> 622         if self.modulus() == 1 or self.is_trivial():
    623             return 1
    624         F = arith.factor(self.modulus())

/home/bober/sage/local/lib/python2.6/site-packages/sage/misc/cachefunc.pyc in __call__(self, *args, **kwds)
    240             return cache[key]
    241         else:
--> 242             cache[key] = self.f(self._instance, *args, **kwds)
    243             return cache[key]
    244 

/home/bober/sage/local/lib/python2.6/site-packages/sage/modular/dirichlet.pyc in is_trivial(self)
   1177             True
   1178         """
-> 1179         return (self.element() == 0)
   1180 
   1181     def kernel(self):

/home/bober/sage/local/lib/python2.6/site-packages/sage/modular/dirichlet.pyc in element(self)
   1531             M    = P._module
   1532             dlog = P._zeta_dlog
-> 1533             v = M([dlog[x] for x in self.values_on_gens()])
   1534             self.__element = v
   1535             return v

KeyError: -1.00000000000000 - 2.63677968348475e-16*I
sage:
```



---

Comment by bober created at 2011-04-02 01:25:37

The attached patch may fix the issues. (But perhaps some issues remain.)

The main solution is to fix things so that the discrete log table is not used when the base ring is a complex field. (It really isn't needed since the nth root of unity that is chosen will always be e(1/n).)

There are also some small fixes to deal with the gauss sum, and to deal with is_even and is_odd. In the latter case, we again have the problem that we can't test chi(-1) == -1, for example, since things are approximate.

There might be some more issues to fix to make things work well, but all doctests pass for me, so the patch at least doesn't break anything.


---

Comment by bober created at 2011-04-02 01:27:41

Changing status from new to needs_review.


---

Comment by wuthrich created at 2011-04-05 16:24:05

Changing status from needs_review to needs_work.


---

Comment by wuthrich created at 2011-04-05 16:24:05

It looks to me as you attached the printout of an "ls" rather than the ticket in this directory.


---

Comment by bober created at 2011-04-05 18:11:49

Replying to [comment:4 wuthrich]:
> It looks to me as you attached the printout of an "ls" rather than the ticket in this directory.

Oops. Fixed now. 

(Curiously, my bash history contains the lines:

hg export 15468
ls
ls > trac7191.patch
)


---

Comment by bober created at 2011-04-05 18:11:49

Changing status from needs_work to needs_review.


---

Comment by bober created at 2011-04-08 19:06:05

I just discovered a spot where rishi's lcalc wrapper uses

` if chi(-1) == 1 `

to check whether chi is even. This causes problems. (It should use chi.is_even().) Since this problem may well occur elsewhere, I'm going to change this back to "needs work" for now.


---

Comment by bober created at 2011-04-08 19:06:05

Changing status from needs_review to needs_work.


---

Comment by bober created at 2011-04-08 19:06:20

Changing assignee from was to bober.


---

Attachment


---

Comment by bober created at 2011-09-02 10:44:50

Changing status from needs_work to needs_review.


---

Comment by bober created at 2011-09-02 10:44:50

I changed the patch now to include the one-line fix to the lcalc wrapper. I think it is probably not a waste of time for someone to review this now.


---

Comment by johanbosman created at 2011-11-14 18:01:16

Changing status from needs_review to needs_work.


---

Comment by johanbosman created at 2011-11-14 18:01:16

The NotImplementedError message should also be adjusted in the gauss_sum() function as you did in gauss_sum_numerical().

```
sage: G = DirichletGroup(500, base_ring=RR)
sage: G[1].gauss_sum()
---------------------------------------------------------------------------
NotImplementedError                       Traceback (most recent call last)
...
NotImplementedError: Gauss sums only currently implemented when the base ring is a cyclotomic field or QQ.
```


In the function is_odd:

```
       if rings.is_ComplexField(self.base_ring()):
            return abs(self(-1) - self.base_ring()(-1)) < 1.0/self.parent().zeta_order()
```

I do not understand why the rather mysterious expression 1.0/self.parent().zeta_order() is used.  I'd say that the difference is either 0 or 2, so if it's less than 1 in absolute value, this should already be sufficient to test numerically that it is 0.  Similarly for is_even().

And now that I've put you back to work anyway, let's remove the C-style brackets in the if-statement in line 1616. ;).

```
            if(rings.is_ComplexField(C)):
```



---

Attachment


---

Comment by chapoton created at 2013-10-19 20:51:24

Here is a new version with minor changes.

apply trac_7191_v2.patch


---

Comment by chapoton created at 2014-01-07 19:34:26

Here is a git branch
----
New commits:


---

Comment by AlexGhitza created at 2014-04-24 08:02:49

Changing status from needs_work to needs_review.


---

Comment by pbruin created at 2014-04-24 14:17:36

There was a merge conflict with the current development branch.  I also fixed a doctest and made the changes suggested by Johan in comment:9.  If you agree with these, it is a positive review from me.


---

Comment by git created at 2014-05-27 14:39:08

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by pbruin created at 2014-05-27 14:39:24

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2014-05-29 18:54:20

Resolution: fixed
