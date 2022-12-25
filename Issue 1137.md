# Issue 1137: matrix visualize_structure is completely broken on osx (at least 10.5) -- why no doctest to catch this!?

archive/issues_001137.json:
```json
{
    "body": "Assignee: @williamstein\n\n\n```\nsage: sr = mq.SR(2,1,1,4,gf2=True)\nsage: sr\nSR(2,1,1,4)\nsage: F,s = sr.polynomial_system()\nsage: F\nPolynomial System with 104 Polynomials in 36 Variables\nsage: gb = F.groebner_basis()\nsage: Ideal(gb).variety()\n[{x101: 0, x100: 0, x103: 1, x102: 0, k103: 1, x202: 0, x203: 1, x200: 1, x201: 1, w100: 0, w101: 0, w102: 0, w103: 1, k102: 1, k203: 0, k202: 1, k201: 0, k200: 1, s001: 0, s000: 1, s003: 1, s002: 1, k001: 1, k000: 0, k003: 1, k002: 0, w203: 0, w202: 0, w201: 1, w200: 0, s100: 1, s101: 0, s102: 0, s103: 0, k100: 1, k101: 1}]\nsage: s\n{k001: 1, k000: 0, k003: 1, k002: 0}\nsage: A,v = F.coefficient_matrix()\nsage: A.visualize_structure()\nTraceback (most recent call last):\n...\nImportError: dlopen(/Users/was/s/local/lib/python2.5/site-packages/_gd.so, 2): Library not loaded: /Users/was/Desktop/sage-2.8.10.rc1/local/lib/libpng.3.dylib\n  Referenced from: /Users/was/s/local/lib/python2.5/site-packages/_gd.so\n  Reason: image not found\n```\n\n\nTodo:\n1. Make a doctest that would catch this\n2. Fix the problem.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1137\n\n",
    "created_at": "2007-11-10T12:09:31Z",
    "labels": [
        "component: linear algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.2",
    "title": "matrix visualize_structure is completely broken on osx (at least 10.5) -- why no doctest to catch this!?",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1137",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein


```
sage: sr = mq.SR(2,1,1,4,gf2=True)
sage: sr
SR(2,1,1,4)
sage: F,s = sr.polynomial_system()
sage: F
Polynomial System with 104 Polynomials in 36 Variables
sage: gb = F.groebner_basis()
sage: Ideal(gb).variety()
[{x101: 0, x100: 0, x103: 1, x102: 0, k103: 1, x202: 0, x203: 1, x200: 1, x201: 1, w100: 0, w101: 0, w102: 0, w103: 1, k102: 1, k203: 0, k202: 1, k201: 0, k200: 1, s001: 0, s000: 1, s003: 1, s002: 1, k001: 1, k000: 0, k003: 1, k002: 0, w203: 0, w202: 0, w201: 1, w200: 0, s100: 1, s101: 0, s102: 0, s103: 0, k100: 1, k101: 1}]
sage: s
{k001: 1, k000: 0, k003: 1, k002: 0}
sage: A,v = F.coefficient_matrix()
sage: A.visualize_structure()
Traceback (most recent call last):
...
ImportError: dlopen(/Users/was/s/local/lib/python2.5/site-packages/_gd.so, 2): Library not loaded: /Users/was/Desktop/sage-2.8.10.rc1/local/lib/libpng.3.dylib
  Referenced from: /Users/was/s/local/lib/python2.5/site-packages/_gd.so
  Reason: image not found
```


Todo:
1. Make a doctest that would catch this
2. Fix the problem.


Issue created by migration from https://trac.sagemath.org/ticket/1137





---

archive/issue_comments_006879.json:
```json
{
    "body": "With 2.8.13.rc0 in bsd the above code works and outputs a png. So who can actually still reproduce this?\n\nCheers,\n\nMichael",
    "created_at": "2007-11-20T13:59:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1137",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1137#issuecomment-6879",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

With 2.8.13.rc0 in bsd the above code works and outputs a png. So who can actually still reproduce this?

Cheers,

Michael



---

archive/issue_events_003045.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-11-20T13:59:10Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1137",
    "milestone": "sage-2.8.13",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1137#event-3045"
}
```



---

archive/issue_comments_006880.json:
```json
{
    "body": "\n```\nsage: M = random_matrix(CC, 4)\nsage: M.visualize_structure()\nsage:\n```\n\non OS 10.5.1. However,\n\n```\nsage: M\n\n[ 1.00000000000000                 0  2.00000000000000 -2.00000000000000]\n[ 2.00000000000000 -1.00000000000000  2.00000000000000  2.00000000000000]\n[                0 -2.00000000000000  2.00000000000000                 0]\n[-2.00000000000000 -1.00000000000000 -2.00000000000000  1.00000000000000]\n```\n\nand the output is all white.",
    "created_at": "2007-12-02T00:42:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1137",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1137#issuecomment-6880",
    "user": "https://github.com/rlmill"
}
```


```
sage: M = random_matrix(CC, 4)
sage: M.visualize_structure()
sage:
```

on OS 10.5.1. However,

```
sage: M

