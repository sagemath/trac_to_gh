# Issue 5970: [with patch, needs review] Weak references in Polynomial Ring cache

Issue created by migration from https://trac.sagemath.org/ticket/5970

Original creator: SimonKing

Original creation time: 2009-05-03 07:21:37

Assignee: malb

CC:  jpflori zimmerma vbraun

Keywords: polynomial ring cache weak reference

At http://groups.google.com/group/sage-support/browse_thread/thread/ef01dae47c835137 a memory leak was reported.

Reason for the leak: Many different polynomial rings are created, but used only once. But since we want to have unique parents, they are all cached and thus prevented from deletion.

As Robert pointed out, using weak references enables us to both have unique parents and garbage collection.

With the patch, that should at least apply to sage 3.4.1.rc3, one can do

```
sage: for p in primes(2,1000000):
....:     R.<x,y,z> = GF(p)[]
```

without running into memory problems.


---

Attachment

Introduce Weak Reference to the cache of PolynomialRing


---

Comment by mabshoff created at 2009-05-03 07:49:22

Ooops, but this does seem to expose some problems:

```
        sage -t -long devel/sage/sage/rings/number_field/number_field.py # Segfault
        sage -t -long devel/sage/sage/rings/tests.py # Segfault
        sage -t -long devel/sage/sage/rings/number_field/number_field_rel.py # Segfault
        sage -t -long devel/sage/sage/rings/number_field/number_field_element.pyx # Segfault
        sage -t -long devel/sage/sage/rings/residue_field.pyx # Segfault
        sage -t -long devel/sage/sage/rings/number_field/number_field_ideal_rel.py # Segfault
        sage -t -long devel/sage/sage/rings/number_field/morphism.py # Segfault
        sage -t -long devel/sage/sage/rings/polynomial/polynomial_singular_interface.py # Segfault
        sage -t -long devel/sage/sage/rings/number_field/unit_group.py # Segfault
        sage -t -long devel/sage/sage/rings/number_field/small_primes_of_degree_one.py # Segfault
        sage -t -long devel/sage/doc/en/bordeaux_2008/nf_orders.rst # Segfault
        sage -t -long devel/sage/sage/rings/number_field/maps.py # Segfault
        sage -t -long devel/sage/sage/schemes/generic/affine_space.py # Segfault
```

And something this low level will definitely *not* go into 3.4.2 at this stage. 

Cheers,

Michael


---

Comment by AlexGhitza created at 2009-05-03 08:02:03

In case this might help somebody working on this, I've attached a small file with test functions for checking the memory usage for loops with elliptic curve, plane curves, and just polynomial rings.  It should be fairly easy to use:


```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: attach test.sage
sage: test_poly_leak(2^17)
271.75390625
```

| Sage Version 3.4.2.rc0, Release Date: 2009-04-30                   |
| Type notebook() for the GUI, and license() for information.        |
This indicates that the memory usage after the loop is 271MB more than before.

Note also that if you run different tests one after the other you can see, e.g. how much of the leakage in elliptic curves is "independent" of the polynomial ring issue:


```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: attach test.sage
sage: test_poly_leak(2^17)
271.73046875
sage: test_ec_leak(2^17)
53.10546875
```



---

Attachment

simple-minded test suite


---

Comment by SimonKing created at 2009-05-03 08:51:59

Replying to [comment:1 mabshoff]:
> Ooops, but this does seem to expose some problems:

Sorry, I did not do any tests, since I thought that weak references Just Work (c), and so the change from a dictionary to a WeakValueDictionary would be almost trivial.

> And something this low level will definitely *not* go into 3.4.2 at this stage. 

Again sorry. Since I thought it is almost trivial, I concluded it could easily be in the next distribution.

If weak references break cython code at a very fundamental level then I see _no chance_ for my approach to work, unless Cython changes.

Won't fix, then?


---

Comment by mabshoff created at 2009-05-03 09:00:57

Changing priority from major to blocker.


---

Comment by mabshoff created at 2009-05-03 09:00:57

Replying to [comment:3 SimonKing]:
> Replying to [comment:1 mabshoff]:
> > Ooops, but this does seem to expose some problems:
> 
> Sorry, I did not do any tests, since I thought that weak references Just Work (c), and so the change from a dictionary to a WeakValueDictionary would be almost trivial.

Hehe, I hope you will remember this now :)

