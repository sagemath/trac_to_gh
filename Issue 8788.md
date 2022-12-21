# Issue 8788: segfault in Sage-4.4 built using GCC-4.5.0

Issue created by migration from Trac.

Original creator: was

Original creation time: 2010-04-28 00:03:28

Assignee: GeorgSWeber

CC:  wjp leif

If we build Sage-4.4 (with several tickets/patches/elbow grease) with GCC-4.5.0, then many things cause it to segfault at exit.  The simplest I found so far is this:


```
sage: Mat(GF(9,'a'),3,sparse=True).random_element()
sage: from sage.matrix.matrix_space import test_trivial_matrices_inverse as tinv
sage: tinv(ZZ, sparse=False)
sage: quit
Exiting Sage (CPU time 0m0.11s, Wall time 0m0.15s).
*** glibc detected *** python: double free or corruption (fasttop): 0x000000000233a930 ***
======= Backtrace: =========
/lib64/libc.so.6[0x39a6c74a76]
/lib64/libc.so.6(exit+0xe2)[0x39a6c35b82]
python[0x4c3896]
python[0x4c30f5]
python(PyRun_SimpleFileExFlags+0x159)[0x4c5e69]
python(Py_Main+0xa5e)[0x413cde]
/lib64/libc.so.6(__libc_start_main+0xfd)[0x39a6c1eb1d]
python[0x412f79]
======= Memory map: ========
00400000-00566000 r-xp 00000000 00:13 12537003                           /home/wstein/screen/lena/sage-4.4/local/bin/python
00765000-0079e000 rw-p 00165000 00:13 12537003                           /home/wstein/screen/lena/sage-4.4/local/bin/python
0079e000-007ad000 rw-p 00000000 00:00 0
00bf1000-04d16000 rw-p 00000000 00:00 0                                  [heap]
316e600000-316e61c000 r-xp 00000000 fd:00 8683576                        /lib64/libselinux.so.1
316e61c000-316e81b000 ---p 0001c000 fd:00 8683576                        /lib64/libselinux.so.1
316e81b000-316e81c000 r--p 0001b000 fd:00 8683576                        /lib64/libselinux.so.1
316e81c000-316e81d000 rw-p 0001c000 fd:00 8683576                        /lib64/libselinux.so.1
316e81d000-316e81e000 rw-p 00000000 00:00 0
3171200000-3171203000 r-xp 00000000 fd:00 8683697                        /lib64/libcom_err.so.2.1
3171203000-3171402000 ---p 00003000 fd:00 8683697                        /lib64/libcom_err.so.2.1
3171402000-3171403000 rw-p 00002000 fd:00 8683697                        /lib64/libcom_err.so.2.1
3171600000-31716b3000 r-xp 00000000 fd:00 8683698                        /lib64/libkrb5.so.3.3
31716b3000-31718b3000 ---p 000b3000 fd:00 8683698                        /lib64/libkrb5.so.3.3
31718b3000-31718bd000 rw-p 000b3000 fd:00 8683698                        /lib64/libkrb5.so.3.3
3171a00000-3171a2d000 r-xp 00000000 fd:00 8683700                        /lib64/libgssapi_krb5.so.2.2
3171a2d000-3171c2d000 ---p 0002d000 fd:00 8683700                        /lib64/libgssapi_krb5.so.2.2
3171c2d000-3171c2f000 rw-p 0002d000 fd:00 8683700                        /lib64/libgssapi_krb5.so.2.2
3171e00000-3171e2a000 r-xp 00000000 fd:00 8683677                        /lib64/libk5crypto.so.3.1
3171e2a000-317202a000 ---p 0002a000 fd:00 8683677                        /lib64/libk5crypto.so.3.1
317202a000-317202c000 rw-p 0002a000 fd:00 8683677                        /lib64/libk5crypto.so.3.1
3172200000-3172208000 r-xp 00000000 fd:00 8683667                        /lib64/libkrb5support.so.0.1
3172208000-3172408000 ---p 00008000 fd:00 8683667                        /lib64/libkrb5support.so.0.1
3172408000-3172409000 rw-p 00008000 fd:00 8683667                        /lib64/libkrb5support.so.0.1
3172600000-3172652000 r-xp 00000000 fd:00 52070079                       /usr/lib64/libssl.so.1.0.0
3172652000-3172851000 ---p 00052000 fd:00 52070079                       /usr/lib64/libssl.so.1.0.0
3172851000-3172859000 rw-p 00051000 fd:00 52070079                       /usr/lib64/libssl.so.1.0.0
39a6800000-39a681e000 r-xp 00000000 fd:00 8683525                        /lib64/ld-2.11.1.so
39a6a1d000-39a6a1e000 r--p 0001d000 fd:00 8683525                        /lib64/ld-2.11.1.so
39a6a1e000-39a6a1f000 rw-p 0001e000 fd:00 8683525                        /lib64/ld-2.11.1.so
...
```



