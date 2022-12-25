# Issue 3814: [with patch, needs quick review] Bug introduced in trac #3800 fix

archive/issues_003814.json:
```json
{
    "body": "Assignee: @craigcitro\n\nI introduced a small bug in trac #3800, which John Cremona ran into while running doctests. Here's a chunk of code that illustrates the failure:\n\n\n```\nsage: chi = DirichletGroup(20).1**3 ; M = ModularSymbols(chi, weight=3, sign=1)\n\nsage: M.cuspidal_subspace()\n```\n\n\nThis raises an exception, but shouldn't be a problem. Patch coming up.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3814\n\n",
    "created_at": "2008-08-12T11:58:09Z",
    "labels": [
        "component: modular forms",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1",
    "title": "[with patch, needs quick review] Bug introduced in trac #3800 fix",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3814",
    "user": "https://github.com/craigcitro"
}
```
Assignee: @craigcitro

I introduced a small bug in trac #3800, which John Cremona ran into while running doctests. Here's a chunk of code that illustrates the failure:


```
sage: chi = DirichletGroup(20).1**3 ; M = ModularSymbols(chi, weight=3, sign=1)

sage: M.cuspidal_subspace()
```


This raises an exception, but shouldn't be a problem. Patch coming up.

Issue created by migration from https://trac.sagemath.org/ticket/3814





---

archive/issue_comments_027075.json:
```json
{
    "body": "Where's the patch??!",
    "created_at": "2008-08-12T19:56:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3814",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3814#issuecomment-27075",
    "user": "https://github.com/JohnCremona"
}
```

Where's the patch??!



---

