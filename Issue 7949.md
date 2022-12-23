# Issue 7949: Bit-shifts in Z/(n)

Issue created by migration from https://trac.sagemath.org/ticket/7949

Original creator: spancratz

Original creation time: 2010-01-16 17:43:34

Assignee: spancratz

Keywords: bit shift, integer mod ring

Currently, some code for bit-shifts in Z/(n) looks like


```
    def __lshift__(IntegerMod_gmp self, int right):
        ...
        cdef IntegerMod_gmp x
        x = self._new_c()
        mpz_mul_2exp(x.value, self.value, right)
        mpz_fdiv_r(x.value, x.value, self.__modulus.sageInteger.value)
        return x
```


where the method ``mpz_mul_2exp`` expect an ``unsigned long``.  Negative values of ``right`` thus cause undesired integral promotion.


---

Comment by spancratz created at 2010-01-16 18:14:34

Looking at the related methods for types ``IntegerMod_int``, note that

```
    def __rshift__(IntegerMod_int self, int right):
        ...
        return self._new_c(self.ivalue >> right)
```

Here, the code ignores right shifts with negative values of ``right``, in which case one has to take the modulus.

The patch (to be attached) will address this, too.


---

Comment by spancratz created at 2010-01-16 18:36:18

For each of the three types for moduli (32-bit, 64-bit, mpz_t), the patch provides a method ``shift``, which in turns is called by the methods ``__lshift__`` and ``__rshift__``.

Finally, in the previous code the doctests with modulus `2^{31}-1` did not test any of the 64-bit code because of code in the method ``def __init__(NativeIntStruct self, sage.rings.integer.Integer z)`` in the file ``integer_mod.pyx``.  There, a comparisons were carried out with ``<`` rather than ``<=``, which this patch changes, too.


---

Attachment


---

Comment by spancratz created at 2010-01-16 18:55:12

Changing status from new to needs_review.


---

Attachment

Additional patch (more doctests)


---

Comment by spancratz created at 2010-01-19 03:00:05

This patch adds documentation, hopefully this will do.


---

Comment by boothby created at 2010-01-19 07:25:03

looks good to me.  I tested on 64-bit.


---

Comment by boothby created at 2010-01-19 07:25:03

Changing status from needs_review to positive_review.


---

Comment by mvngu created at 2010-01-22 21:36:28

Resolution: fixed
