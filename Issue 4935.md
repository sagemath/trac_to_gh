# Issue 4935: is_perfect_power leaks

Issue created by migration from https://trac.sagemath.org/ticket/4935

Original creator: mabshoff

Original creation time: 2009-01-04 02:33:12

Assignee: robertwb

I discovered this while playing with #4612.

This is with the old gmp, i.e. not the new eMPIRe, but that also shows roughly the same numbers:

```
sage: get_memory_usage()
790.43359375
sage: time len([a for a in srange(10**5) if not (-a^3).is_perfect_power()])
CPU times: user 0.27 s, sys: 0.03 s, total: 0.30 s
Wall time: 0.31 s
24128
sage: get_memory_usage()
798.4765625
sage: time len([a for a in srange(10**6) if not (-a^3).is_perfect_power()])
CPU times: user 2.84 s, sys: 0.27 s, total: 3.12 s
Wall time: 3.12 s
241224
sage: get_memory_usage()
868.921875
```


Valgrinding this didn't turn up anything useful. Thoughts?

Cheers,

Michael


---

Comment by robertwb created at 2009-01-04 02:52:54

This would almost certainly be a memory leak in mpz_perfect_power_p, as (in this case) (-a^3) is an integer, and the implementation of is_perfect_power is a one-liner.


---

Comment by mabshoff created at 2009-01-04 02:58:19

Replying to [comment:1 robertwb]:
> This would almost certainly be a memory leak in mpz_perfect_power_p, as (in this case) (-a^3) is an integer, and the implementation of is_perfect_power is a one-liner. 

Well, I did run valgrind on it and nothing showed. I will valgrind some pure C code to make 100% sure it isn't [gmp|mpir]. My guess would be that Cython could be involved, but before I point the finger I should have some data.

It seems like Cython is the new scape goat taking that role from Coercion :p

Cheers,

Michael


---

Comment by robertwb created at 2009-01-04 03:08:57

:)

The Cython code looks plenty clean though. 


```
#define __Pyx_PyBool_FromLong(b) ((b) ? (Py_INCREF(Py_True), Py_True) : (Py_INCREF(Py_False), Py_False))

...

static PyObject *__pyx_pf_4sage_5rings_7integer_7Integer_is_perfect_power(PyObject *__pyx_v_self, PyObject *unused) {
  PyObject *__pyx_r;
  PyObject *__pyx_1 = 0;

  /* "/Users/robert/sage/sage-3.1.3/devel/sage-main/sage/rings/integer.pyx":3002
 *             False
 *         """
 *         return mpz_perfect_power_p(self.value)             # <<<<<<<<<<<<<<
 * 
 *     def jacobi(self, b):
 */
  __pyx_1 = __Pyx_PyBool_FromLong(mpz_perfect_power_p(((struct __pyx_obj_4sage_5rings_7integer_Integer *)__pyx_v_self)->value)); if (unlikely(!__pyx_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 3002; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __pyx_r = __pyx_1;
  __pyx_1 = 0;
  goto __pyx_L0;

  __pyx_r = Py_None; Py_INCREF(Py_None);
  goto __pyx_L0;
  __pyx_L1_error:;
  Py_XDECREF(__pyx_1);
  __Pyx_AddTraceback("sage.rings.integer.Integer.is_perfect_power");
  __pyx_r = NULL;
  __pyx_L0:;
  return __pyx_r;
}

```


(Note that much of that gets optimized away at compile time, for example the error branch is never taken).


---

Comment by mabshoff created at 2009-01-04 04:03:03

Well, sorry to disappoint you, but t-perfpow.c from very recent mpir-svn doesn't leak:

```
gmp-mpir-svn1523/src/tests/mpz/.libs$ valgrind --tool=memcheck --leak-resolution=high ./t-perfpow
==31616== Memcheck, a memory error detector.
==31616== Copyright (C) 2002-2007, and GNU GPL'd, by Julian Seward et al.
==31616== Using LibVEX rev 1854, a library for dynamic binary translation.
==31616== Copyright (C) 2004-2007, and GNU GPL'd, by OpenWorks LLP.
==31616== Using valgrind-3.3.1, a dynamic binary instrumentation framework.
==31616== Copyright (C) 2000-2007, and GNU GPL'd, by Julian Seward et al.
==31616== For more details, rerun with: -v
==31616== 
==31616== 
==31616== ERROR SUMMARY: 0 errors from 0 contexts (suppressed: 3 from 1)
==31616== malloc/free: in use at exit: 0 bytes in 0 blocks.
==31616== malloc/free: 375,348 allocs, 375,348 frees, 7,978,732 bytes allocated.
==31616== For counts of detected errors, rerun with: -v
==31616== All heap blocks were freed -- no leaks are possible.
```