> > And something this low level will definitely *not* go into 3.4.2 at this stage. 
> 
> Again sorry. Since I thought it is almost trivial, I concluded it could easily be in the next distribution.

This stems from long experience that every even trivial fix has a non-zero chance of breaking things. Weak references are particularly troublesome in this context. And 3.4.2 was supposed to be out two days ago and now William and I will fix the last couple issues today and push out 3.4.2.final, so no potentially risky patches. I can valgrind this in some 4.0.alphaX (assuming the segfaults go away). 

> If weak references break cython code at a very fundamental level then I see _no chance_ for my approach to work, unless Cython changes.
> 
> Won't fix, then?

No, as mentioned in sage-support RobertWB pointed out some other ticket as guideline to what is wrong.

This patch does not fix the problem the reported in the thread at http://groups.google.com/group/sage-support/t/ef01dae47c835137 reported, but it seems to fix something else or is part of the fix to get #5949 resolved, so lets keep this open for now. It seems to be a valuable patch.

Cheers,

Michael

Cheers,

Michael


---

Comment by SimonKing created at 2009-05-03 09:05:57

At http://docs.python.org/library/weakref.html they say:
  Caution: Because a WeakKeyDictionary is built on top of a Python dictionary, it must not change size when iterating over it. This can be difficult to ensure for a WeakKeyDictionary because actions performed by the program during iteration may cause items in the dictionary to vanish “by magic” (as a side effect of garbage collection).

Can this be part of the trouble with my patch?


---

Comment by was created at 2009-06-15 23:29:19

Changing priority from blocker to critical.


---

Comment by was created at 2009-06-15 23:29:19

If we've released for 2 months without fixing this, it doesn't make sense to keep it as a blocker. Note that the lisp interface is in fact 100% completely broken right now.


---

Comment by malb created at 2009-08-25 23:44:01

slightly safer weakref patch


---

Attachment

The attached patch uses weakrefs for multivariate polynomials but not for univariate polynomials (we still use the same `_cache` object to hold both though). It seems the SIGSEGV is due to some Pari issue so the patch seems safe at first sight (famous last words). I will post debug info in a minute.


---

Comment by malb created at 2009-08-25 23:49:45

Valgrind output for `-O0 -ggdb`:


```
==27448== Invalid write of size 8
==27448==    at 0xA436E60: reset_traps (init.c:510)
==27448==    by 0xA438A5B: err_leave (init.c:984)
==27448==    by 0x11674DE6: __pyx_f_4sage_4libs_4pari_3gen_12PariInstance_GEN_to_str (gen.c:39989)
==27448==    by 0x116048BD: __pyx_pf_4sage_4libs_4pari_3gen_3gen___repr__ (gen.c:3971)
==27448==    by 0x44D91E: _PyObject_Str (object.c:424)
==27448==    by 0x44D9D2: PyObject_Str (object.c:445)
==27448==    by 0x45A0D9: string_new (stringobject.c:4075)
==27448==    by 0x4682D2: type_call (typeobject.c:731)
==27448==    by 0x41A95C: PyObject_Call (abstract.c:2492)
==27448==    by 0x49C3FE: PyEval_EvalFrameEx (ceval.c:3917)
==27448==    by 0x4A0908: PyEval_EvalCodeEx (ceval.c:2968)
==27448==    by 0x49EFC7: PyEval_EvalFrameEx (ceval.c:3802)
==27448==    by 0x4A0908: PyEval_EvalCodeEx (ceval.c:2968)
==27448==    by 0x4F74DC: function_call (funcobject.c:524)
==27448==    by 0x41A95C: PyObject_Call (abstract.c:2492)
==27448==    by 0x4222D3: instancemethod_call (classobject.c:2579)
==27448==    by 0x41A95C: PyObject_Call (abstract.c:2492)
==27448==    by 0xB7DBC1F: __pyx_pf_4sage_9structure_11sage_object_10SageObject___repr__ (sage_object.c:1387)
==27448==    by 0x41A95C: PyObject_Call (abstract.c:2492)
==27448==    by 0x4991B5: PyEval_CallObjectWithKeywords (ceval.c:3575)
==27448==    by 0x47118D: slot_tp_repr (typeobject.c:5295)
==27448==    by 0x44D91E: _PyObject_Str (object.c:424)
==27448==    by 0x45F3F5: PyString_Format (stringobject.c:4848)
==27448==    by 0x41AFB0: binary_op1 (abstract.c:917)
==27448==    by 0x41D97D: PyNumber_Remainder (abstract.c:969)
==27448==  Address 0x5c5bdd8 is 0 bytes inside a block of size 424 free'd
==27448==    at 0x4C2261F: free (vg_replace_malloc.c:323)
==27448==    by 0xA4379AB: pari_close_opts (init.c:715)
==27448==    by 0xA437A4E: pari_close (init.c:729)
==27448==    by 0x1166D250: __pyx_pf_4sage_4libs_4pari_3gen_12PariInstance__unsafe_deallocate_pari_stack (gen.c:36617)
==27448==    by 0x49F050: PyEval_EvalFrameEx (ceval.c:3690)
==27448==    by 0x4A0908: PyEval_EvalCodeEx (ceval.c:2968)
==27448==    by 0x49EFC7: PyEval_EvalFrameEx (ceval.c:3802)
==27448==    by 0x4A0908: PyEval_EvalCodeEx (ceval.c:2968)
==27448==    by 0x4A0A21: PyEval_EvalCode (ceval.c:522)
==27448==    by 0x4C03AB: PyRun_FileExFlags (pythonrun.c:1335)
==27448==    by 0x4C06DA: PyRun_SimpleFileExFlags (pythonrun.c:931)
==27448==    by 0x416215: Py_Main (main.c:599)
==27448==    by 0x56EA5C5: (below main) (in /lib/libc-2.9.so)
```



