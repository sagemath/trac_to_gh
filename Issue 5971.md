# Issue 5971: fix dumb error message when modding out by 0: Mod(10,0)

Issue created by migration from https://trac.sagemath.org/ticket/5971

Original creator: was

Original creation time: 2009-05-03 19:09:55

Assignee: somebody

When doing Mod(n,0), either there should be a useful error message, or one should get n back.  The following is no good at all -- one shouldn't get an AttributeError, which is surely due to a bug. 


```
sage: a = Mod(10,0)
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)

    115     cdef IntegerMod_abstract x
--> 116     x = IntegerMod(integer_mod_ring.IntegerModRing(m), n)
    117     if parent is None:
    118         return x

/Users/wstein/build/sage-3.4.2.rc0/local/lib/python2.5/site-packages/sage/rings/integer_mod.so in sage.rings.integer_mod.IntegerMod (sage/rings/integer_mod.c:2730)()
    132     cdef NativeIntStruct modulus
    133     cdef Py_ssize_t res
--> 134     modulus = parent._pyx_order
    135     if modulus.table is not None:
    136         if PY_TYPE_CHECK(value, sage.rings.integer.Integer) or PY_TYPE_CHECK(value, int) or PY_TYPE_CHECK(value, long):

AttributeError: 'sage.rings.integer_ring.IntegerRing_class' object has no attribute '_pyx_order'

```



---

Attachment

based on Sage 4.1.alpha1


---

Comment by kcrisman created at 2009-06-26 14:02:56

Applies fine to 4.1.alpha1 and does what it says.  I like the second doctest.  Unless something goes wrong with docbuild due to the #, all is well.


---

Comment by boothby created at 2009-06-26 23:12:27

Resolution: fixed
