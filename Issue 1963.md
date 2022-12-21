# Issue 1963: unramified and eisenstein extensions

Issue created by migration from Trac.

Original creator: roed

Original creation time: 2008-01-28 22:49:59

Assignee: roed

Keywords: p-adics

Adds unramified and eisenstein extensions of Qp and Zp.  Adds printing features for p-adics, improves construction of p-adic elements, fixes some bugs and memleaks.


---

Comment by roed created at 2008-01-28 22:50:40

Bundled against 2.10


---

Attachment

I got the following merge conflict against 2.10.1.rc2:

```
<<<<<<< /scratch/mabshoff/release-cycle/sage-2.10.1.rc3/devel/sage-main/sage/schemes/elliptic_curves/padics.py.orig.2461327829
    ALGORITHM:
        Proposition 9 of ``Efficient Computation of p-adic Heights'' (David Harvey,
        to appear in LMS JCM).

        Complexity is soft-$O(\log L \log m + \log^2 m)$.
    Complexity is soft $O(\log R \log^2 m)$.
=======
    Complexity is soft $O(\log R \log m)$.
>>>>>>> /tmp/padics.py~other.K30f_Q
```

But I also have a compilation failure:

```
/usr/include/features.h:150:1: warning: this is the location of the previous definition
src/ntl_wrap.cpp: In function ‘void ZZ_pX_InvMod_newton_unram(NTL::ZZ_pX&, const NTL::ZZ_pX&, const NTL::ZZ_pXModulus&, const NTL::ZZ_pContext&, const NTL::ZZ_pContext&)’:
src/ntl_wrap.cpp:1136: error: reference to ‘negate’ is ambiguous
```

I will poke around a little more and update this if I find anything useful.
|||                            
|||----------------------------
|||| /tmp/padics.py~base.ns4Mgb
Cheers,

Michael


---

Comment by mabshoff created at 2008-01-28 23:39:28

The compilation issue is easy to fix: add `NTL::` before negate in lines 1136 and 1163. Patch is comping up shortly.

Cheers,

Michael


---

Attachment

Fix the compilation issue with negate with gcc 4.1 (and others?)


---

Comment by mabshoff created at 2008-01-29 01:48:02

I see doctest failures in 

```
        sage -t  devel/sage-main/sage/rings/padics/padic_capped_relative_element.pyx
        sage -t  devel/sage-main/sage/rings/padics/padic_generic.py
        sage -t  devel/sage-main/sage/rings/padics/padic_generic_element.pyx
        sage -t  devel/sage-main/sage/rings/padics/pow_computer_ext.pyx
        sage -t  devel/sage-main/sage/rings/padics/tests.py
        sage -t  devel/sage-main/sage/rings/padics/padic_ZZ_pX_CA_element.pyx
        sage -t  devel/sage-main/sage/rings/padics/padic_ZZ_pX_CR_element.pyx
        sage -t  devel/sage-main/sage/rings/padics/padic_ZZ_pX_FM_element.pyx
        sage -t  devel/sage-main/sage/rings/polynomial/multi_polynomial.pyx
        sage -t  devel/sage-main/sage/schemes/elliptic_curves/ell_generic.py
        sage -t  devel/sage-main/sage/schemes/elliptic_curves/ell_padic_field.py
        sage -t  devel/sage-main/sage/schemes/elliptic_curves/ell_point.py
        sage -t  devel/sage-main/sage/schemes/elliptic_curves/ell_rational_field.py
        sage -t  devel/sage-main/sage/schemes/elliptic_curves/ell_tate_curve.py
        sage -t  devel/sage-main/sage/schemes/elliptic_curves/padic_lseries.py
        sage -t  devel/sage-main/sage/schemes/elliptic_curves/padics.py
        sage -t  devel/sage-main/sage/schemes/elliptic_curves/sha.py
        sage -t  devel/sage-main/sage/schemes/hyperelliptic_curves/hyperelliptic_padic_field.py
```


Cheers,

Michael


---

Comment by roed created at 2008-02-06 04:06:17