So I am starting to blame not-mpir :)

Cheers,

Michael


---

Comment by robertwb created at 2009-01-04 04:42:13

Hmm... perhaps it's just the integer pool filling up? 


```
sage: get_memory_usage()
'415M'
sage: time len([a for a in srange(10**6) if not (-a^3).is_perfect_power()])
CPU times: user 5.68 s, sys: 1.01 s, total: 6.69 s
Wall time: 9.47 s
241224
sage: get_memory_usage()
'431M'
sage: time len([a for a in srange(10**6) if not (-a^3).is_perfect_power()])
CPU times: user 5.55 s, sys: 0.90 s, total: 6.45 s
Wall time: 6.53 s
241224
sage: get_memory_usage()
'431M'
sage: time len([a for a in srange(10**6) if not (-a^3).is_perfect_power()])
CPU times: user 5.58 s, sys: 0.92 s, total: 6.50 s
Wall time: 6.58 s
241224
sage: get_memory_usage()
'431M'
```


And a fresh start


```
----------------------------------------------------------------------
----------------------------------------------------------------------
Loading Sage library. Current Mercurial branch is: bugs
sage: get_memory_usage()
'415M'
sage: time len(srange(10**6))
CPU times: user 0.40 s, sys: 0.16 s, total: 0.56 s
Wall time: 0.57 s
1000000
sage: get_memory_usage()
'431M'
```

| Sage Version 3.2.2, Release Date: 2008-12-18                       |
| Type notebook() for the GUI, and license() for information.        |
So it's something in srange or the integer pool or something... Or the fact that the large number of objects that all get allocated at the same time enlarge the heap (and it never gives it back). 


```
sage: get_memory_usage()
'415M'
sage: len(ZZ.range(10^6))
1000000
sage: get_memory_usage()
'431M'
```


Also


```
sage: get_memory_usage()
'415M'
sage: time len([True for a in (1..10**6) if not (-a^3).is_perfect_power()])
CPU times: user 9.90 s, sys: 0.96 s, total: 10.86 s
Wall time: 10.98 s
241225
sage: get_memory_usage()
'415M'
```


shows that is_perfect_power is clean, so I think it's just a heap with a million live elements that doesn't shrink back down when the list is freed.


---

Comment by mabshoff created at 2009-01-04 04:49:59

Ok, but isn't the integer pool too aggressive here or am I just not getting the idea here? 

To this day I do not understand why we have to change the GMP allocator to use Python memory since if we used C heap all that memory would be returned to the system.

Cheers,

Michael


---

Comment by robertwb created at 2009-01-04 05:13:22

No, I don't think this has anything to do with pools or the gmp allocator. 


```
sage: get_memory_usage()
'415M'
sage: len(range(10^6))
1000000
sage: get_memory_usage()
'423M'
sage: len([float(a) for a in range(10^6)])
1000000
sage: get_memory_usage()
'439M'
sage: len(range(10^7))
10000000
sage: get_memory_usage()
'552M'
```


(Note that int objects have a smaller memory footprint than Integers).

My understanding is that when a new, small, object is allocated, the python memory manager tries to return an already-allocated chunk of the right size out of the heap. If there isn't one, it needs to grow the heap. The "leaking" examples all construct huge lists, so the heap grows to the size of the whole list. When objects are freed, the memory goes back to the heap, but doesn't get freed (just like the integer pool idea). Usually this makes sense, as thousands of ephemeral Python objects are used and collected all the time, and usually the number of objects grows over time. In our case, if we make another huge list, the memory is sitting there pre-allocated just waiting to be used. 

Large (>256 bytes?) allocations are deferred directly to malloc, as are user-requested and external library ones, so this kind of memory does get reclaimed immediately.


---

Comment by mabshoff created at 2009-01-04 19:38:56

Resolution: invalid


---

Comment by mabshoff created at 2009-01-04 19:38:56

Ok, invalid then. Sorry got the noise :(

I will use iterators for testing then in the future.

Cheers,

Michael
