# Issue 941: creating Z_p can take massive amounts of RAM.  Why?

Issue created by migration from https://trac.sagemath.org/ticket/941

Original creator: was

Original creation time: 2007-10-20 09:54:30

Assignee: somebody


```
David,

I'm getting rid of all the lame "sage.:"'s in SAGE.  In the padics,
we have this doctest:

sage: Zp(next_prime(10^50), 10000)
100000000000000000000000000000000000000000000000151-adic Ring with capped relative precision 10000

Just trying to run it on my laptop is a disaster, since:
 
sage: get_memory_usage()
2320.26171875

Why does it use so much memory?

I will change the doctest to 1000 instead of 10000, which
hardly takes any ram.  

Why is *so* much ram needed though?!
```



---

Comment by mabshoff created at 2007-10-20 10:59:28

Hello,

gmp_realloc goes nuts. See

http://sage.math.washington.edu/home/mabshoff/massif.12284.ps

Also from http://sage.math.washington.edu/home/mabshoff/massif.12284.txt we have:

```
---------------------------------
Context accounted for  9.6% of measured spacetime
  0x5FA6783: __gmpz_mul (in /tmp/Work-mabshoff/sage-2.8.7-debian64-x86_64-Linux/local/lib/libgmp.so.3.4.1)
  0xE02587F: __pyx_f_py_12pow_computer_17PowComputer_class___init__ (pow_computer.c:2481)

Called from:
   9.6% : 0x459220: type_call (typeobject.c:436)

---------------------------------
Context accounted for  9.4% of measured spacetime
  0x5FA9D10: __gmpz_realloc (in /tmp/Work-mabshoff/sage-2.8.7-debian64-x86_64-Linux/local/lib/libgmp.so.3.4.1)
  0x5FAA7E2: __gmpz_set (in /tmp/Work-mabshoff/sage-2.8.7-debian64-x86_64-Linux/local/lib/libgmp.so.3.4.1)

Called from:
   9.5% : 0xE0257B4: __pyx_f_py_12pow_computer_17PowComputer_class___init__ (pow_computer.c:2503)

  and 3 other insignificant places

---------------------------------
```

So somebody ought to check out pow_computer_17PowComputer_class___init__

 Cheers,

Michael


---

Comment by mabshoff created at 2007-10-20 11:09:20

I would assume cache_limit is involved:

```
    def __init__(self, Integer prime, unsigned long cache_limit):
        cdef Py_ssize_t i
        cdef Integer x

        self._cache_limit = cache_limit
        self.prime = prime
        self.in_field = 0

        #self.dense_list_Integer = PyList_New(self.cache_limit + 1)
        self.dense_list_Integer = []

        mpz_init_set_ui(self.dense_list[0], 1)
        x = PY_NEW(Integer)
        mpz_set_ui(x.value, 1)
        #PyList_SET_ITEM(self.dense_list_Integer, 0, x)
        self.dense_list_Integer.append(x)

        mpz_init_set(self.dense_list[1], prime.value)
        x = PY_NEW(Integer)
        mpz_set(x.value, prime.value)
        #PyList_SET_ITEM(self.dense_list_Integer, 1, x)
        self.dense_list_Integer.append(x)

        for i from 2 <= i <= cache_limit:
            mpz_init(self.dense_list[i])
            mpz_mul(self.dense_list[i], self.dense_list[i - 1], prime.value)
            x = PY_NEW(Integer)
            mpz_set(x.value, self.dense_list[i])
            #PyList_SET_ITEM(self.dense_list_Integer, i, x)
            self.dense_list_Integer.append(x)
        mpz_set(self.modulus, self.dense_list[cache_limit])
        self._initialized = 1
```

specifically the line

```
mpz_set(x.value, self.dense_list[i])
```

because valgrind says:

```
==12621== 1,038,246,360 bytes in 9,999 blocks are still reachable in loss record 2,030 of 2,031
==12621==    at 0x4A1BC36: realloc (vg_replace_malloc.c:420)
==12621==    by 0x5FACD10: __gmpz_realloc (in /tmp/Work-mabshoff/sage-2.8.7-debian64-x86_64-Linux/local/lib/libgmp.so.3.4.1)
==12621==    by 0x5FAD7E2: __gmpz_set (in /tmp/Work-mabshoff/sage-2.8.7-debian64-x86_64-Linux/local/lib/libgmp.so.3.4.1)
==12621==    by 0xE4287B4: __pyx_f_py_12pow_computer_17PowComputer_class___init__ (pow_computer.c:2503)
==12621==    by 0x459220: type_call (typeobject.c:436)
==12621==    by 0x415522: PyObject_Call (abstract.c:1860)
==12621==    by 0x47C850: PyEval_CallObjectWithKeywords (ceval.c:3433)
==12621==    by 0xE426C81: __pyx_f_py_12pow_computer_PowComputer (pow_computer.c:3376)
==12621==    by 0x483031: PyEval_EvalFrameEx (ceval.c:3564)
==12621==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)
==12621==    by 0x4CE527: function_call (funcobject.c:517)
==12621==    by 0x415522: PyObject_Call (abstract.c:1860)
==12621==
==12621==
==12621== 1,038,278,736 bytes in 9,999 blocks are still reachable in loss record 2,031 of 2,031
==12621==    at 0x4A1BB35: malloc (vg_replace_malloc.c:207)
==12621==    by 0x5FA9783: __gmpz_mul (in /tmp/Work-mabshoff/sage-2.8.7-debian64-x86_64-Linux/local/lib/libgmp.so.3.4.1)
==12621==    by 0xE42887F: __pyx_f_py_12pow_computer_17PowComputer_class___init__ (pow_computer.c:2481)
==12621==    by 0x459220: type_call (typeobject.c:436)
==12621==    by 0x415522: PyObject_Call (abstract.c:1860)
==12621==    by 0x47C850: PyEval_CallObjectWithKeywords (ceval.c:3433)
==12621==    by 0xE426C81: __pyx_f_py_12pow_computer_PowComputer (pow_computer.c:3376)
==12621==    by 0x483031: PyEval_EvalFrameEx (ceval.c:3564)
==12621==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)
==12621==    by 0x4CE527: function_call (funcobject.c:517)
==12621==    by 0x415522: PyObject_Call (abstract.c:1860)
==12621==    by 0x41BC42: instancemethod_call (classobject.c:2497)
```

Cheers,

Michael


---

Comment by dmharvey created at 2007-10-20 15:29:09

This could be related to #919.


---

Comment by was created at 2007-10-20 17:43:37

David roe says this *is* just a dupe of #919.


---

Comment by was created at 2007-10-20 17:59:35

Resolution: fixed