archive/issue_comments_027076.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-08-12T20:49:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3814",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3814#issuecomment-27076",
    "user": "https://github.com/craigcitro"
}
```

Changing status from new to assigned.



---

archive/issue_comments_027077.json:
```json
{
    "body": "Oops. Tag removed until I post the patch. ;)",
    "created_at": "2008-08-12T20:49:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3814",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3814#issuecomment-27077",
    "user": "https://github.com/craigcitro"
}
```

Oops. Tag removed until I post the patch. ;)



---

archive/issue_comments_027078.json:
```json
{
    "body": "Ok, I'm posting a patch now.",
    "created_at": "2008-08-14T10:07:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3814",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3814#issuecomment-27078",
    "user": "https://github.com/craigcitro"
}
```

Ok, I'm posting a patch now.



---

archive/issue_comments_027079.json:
```json
{
    "body": "Attachment [trac-3814.patch](tarball://root/attachments/some-uuid/ticket3814/trac-3814.patch) by @JohnCremona created at 2008-08-14 16:17:21\n\nPatch code looks good to me, it applies cleanly to a fresh 3.1.alpha2, and all doctests in sage/modular ....passed (in 392s) except for these two:\n\n```\n\tsage -t  devel/sage-3814/sage/modular/modsym/modsym.py\n\tsage -t  devel/sage-3814/sage/modular/modsym/boundary.py\n```\n\n\nDetails:\n\n```\nsage -t  devel/sage-3814/sage/modular/modsym/modsym.py      **********************************************************************\nFile \"/home/john/sage-3.1.alpha2/tmp/modsym.py\", line 51:\n    sage: ModularSymbols(DirichletGroup(20).1**3, weight=3, sign=1).cuspidal_subspace()\nException raised:\n    Traceback (most recent call last):\n      File \"/home/john/sage-3.1.alpha2/local/lib/python2.5/doctest.py\", line 1228, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_0[17]>\", line 1, in <module>\n        ModularSymbols(DirichletGroup(Integer(20)).gen(1)**Integer(3), weight=Integer(3), sign=Integer(1)).cuspidal_subspace()###line 51:\n    sage: ModularSymbols(DirichletGroup(20).1**3, weight=3, sign=1).cuspidal_subspace()\n      File \"/home/john/sage-3.1.alpha2/local/lib/python2.5/site-packages/sage/modular/modsym/space.py\", line 156, in cuspidal_subspace\n        return self.cuspidal_submodule()\n      File \"/home/john/sage-3.1.alpha2/local/lib/python2.5/site-packages/sage/modular/modsym/ambient.py\", line 896, in cuspidal_submodule\n        assert d == S.dimension(), \"According to dimension formulas the cuspidal subspace of \\\"%s\\\" has dimension %s; however, computing it using modular symbols we obtained %s, so there is a bug (please report!).\"%(self, d, S.dimension())\n    AssertionError: According to dimension formulas the cuspidal subspace of \"Modular Symbols space of dimension 6 and level 20, weight 3, character [1, -zeta4], sign 1, over Cyclotomic Field of order 4 and degree 2\" has dimension 3; however, computing it using modular symbols we obtained 2, so there is a bug (please report!).\n**********************************************************************\n1 items had failures:\n   1 of  18 in __main__.example_0\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /home/john/sage-3.1.alpha2/tmp/.doctest_modsym.py\n\t [3.1 s]\n```\n\n\nand\n\n\n```\nsage -t  devel/sage-3814/sage/modular/modsym/boundary.py    **********************************************************************\nFile \"/home/john/sage-3.1.alpha2/tmp/boundary.py\", line 794:\n    sage: B._coerce_cusp(Cusp(0))\nExpected:\n    0\nGot:\n    [0]\n**********************************************************************\nFile \"/home/john/sage-3.1.alpha2/tmp/boundary.py\", line 813:\n    sage: [ B(Cusp(i,7)) for i in range(7) ]\nExpected:\n    [[0], 0, 0, 0, 0, 0, 0]\nGot:\n    [[0], [1/7], [2/7], [3/7], -[3/7], -[2/7], -[1/7]]\n**********************************************************************\nFile \"/home/john/sage-3.1.alpha2/tmp/boundary.py\", line 816:\n    sage: [ B(Cusp(i,7)) for i in range(7) ]\nExpected:\n    [0, [1/7], [2/7], [3/7], -[3/7], -[2/7], -[1/7]]\nGot:\n    [[0], [1/7], [2/7], [3/7], -[3/7], -[2/7], -[1/7]]\n**********************************************************************\nFile \"/home/john/sage-3.1.alpha2/tmp/boundary.py\", line 1003:\n    sage: [ B(Cusp(i,11)) for i in range(11) ]\nExpected:\n    [[0], 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]\nGot:\n    [[0], [1/11], -[1/11], [1/11], [1/11], [1/11], -[1/11], -[1/11], -[1/11], [1/11], -[1/11]]\n**********************************************************************\nFile \"/home/john/sage-3.1.alpha2/tmp/boundary.py\", line 1006:\n    sage: [ B(Cusp(i,11)) for i in range(11) ]\nExpected:\n    [0,\n    [1/11],\n    -[1/11],\n    [1/11],\n    [1/11],\n    [1/11],\n    -[1/11],\n    -[1/11],\n    -[1/11],\n    [1/11],\n    -[1/11]]\nGot:\n    [[0], [1/11], -[1/11], [1/11], [1/11], [1/11], -[1/11], -[1/11], -[1/11], [1/11], -[1/11]]\n**********************************************************************\nFile \"/home/john/sage-3.1.alpha2/tmp/boundary.py\", line 1206:\n    sage: [ B(Cusp(i,13)) for i in range(13) ]\nExpected:\n    [[0], 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]\nGot:\n    [[0], [1/13], (-zeta4)*[1/13], [1/13], (-1)*[1/13], (-zeta4)*[1/13], (-zeta4)*[1/13], zeta4*[1/13], zeta4*[1/13], [1/13], (-1)*[1/13], zeta4*[1/13], (-1)*[1/13]]\n**********************************************************************\nFile \"/home/john/sage-3.1.alpha2/tmp/boundary.py\", line 1208:\n    sage: B._coerce_cusp(Cusp(oo))\nExpected:\n    0\nGot:\n    [1/13]\n**********************************************************************\nFile \"/home/john/sage-3.1.alpha2/tmp/boundary.py\", line 1211:\n    sage: [ B(Cusp(i,13)) for i in range(13) ]\nExpected:\n    [0,\n    [1/13],\n    (-zeta4)*[1/13],\n    [1/13],\n    (-1)*[1/13],\n    (-zeta4)*[1/13],\n    (-zeta4)*[1/13],\n    zeta4*[1/13],\n    zeta4*[1/13],\n    [1/13],\n    (-1)*[1/13],\n    zeta4*[1/13],\n    (-1)*[1/13]]\nGot:\n    [[0], [1/13], (-zeta4)*[1/13], [1/13], (-1)*[1/13], (-zeta4)*[1/13], (-zeta4)*[1/13], zeta4*[1/13], zeta4*[1/13], [1/13], (-1)*[1/13], zeta4*[1/13], (-1)*[1/13]]\n**********************************************************************\n3 items had failures:\n   3 of  20 in __main__.example_32\n   2 of  15 in __main__.example_37\n   3 of  14 in __main__.example_42\n***Test Failed*** 8 failures.\nFor whitespace errors, see the file /home/john/sage-3.1.alpha2/tmp/.doctest_boundary.py\n```\n\n\nMy guess is that some of these are caused by other differences between 3.1.alpha2 and whatever version Craig was working with.",
    "created_at": "2008-08-14T16:17:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3814",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3814#issuecomment-27079",
    "user": "https://github.com/JohnCremona"
}
```

Attachment [trac-3814.patch](tarball://root/attachments/some-uuid/ticket3814/trac-3814.patch) by @JohnCremona created at 2008-08-14 16:17:21

Patch code looks good to me, it applies cleanly to a fresh 3.1.alpha2, and all doctests in sage/modular ....passed (in 392s) except for these two:

```
	sage -t  devel/sage-3814/sage/modular/modsym/modsym.py
	sage -t  devel/sage-3814/sage/modular/modsym/boundary.py
