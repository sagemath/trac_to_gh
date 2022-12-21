# Issue 9881: slow random_element() for integer mod ring

Issue created by migration from Trac.

Original creator: dmharvey

Original creation time: 2010-09-09 15:56:20

Assignee: tbd

Sage 4.5.3, 2.6GHz Opteron, Linux:


```
sage: R = Integers(3^20)
sage: timeit("u = R.random_element()")
625 loops, best of 3: 22.5 µs per loop
```


That's about 58000 cycles for each random number. This seems unnecessarily slow. Are the random numbers really that high quality? Compare with the cost for ZZ:

```
sage: timeit("u = ZZ.random_element()")
625 loops, best of 3: 432 ns per loop
```




---

Comment by roed created at 2010-09-23 11:33:38

The distributions are somewhat different: `R.random_element` uses a uniform distribution, while `ZZ.random_element` uses a different one (see its documentation).  But the patch at #9887 speeds up `R.random_element` by a factor of about 7, so I would suggest closing this ticket if that is positively reviewed.


---

Comment by mmezzarobba created at 2014-03-14 17:15:35

The following implementation of `R.random_element()` is 30-40% faster than the existing one (and correctly uses the uniform distribution, according to the docstring of `ZZ.random_element()`):

```
    def random_element(self, bound=None):
        if bound is None:
            return self(ZZ.random_element(0, self.__order-1))
        else:
            return commutative_ring.CommutativeRing.random_element(self, bound)
```

6.2.beta4:

```
sage: %timeit R.random_element()
100000 loops, best of 3: 5.67 µs per loop
```

With patch:

```
sage: %timeit R.random_element()
100000 loops, best of 3: 3.53 µs per loop
```

But I don't understand where the time goes:

```
sage: foo = None
sage: %timeit if foo is None: ZZ.random_element(0, R.order()-1)
1000000 loops, best of 3: 809 ns per loop
```



---

Comment by ppurka created at 2014-03-22 07:45:51

Replying to [comment:2 mmezzarobba]:
> But I don't understand where the time goes:

All of the time goes in returning an element of the integer mod ring.

```
sage: R = Integers(3^20)
sage: a = 3^20; b = a+1
sage: %timeit ZZ.random_element(-a, b)
1000000 loops, best of 3: 705 ns per loop
sage: %timeit R(ZZ.random_element(-a, b))
100000 loops, best of 3: 2.07 us per loop


sage: c = a-1
sage: %timeit R(c)
1000000 loops, best of 3: 749 ns per loop
sage: c = (a-1)/2
sage: %timeit R(c)
100000 loops, best of 3: 7.71 us per loop
```



---

Comment by mmezzarobba created at 2014-03-22 10:51:02

Replying to [comment:3 ppurka]:
> Replying to [comment:2 mmezzarobba]:
> > But I don't understand where the time goes:
> 
> All of the time goes in returning an element of the integer mod ring.

Thanks for your reply, and... sorry for being thick, but I still don't understand! I get:

```
sage: %timeit ZZ.random_element(0, R.order()-1)
1000000 loops, best of 3: 650 ns per loop
sage: a = (R.order()-1)
sage: %timeit R(a)
1000000 loops, best of 3: 325 ns per loop
sage: a = (R.order()-1)//2
sage: %timeit R(a)
1000000 loops, best of 3: 324 ns per loop
```

so I would hope for a total running time of the order of 1 µs + some overhead for my function, but I get:

```
sage: %timeit R.random_element()
100000 loops, best of 3: 3.45 µs per loop
```



---

Comment by mmezzarobba created at 2014-03-22 12:31:07

Other option (no time to clean it up):

