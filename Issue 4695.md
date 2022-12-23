# Issue 4695: [with patch, needs review] add support for pari's rnfidealdown

Issue created by migration from https://trac.sagemath.org/ticket/4695

Original creator: ncalexan

Original creation time: 2008-12-04 18:43:58

Assignee: was

CC:  was cc

Keywords: relative rnf ideal down

The attached patch adds support for pari's rnfidealdown.  This is simple but exposes a weakness in Sage's number field relativize() function, which I address at the same time.  Namely, relativize always constructs a new base number field and embedding rather than (possibly) using an existing one.  The doctests are extensive and reveal (and document!) a bug in the existing code.


---

Attachment

I read through the code and the only problem I have is that  

```
def rnfidealdown(self, x): 
```

has no docstring or doctest, which violates our 100% coverage rule.

Also, a bunch of doctests fail on x86_64 linux (sage.math), and these all have to get fixed.  So once these are fixed and the above function has a doctest, I'll be happy.  The doctest failures (except the segfault) look like some kind of randomness in the output.  


```
was@sage:~/build/sage-3.2.1.rc1$ ./sage -tp 12 devel/sage/sage/rings/
Global iterations: 1
File iterations: 1
TeX files: 0
 
----------------------------------------------------------------------
sage -t  devel/sage/sage/rings/padics/padic_field_base_generic.py
	 [0.1 s]
sage -t  devel/sage/sage/rings/padics/lazy_ring_generic.py
	 [0.1 s]
... passes
sage -t  devel/sage/sage/rings/number_field/number_field_ideal_rel.py
**********************************************************************
File "/home/was/build/sage-3.2.1.rc1/devel/sage-main/sage/rings/number_field/number_field_ideal_rel.py", line 197:
    sage: K0.factor(19)
Expected:
    (Fractional ideal (-a0 + 1)) * (Fractional ideal (-a0 + 5))
Got:
    (Fractional ideal (a0 - 1)) * (Fractional ideal (-a0 + 5))
**********************************************************************
File "/home/was/build/sage-3.2.1.rc1/devel/sage-main/sage/rings/number_field/number_field_ideal_rel.py", line 200:
    sage: P1, w1
Expected:
    (Fractional ideal (-a0 + 1), -a0 + 1)
Got:
    (Fractional ideal (a0 - 1), a0 - 1)
**********************************************************************
File "/home/was/build/sage-3.2.1.rc1/devel/sage-main/sage/rings/number_field/number_field_ideal_rel.py", line 216:
    sage: K_into_L1(P).ideal_below()
Expected:
    Fractional ideal (-a0 + 1)
Got:
    Fractional ideal (a0 - 1)
**********************************************************************
1 items had failures:
   3 of  36 in __main__.example_6
***Test Failed*** 3 failures.
For whitespace errors, see the file /home/was/build/sage-3.2.1.rc1/tmp/.doctest_number_field_ideal_rel.py

	 [3.9 s]

sage -t  devel/sage/sage/rings/number_field/number_field.py
**********************************************************************
File "/home/was/build/sage-3.2.1.rc1/devel/sage-main/sage/rings/number_field/number_field.py", line 4200:
    sage: Pp = L1.ideal(K_into_L1(w1)).ideal_below(); Pp
Expected:
    Fractional ideal (4*a0 + 1)
Got:
    Fractional ideal (5*a0 - 9)
For whitespace errors, see the file /home/was/build/sage-3.2.1.rc1/tmp/.doctest_number_field.py

------------------------------------------------------------
Unhandled SIGSEGV: A segmentation fault occured in SAGE.
This probably occured because a *compiled* component
of SAGE has a bug in it (typically accessing invalid memory)
or is not properly wrapped with _sig_on, _sig_off.
You might want to run SAGE under gdb with 'sage -gdb' to debug this.
SAGE will now terminate (sorry).
------------------------------------------------------------


A mysterious error (perphaps a memory error?) occurred, which may have crashed doctest.

	 [8.0 s]
```



---

Attachment

4695-ncalexan-rnfidealdown.2.patch addresses the referee's concerns and implements relativize over relative fields.  This required updating the number field isomorphisms to the newer coercion model.  Along the way I added lots of doctests.

I haven't addressed the crashes on sage.math.


---

Comment by ncalexan created at 2008-12-09 18:55:54

