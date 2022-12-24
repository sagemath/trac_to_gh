# Issue 2156: [with spkg, needs review] Cython 0.9.6.12

archive/issues_002156.json:
```json
{
    "body": "Assignee: mabshoff\n\nGet the spkg in http://sage.math.washington.edu/home/robertwb/cython/ \n\nsage -ba; sage -testall works on intel OS X 10.4. \n\nThe most significant change is more flexible c(p)def functions and overriding. Specifically, c(p)def functions can now:\n* have optional arguments (which may grow)\n* be defined in the module scope\n* are always cimport-able if defined in the .pxd (i.e. \"api\" by default)\n* declare narrower return types than the superclass\n* cpdef can override cdef\n\nThere are also better conversions (<type?> does a type-checked cast, <int>x does the right thing), and numerous optimizations (especially with regard to tuple unpacking) and bugfixes. \n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2156\n\n",
    "created_at": "2008-02-14T04:32:28Z",
    "labels": [
        "packages: standard",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.2",
    "title": "[with spkg, needs review] Cython 0.9.6.12",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2156",
    "user": "robertwb"
}
```
Assignee: mabshoff

Get the spkg in http://sage.math.washington.edu/home/robertwb/cython/ 

sage -ba; sage -testall works on intel OS X 10.4. 

The most significant change is more flexible c(p)def functions and overriding. Specifically, c(p)def functions can now:
* have optional arguments (which may grow)
* be defined in the module scope
* are always cimport-able if defined in the .pxd (i.e. "api" by default)
* declare narrower return types than the superclass
* cpdef can override cdef

There are also better conversions (<type?> does a type-checked cast, <int>x does the right thing), and numerous optimizations (especially with regard to tuple unpacking) and bugfixes. 


Issue created by migration from https://trac.sagemath.org/ticket/2156





---

archive/issue_comments_014158.json:
```json
{
    "body": "Two things\n* the name of the spkg needs to be lower case, i.e. `Cython` vs. `cython`\n* A `sage -ba` works fine on sage.math, but upon startup I get:\n\n```\nmabshoff@sage:/scratch/mabshoff/release-cycle/sage-2.10.2.alpha0$ ./sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n| SAGE Version 2.10.1, Release Date: 2008-02-02                      |\n| Type notebook() for the GUI, and license() for information.        |\n---------------------------------------------------------------------------\n<type 'exceptions.TypeError'>             Traceback (most recent call last)\n\n/scratch/mabshoff/release-cycle/sage-2.10.2.alpha0/local/bin/<ipython console> in <module>()\n\n/scratch/mabshoff/release-cycle/sage-2.10.2.alpha0/local/lib/python2.5/site-packages/sage/all_cmdline.py in <module>()\n     12 try:\n     13\n---> 14     from sage.all import *\n     15     from sage.calculus.predefined import x\n     16     preparser(on=True)\n\n/scratch/mabshoff/release-cycle/sage-2.10.2.alpha0/local/lib/python2.5/site-packages/sage/all.py in <module>()\n     59 get_sigs()\n     60\n---> 61 from sage.rings.all      import *\n     62 from sage.matrix.all     import *\n     63\n\n/scratch/mabshoff/release-cycle/sage-2.10.2.alpha0/local/lib/python2.5/site-packages/sage/rings/all.py in <module>()\n     90\n     91 # Algebraic numbers\n---> 92 from qqbar import (AlgebraicRealField, is_AlgebraicRealField, AA,\n     93                    AlgebraicReal, is_AlgebraicReal,\n     94                    AlgebraicField, is_AlgebraicField, QQbar,\n\n/scratch/mabshoff/release-cycle/sage-2.10.2.alpha0/local/lib/python2.5/site-packages/sage/rings/qqbar.py in <module>()\n   4038\n   4039\n-> 4040 RR_1_10 = RR(ZZ(1)/10)\n   4041 QQ_0 = QQ(0)\n   4042 QQ_1 = QQ(1)\n\n/scratch/mabshoff/release-cycle/sage-2.10.2.alpha0/local/bin/element.pyx in sage.structure.element.RingElement.__div__()\n\n/scratch/mabshoff/release-cycle/sage-2.10.2.alpha0/local/bin/coerce.pyx in sage.structure.coerce.CoercionModel_cache_maps.bin_op_c()\n\n/scratch/mabshoff/release-cycle/sage-2.10.2.alpha0/local/bin/coerce.pyx in sage.structure.coerce.CoercionModel_cache_maps.get_action_c()\n\n/scratch/mabshoff/release-cycle/sage-2.10.2.alpha0/local/bin/coerce_dict.pyx in sage.structure.coerce_dict.TripleDict.get()\n\n<type 'exceptions.TypeError'>: 'sage.rings.integer_ring.IntegerRing_class' object cannot be interpreted as an index\nsage:\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2008-02-14T12:58:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2156",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2156#issuecomment-14158",
    "user": "mabshoff"
}
```

Two things
* the name of the spkg needs to be lower case, i.e. `Cython` vs. `cython`
* A `sage -ba` works fine on sage.math, but upon startup I get:

```
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-2.10.2.alpha0$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 2.10.1, Release Date: 2008-02-02                      |
| Type notebook() for the GUI, and license() for information.        |
---------------------------------------------------------------------------
<type 'exceptions.TypeError'>             Traceback (most recent call last)

/scratch/mabshoff/release-cycle/sage-2.10.2.alpha0/local/bin/<ipython console> in <module>()

/scratch/mabshoff/release-cycle/sage-2.10.2.alpha0/local/lib/python2.5/site-packages/sage/all_cmdline.py in <module>()
     12 try:
     13