```
diff --git a/src/sage/rings/finite_rings/integer_mod.pxd b/src/sage/rings/finite_rings/integer_mod.pxd
index 8067647..358c902 100644
--- a/src/sage/rings/finite_rings/integer_mod.pxd
+++ b/src/sage/rings/finite_rings/integer_mod.pxd
`@``@` -17,6 +17,7 `@``@` cdef class IntegerMod_abstract(FiniteRingElement):
     cdef _new_c_from_long(self, long value)
     cdef void set_from_mpz(self, mpz_t value)
     cdef void set_from_long(self, long value)
+    cdef void _randomize(self)
     cdef bint is_square_c(self) except -2
     cpdef bint is_one(self)
     cpdef bint is_unit(self)
diff --git a/src/sage/rings/finite_rings/integer_mod.pyx b/src/sage/rings/finite_rings/integer_mod.pyx
index a5d3209..bfb121a 100644
--- a/src/sage/rings/finite_rings/integer_mod.pyx
+++ b/src/sage/rings/finite_rings/integer_mod.pyx
`@``@` -1,3 +1,4 `@``@`
+# cython: profile=True
 r"""
 Elements of `\ZZ/n\ZZ`
 
`@``@` -69,6 +70,8 `@``@` TESTS::
 
 include "sage/ext/interrupt.pxi"  # ctrl-c interrupt block support
 include "sage/ext/stdsage.pxi"
+include "sage/ext/gmp.pxi"
+include "sage/ext/random.pxi"
 
 from cpython.int cimport *
 from cpython.list cimport *
`@``@` -185,6 +188,13 `@``@` def IntegerMod(parent, value):
     else:
         return IntegerMod_gmp(parent, value)
 
+def random_IntegerMod(parent):
+    # TODO: implement and use element_class instead?
+    cdef IntegerMod_abstract zero = parent.zero_element()
+    cdef IntegerMod_abstract tmp = zero._new_c_from_long(0)
+    tmp._randomize()
+    return tmp
+
 def is_IntegerMod(x):
     """
     Return ``True`` if and only if x is an integer modulo
`@``@` -322,6 +332,9 `@``@` cdef class IntegerMod_abstract(FiniteRingElement):
     cdef void set_from_long(self, long value):
         raise NotImplementedError, "Must be defined in child class."
 
+    cdef void _randomize(self):
+        pass # FIXME
+
     def __abs__(self):
         """
         Raise an error message, since ``abs(x)`` makes no sense
`@``@` -1706,6 +1719,9 `@``@` cdef class IntegerMod_gmp(IntegerMod_abstract):
         if value < 0 or mpz_cmp_si(self.__modulus.sageInteger.value, value) >= 0:
             mpz_mod(self.value, self.value, self.__modulus.sageInteger.value)
 
+    cdef void _randomize(self):
+        mpz_urandomm(self.value, current_randstate().gmp_state, self.__modulus.sageInteger.value)
+
     cdef mpz_t* get_value(IntegerMod_gmp self):
         return &self.value
 
diff --git a/src/sage/rings/finite_rings/integer_mod_ring.py b/src/sage/rings/finite_rings/integer_mod_ring.py
index 3ed643b..c11db8a 100644
--- a/src/sage/rings/finite_rings/integer_mod_ring.py
+++ b/src/sage/rings/finite_rings/integer_mod_ring.py
`@``@` -1224,10 +1224,10 `@``@` class IntegerModRing_generic(quotient_ring.QuotientRing_generic):
             sage: R.random_element()
             2
         """
-        if not (bound is None):
+        if bound is None:
+            return integer_mod.random_IntegerMod(self)
+        else:
             return commutative_ring.CommutativeRing.random_element(self, bound)
-        a = random.randint(0,self.order()-1)
-        return self(a)
 
     #######################################################
     # Suppose for interfaces
```



```
sage: %timeit R.random_element()
1000000 loops, best of 3: 609 ns per loop
```



---

Comment by ppurka created at 2014-03-23 08:52:31

Replying to [comment:4 mmezzarobba]:
> Thanks for your reply, and... sorry for being thick, but I still don't understand! I get:
> {{{
> sage: %timeit ZZ.random_element(0, R.order()-1)
> 1000000 loops, best of 3: 650 ns per loop
> sage: a = (R.order()-1)
> sage: %timeit R(a)
> 1000000 loops, best of 3: 325 ns per loop
> sage: a = (R.order()-1)//2
> sage: %timeit R(a)
> 1000000 loops, best of 3: 324 ns per loop
> }}}
> so I would hope for a total running time of the order of 1 µs + some overhead for my function

With the `//` operator you are actually getting Sage integers, whereas I was getting Sage rationals with the `/` operator. That explains why the coercion to `Integers` was taking so much time.

Perhaps the best way is to use gmp as you have done above.


---

Comment by mmezzarobba created at 2014-03-23 09:39:11

Replying to [comment:6 ppurka]:
> With the `//` operator you are actually getting Sage integers, whereas I was getting Sage rationals with the `/` operator. That explains why the coercion to `Integers` was taking so much time.

Yes, I noticed that, but I thought you were using rationals on purpose. What I would like to understand is where the ~2 µs of overhead in the version using `self(ZZ.random_element(0, self.__order-1))` come from...
