# Issue 1137: matrix visualize_structure is completely broken on osx (at least 10.5) -- why no doctest to catch this!?

archive/issues_001137.json:
```json
{
    "body": "Assignee: was\n\n\n```\nsage: sr = mq.SR(2,1,1,4,gf2=True)\nsage: sr\nSR(2,1,1,4)\nsage: F,s = sr.polynomial_system()\nsage: F\nPolynomial System with 104 Polynomials in 36 Variables\nsage: gb = F.groebner_basis()\nsage: Ideal(gb).variety()\n[{x101: 0, x100: 0, x103: 1, x102: 0, k103: 1, x202: 0, x203: 1, x200: 1, x201: 1, w100: 0, w101: 0, w102: 0, w103: 1, k102: 1, k203: 0, k202: 1, k201: 0, k200: 1, s001: 0, s000: 1, s003: 1, s002: 1, k001: 1, k000: 0, k003: 1, k002: 0, w203: 0, w202: 0, w201: 1, w200: 0, s100: 1, s101: 0, s102: 0, s103: 0, k100: 1, k101: 1}]\nsage: s\n{k001: 1, k000: 0, k003: 1, k002: 0}\nsage: A,v = F.coefficient_matrix()\nsage: A.visualize_structure()\nTraceback (most recent call last):\n...\nImportError: dlopen(/Users/was/s/local/lib/python2.5/site-packages/_gd.so, 2): Library not loaded: /Users/was/Desktop/sage-2.8.10.rc1/local/lib/libpng.3.dylib\n  Referenced from: /Users/was/s/local/lib/python2.5/site-packages/_gd.so\n  Reason: image not found\n```\n\n\nTodo:\n1. Make a doctest that would catch this\n2. Fix the problem.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1137\n\n",
    "created_at": "2007-11-10T12:09:31Z",
    "labels": [
        "linear algebra",
        "major",
        "bug"
    ],
    "title": "matrix visualize_structure is completely broken on osx (at least 10.5) -- why no doctest to catch this!?",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1137",
    "user": "was"
}
```
Assignee: was


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

archive/issue_comments_006900.json:
```json
{
    "body": "With 2.8.13.rc0 in bsd the above code works and outputs a png. So who can actually still reproduce this?\n\nCheers,\n\nMichael",
    "created_at": "2007-11-20T13:59:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1137",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1137#issuecomment-6900",
    "user": "mabshoff"
}
```

With 2.8.13.rc0 in bsd the above code works and outputs a png. So who can actually still reproduce this?

Cheers,

Michael



---

archive/issue_comments_006901.json:
```json
{
    "body": "\n```\nsage: M = random_matrix(CC, 4)\nsage: M.visualize_structure()\nsage:\n```\n\non OS 10.5.1. However,\n\n```\nsage: M\n\n[ 1.00000000000000                 0  2.00000000000000 -2.00000000000000]\n[ 2.00000000000000 -1.00000000000000  2.00000000000000  2.00000000000000]\n[                0 -2.00000000000000  2.00000000000000                 0]\n[-2.00000000000000 -1.00000000000000 -2.00000000000000  1.00000000000000]\n```\n\nand the output is all white.",
    "created_at": "2007-12-02T00:42:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1137",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1137#issuecomment-6901",
    "user": "rlm"
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

archive/issue_comments_006902.json:
```json
{
    "body": "Attachment\n\nI can't get this to work at all on OS X 10.4 (intel)\n\n\n```\nsage: sage: M.visualize_structure()\n------------------------------------------------------------\nTraceback (most recent call last):\n  File \"<ipython console>\", line 1, in <module>\n  File \"matrix2.pyx\", line 2853, in sage.matrix.matrix2.Matrix.visualize_structure\n  File \"/Users/robert/sage/current/local/lib/python2.5/site-packages/gd.py\", line 10, in <module>\n    import _gd\n<type 'exceptions.ImportError'>: dlopen(/Users/robert/sage/current/local/lib/python2.5/site-packages/_gd.so, 2): Symbol not found: _png_get_rowbytes\n  Referenced from: /Users/robert/sage/current/local/lib//libgd.2.dylib\n  Expected in: flat namespace\n```\n",
    "created_at": "2007-12-02T02:22:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1137",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1137#issuecomment-6902",
    "user": "robertwb"
}
```

Attachment

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

archive/issue_comments_006903.json:
```json
{
    "body": "This patch does not fix the OS X 10.4 problem, but it does fix some other bugs in the same function.",
    "created_at": "2007-12-03T03:21:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1137",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1137#issuecomment-6903",
    "user": "rlm"
}
```

This patch does not fix the OS X 10.4 problem, but it does fix some other bugs in the same function.



---

archive/issue_comments_006904.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-15T14:10:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1137",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1137#issuecomment-6904",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_006905.json:
```json
{
    "body": "Merged in 2.9.rc0.",
    "created_at": "2007-12-15T14:10:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1137",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1137#issuecomment-6905",
    "user": "mabshoff"
}
```

Merged in 2.9.rc0.



---

archive/issue_comments_006906.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2007-12-16T14:27:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1137",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1137#issuecomment-6906",
    "user": "mabshoff"
}
```

Changing status from closed to reopened.



---

archive/issue_comments_006907.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2007-12-16T14:27:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1137",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1137#issuecomment-6907",
    "user": "mabshoff"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_006908.json:
```json
{
    "body": "Fixing the issue by updating libpng breaks other spkgs like R, so revert it until we can figure out how to solve it properly.\n\nCheers,\n\nMichael",
    "created_at": "2007-12-16T14:27:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1137",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1137#issuecomment-6908",
    "user": "mabshoff"
}
```

Fixing the issue by updating libpng breaks other spkgs like R, so revert it until we can figure out how to solve it properly.

Cheers,

Michael



---

archive/issue_comments_006909.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-10T03:05:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1137",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1137#issuecomment-6909",
    "user": "rlm"
}
```

Resolution: fixed