Bundle vs 2.10.1 at http://sage.math.washington.edu/home/roed/giant_padics_vs_2_10_1.hg


---

Comment by bober created at 2008-02-06 05:53:23

With new patch, on Ubuntu 7.10, Intel Core Duo, four failures:

```
sage -t  devel/sage-padics_again/sage/rings/padics/padic_ZZ_pX_CA_element.pyx
sage -t  devel/sage-padics_again/sage/rings/padics/factory.py
sage -t  devel/sage-padics_again/sage/rings/padics/tutorial.py
sage -t  devel/sage-padics_again/sage/rings/polynomial/multi_polynomial.
```



---

Comment by robertwb created at 2008-02-06 06:07:19


```
sage: R = Zp(5,5)
sage: S.<x> = R[]
sage: f = x^5 + 75*x^3 - 15*x^2 +125*x - 5
sage: W.<w> = R.ext(f); W
sage: W.residue_system()
------------------------------------------------------------
Traceback (most recent call last):
  File "<ipython console>", line 1, in <module>
  File "/Users/robert/sage/current/local/lib/python2.5/site-packages/sage/rings/padics/padic_generic.py", line 274, in residue_system
    return [self(i) for i in self.residue_class_field()]
  File "/Users/robert/sage/current/local/lib/python2.5/site-packages/sage/rings/padics/padic_generic.py", line 84, in __call__
    return self._element_class(self, x, absprec, relprec)
  File "padic_ZZ_pX_CR_element.pyx", line 231, in sage.rings.padics.padic_ZZ_pX_CR_element.pAdicZZpXCRElement.__init__
<type 'exceptions.TypeError'>: cannot coerce from the given integer mod ring (not a power of the same prime)
```



---

Attachment


---

Attachment


---

Attachment


---

Attachment


---

Attachment


---

Attachment


---

Attachment

Must apply against latest bundle


---

Attachment

Must apply against latest bundle


---

Comment by kedlaya created at 2008-02-08 23:35:45

Must apply against latest bundle


---

Attachment

The patches kedlaya2.patch and kedlaya2.2.patch are identical, so no need to grab the second one. Sorry about that.


---

Attachment

Bundle as of end of SD7


---

Attachment

doctest fix


---

Comment by mabshoff created at 2008-02-13 08:03:13

Hi,

what is the status of this now? I assume I need to apply 1963-padics-bundle-sd7-final.hg and padic-sd7-fix.patch. Let's get this merged :)

Cheers,

Michael


---

Comment by robertwb created at 2008-02-14 05:41:43

Status: waiting on David Roe for norm, degree, and trace. This is (almost) implemented, but not yet polished?? 

If he's to busy to do this in the short term, perhaps we could put NotImplementedErrors in their place and merge, postponing the implementation of the above to a later ticket.


---

Comment by mabshoff created at 2008-02-15 02:55:42

Merged 1963-padics-bundle-sd7-final.hg and padic-sd7-fix.patch in Sage 2.10.2.alpha0


---

Comment by mabshoff created at 2008-02-15 04:36:40

Running `-long` doctests showed (still) a lot of failures:

```
        sage -t -long devel/sage-main/sage/groups/group.pyx
        sage -t -long devel/sage-main/sage/misc/functional.py
        sage -t -long devel/sage-main/sage/rings/padics/padic_ZZ_pX_CA_element.pyx
        sage -t -long devel/sage-main/sage/rings/padics/padic_ZZ_pX_CR_element.pyx
        sage -t -long devel/sage-main/sage/rings/padics/padic_capped_relative_element.pyx
        sage -t -long devel/sage-main/sage/rings/padics/padic_generic.py
        sage -t -long devel/sage-main/sage/rings/padics/padic_generic_element.pyx
        sage -t -long devel/sage-main/sage/rings/padics/pow_computer_ext.pyx
        sage -t -long devel/sage-main/sage/rings/padics/tests.py
        sage -t -long devel/sage-main/sage/rings/padics/padic_ZZ_pX_FM_element.pyx
        sage -t -long devel/sage-main/sage/rings/padics/padic_ZZ_pX_element.pyx
        sage -t -long devel/sage-main/sage/rings/polynomial/multi_polynomial.pyx
        sage -t -long devel/sage-main/sage/schemes/elliptic_curves/ell_generic.py
        sage -t -long devel/sage-main/sage/schemes/elliptic_curves/ell_padic_field.py
        sage -t -long devel/sage-main/sage/schemes/elliptic_curves/ell_point.py
        sage -t -long devel/sage-main/sage/schemes/elliptic_curves/ell_rational_field.py
        sage -t -long devel/sage-main/sage/schemes/elliptic_curves/ell_tate_curve.py
        sage -t -long devel/sage-main/sage/schemes/elliptic_curves/padic_lseries.py
        sage -t -long devel/sage-main/sage/schemes/elliptic_curves/padics.py
        sage -t -long devel/sage-main/sage/schemes/elliptic_curves/sha.py
        sage -t -long devel/sage-main/sage/schemes/hyperelliptic_curves/hyperelliptic_padic_field.py
```