```


Details:

```
sage -t  devel/sage-3814/sage/modular/modsym/modsym.py      **********************************************************************
File "/home/john/sage-3.1.alpha2/tmp/modsym.py", line 51:
    sage: ModularSymbols(DirichletGroup(20).1**3, weight=3, sign=1).cuspidal_subspace()
Exception raised:
    Traceback (most recent call last):
      File "/home/john/sage-3.1.alpha2/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[17]>", line 1, in <module>
        ModularSymbols(DirichletGroup(Integer(20)).gen(1)**Integer(3), weight=Integer(3), sign=Integer(1)).cuspidal_subspace()###line 51:
    sage: ModularSymbols(DirichletGroup(20).1**3, weight=3, sign=1).cuspidal_subspace()
      File "/home/john/sage-3.1.alpha2/local/lib/python2.5/site-packages/sage/modular/modsym/space.py", line 156, in cuspidal_subspace
        return self.cuspidal_submodule()
      File "/home/john/sage-3.1.alpha2/local/lib/python2.5/site-packages/sage/modular/modsym/ambient.py", line 896, in cuspidal_submodule
        assert d == S.dimension(), "According to dimension formulas the cuspidal subspace of \"%s\" has dimension %s; however, computing it using modular symbols we obtained %s, so there is a bug (please report!)."%(self, d, S.dimension())
    AssertionError: According to dimension formulas the cuspidal subspace of "Modular Symbols space of dimension 6 and level 20, weight 3, character [1, -zeta4], sign 1, over Cyclotomic Field of order 4 and degree 2" has dimension 3; however, computing it using modular symbols we obtained 2, so there is a bug (please report!).
**********************************************************************
1 items had failures:
   1 of  18 in __main__.example_0
***Test Failed*** 1 failures.
For whitespace errors, see the file /home/john/sage-3.1.alpha2/tmp/.doctest_modsym.py
	 [3.1 s]
```


and


```
sage -t  devel/sage-3814/sage/modular/modsym/boundary.py    **********************************************************************
File "/home/john/sage-3.1.alpha2/tmp/boundary.py", line 794:
    sage: B._coerce_cusp(Cusp(0))
Expected:
    0
Got:
    [0]
**********************************************************************
File "/home/john/sage-3.1.alpha2/tmp/boundary.py", line 813:
    sage: [ B(Cusp(i,7)) for i in range(7) ]
Expected:
    [[0], 0, 0, 0, 0, 0, 0]
Got:
    [[0], [1/7], [2/7], [3/7], -[3/7], -[2/7], -[1/7]]
