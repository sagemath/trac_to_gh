# Issue 4360: [with patch, needs review] fraction field improvements

Issue created by migration from https://trac.sagemath.org/ticket/4360

Original creator: burcin

Original creation time: 2008-10-24 09:23:03

Assignee: somebody

Attached patches move `sage.rings.fraction_field.FractionField_generic` to the new coercion model, and cythonize the `sage.rings.fraction_field_element.FractionFieldElement` class. They also allow homomorphisms of fraction fields to work, and make the `random_element()` method of fractions fields return sensible results.

I will follow these up with specialized classes for rational functions.

The patches depend on #4278.

Since one of the patches renames a file (from *.py to *.pyx) it contains a git style patch.


---

Comment by burcin created at 2008-11-17 13:27:59

Changing assignee from somebody to burcin.


---

Comment by burcin created at 2008-11-17 13:27:59

Changing status from new to assigned.


---

Comment by burcin created at 2008-11-17 13:27:59

I replaced the patches with ones that apply cleanly to 3.2.rc1.


---

Comment by was created at 2008-11-28 07:00:09

REFEREE REPORT:

Burcin, I didn't get far (against 3.2.1.alpha1).  Could you rebase again and let me know ASAP so I can referee?

```
was@sage:~/build/sage-3.2.1.alpha1$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: hg_sage.apply('http://trac.sagemath.org/sage_trac/attachment/ticket/4360/01_fraction_field_element_class.patch')
Attempting to load remote file: http://trac.sagemath.org/sage_trac/attachment/ticket/4360/01_fraction_field_element_class.patch?format=raw
Loading: [..]
cd "/home/was/build/sage-3.2.1.alpha1/devel/sage" && hg status
cd "/home/was/build/sage-3.2.1.alpha1/devel/sage" && hg status
cd "/home/was/build/sage-3.2.1.alpha1/devel/sage" && hg import   "/home/was/.sage/temp/sage/23856/tmp_0.patch"
applying /home/was/.sage/temp/sage/23856/tmp_0.patch
patching file sage/rings/fraction_field.py
Hunk #5 succeeded at 259 with fuzz 1 (offset 0 lines).
Hunk #6 FAILED at 270
1 out of 12 hunks FAILED -- saving rejects to file sage/rings/fraction_field.py.rej
abort: patch failed to apply
```



---

Attachment

fix fraction field homomorphisms


---

Comment by burcin created at 2008-11-28 12:19:04

Rebased against 3.2.1.alpha2. Please ignore the file `02_fraction_field_random_element.2.patch`.


---

Comment by was created at 2008-11-29 21:28:47

REFEREEING.

I took sage-3.2.1.rc0 and built it on sage.math and it doctested fine:

```
All tests passed!
Total time for all tests: 4285.2 seconds
```


I applied the above patches (all apply cleanly), rebuilt sage, and two doctests fail:

```
        sage -t  devel/sage/sage/structure/sage_object.pyx # 1 doctests failed
        sage -t  devel/sage/sage/calculus/desolvers.py # 1 doctests failed
```


I reran them individually, and both still fail.  Here is what you broke:

```
sage -t  "devel/sage/sage/calculus/desolvers.py"            **********************************************************************
File "/home/was/build/sage-3.2.1.rc0/devel/sage/sage/calculus/desolvers.py", line 437:
    sage: eulers_method_2x2(f,g, 0, 1, -1, 1/4, 1)
Expected:
        t                    x                h*f(t,x,y)                    y           h*g(t,x,y)
        0                    1                     -0.25                   -1                 0.50
      1/4                 0.75                     -0.12                -0.50                 0.29
      1/2                 0.63                    -0.054                -0.21                 0.19
      3/4                 0.63                   -0.0078               -0.031                 0.11
        1                 0.63                     0.020                0.079                0.071
Got:
             t                    x                h*f(t,x,y)                    y           h*g(t,x,y)
             0                    1                     -0.25                   -1                 0.50
           1/4                 0.75                     -0.12                -0.50                 0.32
           1/2                 0.63                    -0.046                -0.18                 0.21
           3/4                 0.63                    0.0040                0.016                 0.16
             1                 0.69                     0.043                 0.18                 0.15
**********************************************************************
1 items had failures:
   1 of  18 in __main__.example_7
***Test Failed*** 1 failures.
For whitespace errors, see the file /home/was/build/sage-3.2.1.rc0/tmp/.doctest_desolvers.py
         [9.3 s]
```