Am I missing something?

Cheers,

Michael


---

Attachment

This patch fixes the import issue from 2.10.2.alpha0


---

Comment by mabshoff created at 2008-02-16 01:48:42

Here are some of the doctest failures:

```
sage -t  const.tex
**********************************************************************
File "const.py", line 2503:
    : b^4
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/release-cycle/sage-2.10.2.alpha1/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_82[8]>", line 1, in <module>
        b**Integer(4)###line 2503:
    : b^4
      File "padic_capped_relative_element.pyx", line 747, in sage.rings.padics.padic_capped_relative_element.pAdicCappedRela
tiveElement.__pow__
    ValueError: Valuation too large
**********************************************************************
```

and

```
sage -t  devel/sage-main/sage/rings/padics/padic_ZZ_pX_CA_element.pyx
**********************************************************************
File "padic_ZZ_pX_CA_element.pyx", line 48:
    sage: (1/w)^12+w
Expected:
    w^-12 + w + O(w^12)
Got:
    0
**********************************************************************
File "padic_ZZ_pX_CA_element.pyx", line 62:
    sage: 1/a
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/release-cycle/sage-2.10.2.alpha1/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[17]>", line 1, in <module>
        Integer(1)/a###line 62:
    sage: 1/a
      File "element.pyx", line 1482, in sage.structure.element.RingElement.__div__
      File "coerce.pyx", line 253, in sage.structure.coerce.CoercionModel_cache_maps.bin_op_c
      File "element.pyx", line 1480, in sage.structure.element.RingElement.__div__
      File "coerce.pxi", line 138, in sage.structure.element._div_c
      File "padic_ZZ_pX_CA_element.pyx", line 1303, in sage.rings.padics.padic_ZZ_pX_CA_element.pAdicZZpXCAElement._div_c_im
pl
        return self.to_fraction_field() * (~right)
      File "element.pyx", line 1372, in sage.structure.element.RingElement.__mul__
      File "coerce.pxi", line 126, in sage.structure.element._mul_c
      File "padic_ZZ_pX_CR_element.pyx", line 1789, in sage.rings.padics.padic_ZZ_pX_CR_element.pAdicZZpXCRElement._mul_c_im
pl
        raise ValueError, "valuation overflow"
    ValueError: valuation overflow
**********************************************************************
```


Cheers,

Michael


---

Comment by mabshoff created at 2008-02-20 20:22:45

#2233 fixes all 64 bit specific doctest failures. We currently have four NotYetImplemented and one fixme doctest failures left, that should happen on 32 as well as 64 bit.

Cheers,

Michael


---

Comment by mabshoff created at 2008-02-21 03:07:45

Craig Citro, Kiran Kedlaya, Robert Bradshaw and David Roe did extensive review and bug fixing at Sage Days 7. So I am giving this a positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-02-21 03:08:34

Resolution: fixed


---

Comment by mabshoff created at 2008-02-21 03:08:34

Merged in Sage 2.10.2.alpha1 - there are some small issues left, please open another ticket for any new patch. This ticket is overloaded as is.

Cheers,

Michael