---

Comment by was created at 2010-04-29 00:39:57

Here is what fails WITH THE DOUBLE FREE ERROR when doctesting sage-4.4.1.alpha0:

```
        sage -t  "devel/sage/sage/modular/modsym/space.py" # Killed/crashed
        sage -t  "devel/sage/sage/modular/modsym/modsym.py" # Killed/crashed
        sage -t  "devel/sage/sage/modular/modform/ambient.py" # Killed/crashed
        sage -t  "devel/sage/sage/modular/ssmod/ssmod.py" # Killed/crashed
        sage -t  "devel/sage/sage/modules/free_module.py" # Killed/crashed
        sage -t  "devel/sage/sage/matrix/matrix_sparse.pyx" # Killed/crashed
        sage -t  "devel/sage/sage/matrix/matrix_space.py" # Killed/crashed
        sage -t  "devel/sage/sage/matrix/matrix2.pyx" # Killed/crashed
        sage -t  "devel/sage/sage/rings/number_field/number_field.py" # Killed/crashed
        sage -t  "devel/sage/sage/rings/number_field/number_field_rel.py" # Killed/crashed
        sage -t  "devel/sage/sage/rings/finite_rings/element_ntl_gf2e.pyx" # Killed/crashed
        sage -t  "devel/sage/sage/rings/finite_rings/finite_field_ext_pari.py" # Killed/crashed
        sage -t  "devel/sage/sage/rings/finite_rings/homset.py" # Killed/crashed
        sage -t  "devel/sage/sage/rings/polynomial/polynomial_quotient_ring_element.py" # Killed/crashed
        sage -t  "devel/sage/sage/groups/generic.py" # Killed/crashed
        sage -t  "devel/sage/sage/tests/benchmark.py" # Killed/crashed
        sage -t  "devel/sage/sage/schemes/hyperelliptic_curves/hyperelliptic_generic.py" # Killed/crashed
        sage -t  "devel/sage/sage/schemes/hyperelliptic_curves/hyperelliptic_finite_field.py" # Killed/crashed
        sage -t  "devel/sage/sage/schemes/elliptic_curves/ell_point.py" # Killed/crashed
        sage -t  "devel/sage/sage/coding/linear_code.py" # Killed/crashed
        sage -t  "devel/sage/sage/coding/code_constructions.py" # Killed/crashed
```


Everything is likely to involve something in linear algebra... that's a common theme!  Linbox?


---

Comment by wjp created at 2010-04-29 16:58:42

From what I can tell, the issue is related to linbox and givaro both using the
randstate stuff in givaro's gmp++_int.inl. On my home machine the internal
random states (a local static in `Integer::randstate()` ) in both end up as different objects, but on lena they seem to
use the exact same object in memory, causing it to be deleted twice on exit.

If anybody else wants to take a look, I tracked this down by putting a breakpoint on mpir's 'randclear_lc' and looking at the rdi register which is the pointer to the randstate.