---

Comment by malb created at 2009-08-25 23:50:21

Just to make sure, this backtrace is not with the patch I just attached but with the original patch.


---

Comment by malb created at 2009-08-26 00:03:26

Mhh, from the changelog it seems caching was disabled because of a SIGSEGV in matrix2.pyx. I cannot reproduce it though.


---

Comment by malb created at 2009-08-26 09:56:24

I am having trouble to reproduce the segfault in `matrix2.pyx`, cf.

  http://hg.sagemath.org/sage-main/annotate/b4f33dc4908b/sage/rings/polynomial/polynomial_ring_constructor.py#337

William, do you recall on which platform you saw it?


---

Comment by SimonKing created at 2009-12-13 23:22:31

Hi!

I almost forgot this ticket. But now, it hit me while working at #7580 (I had the impression I got a memory leak there, but in fact the Polynomial Ring cache just contains more and more unused items).

Martin, since your patch is quite different from my original suggestion, I guess that I am allowed to be referee? Or must it be someone else?

Cheers,
Simon


---

Comment by malb created at 2009-12-14 00:36:04

Yes, you are okay to review it. Make sure you push it hard, try to make it crash etc. :)


---

Comment by SimonKing created at 2009-12-15 16:33:34

This is not a review yet, but some first tests.

There is some progress. Consider the following code snipped (slightly modifying Alex' code):

```
def test_poly_leak(upper):
    a = get_memory_usage()
    c = 0
    for p in prime_range(upper):
        c+=1
        R.<x, y, z> = PolynomialRing(GF(p), 3)
    b = get_memory_usage()
    return (b - a)/c
```


So, the average memory allocation for each created polynomial ring is counted.

Result on sage.math:

```
sage: attach test.sage
sage: test_poly_leak(100000)
0.03225588380942452
```

which I can confirm on my computer with original 4.3.rc0.

With the patch, one has

```
sage: attach test.sage
sage: test_poly_leak(100000)
0.0072749426605504585
```


I did not yet try to crash the patch intentionally. However, I did some indirect stress tests. Namely, I did some series of random examples of Symmetric Groebner bases (this is about infinite polynomial rings, see #7580). Here, many _finite_ polynomial rings are created. There was no segfault or so, which I take as a good sign. 

So long,

Simon


---

Comment by SimonKing created at 2010-02-08 18:52:55

Hi!

Taking the `test.sage` file, modifying it by scaling the output by the number of examples, I obtain with sage-4.3.2:


```
sage: attach test.sage
sage: %time test_poly_leak(10^5)
CPU times: user 9.38 s, sys: 0.24 s, total: 9.62 s
Wall time: 9.63 s
0.032462354696622182
sage: %time test_ec_leak(10^5)
CPU times: user 39.26 s, sys: 0.26 s, total: 39.51 s
Wall time: 39.52 s
0.021538141944734097
sage: %time test_pc_leak(10^5)
CPU times: user 14.63 s, sys: 0.05 s, total: 14.68 s
Wall time: 14.70 s
0.0056423158621768136
```

With the patch (that applies, though with a warning), I obtain:


```
sage: attach test.sage
sage: %time test_poly_leak(10^5)
CPU times: user 8.01 s, sys: 0.07 s, total: 8.08 s
Wall time: 8.12 s
0.0073502821361551294
sage: %time test_ec_leak(10^5)
CPU times: user 49.45 s, sys: 0.34 s, total: 49.79 s
Wall time: 49.86 s
0.047167052267987487
sage: %time test_pc_leak(10^5)
CPU times: user 14.94 s, sys: 0.08 s, total: 15.02 s
Wall time: 15.08 s
0.005620324880108424
```

Now that's kind of strange. In one of the three tests, there is an improvement in both memory and CPU consumption, in one example more or less nothing changes, and in one example there is a regression in both memory and CPU.

At least, for quite a while I did heavy polynomial computations, involving the temporary creation of many polynomial rings. It never crashed.

So, I would give it a positive review, if there wouldn't be the regression in one of the tests.

Can you explain why this regression occurs?

Best regards,

Simon


---

Comment by SimonKing created at 2010-02-08 18:52:55

Changing status from needs_review to needs_info.


---

Comment by malb created at 2010-02-09 17:50:33

First, I can reproduce your results:

*without patch*

```python
sage: %time test_poly_leak(10^5)
CPU times: user 11.11 s, sys: 0.31 s, total: 11.43 s
Wall time: 11.84 s
311.71875
sage: %time test_ec_leak(10^5)
CPU times: user 46.12 s, sys: 0.27 s, total: 46.39 s
Wall time: 47.27 s
206.26953125
sage: %time test_pc_leak(10^5)
CPU times: user 16.95 s, sys: 0.08 s, total: 17.03 s
Wall time: 17.64 s
54.1328125
```


*with patch*

```python
sage: %time test_poly_leak(10^5)
CPU times: user 9.14 s, sys: 0.10 s, total: 9.25 s
Wall time: 9.58 s
70.53125
sage: %time test_ec_leak(10^5)
CPU times: user 57.96 s, sys: 0.50 s, total: 58.46 s
Wall time: 59.63 s
452.3671875
sage: %time test_pc_leak(10^5)
CPU times: user 17.03 s, sys: 0.07 s, total: 17.10 s
Wall time: 17.53 s
54.23046875
```


I would assume this is due to the fact that the elliptic curve constructor does its own hashing somewhere (someone more familiar with this area might want to comment on that) which prevents the GC from collecting the unused polynomial rings. Also, since weak references need to keep track of more information I find it plausible that each weak reference has some memory overhead. Since we cannot free the unused polynomial rings this overhead accumulates.

Maybe the elliptic curve constructor should use weak references as well?


---

Comment by SimonKing created at 2011-01-18 08:23:29

I'd like to revive that ticket.

With `sage-4.6.2.alpha0` and the tickets from #8611, #10467 and #10496 (all with positive review), I obtain:


```
sage: attach test.sage
sage: %time test_poly_leak(10^5)
CPU times: user 11.63 s, sys: 0.16 s, total: 11.79 s
Wall time: 11.85 s
330.4296875
sage: %time test_ec_leak(10^5)
CPU times: user 41.47 s, sys: 0.14 s, total: 41.61 s
Wall time: 42.11 s
193.3828125
sage: %time test_pc_leak(10^5)
CPU times: user 13.24 s, sys: 0.04 s, total: 13.29 s
Wall time: 13.29 s
57.25390625
```



Additionally applying Martin's patch from here, one has

```
sage: attach test.sage
sage: %time test_poly_leak(10^5)
CPU times: user 9.09 s, sys: 0.06 s, total: 9.14 s
Wall time: 9.26 s
77.1015625
sage: %time test_ec_leak(10^5)
CPU times: user 51.72 s, sys: 0.22 s, total: 51.94 s
Wall time: 52.49 s
448.65234375
sage: %time test_pc_leak(10^5)
CPU times: user 13.64 s, sys: 0.03 s, total: 13.68 s
Wall time: 13.85 s
57.796875
```


So, the situation has not changed: We need to look into the elliptic curves code.


---

Comment by SimonKing created at 2011-01-18 08:49:39

Now I really wonder whether this ticket is relevant at all.

If I understand correctly, the purpose of this ticket is to use weak references, so that unused polynomial rings can be removed from the cache. But the "test suite" in `test.sage` is not affected from the length of the cache:

```
sage: attach test.sage
sage: from sage.rings.polynomial.polynomial_ring_constructor import _cache
sage: len(_cache)
16
sage: %time test_poly_leak(10^5)
CPU times: user 11.06 s, sys: 0.13 s, total: 11.18 s
Wall time: 11.19 s
330.40625
sage: len(_cache)
9608
sage: %time test_ec_leak(10^5)
CPU times: user 27.01 s, sys: 0.11 s, total: 27.12 s
Wall time: 27.13 s
192.51171875
sage: len(_cache)
9608
```


The memory consumption depends on applying the patch. But `len(_cache)` is the same, with or without the patch.

Also, the original problem

```
sage: for p in primes(2,1000000):
....:     print get_memory_usage()
....:     R.<x,y,z> = GF(p)[]
```

does not seem to be seriously affected by the patch (at least when one has the patches from  #8611, #10467 and #10496 applied on top of `sage-4.6.2.alpha0`.

Thoughts?


---

Comment by SimonKing created at 2011-12-21 20:13:39

Changing status from needs_info to needs_review.


---

Comment by SimonKing created at 2011-12-21 20:13:39

This is related with a couple of other tickets that aim at using weak references:

 * #11521 uses weak references for the cache of homsets.
 * #715, which aims at using weak references for the coercion cache.

I think the whole project only makes sense if _all three_ approaches are simultaneously used. Two of them will not be enough.

Currently, I test on top of #11521 and some preliminary patch for #715, whether it is now possible to simply use a `WeakValueDictionary`. If it still doesn't then we should revive Martin's patch.


---

Comment by SimonKing created at 2011-12-21 20:13:48

Changing status from needs_review to needs_work.


---

Comment by SimonKing created at 2011-12-21 20:29:43

Even using all three techniques is not enough, as I found out with the example from the ticket description.


---

Comment by SimonKing created at 2011-12-21 21:34:55

I wonder why the example leaks, though. With the patches from #11521 and a not-yet-published patch for #715, I obtain:

```
sage: import gc
sage: from sage.rings.finite_rings.finite_field_base import is_FiniteField
sage: K = GF(151)
sage: predicate = lambda x: is_FiniteField(x) and x.order() == 151
sage: del K
sage: gc.collect()
174
sage: [bla for bla in gc.get_objects() if predicate(bla)]
[]
```


So, prime fields do not seem to leak.

```
sage: from sage.rings.polynomial.multi_polynomial_ring import is_MPolynomialRing
sage: K = GF(151)
sage: P = K['x','y','z']
sage: del P
sage: gc.collect()
33
sage: predicate = lambda x: is_MPolynomialRing(x) and x.variable_names()==['x','y','z'] and x.base_ring() is K
sage: [bla for bla in gc.get_objects() if predicate(bla)]
[]
```


So, where does the leak come from??? The example from the ticket description does use polynomial rings over finite prime fields!


---

Comment by SimonKing created at 2011-12-21 21:48:08

Aha!

The combination of a finite field with a polynomial ring seems to reveal the leak:

```
sage: K = GF(next_prime(1000))
sage: p = K.order()
sage: predicate = lambda x: is_FiniteField(x) and x.order() == p
sage: del K
sage: gc.collect()
23
sage: [bla for bla in gc.get_objects() if predicate(bla)]
[]
sage: K = GF(next_prime(1000))
sage: P = K['x','y','z']
sage: del P
sage: del K
sage: gc.collect()
39
sage: [bla for bla in gc.get_objects() if predicate(bla)]
[Finite Field of size 1009]
sage: predicate = lambda x: is_MPolynomialRing(x) and x.variable_names()==['x','y','z']
sage: [bla for bla in gc.get_objects() if predicate(bla)]
[]
```


So, the polynomial ring is gone, but the base ring remains. And I think this is indeed because of the thing tracked at #12215:

 * The polynomial ring belongs to the category of algebras over the base ring (at least by #9138, which I have applied), 
 * The category is strongly cached (see #12215)
 * The category has a reference to its base ring.

So, indeed we absolutely need to have `UniqueRepresentation` use weak references.


---

Comment by vbraun created at 2011-12-21 21:51:21

I can't really comment on what is going on in your unpublished patch, but I do recommend heapy to track down the memory leaks. For starters, it can show you a statistic of which types occupy most of the memory. Its just an `easy_install` away... But we don't have to solve every memory leak in a day, I'm happy to review any progress towards making cache weaker even if its not the final word.


---

Comment by SimonKing created at 2011-12-21 23:42:47

Replying to [comment:27 vbraun]:
> I can't really comment on what is going on in your unpublished patch, but I do recommend heapy to track down the memory leaks. ... Its just an `easy_install` away...

It isn't.


```
(sage subshell) linux-sqwp:sage-main simon$ easy_install heapy
Searching for heapy
Reading http://pypi.python.org/simple/heapy/
Couldn't find index page for 'heapy' (maybe misspelled?)
Scanning index of all packages (this may take a while)
Reading http://pypi.python.org/simple/
No local packages or download links found for heapy
error: Could not find suitable distribution for Requirement.parse('heapy')
```


What did I do wrong?


---

Comment by SimonKing created at 2011-12-21 23:45:47

Aha! Do I need to install guppy for getting heapy?


---

Comment by SimonKing created at 2011-12-21 23:51:40

Interesting. Heapy shows (again with the example from the ticket description) that most of the memory is filled by strings:

```
sage: H.heap()
Partition of a set of 479076 objects. Total size = 78965680 bytes.
 Index  Count   %     Size   % Cumulative  % Kind (class / dict of class)
     0 228412  48 38602736  49  38602736  49 str
     1 123581  26 10681888  14  49284624  62 tuple
     2   1755   0  4241544   5  53526168  68 dict of module
     3   4657   1  3835672   5  57361840  73 dict (no owner)
     4  29863   6  3583560   5  60945400  77 function
     5  29851   6  3582120   5  64527520  82 types.CodeType
     6   3071   1  2974952   4  67502472  85 dict of type
     7   3071   1  2759672   3  70262144  89 type
     8   6651   1  1202264   2  71464408  91 list
     9    937   0   922072   1  72386480  92 dict of class
<1072 more rows. Type e.g. '_.more' to view.>
```


What are these strings? Messages of cached exceptions (there is a ticket concerning cached exceptions, but I can't find it right now)? Keys of dictionaries? But then we should also see the corresponding values.


---

Comment by SimonKing created at 2011-12-23 09:55:53

I introduced a weak cache for polynomial rings in two lines of my patch for #715, which now needs review. I therefore suggest that this ticket is marked as a duplicate.


---

Comment by SimonKing created at 2011-12-23 09:55:53

Changing status from needs_work to positive_review.


---

Comment by zimmerma created at 2011-12-23 10:02:28

Simon, there is a `duplicate` field, which would be better than `positive review`.

Also, maybe you might put this as `needs review`, asking someone (maybe you) to check that your patch for #715 indeed solves the problem.

Paul


---

Comment by SimonKing created at 2011-12-23 10:15:47

Replying to [comment:32 zimmerma]:
> Simon, there is a `duplicate` field, which would be better than `positive review`.

There is no duplicate field, because choosing the resolution of a ticket is reserved to people with administrator rights. Apparently you have these rights, but I haven't.

In addition, I am very much sure that Jeroen said that this is the correct way to proceed: If one thinks that the ticket is a duplicate then you review it accordingly, putting it as "positive review". Then the RELEASE MANAGER (nobody else!!) closes the ticket by choosing the resolution "duplicate", if he believes that the reasons given in the review make sense.

> Also, maybe you might put this as `needs review`, asking someone (maybe you) to check that your patch for #715 indeed solves the problem.

I can of course not review my own patch from #715. I can merely state that the problem of the ticket here is in fact a sub-problem of ticket #715.


---

Comment by jdemeyer created at 2011-12-23 11:10:43

Replying to [comment:33 SimonKing]:
> I am very much sure that Jeroen said that this is the correct way to proceed: If one thinks that the ticket is a duplicate then you review it accordingly, putting it as "positive review". Then the RELEASE MANAGER (nobody else!!) closes the ticket by choosing the resolution "duplicate", if he believes that the reasons given in the review make sense.

True, but you forget one important step: you should put the milestone to sage-duplicate/invalid/wontfix yourself, so I know the intention is to close this ticket as duplicate and no patch should be merged.

Nobody except for the release manager should close or reopen tickets (with a few exceptions like spam tickets, tickets marked as duplicate by the person who reported the ticket and with no other activity).

And if it's a duplicate, it would be nice to add a pointer in the description to the ticket of which it is a duplicate of.


---

Comment by jdemeyer created at 2012-01-05 13:34:39

Resolution: duplicate