**********************************************************************
File "/home/john/sage-3.1.alpha2/tmp/boundary.py", line 816:
    sage: [ B(Cusp(i,7)) for i in range(7) ]
Expected:
    [0, [1/7], [2/7], [3/7], -[3/7], -[2/7], -[1/7]]
Got:
    [[0], [1/7], [2/7], [3/7], -[3/7], -[2/7], -[1/7]]
**********************************************************************
File "/home/john/sage-3.1.alpha2/tmp/boundary.py", line 1003:
    sage: [ B(Cusp(i,11)) for i in range(11) ]
Expected:
    [[0], 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
Got:
    [[0], [1/11], -[1/11], [1/11], [1/11], [1/11], -[1/11], -[1/11], -[1/11], [1/11], -[1/11]]
**********************************************************************
File "/home/john/sage-3.1.alpha2/tmp/boundary.py", line 1006:
    sage: [ B(Cusp(i,11)) for i in range(11) ]
Expected:
    [0,
    [1/11],
    -[1/11],
    [1/11],
    [1/11],
    [1/11],
    -[1/11],
    -[1/11],
    -[1/11],
    [1/11],
    -[1/11]]
Got:
    [[0], [1/11], -[1/11], [1/11], [1/11], [1/11], -[1/11], -[1/11], -[1/11], [1/11], -[1/11]]
**********************************************************************
File "/home/john/sage-3.1.alpha2/tmp/boundary.py", line 1206:
    sage: [ B(Cusp(i,13)) for i in range(13) ]
Expected:
    [[0], 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
Got:
    [[0], [1/13], (-zeta4)*[1/13], [1/13], (-1)*[1/13], (-zeta4)*[1/13], (-zeta4)*[1/13], zeta4*[1/13], zeta4*[1/13], [1/13], (-1)*[1/13], zeta4*[1/13], (-1)*[1/13]]
**********************************************************************
File "/home/john/sage-3.1.alpha2/tmp/boundary.py", line 1208:
    sage: B._coerce_cusp(Cusp(oo))
Expected:
    0
Got:
    [1/13]
**********************************************************************
File "/home/john/sage-3.1.alpha2/tmp/boundary.py", line 1211:
    sage: [ B(Cusp(i,13)) for i in range(13) ]
Expected:
    [0,
    [1/13],
    (-zeta4)*[1/13],
    [1/13],
    (-1)*[1/13],
    (-zeta4)*[1/13],
    (-zeta4)*[1/13],
    zeta4*[1/13],
    zeta4*[1/13],
    [1/13],
    (-1)*[1/13],
    zeta4*[1/13],
    (-1)*[1/13]]
Got:
    [[0], [1/13], (-zeta4)*[1/13], [1/13], (-1)*[1/13], (-zeta4)*[1/13], (-zeta4)*[1/13], zeta4*[1/13], zeta4*[1/13], [1/13], (-1)*[1/13], zeta4*[1/13], (-1)*[1/13]]
**********************************************************************
3 items had failures:
   3 of  20 in __main__.example_32
   2 of  15 in __main__.example_37
   3 of  14 in __main__.example_42
***Test Failed*** 8 failures.
For whitespace errors, see the file /home/john/sage-3.1.alpha2/tmp/.doctest_boundary.py
```


My guess is that some of these are caused by other differences between 3.1.alpha2 and whatever version Craig was working with.



---

archive/issue_comments_027080.json:
```json
{
    "body": "My mistake, apologies to Craig:  I forgot to do \"sage -b\" after applying the patches and testing.  Those two files do pass.\n\nThe patch is good!",
    "created_at": "2008-08-14T17:21:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3814",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3814#issuecomment-27080",
    "user": "https://github.com/JohnCremona"
}
```

My mistake, apologies to Craig:  I forgot to do "sage -b" after applying the patches and testing.  Those two files do pass.

The patch is good!



---

archive/issue_comments_027081.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-15T01:33:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3814",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3814#issuecomment-27081",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_027082.json:
```json
{
    "body": "Merged in Sage 3.1.rc0",
    "created_at": "2008-08-15T01:33:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3814",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3814#issuecomment-27082",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.1.rc0



---

archive/issue_events_004038.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-08-15T01:33:59Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3814",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3814#event-4038"
}
```