[ 1.00000000000000                 0  2.00000000000000 -2.00000000000000]
[ 2.00000000000000 -1.00000000000000  2.00000000000000  2.00000000000000]
[                0 -2.00000000000000  2.00000000000000                 0]
[-2.00000000000000 -1.00000000000000 -2.00000000000000  1.00000000000000]
```

and the output is all white.



---

archive/issue_comments_006881.json:
```json
{
    "body": "Attachment [vis.patch](tarball://root/attachments/some-uuid/ticket1137/vis.patch) by @robertwb created at 2007-12-02 02:22:39\n\nI can't get this to work at all on OS X 10.4 (intel)\n\n\n```\nsage: sage: M.visualize_structure()\n------------------------------------------------------------\nTraceback (most recent call last):\n  File \"<ipython console>\", line 1, in <module>\n  File \"matrix2.pyx\", line 2853, in sage.matrix.matrix2.Matrix.visualize_structure\n  File \"/Users/robert/sage/current/local/lib/python2.5/site-packages/gd.py\", line 10, in <module>\n    import _gd\n<type 'exceptions.ImportError'>: dlopen(/Users/robert/sage/current/local/lib/python2.5/site-packages/_gd.so, 2): Symbol not found: _png_get_rowbytes\n  Referenced from: /Users/robert/sage/current/local/lib//libgd.2.dylib\n  Expected in: flat namespace\n```\n",
    "created_at": "2007-12-02T02:22:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1137",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1137#issuecomment-6881",
    "user": "https://github.com/robertwb"
}
```

Attachment [vis.patch](tarball://root/attachments/some-uuid/ticket1137/vis.patch) by @robertwb created at 2007-12-02 02:22:39

I can't get this to work at all on OS X 10.4 (intel)


```
sage: sage: M.visualize_structure()
------------------------------------------------------------
Traceback (most recent call last):
  File "<ipython console>", line 1, in <module>
  File "matrix2.pyx", line 2853, in sage.matrix.matrix2.Matrix.visualize_structure
  File "/Users/robert/sage/current/local/lib/python2.5/site-packages/gd.py", line 10, in <module>
    import _gd
<type 'exceptions.ImportError'>: dlopen(/Users/robert/sage/current/local/lib/python2.5/site-packages/_gd.so, 2): Symbol not found: _png_get_rowbytes
  Referenced from: /Users/robert/sage/current/local/lib//libgd.2.dylib
  Expected in: flat namespace
```




---

archive/issue_comments_006882.json:
```json
{
    "body": "This patch does not fix the OS X 10.4 problem, but it does fix some other bugs in the same function.",
    "created_at": "2007-12-03T03:21:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1137",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1137#issuecomment-6882",
    "user": "https://github.com/rlmill"
}
```

This patch does not fix the OS X 10.4 problem, but it does fix some other bugs in the same function.



---

archive/issue_events_003046.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-12-15T14:10:48Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1137",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1137#event-3046"
}
```



---

archive/issue_comments_006883.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-15T14:10:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1137",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1137#issuecomment-6883",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_006884.json:
```json
{
    "body": "Merged in 2.9.rc0.",
    "created_at": "2007-12-15T14:10:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1137",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1137#issuecomment-6884",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in 2.9.rc0.



---

archive/issue_comments_006885.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2007-12-16T14:27:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1137",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1137#issuecomment-6885",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from closed to reopened.



---

archive/issue_events_003047.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-12-16T14:27:11Z",
    "event": "reopened",
    "issue": "https://github.com/sagemath/sagetest/issues/1137",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1137#event-3047"
}
```



---

archive/issue_events_003048.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-12-16T14:27:11Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1137",
    "milestone": "sage-2.8.13",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1137#event-3048"
}
```



---

archive/issue_events_003049.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-12-16T14:27:11Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1137",
    "milestone": "sage-2.9.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1137#event-3049"
}
```



---

archive/issue_comments_006886.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2007-12-16T14:27:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1137",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1137#issuecomment-6886",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_006887.json:
```json
{
    "body": "Fixing the issue by updating libpng breaks other spkgs like R, so revert it until we can figure out how to solve it properly.\n\nCheers,\n\nMichael",
    "created_at": "2007-12-16T14:27:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1137",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1137#issuecomment-6887",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Fixing the issue by updating libpng breaks other spkgs like R, so revert it until we can figure out how to solve it properly.

Cheers,

Michael



---

archive/issue_events_003050.json:
```json
{
    "actor": "https://github.com/rlmill",
    "created_at": "2008-02-10T03:05:22Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1137",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1137#event-3050"
}
```



---

archive/issue_comments_006888.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-10T03:05:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1137",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1137#issuecomment-6888",
    "user": "https://github.com/rlmill"
}
```

Resolution: fixed