and


```
sage -t  "devel/sage/sage/structure/sage_object.pyx"

**********************************************************************
File "/home/was/build/sage-3.2.1.rc0/devel/sage/sage/structure/sage_object.pyx", line 744:
    sage: sage.structure.sage_object.unpickle_all(std)
Expected:
    Successfully unpickled ... objects.
    Failed to unpickle 0 objects.
Got:
    ** failed:  _class__sage_combinat_sf_llt_LLT_cospin__.sobj
    ** failed:  _class__sage_combinat_sf_macdonald_MacdonaldPolynomials_s__.sobj
    ** failed:  _class__sage_combinat_sf_jack_JackPolynomials_j__.sobj
    ** failed:  _class__sage_combinat_sf_jack_JackPolynomials_p__.sobj
    ** failed:  _class__sage_combinat_sf_macdonald_MacdonaldPolynomials_p__.sobj
    ** failed:  _class__sage_combinat_sf_hall_littlewood_HallLittlewood_q__.sobj
    ** failed:  _class__sage_combinat_sf_macdonald_MacdonaldPolynomials_q__.sobj
    ** failed:  _class__sage_combinat_sf_llt_LLT_spin__.sobj
    ** failed:  _class__sage_combinat_sf_hall_littlewood_HallLittlewood_p__.sobj
    ** failed:  _class__sage_combinat_sf_jack_JackPolynomials_q__.sobj
    ** failed:  _class__sage_combinat_sf_macdonald_MacdonaldPolynomials_h__.sobj
    ** failed:  _class__sage_combinat_sf_macdonald_MacdonaldPolynomials_ht__.sobj
    ** failed:  _class__sage_combinat_sf_macdonald_MacdonaldPolynomials_j__.sobj
    ** failed:  _class__sage_combinat_sf_hall_littlewood_HallLittlewood_qp__.sobj
    Failed:
    _class__sage_combinat_sf_llt_LLT_cospin__.sobj
    _class__sage_combinat_sf_macdonald_MacdonaldPolynomials_s__.sobj
    _class__sage_combinat_sf_jack_JackPolynomials_j__.sobj
    _class__sage_combinat_sf_jack_JackPolynomials_p__.sobj
    _class__sage_combinat_sf_macdonald_MacdonaldPolynomials_p__.sobj
    _class__sage_combinat_sf_hall_littlewood_HallLittlewood_q__.sobj
    _class__sage_combinat_sf_macdonald_MacdonaldPolynomials_q__.sobj
    _class__sage_combinat_sf_llt_LLT_spin__.sobj
    _class__sage_combinat_sf_hall_littlewood_HallLittlewood_p__.sobj
    _class__sage_combinat_sf_jack_JackPolynomials_q__.sobj
    _class__sage_combinat_sf_macdonald_MacdonaldPolynomials_h__.sobj
    _class__sage_combinat_sf_macdonald_MacdonaldPolynomials_ht__.sobj
    _class__sage_combinat_sf_macdonald_MacdonaldPolynomials_j__.sobj
    _class__sage_combinat_sf_hall_littlewood_HallLittlewood_qp__.sobj
    Successfully unpickled 440 objects.
    Failed to unpickle 14 objects.
**********************************************************************
1 items had failures:
   1 of   7 in __main__.example_18
```



---

Comment by burcin created at 2008-12-04 23:28:57

add random_element() method


---

Attachment

move element class to cython


---

Comment by burcin created at 2008-12-05 23:12:34

new coercion model, element class a parameter


---

Attachment

I posted new patches that fix the doctest errors in comment:6.

The fix for the pickles depends on #4698.


---

Comment by robertwb created at 2008-12-07 05:18:55

It looks good. I didn't to a testall, but all the touched files, as well as the failures above and the sage/rings/polynomials directory pass. Also, the code looks good and I haven't been able to break it in the testing I did of it.


---

Comment by mabshoff created at 2008-12-07 08:05:27

Resolution: fixed


---

Comment by mabshoff created at 2008-12-07 08:05:27

Merged all four patches in Sage 3.2.2.alpha1
