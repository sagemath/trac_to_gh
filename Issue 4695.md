# Issue 4695: [with patch, needs review] add support for pari's rnfidealdown

archive/issues_004695.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  was cc\n\nKeywords: relative rnf ideal down\n\nThe attached patch adds support for pari's rnfidealdown.  This is simple but exposes a weakness in Sage's number field relativize() function, which I address at the same time.  Namely, relativize always constructs a new base number field and embedding rather than (possibly) using an existing one.  The doctests are extensive and reveal (and document!) a bug in the existing code.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4695\n\n",
    "created_at": "2008-12-04T18:43:58Z",
    "labels": [
        "component: number theory"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.2",
    "title": "[with patch, needs review] add support for pari's rnfidealdown",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4695",
    "user": "https://github.com/ncalexan"
}
```
Assignee: @williamstein

CC:  was cc

Keywords: relative rnf ideal down

The attached patch adds support for pari's rnfidealdown.  This is simple but exposes a weakness in Sage's number field relativize() function, which I address at the same time.  Namely, relativize always constructs a new base number field and embedding rather than (possibly) using an existing one.  The doctests are extensive and reveal (and document!) a bug in the existing code.

Issue created by migration from https://trac.sagemath.org/ticket/4695





---

archive/issue_comments_035308.json:
```json
{
    "body": "Attachment [4695-ncalexan-rnfidealdown.patch](tarball://root/attachments/some-uuid/ticket4695/4695-ncalexan-rnfidealdown.patch) by @williamstein created at 2008-12-04 22:57:27\n\nI read through the code and the only problem I have is that  \n\n```\ndef rnfidealdown(self, x): \n```\n\nhas no docstring or doctest, which violates our 100% coverage rule.\n\nAlso, a bunch of doctests fail on x86_64 linux (sage.math), and these all have to get fixed.  So once these are fixed and the above function has a doctest, I'll be happy.  The doctest failures (except the segfault) look like some kind of randomness in the output.  \n\n\n```\nwas@sage:~/build/sage-3.2.1.rc1$ ./sage -tp 12 devel/sage/sage/rings/\nGlobal iterations: 1\nFile iterations: 1\nTeX files: 0\n \n----------------------------------------------------------------------\nsage -t  devel/sage/sage/rings/padics/padic_field_base_generic.py\n\t [0.1 s]\nsage -t  devel/sage/sage/rings/padics/lazy_ring_generic.py\n\t [0.1 s]\n... passes\nsage -t  devel/sage/sage/rings/number_field/number_field_ideal_rel.py\n**********************************************************************\nFile \"/home/was/build/sage-3.2.1.rc1/devel/sage-main/sage/rings/number_field/number_field_ideal_rel.py\", line 197:\n    sage: K0.factor(19)\nExpected:\n    (Fractional ideal (-a0 + 1)) * (Fractional ideal (-a0 + 5))\nGot:\n    (Fractional ideal (a0 - 1)) * (Fractional ideal (-a0 + 5))\n**********************************************************************\nFile \"/home/was/build/sage-3.2.1.rc1/devel/sage-main/sage/rings/number_field/number_field_ideal_rel.py\", line 200:\n    sage: P1, w1\nExpected:\n    (Fractional ideal (-a0 + 1), -a0 + 1)\nGot:\n    (Fractional ideal (a0 - 1), a0 - 1)\n**********************************************************************\nFile \"/home/was/build/sage-3.2.1.rc1/devel/sage-main/sage/rings/number_field/number_field_ideal_rel.py\", line 216:\n    sage: K_into_L1(P).ideal_below()\nExpected:\n    Fractional ideal (-a0 + 1)\nGot:\n    Fractional ideal (a0 - 1)\n**********************************************************************\n1 items had failures:\n   3 of  36 in __main__.example_6\n***Test Failed*** 3 failures.\nFor whitespace errors, see the file /home/was/build/sage-3.2.1.rc1/tmp/.doctest_number_field_ideal_rel.py\n\n\t [3.9 s]\n\nsage -t  devel/sage/sage/rings/number_field/number_field.py\n**********************************************************************\nFile \"/home/was/build/sage-3.2.1.rc1/devel/sage-main/sage/rings/number_field/number_field.py\", line 4200:\n    sage: Pp = L1.ideal(K_into_L1(w1)).ideal_below(); Pp\nExpected:\n    Fractional ideal (4*a0 + 1)\nGot:\n    Fractional ideal (5*a0 - 9)\nFor whitespace errors, see the file /home/was/build/sage-3.2.1.rc1/tmp/.doctest_number_field.py\n\n------------------------------------------------------------\nUnhandled SIGSEGV: A segmentation fault occured in SAGE.\nThis probably occured because a *compiled* component\nof SAGE has a bug in it (typically accessing invalid memory)\nor is not properly wrapped with _sig_on, _sig_off.\nYou might want to run SAGE under gdb with 'sage -gdb' to debug this.\nSAGE will now terminate (sorry).\n------------------------------------------------------------\n\n\nA mysterious error (perphaps a memory error?) occurred, which may have crashed doctest.\n\n\t [8.0 s]\n```\n",
    "created_at": "2008-12-04T22:57:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4695",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4695#issuecomment-35308",
    "user": "https://github.com/williamstein"
}
```

Attachment [4695-ncalexan-rnfidealdown.patch](tarball://root/attachments/some-uuid/ticket4695/4695-ncalexan-rnfidealdown.patch) by @williamstein created at 2008-12-04 22:57:27

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

archive/issue_comments_035309.json:
```json
{
    "body": "Attachment [4695-ncalexan-rnfidealdown.2.patch](tarball://root/attachments/some-uuid/ticket4695/4695-ncalexan-rnfidealdown.2.patch) by @ncalexan created at 2008-12-07 01:21:15\n\n4695-ncalexan-rnfidealdown.2.patch addresses the referee's concerns and implements relativize over relative fields.  This required updating the number field isomorphisms to the newer coercion model.  Along the way I added lots of doctests.\n\nI haven't addressed the crashes on sage.math.",
    "created_at": "2008-12-07T01:21:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4695",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4695#issuecomment-35309",
    "user": "https://github.com/ncalexan"
}
```

Attachment [4695-ncalexan-rnfidealdown.2.patch](tarball://root/attachments/some-uuid/ticket4695/4695-ncalexan-rnfidealdown.2.patch) by @ncalexan created at 2008-12-07 01:21:15

4695-ncalexan-rnfidealdown.2.patch addresses the referee's concerns and implements relativize over relative fields.  This required updating the number field isomorphisms to the newer coercion model.  Along the way I added lots of doctests.

I haven't addressed the crashes on sage.math.



---

archive/issue_comments_035310.json:
```json
{
    "body": "Doctesting the updated patch on sage.math:  (I haven't tested the whole tree)\n\n\n```\nncalexan@sage:~/sage/devel/sage-nca$ ~/sage/sage -tp 6 sage/rings/number_field/* \nGlobal iterations: 1\nFile iterations: 1\nTeX files: 0\nNo cached timings exist; will create upon successful finish.\n \n----------------------------------------------------------------------\nsage -t  3.2.2.alpha0-x86_64-Linux/devel/sage-nca/sage/rings/number_field/class_group.py\n         [15.1 s]\nsage -t  3.2.2.alpha0-x86_64-Linux/devel/sage-nca/sage/rings/number_field/galois_group.py\n         [15.1 s]\nsage -t  3.2.2.alpha0-x86_64-Linux/devel/sage-nca/sage/rings/number_field/number_field_base.pyx\n         [15.1 s]\nsage -t  3.2.2.alpha0-x86_64-Linux/devel/sage-nca/sage/rings/number_field/morphism.py\n         [15.1 s]\nsage -t  3.2.2.alpha0-x86_64-Linux/devel/sage-nca/sage/rings/number_field/maps.py\n         [15.2 s]\nsage -t  3.2.2.alpha0-x86_64-Linux/devel/sage-nca/sage/rings/number_field/number_field_ideal_rel.py\n         [4.1 s]\nsage -t  3.2.2.alpha0-x86_64-Linux/devel/sage-nca/sage/rings/number_field/number_field_morphisms.pyx\n         [4.1 s]\nsage -t  3.2.2.alpha0-x86_64-Linux/devel/sage-nca/sage/rings/number_field/number_field_element_quadratic.pyx\n         [4.2 s]\nsage -t  3.2.2.alpha0-x86_64-Linux/devel/sage-nca/sage/rings/number_field/small_primes_of_degree_one.py\n         [5.1 s]\nsage -t  3.2.2.alpha0-x86_64-Linux/devel/sage-nca/sage/rings/number_field/number_field_ideal.py\n         [11.2 s]\nsage -t  3.2.2.alpha0-x86_64-Linux/devel/sage-nca/sage/rings/number_field/totallyreal.pyx\n         [7.1 s]\nsage -t  3.2.2.alpha0-x86_64-Linux/devel/sage-nca/sage/rings/number_field/totallyreal_data.pyx\n         [3.1 s]\nsage -t  3.2.2.alpha0-x86_64-Linux/devel/sage-nca/sage/rings/number_field/unit_group.py\n         [0.1 s]\nsage -t  3.2.2.alpha0-x86_64-Linux/devel/sage-nca/sage/rings/number_field/number_field_element.pyx\n         [13.2 s]\nsage -t  3.2.2.alpha0-x86_64-Linux/devel/sage-nca/sage/rings/number_field/totallyreal_phc.py\n         [3.1 s]\nsage -t  3.2.2.alpha0-x86_64-Linux/devel/sage-nca/sage/rings/number_field/order.py\n         [10.2 s]\nsage -t  3.2.2.alpha0-x86_64-Linux/devel/sage-nca/sage/rings/number_field/totallyreal_rel.py\n         [4.1 s]\n  ***   Warning: large Minkowski bound: certification will be VERY long.\n  ***   Warning: large Minkowski bound: certification will be VERY long.\nsage -t  3.2.2.alpha0-x86_64-Linux/devel/sage-nca/sage/rings/number_field/number_field.py\n         [45.6 s]\nAll tests passed!\nTimings have been updated.\nTotal time for all tests: 45.6 seconds\n\n\nncalexan@sage:~/sage/devel/sage-nca$ ~/sage/sage -tp 6 sage/libs/pari/*\nGlobal iterations: 1\nFile iterations: 1\nTeX files: 0\nUsing cached timings.\n \n----------------------------------------------------------------------\nsage -t  3.2.2.alpha0-x86_64-Linux/devel/sage-nca/sage/libs/pari/gen.pxi\n         [0.1 s]\nsage -t  3.2.2.alpha0-x86_64-Linux/devel/sage-nca/sage/libs/pari/decl.pxi\n         [0.1 s]\nsage -t  3.2.2.alpha0-x86_64-Linux/devel/sage-nca/sage/libs/pari/misc.pxi\n         [0.1 s]\nsage -t  3.2.2.alpha0-x86_64-Linux/devel/sage-nca/sage/libs/pari/pari_err.pxi\n         [0.1 s]\nsage -t  3.2.2.alpha0-x86_64-Linux/devel/sage-nca/sage/libs/pari/to_gen.pxi\n         [0.1 s]\nsage -t  3.2.2.alpha0-x86_64-Linux/devel/sage-nca/sage/libs/pari/setlvalue.pxi\n         [0.1 s]\nsage -t  3.2.2.alpha0-x86_64-Linux/devel/sage-nca/sage/libs/pari/gen_py.py\n         [3.1 s]\nsage -t  3.2.2.alpha0-x86_64-Linux/devel/sage-nca/sage/libs/pari/gen.pyx\n         [5.4 s]\nAll tests passed!\nTimings have been updated.\nTotal time for all tests: 5.4 seconds\nncalexan@sage:~/sage/devel/sage-nca$\n```\n",
    "created_at": "2008-12-09T18:55:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4695",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4695#issuecomment-35310",
    "user": "https://github.com/ncalexan"
}
```

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

archive/issue_comments_035311.json:
```json
{
    "body": "4695-ncalexan-rnfidealdown.2.patch applied to my current merge tree passes long doctests. So all we need now is a positive review :)\n\nCheers,\n\nMichael",
    "created_at": "2008-12-10T10:26:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4695",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4695#issuecomment-35311",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

4695-ncalexan-rnfidealdown.2.patch applied to my current merge tree passes long doctests. So all we need now is a positive review :)

Cheers,

Michael



---

archive/issue_comments_035312.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-12-10T16:24:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4695",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4695#issuecomment-35312",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_004940.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-12-10T16:24:04Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4695",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4695#event-4940"
}
```



---

archive/issue_comments_035313.json:
```json
{
    "body": "Merged 4695-ncalexan-rnfidealdown.2.patch in Sage 3.2.2.alpha2",
    "created_at": "2008-12-10T16:24:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4695",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4695#issuecomment-35313",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged 4695-ncalexan-rnfidealdown.2.patch in Sage 3.2.2.alpha2