---> 14     from sage.all import *
     15     from sage.calculus.predefined import x
     16     preparser(on=True)

/scratch/mabshoff/release-cycle/sage-2.10.2.alpha0/local/lib/python2.5/site-packages/sage/all.py in <module>()
     59 get_sigs()
     60
---> 61 from sage.rings.all      import *
     62 from sage.matrix.all     import *
     63

/scratch/mabshoff/release-cycle/sage-2.10.2.alpha0/local/lib/python2.5/site-packages/sage/rings/all.py in <module>()
     90
     91 # Algebraic numbers
---> 92 from qqbar import (AlgebraicRealField, is_AlgebraicRealField, AA,
     93                    AlgebraicReal, is_AlgebraicReal,
     94                    AlgebraicField, is_AlgebraicField, QQbar,

/scratch/mabshoff/release-cycle/sage-2.10.2.alpha0/local/lib/python2.5/site-packages/sage/rings/qqbar.py in <module>()
   4038
   4039
-> 4040 RR_1_10 = RR(ZZ(1)/10)
   4041 QQ_0 = QQ(0)
   4042 QQ_1 = QQ(1)

/scratch/mabshoff/release-cycle/sage-2.10.2.alpha0/local/bin/element.pyx in sage.structure.element.RingElement.__div__()

/scratch/mabshoff/release-cycle/sage-2.10.2.alpha0/local/bin/coerce.pyx in sage.structure.coerce.CoercionModel_cache_maps.bin_op_c()

/scratch/mabshoff/release-cycle/sage-2.10.2.alpha0/local/bin/coerce.pyx in sage.structure.coerce.CoercionModel_cache_maps.get_action_c()

/scratch/mabshoff/release-cycle/sage-2.10.2.alpha0/local/bin/coerce_dict.pyx in sage.structure.coerce_dict.TripleDict.get()

<type 'exceptions.TypeError'>: 'sage.rings.integer_ring.IntegerRing_class' object cannot be interpreted as an index
sage:
```


Cheers,

Michael



---

archive/issue_comments_014159.json:
```json
{
    "body": "Changing the case is easy enough. I'll look into what's going wrong on sage.math.",
    "created_at": "2008-02-14T18:12:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2156",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2156#issuecomment-14159",
    "user": "robertwb"
}
```

Changing the case is easy enough. I'll look into what's going wrong on sage.math.



---

archive/issue_comments_014160.json:
```json
{
    "body": "About the case: sure, I ended up doing that when I looked into the spkg and made sure there was no \"junk\" in it due to the increased size.\n\nAn interesting data point: After installing the old cython.spkg (0.9.6.11b) and doing a `sage -ba` I still go the same error. Only after deleting the installed Cython in `site-packages`, doing another install of 0.9.6.11b and then `sage -ba` did the error disappear.\n\nCheers,\n\nMichael",
    "created_at": "2008-02-14T18:16:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2156",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2156#issuecomment-14160",
    "user": "mabshoff"
}
```

About the case: sure, I ended up doing that when I looked into the spkg and made sure there was no "junk" in it due to the increased size.

An interesting data point: After installing the old cython.spkg (0.9.6.11b) and doing a `sage -ba` I still go the same error. Only after deleting the installed Cython in `site-packages`, doing another install of 0.9.6.11b and then `sage -ba` did the error disappear.

Cheers,

Michael



---

archive/issue_comments_014161.json:
```json
{
    "body": "I thing the above may be a case issue (cython didn't overwrite Cython) but I know what the issue is--there's a patch that needs to be installed because <int>x no longer returns the address of x (which is used in `coerce_dict.TripleDict.get()`.",
    "created_at": "2008-02-14T18:25:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2156",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2156#issuecomment-14161",
    "user": "robertwb"
}
```

I thing the above may be a case issue (cython didn't overwrite Cython) but I know what the issue is--there's a patch that needs to be installed because <int>x no longer returns the address of x (which is used in `coerce_dict.TripleDict.get()`.



---

archive/issue_comments_014162.json:
```json
{
    "body": "Attachment [2156-tripledict.patch](tarball://root/attachments/some-uuid/ticket2156/2156-tripledict.patch) by robertwb created at 2008-02-14 18:29:51\n\nI've uploaded a new spkg with a lowercase 'c' to the same directory as before. With the attached patch, things should work fine.",
    "created_at": "2008-02-14T18:29:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2156",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2156#issuecomment-14162",
    "user": "robertwb"
}
```

Attachment [2156-tripledict.patch](tarball://root/attachments/some-uuid/ticket2156/2156-tripledict.patch) by robertwb created at 2008-02-14 18:29:51

I've uploaded a new spkg with a lowercase 'c' to the same directory as before. With the attached patch, things should work fine.



---

archive/issue_comments_014163.json:
```json
{
    "body": "Good news: the updated spkg and the additional patch make sage start after a `sage -ba`. Ergo positive review, running `-testall` to make sure everything is still working.\n\nCheers,\n\nMichael",
    "created_at": "2008-02-14T20:39:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2156",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2156#issuecomment-14163",
    "user": "mabshoff"
}
```

Good news: the updated spkg and the additional patch make sage start after a `sage -ba`. Ergo positive review, running `-testall` to make sure everything is still working.

Cheers,

Michael



---

archive/issue_comments_014164.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-14T21:29:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2156",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2156#issuecomment-14164",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_014165.json:
```json
{
    "body": "Merged in Sage 2.10.2.alpha0",
    "created_at": "2008-02-14T21:29:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2156",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2156#issuecomment-14165",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.2.alpha0