Doctesting the updated patch on sage.math:  (I haven't tested the whole tree)


```
ncalexan@sage:~/sage/devel/sage-nca$ ~/sage/sage -tp 6 sage/rings/number_field/* 
Global iterations: 1
File iterations: 1
TeX files: 0
No cached timings exist; will create upon successful finish.
 
----------------------------------------------------------------------
sage -t  3.2.2.alpha0-x86_64-Linux/devel/sage-nca/sage/rings/number_field/class_group.py
         [15.1 s]
sage -t  3.2.2.alpha0-x86_64-Linux/devel/sage-nca/sage/rings/number_field/galois_group.py
         [15.1 s]
sage -t  3.2.2.alpha0-x86_64-Linux/devel/sage-nca/sage/rings/number_field/number_field_base.pyx
         [15.1 s]
sage -t  3.2.2.alpha0-x86_64-Linux/devel/sage-nca/sage/rings/number_field/morphism.py
         [15.1 s]
sage -t  3.2.2.alpha0-x86_64-Linux/devel/sage-nca/sage/rings/number_field/maps.py
         [15.2 s]
sage -t  3.2.2.alpha0-x86_64-Linux/devel/sage-nca/sage/rings/number_field/number_field_ideal_rel.py
         [4.1 s]
sage -t  3.2.2.alpha0-x86_64-Linux/devel/sage-nca/sage/rings/number_field/number_field_morphisms.pyx
         [4.1 s]
sage -t  3.2.2.alpha0-x86_64-Linux/devel/sage-nca/sage/rings/number_field/number_field_element_quadratic.pyx
         [4.2 s]
sage -t  3.2.2.alpha0-x86_64-Linux/devel/sage-nca/sage/rings/number_field/small_primes_of_degree_one.py
         [5.1 s]
sage -t  3.2.2.alpha0-x86_64-Linux/devel/sage-nca/sage/rings/number_field/number_field_ideal.py
         [11.2 s]
sage -t  3.2.2.alpha0-x86_64-Linux/devel/sage-nca/sage/rings/number_field/totallyreal.pyx
         [7.1 s]
sage -t  3.2.2.alpha0-x86_64-Linux/devel/sage-nca/sage/rings/number_field/totallyreal_data.pyx
         [3.1 s]
sage -t  3.2.2.alpha0-x86_64-Linux/devel/sage-nca/sage/rings/number_field/unit_group.py
         [0.1 s]
sage -t  3.2.2.alpha0-x86_64-Linux/devel/sage-nca/sage/rings/number_field/number_field_element.pyx
         [13.2 s]
sage -t  3.2.2.alpha0-x86_64-Linux/devel/sage-nca/sage/rings/number_field/totallyreal_phc.py
         [3.1 s]
sage -t  3.2.2.alpha0-x86_64-Linux/devel/sage-nca/sage/rings/number_field/order.py
         [10.2 s]
sage -t  3.2.2.alpha0-x86_64-Linux/devel/sage-nca/sage/rings/number_field/totallyreal_rel.py
         [4.1 s]
  ***   Warning: large Minkowski bound: certification will be VERY long.
  ***   Warning: large Minkowski bound: certification will be VERY long.
sage -t  3.2.2.alpha0-x86_64-Linux/devel/sage-nca/sage/rings/number_field/number_field.py
         [45.6 s]
All tests passed!
Timings have been updated.
Total time for all tests: 45.6 seconds


ncalexan@sage:~/sage/devel/sage-nca$ ~/sage/sage -tp 6 sage/libs/pari/*
Global iterations: 1
File iterations: 1
TeX files: 0
Using cached timings.
 
----------------------------------------------------------------------
sage -t  3.2.2.alpha0-x86_64-Linux/devel/sage-nca/sage/libs/pari/gen.pxi
         [0.1 s]
sage -t  3.2.2.alpha0-x86_64-Linux/devel/sage-nca/sage/libs/pari/decl.pxi
         [0.1 s]
sage -t  3.2.2.alpha0-x86_64-Linux/devel/sage-nca/sage/libs/pari/misc.pxi
         [0.1 s]
sage -t  3.2.2.alpha0-x86_64-Linux/devel/sage-nca/sage/libs/pari/pari_err.pxi
         [0.1 s]
sage -t  3.2.2.alpha0-x86_64-Linux/devel/sage-nca/sage/libs/pari/to_gen.pxi
         [0.1 s]
sage -t  3.2.2.alpha0-x86_64-Linux/devel/sage-nca/sage/libs/pari/setlvalue.pxi
         [0.1 s]
sage -t  3.2.2.alpha0-x86_64-Linux/devel/sage-nca/sage/libs/pari/gen_py.py
         [3.1 s]
sage -t  3.2.2.alpha0-x86_64-Linux/devel/sage-nca/sage/libs/pari/gen.pyx
         [5.4 s]
All tests passed!
Timings have been updated.
Total time for all tests: 5.4 seconds
ncalexan@sage:~/sage/devel/sage-nca$
```



---

Comment by mabshoff created at 2008-12-10 10:26:24

4695-ncalexan-rnfidealdown.2.patch applied to my current merge tree passes long doctests. So all we need now is a positive review :)

Cheers,

Michael


---

Comment by mabshoff created at 2008-12-10 16:24:04

Resolution: fixed


---

Comment by mabshoff created at 2008-12-10 16:24:04

Merged 4695-ncalexan-rnfidealdown.2.patch in Sage 3.2.2.alpha2
