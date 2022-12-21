# Issue 6072: Boundary space for GammaH fails to identify vanishing classes

Issue created by migration from Trac.

Original creator: davidloeffler

Original creation time: 2009-05-18 17:52:59

Assignee: craigcitro

CC:  craigcitro

If G is a congruence subgroup (not containing -1), then cusps of G can "magically" vanish in the space of odd weight boundary symbols when the weight is odd.

Reading the explanation in boundary.py, I think that the explanation there just boils down to that this happens if and only if the cusp is irregular (in the sense that the generator of its stabiliser looks like [-1, h ; 0, -1]). But for the group `GammaH(8, [3])` there are 4 cusps of which 2 are irregular, namely 1/2 and 1/4 -- but the boundary space doesn't realise this. It's possible that I've misunderstood the definitions, but I'm pretty sure that the boundary space is supposed to be dual to the space of Eisenstein series, and that certainly has dimension 2 here.

This is certainly of no great significance at the moment since we don't really have much functionality working for GammaH spaces anyway, but it's still not ideal that the functionality we do have implemented is giving wrong answers.

Craig: I'm ccing you here as I got the impression you wrote most of the GammaH stuff -- do you have any idea what's going on here?


---

Comment by craigcitro created at 2009-05-19 08:37:00

Hi David,

Yep, I'm definitely responsible for this code. There *is* a bug here -- in the case that the sign is 0, and the weight is odd, there are definitely relations I didn't use to determine if a cusp that gets coerced in is 0. (Note that the relation still gets picked up if you're computing with sign equal to 1 or -1.) Luckily, though, the code that's used to compute modular symbols spaces is `_coerce_in_manin_symbol` -- so it wasn't really affecting the resulting modular symbols spaces that were computed. (I had checked the dimensions of these spaces were correct via the dimension formulas, so I would have been a little surprised if they were wrong.)

I think the attached patch should fix this -- let me know if you don't trust it, or if you think it needs more documentation/doctests.


---

Attachment

Sorry it's taken me so long to get around to reviewing this, but it still doesn't seem to quite fix the problem:


```
sage: G = GammaH(4, [])
sage: B3 = G.modular_symbols(weight=3).boundary_space()
sage: [B3(x) for x in G.cusps()]
[[0], 0, [Infinity]]
sage: B3.rank()
3
```


I think the problem is that the check to see whether or not the new cusp class vanishes gets done *after* the cusp is added to `B3._known_cusps`, and the rank method just checks the length of known_cusps. The same happens if instead of explicitly coercing all the cusps of G into B3, you do `B3 = G.modular_symbols(weight=3).boundary_map().codomain()` to get a fully-initialised version.

Another silly minor quibble: if -1 is in G, then the boundary space should clearly be zero in all odd weights, but this doesn't seem to happen: 


```
sage: G = GammaH(10, [9])
sage: B3 = G.modular_symbols(weight=3).boundary_space()
sage: B3(Cusp(1))
sage: [B3(x) for x in G.cusps()]
[[1], 0, [1/4], 0, [1/3], 0, [1/2], 0]
```


Finally, here's another (possibly completely unrelated) bug:

```
sage: G = GammaH(8, [5])
sage: G.modular_symbols(weight=3).boundary_map() 
---------------------------------------------------------------------------                 
AssertionError                            Traceback (most recent call last)                 

/home/david/.sage/temp/groke/13903/_home_david__sage_init_sage_0.py in <module>()

/home/david/sage-4.0.alpha0/local/lib/python2.5/site-packages/sage/modular/modsym/ambient.pyc in boundary_map(self)                                                                     
   1251             # compute boundary map                                                  
   1252             B = self.boundary_space()                                               
-> 1253             I = [B(b) for b in self.basis()]                                        
   1254             W = matrix_space.MatrixSpace(self.base_ring(), len(I), B.rank(), sparse=True)                                                                                       
   1255                                                                                     

/home/david/sage-4.0.alpha0/local/lib/python2.5/site-packages/sage/modular/modsym/boundary.pyc in __call__(self, x)                                                                     
    583             if len(S) == 0:                                                         
    584                 return self(0)                                                      
--> 585             return sum([c*self._coerce_in_manin_symbol(v) for c, v in S])           
    586                                                                                     
    587         elif is_FreeModuleElement(x):

/home/david/sage-4.0.alpha0/local/lib/python2.5/site-packages/sage/modular/modsym/boundary.pyc in _coerce_in_manin_symbol(self, x)
    532         """
    533         i = x.i
--> 534         alpha, beta = x.endpoints(self.level())
    535         if self.weight() == 2:
    536             return self(alpha) - self(beta)

/home/david/sage-4.0.alpha0/local/lib/python2.5/site-packages/sage/modular/modsym/manin_symbols.pyc in endpoints(self, N)
   1758             if N < 1:
   1759                 raise ArithmeticError, "N must be positive"
-> 1760         a,b,c,d = self.lift_to_sl2z()
   1761         return cusps.Cusp(b,d), cusps.Cusp(a,c)
   1762

/home/david/sage-4.0.alpha0/local/lib/python2.5/site-packages/sage/modular/modsym/manin_symbols.pyc in lift_to_sl2z(self, N)
   1735         d += N*m
   1736         g, z1, z2 = arith.XGCD(c,d)
-> 1737         assert g==1
   1738         return [z2, -z1, c, d]
   1739

AssertionError:
```


(This may well be nothing to do with any of this, I just happened to spot it while testing your patch, so feel free to ignore it if it's not relevant).


---

Comment by chapoton created at 2014-03-21 21:18:26

Here is a git branch
----
New commits:


---

Comment by chapoton created at 2017-04-17 09:18:35

why does this needs work ?


---

Comment by davidloeffler created at 2017-04-19 08:14:11

> why does this needs work ?

Because nobody worked on it? 

My comment (from 8 years ago!) clearly points out a corner case of the bug which is not fixed by Craig Citro's patch; nobody has done anything since, except convert the existing partial fix into a Git branch; ergo, it is "needs work".


---

Comment by davidloeffler created at 2018-05-12 21:37:50

I revisited this, after 8 years delay, because this ticket, #7837 and #25268 are sufficiently closely related that it made sense to do them all at once. 

The old code was sometimes failing to determine correctly which cusps are irregular; we now have a method ` is_regular_cusp ` of arithmetic groups that does exactly this (reliably), so I just stripped out the buggy code here and replaced it with calls to that other implementation. I also tweaked the way boundary symbols are represented, avoiding the redundant 0 entries in their coordinate vectors when the relations force a cusp to vanish; this solves the problems noticed here and at #7837 about ` rank()` giving misleading answers.
----
New commits:


---

Comment by davidloeffler created at 2018-05-12 21:37:50

Changing status from needs_work to needs_review.


---

Comment by davidloeffler created at 2018-05-12 21:37:50

Changing priority from minor to major.


---

Comment by chapoton created at 2018-05-13 12:11:05

Changing status from needs_review to positive_review.


---

Comment by chapoton created at 2018-05-13 12:11:05

ok, let it be


---

Comment by vbraun created at 2018-05-15 22:34:01

Resolution: fixed
