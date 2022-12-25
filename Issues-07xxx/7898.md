# Issue 7898: Change common variables to names in singular

archive/issues_007898.json:
```json
{
    "body": "Assignee: GeorgSWeber\n\nCC:  @jaapspies\n\nIt was agreed recently that variables would not be used for very common commands like MV, MKDIR etc. \n\nhttp://groups.google.com/group/sage-devel/browse_thread/thread/bd7ae07a1157bead/970aa0dc8fa56ab7?lnk=raot\n\n#7818 usets these, so this package will break. The fix is to simply replace things like \n\n$LN with 'ln'\n\nAn updated .spkg can be found at\n\nhttp://boxen.math.washington.edu/home/kirkby/portability/singular-3-1-0-4-20090818.p3/singular-3-1-0-4-20090818.p3.spkg\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7898\n\n",
    "closed_at": "2010-01-16T02:29:09Z",
    "created_at": "2010-01-12T03:12:28Z",
    "labels": [
        "component: build",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.1",
    "title": "Change common variables to names in singular",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7898",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: GeorgSWeber

CC:  @jaapspies

It was agreed recently that variables would not be used for very common commands like MV, MKDIR etc. 

http://groups.google.com/group/sage-devel/browse_thread/thread/bd7ae07a1157bead/970aa0dc8fa56ab7?lnk=raot

#7818 usets these, so this package will break. The fix is to simply replace things like 

$LN with 'ln'

An updated .spkg can be found at

http://boxen.math.washington.edu/home/kirkby/portability/singular-3-1-0-4-20090818.p3/singular-3-1-0-4-20090818.p3.spkg



Issue created by migration from https://trac.sagemath.org/ticket/7898





---

archive/issue_comments_068572.json:
```json
{
    "body": "Replace all things like $MKDIR with mkdir",
    "created_at": "2010-01-12T03:13:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7898",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7898#issuecomment-68572",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Replace all things like $MKDIR with mkdir



---

archive/issue_comments_068573.json:
```json
{
    "body": "Attachment [singular-variables-to-names.patch](tarball://root/attachments/some-uuid/ticket7898/singular-variables-to-names.patch) by drkirkby created at 2010-01-12 03:41:04\n\nNote, $CP is purposely left as '$CP', since the GNU version of 'cp' have an extra option which can be useful.",
    "created_at": "2010-01-12T03:41:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7898",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7898#issuecomment-68573",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Attachment [singular-variables-to-names.patch](tarball://root/attachments/some-uuid/ticket7898/singular-variables-to-names.patch) by drkirkby created at 2010-01-12 03:41:04

Note, $CP is purposely left as '$CP', since the GNU version of 'cp' have an extra option which can be useful.



---

archive/issue_comments_068574.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-12T03:41:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7898",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7898#issuecomment-68574",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_068575.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-12T10:24:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7898",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7898#issuecomment-68575",
    "user": "https://github.com/jaapspies"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_068576.json:
```json
{
    "body": "The new spkg looks good. Checked on Fedora and Open Solaris.\n\nPositive review.\n\nJaap",
    "created_at": "2010-01-12T10:24:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7898",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7898#issuecomment-68576",
    "user": "https://github.com/jaapspies"
}
```

The new spkg looks good. Checked on Fedora and Open Solaris.

Positive review.

Jaap



---

archive/issue_events_018892.json:
```json
{
    "actor": "https://github.com/rlmill",
    "created_at": "2010-01-14T02:50:33Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7898",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7898#event-18892"
}
```



---

archive/issue_comments_068577.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-14T02:50:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7898",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7898#issuecomment-68577",
    "user": "https://github.com/rlmill"
}
```

Resolution: fixed



---

archive/issue_comments_068578.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2010-01-14T06:35:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7898",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7898#issuecomment-68578",
    "user": "https://github.com/rlmill"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_068579.json:
```json
{
    "body": "Changing status from closed to new.",
    "created_at": "2010-01-14T06:35:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7898",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7898#issuecomment-68579",
    "user": "https://github.com/rlmill"
}
```

Changing status from closed to new.



---

archive/issue_events_018893.json:
```json
{
    "actor": "https://github.com/rlmill",
    "created_at": "2010-01-14T06:35:28Z",
    "event": "reopened",
    "issue": "https://github.com/sagemath/sagetest/issues/7898",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7898#event-18893"
}
```



---

archive/issue_comments_068580.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-01-14T06:36:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7898",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7898#issuecomment-68580",
    "user": "https://github.com/rlmill"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_068581.json:
```json
{
    "body": "Sage did not start after building this spkg on boxen:\n\n```\nrlmill@boxen:/scratch/rlm/sage-4.3.1.rc0/devel/sage-main$ ../../sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n**********************************************************************\n*                                                                    *\n* Warning: this is a prerelease version, and it may be unstable.     *\n*                                                                    *\n**********************************************************************\n---------------------------------------------------------------------------\nNotImplementedError                       Traceback (most recent call last)\n| Sage Version 4.3.1.alpha2, Release Date: 2010-01-13                |\n| Type notebook() for the GUI, and license() for information.        |\n/virtual/scratch/rlm/sage-4.3.1.rc0/local/lib/python2.6/site-packages/IPython/ipmaker.pyc\nin force_import(modname)\n    64         reload(sys.modules[modname])\n    65     else:\n---> 66         __import__(modname)\n    67\n    68\n\n/virtual/scratch/rlm/sage-4.3.1.rc0/local/bin/ipy_profile_sage.py in <module>()\n     5     preparser(True)\n     6\n----> 7     import sage.all_cmdline\n     8     sage.all_cmdline._init_cmdline(globals())\n     9\n\n/virtual/scratch/rlm/sage-4.3.1.rc0/local/lib/python2.6/site-packages/sage/all_cmdline.py\nin <module>()\n    12 try:\n    13\n---> 14     from sage.all import *\n    15     from sage.calculus.predefined import x\n    16     preparser(on=True)\n\n/virtual/scratch/rlm/sage-4.3.1.rc0/local/lib/python2.6/site-packages/sage/all.py\nin <module>()\n    70 get_sigs()\n    71\n---> 72 from sage.rings.all      import *\n    73 from sage.matrix.all     import *\n    74\n\n/virtual/scratch/rlm/sage-4.3.1.rc0/local/lib/python2.6/site-packages/sage/rings/all.py\nin <module>()\n    92\n    93 # Algebraic numbers\n\n---> 94 from qqbar import (AlgebraicRealField, is_AlgebraicRealField, AA,\n    95                    AlgebraicReal, is_AlgebraicReal,\n    96                    AlgebraicField, is_AlgebraicField, QQbar,\n\n/virtual/scratch/rlm/sage-4.3.1.rc0/local/lib/python2.6/site-packages/sage/rings/qqbar.py\nin <module>()\n  1414 QQy = QQ['y']\n  1415 QQy_y = QQy.gen()\n-> 1416 QQxy = QQ['x', 'y']\n  1417 QQxy_x = QQxy.gen(0)\n  1418 QQxy_y = QQxy.gen(1)\n\n/virtual/scratch/rlm/sage-4.3.1.rc0/local/lib/python2.6/site-packages/sage/rings/ring.so\nin sage.rings.ring.Ring.__getitem__ (sage/rings/ring.c:2685)()\n\n/virtual/scratch/rlm/sage-4.3.1.rc0/local/lib/python2.6/site-packages/sage/rings/polynomial/polynomial_ring_constructor.pyc\nin PolynomialRing(base_ring, arg1, arg2, sparse, order, names, name,\nimplementation)\n   353             names = arg1\n   354             n = len(names)\n--> 355             R = _multi_variate(base_ring, names, n, sparse, order)\n   356\n   357     if arg1 is None and arg2 is None:\n\n/virtual/scratch/rlm/sage-4.3.1.rc0/local/lib/python2.6/site-packages/sage/rings/polynomial/polynomial_ring_constructor.pyc\nin _multi_variate(base_ring, names, n, sparse, order)\n   451         return R\n   452\n--> 453     from sage.rings.polynomial.multi_polynomial_libsingular\nimport MPolynomialRing_libsingular\n   454     if m.integral_domain.is_IntegralDomain(base_ring):\n   455         if n < 1:\n\n/virtual/scratch/rlm/sage-4.3.1.rc0/local/bin/multi_polynomial_libsingular.pyx\nin init sage.rings.polynomial.multi_polynomial_libsingular\n(sage/rings/polynomial/multi_polynomial_libsingular.cpp:29460)()\n\n/virtual/scratch/rlm/sage-4.3.1.rc0/local/lib/python2.6/site-packages/sage/libs/singular/__init__.py\nin <module>()\n     6\n     7 ## We predefine a couple of often used functions here to avoid\nthe fetch overhead ##\n\n----> 8 groebner = singular_function('groebner')\n     9\n    10\n\n/virtual/scratch/rlm/sage-4.3.1.rc0/local/lib/python2.6/site-packages/sage/libs/singular/function.so\nin sage.libs.singular.function.singular_function\n(sage/libs/singular/function.cpp:11103)()\n\n/virtual/scratch/rlm/sage-4.3.1.rc0/local/lib/python2.6/site-packages/sage/libs/singular/function.so\nin sage.libs.singular.function.SingularKernelFunction.__init__\n(sage/libs/singular/function.cpp:10853)()\n\n/virtual/scratch/rlm/sage-4.3.1.rc0/local/lib/python2.6/site-packages/sage/libs/singular/function.so\nin sage.libs.singular.function.SingularFunction.get_call_handler\n(sage/libs/singular/function.cpp:9141)()\n\nNotImplementedError:\nError importing ipy_profile_sage - perhaps you should run %upgrade?\nWARNING: Loading of ipy_profile_sage failed.\n```",
    "created_at": "2010-01-14T06:36:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7898",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7898#issuecomment-68581",
    "user": "https://github.com/rlmill"
}
```

Sage did not start after building this spkg on boxen:

```
rlmill@boxen:/scratch/rlm/sage-4.3.1.rc0/devel/sage-main$ ../../sage
----------------------------------------------------------------------
----------------------------------------------------------------------
**********************************************************************
*                                                                    *
* Warning: this is a prerelease version, and it may be unstable.     *
*                                                                    *
**********************************************************************
---------------------------------------------------------------------------
NotImplementedError                       Traceback (most recent call last)
| Sage Version 4.3.1.alpha2, Release Date: 2010-01-13                |
| Type notebook() for the GUI, and license() for information.        |
/virtual/scratch/rlm/sage-4.3.1.rc0/local/lib/python2.6/site-packages/IPython/ipmaker.pyc
in force_import(modname)
    64         reload(sys.modules[modname])
    65     else:
---> 66         __import__(modname)
    67
    68

/virtual/scratch/rlm/sage-4.3.1.rc0/local/bin/ipy_profile_sage.py in <module>()
     5     preparser(True)
     6
----> 7     import sage.all_cmdline
     8     sage.all_cmdline._init_cmdline(globals())
     9

/virtual/scratch/rlm/sage-4.3.1.rc0/local/lib/python2.6/site-packages/sage/all_cmdline.py
in <module>()
    12 try:
    13
---> 14     from sage.all import *
    15     from sage.calculus.predefined import x
    16     preparser(on=True)

/virtual/scratch/rlm/sage-4.3.1.rc0/local/lib/python2.6/site-packages/sage/all.py
in <module>()
    70 get_sigs()
    71
---> 72 from sage.rings.all      import *
    73 from sage.matrix.all     import *
    74

/virtual/scratch/rlm/sage-4.3.1.rc0/local/lib/python2.6/site-packages/sage/rings/all.py
in <module>()
    92
    93 # Algebraic numbers

---> 94 from qqbar import (AlgebraicRealField, is_AlgebraicRealField, AA,
    95                    AlgebraicReal, is_AlgebraicReal,
    96                    AlgebraicField, is_AlgebraicField, QQbar,

/virtual/scratch/rlm/sage-4.3.1.rc0/local/lib/python2.6/site-packages/sage/rings/qqbar.py
in <module>()
  1414 QQy = QQ['y']
  1415 QQy_y = QQy.gen()
-> 1416 QQxy = QQ['x', 'y']
  1417 QQxy_x = QQxy.gen(0)
  1418 QQxy_y = QQxy.gen(1)

/virtual/scratch/rlm/sage-4.3.1.rc0/local/lib/python2.6/site-packages/sage/rings/ring.so
in sage.rings.ring.Ring.__getitem__ (sage/rings/ring.c:2685)()

/virtual/scratch/rlm/sage-4.3.1.rc0/local/lib/python2.6/site-packages/sage/rings/polynomial/polynomial_ring_constructor.pyc
in PolynomialRing(base_ring, arg1, arg2, sparse, order, names, name,
implementation)
   353             names = arg1
   354             n = len(names)
--> 355             R = _multi_variate(base_ring, names, n, sparse, order)
   356
   357     if arg1 is None and arg2 is None:

/virtual/scratch/rlm/sage-4.3.1.rc0/local/lib/python2.6/site-packages/sage/rings/polynomial/polynomial_ring_constructor.pyc
in _multi_variate(base_ring, names, n, sparse, order)
   451         return R
   452
--> 453     from sage.rings.polynomial.multi_polynomial_libsingular
import MPolynomialRing_libsingular
   454     if m.integral_domain.is_IntegralDomain(base_ring):
   455         if n < 1:

/virtual/scratch/rlm/sage-4.3.1.rc0/local/bin/multi_polynomial_libsingular.pyx
in init sage.rings.polynomial.multi_polynomial_libsingular
(sage/rings/polynomial/multi_polynomial_libsingular.cpp:29460)()

/virtual/scratch/rlm/sage-4.3.1.rc0/local/lib/python2.6/site-packages/sage/libs/singular/__init__.py
in <module>()
     6
     7 ## We predefine a couple of often used functions here to avoid
the fetch overhead ##

----> 8 groebner = singular_function('groebner')
     9
    10

/virtual/scratch/rlm/sage-4.3.1.rc0/local/lib/python2.6/site-packages/sage/libs/singular/function.so
in sage.libs.singular.function.singular_function
(sage/libs/singular/function.cpp:11103)()

/virtual/scratch/rlm/sage-4.3.1.rc0/local/lib/python2.6/site-packages/sage/libs/singular/function.so
in sage.libs.singular.function.SingularKernelFunction.__init__
(sage/libs/singular/function.cpp:10853)()

/virtual/scratch/rlm/sage-4.3.1.rc0/local/lib/python2.6/site-packages/sage/libs/singular/function.so
in sage.libs.singular.function.SingularFunction.get_call_handler
(sage/libs/singular/function.cpp:9141)()

NotImplementedError:
Error importing ipy_profile_sage - perhaps you should run %upgrade?
WARNING: Loading of ipy_profile_sage failed.
```



---

archive/issue_comments_068582.json:
```json
{
    "body": "I'm totally baffled how on earth changing \n\n* $CHMOD to 'chmod'\n* $RM to 'rm'\n* $LN to 'ln'\n\nin singular's spkg-install file can break the singular package. All the variables were defined elsewhere (sage-env) to be just the command - no options were given. \n\nI can't help feel there must be some other explanation, but I'll certainly take a closer look at this. \n\nDave",
    "created_at": "2010-01-14T07:14:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7898",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7898#issuecomment-68582",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

I'm totally baffled how on earth changing 

* $CHMOD to 'chmod'
* $RM to 'rm'
* $LN to 'ln'

in singular's spkg-install file can break the singular package. All the variables were defined elsewhere (sage-env) to be just the command - no options were given. 

I can't help feel there must be some other explanation, but I'll certainly take a closer look at this. 

Dave



---

archive/issue_comments_068583.json:
```json
{
    "body": "This looks like the other errors we got from #7818. I'll give this one another try for rc0.",
    "created_at": "2010-01-16T01:01:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7898",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7898#issuecomment-68583",
    "user": "https://github.com/rlmill"
}
```

This looks like the other errors we got from #7818. I'll give this one another try for rc0.



---

archive/issue_comments_068584.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-16T02:29:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7898",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7898#issuecomment-68584",
    "user": "https://github.com/rlmill"
}
```

Resolution: fixed



---

archive/issue_events_018894.json:
```json
{
    "actor": "https://github.com/rlmill",
    "created_at": "2010-01-16T02:29:09Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7898",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7898#event-18894"
}
```