---

Comment by wjp created at 2010-04-29 20:46:28

Well, this is a fun one. Givaro and Linbox indeed end up destructing the same object.

The destructor is registered once via givaro:


```
#0  0x00000039a6c35dd0 in __cxa_atexit_internal () from /lib64/libc.so.6
#1  0x00007fffddf09ec2 in randstate (...)
    at sage-4.4/local//include/gmp++/gmp++_int.inl:317
#2  seeding (...)
    at sage-4.4/local//include/gmp++/gmp++_int.inl:322
#3  seeding (...)
    at sage-4.4/local//include/givaro/givinteger.h:132
#4  IntFactorDom (...)
    at sage-4.4/local//include/givaro/givintfactor.h:43
#5  IntNumTheoDom (...)
    at sage-4.4/local//include/givaro/givintnumtheo.h:23
#6  GFqDom<int>::GFqDom (...)
    at sage-4.4/local//include/givaro/givgfq.inl:931
```


and once via linbox:


```
#0  0x00000039a6c35dd0 in __cxa_atexit_internal () from /lib64/libc.so.6
#1  0x00007fffd5dbe365 in randstate (...)
    at sage-4.4/local/include/gmp++/gmp++_int.inl:317
#2  seeding (...)
    at sage-4.4/local/include/gmp++/gmp++_int.inl:322
#3  setSeed (...) at ../../linbox/randiter/random-prime.h:57
#4  LinBox::RandomPrimeIterator::RandomPrimeIterator (this=0x7fffffffc600, 
    bits=<value optimized out>, seed=<value optimized out>)
    at ../../linbox/randiter/random-prime.h:26
```


This might be a compiler and/or linker bug...

I'm not altogether sure how best to workaround it. One possible way would just be to avoid clearing the randstate entirely in givaro's `Integer::randstate()`. If I understand things correctly, there won't be more than one copy around for each library using givaro, so it won't actually leak memory except on program exit.

I need to stop looking at this for today, but if anyone wants to test, that would require replacing the following in `[gmp++_int.inl`


```
inline gmp_randclass& Integer::randstate(long unsigned int seed) {
	static gmp_randclass randstate(GMP_RAND_ALG_DEFAULT,seed);
	return static_cast<gmp_randclass&>(randstate);
}
```


by


```
inline gmp_randclass& Integer::randstate(long unsigned int seed) {
        static gmp_randclass* randstate = new gmp_randclass(GMP_RAND_ALG_DEFAULT,seed);
        return *randstate;
}
```


An initial quick test shows that this might fix the issue, but I only rebuilt linbox after this change; nothing else, not even givaro itself. And I only tried the example given in the initial report in the ticket, no doctests.


---

Comment by wjp created at 2010-04-30 04:33:56

All doctests pass after the change I mentioned. I'll turn this into a new givaro spkg ready for more testing later today, unless somebody beats me to it.


---

Comment by wjp created at 2010-04-30 11:33:08

Changing status from new to needs_review.


---

Comment by wjp created at 2010-04-30 11:33:08

A new givaro spkg to work around this problem:

http://www.math.leidenuniv.nl/~wpalenst/sage/givaro-3.2.13rc2.p1.spkg

It basically fixes the problem by not destructing the randstate objects on exit. This shouldn't be a problem because the destructor only frees memory.


---

Comment by drkirkby created at 2010-04-30 21:55:03

Does this mean it will create a memory leak?


---

Comment by wjp created at 2010-04-30 22:29:10

No. The objects persist until sage exits, regardless of if their destructors are called. The only thing that changes is that the objects aren't actually freed when sage exits, which is pretty much irrelevant.

(An exception would be if something were to dlopen/dlclose libgivaro or liblinboxsage repeatedly, but I don't think that's the case.)


---

Comment by was created at 2010-05-01 05:18:55

Changing status from needs_review to positive_review.


---

Comment by was created at 2010-05-01 05:19:21

Resolution: fixed
