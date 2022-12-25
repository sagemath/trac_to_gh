# Issue 2136: matrix visualize_structure is completely broken on osx (at least 10.5) -- why no doctest to catch this!?

archive/issues_002136.json:
```json
{
    "body": "Assignee: @williamstein\n\nThis ticket is a migration of #1137. There was a patch associated with the ticket, that was merged in to the library, but it was not related to the original issue. Below is a reproduction of the original description.\n\n\n```\nsage: sr = mq.SR(2,1,1,4,gf2=True)\nsage: sr\nSR(2,1,1,4)\nsage: F,s = sr.polynomial_system()\nsage: F\nPolynomial System with 104 Polynomials in 36 Variables\nsage: gb = F.groebner_basis()\nsage: Ideal(gb).variety()\n[{x101: 0, x100: 0, x103: 1, x102: 0, k103: 1, x202: 0, x203: 1, x200: 1, x201: 1, w100: 0, w101: 0, w102: 0, w103: 1, k102: 1, k203: 0, k202: 1, k201: 0, k200: 1, s001: 0, s000: 1, s003: 1, s002: 1, k001: 1, k000: 0, k003: 1, k002: 0, w203: 0, w202: 0, w201: 1, w200: 0, s100: 1, s101: 0, s102: 0, s103: 0, k100: 1, k101: 1}]\nsage: s\n{k001: 1, k000: 0, k003: 1, k002: 0}\nsage: A,v = F.coefficient_matrix()\nsage: A.visualize_structure()\nTraceback (most recent call last):\n...\nImportError: dlopen(/Users/was/s/local/lib/python2.5/site-packages/_gd.so, 2): Library not loaded: /Users/was/Desktop/sage-2.8.10.rc1/local/lib/libpng.3.dylib\n  Referenced from: /Users/was/s/local/lib/python2.5/site-packages/_gd.so\n  Reason: image not found\n```\n\n\nTodo:\n\n1. Make a doctest that would catch this\n2. Fix the problem. \n\nRobert WB's comments:\nI can't get this to work at all on OS X 10.4 (intel)\n\n\n```\nsage: sage: M.visualize_structure()\n------------------------------------------------------------\nTraceback (most recent call last):\n  File \"<ipython console>\", line 1, in <module>\n  File \"matrix2.pyx\", line 2853, in sage.matrix.matrix2.Matrix.visualize_structure\n  File \"/Users/robert/sage/current/local/lib/python2.5/site-packages/gd.py\", line 10, in <module>\n    import _gd\n<type 'exceptions.ImportError'>: dlopen(/Users/robert/sage/current/local/lib/python2.5/site-packages/_gd.so, 2): Symbol not found: _png_get_rowbytes\n  Referenced from: /Users/robert/sage/current/local/lib//libgd.2.dylib\n  Expected in: flat namespace\n```\n\n\nMabshoff's comment:\n\nFixing the issue by updating libpng breaks other spkgs like R, so revert it until we can figure out how to solve it properly.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2136\n\n",
    "created_at": "2008-02-10T03:06:18Z",
    "labels": [
        "component: linear algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "matrix visualize_structure is completely broken on osx (at least 10.5) -- why no doctest to catch this!?",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2136",
    "user": "https://github.com/rlmill"
}
```
Assignee: @williamstein

This ticket is a migration of #1137. There was a patch associated with the ticket, that was merged in to the library, but it was not related to the original issue. Below is a reproduction of the original description.


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

Robert WB's comments:
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


Mabshoff's comment:

Fixing the issue by updating libpng breaks other spkgs like R, so revert it until we can figure out how to solve it properly.

Issue created by migration from https://trac.sagemath.org/ticket/2136





---

archive/issue_comments_013977.json:
```json
{
    "body": "This is the same issue as #3324.",
    "created_at": "2008-08-18T19:39:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2136",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2136#issuecomment-13977",
    "user": "https://github.com/malb"
}
```

This is the same issue as #3324.



---

archive/issue_comments_013978.json:
```json
{
    "body": "Changing component from linear algebra to doctest.",
    "created_at": "2008-12-05T04:49:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2136",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2136#issuecomment-13978",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing component from linear algebra to doctest.



---

archive/issue_comments_013979.json:
```json
{
    "body": "Changing assignee from @williamstein to mabshoff.",
    "created_at": "2008-12-05T04:49:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2136",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2136#issuecomment-13979",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing assignee from @williamstein to mabshoff.



---

archive/issue_comments_013980.json:
```json
{
    "body": "This has worked for a while:\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: sr = mq.SR(2,1,1,4,gf2=True)\nsage: F,s = sr.polynomial_system()\nsage: \nsage: gb = F.groebner_basis()\nsage: Ideal(gb).variety()\n| Sage Version 3.2.1.alpha2, Release Date: 2008-11-26                |\n| Type notebook() for the GUI, and license() for information.        |\nsage: sage: Ideal(gb).variety()\n[{s001: 0, s103: 1, s101: 1, x103: 1, s000: 1, x101: 0, k003: 0, k100: 0, k001: 0, k200: 0, x200: 0, k202: 0, x202: 0, w102: 1, w100: 0, w201: 0, s002: 0, w203: 1, k101: 1, s102: 0, s100: 1, x102: 0, x100: 1, k002: 1, k000: 0, x201: 0, k201: 0, x203: 1, k203: 0, k103: 0, w103: 0, k102: 0, w101: 0, w200: 0, s003: 1, w202: 0}]\nsage: \nsage: A,v = F.coefficient_matrix()\nsage: A.visualize_structure()\nsage: \nExiting SAGE (CPU time 0m0.99s, Wall time 0m56.28s).\nExiting spawned Singular process.\n```\n\nSo let's add a doctest and get this ticket closed unless there already is such a doctest. (which I believe there is).\n\nmalb?\n\nCheers,\n\nMichael",
    "created_at": "2008-12-05T04:49:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2136",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2136#issuecomment-13980",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This has worked for a while:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: sr = mq.SR(2,1,1,4,gf2=True)
sage: F,s = sr.polynomial_system()
sage: 
sage: gb = F.groebner_basis()
sage: Ideal(gb).variety()
| Sage Version 3.2.1.alpha2, Release Date: 2008-11-26                |
| Type notebook() for the GUI, and license() for information.        |
sage: sage: Ideal(gb).variety()
[{s001: 0, s103: 1, s101: 1, x103: 1, s000: 1, x101: 0, k003: 0, k100: 0, k001: 0, k200: 0, x200: 0, k202: 0, x202: 0, w102: 1, w100: 0, w201: 0, s002: 0, w203: 1, k101: 1, s102: 0, s100: 1, x102: 0, x100: 1, k002: 1, k000: 0, x201: 0, k201: 0, x203: 1, k203: 0, k103: 0, w103: 0, k102: 0, w101: 0, w200: 0, s003: 1, w202: 0}]
sage: 
sage: A,v = F.coefficient_matrix()
sage: A.visualize_structure()
sage: 
Exiting SAGE (CPU time 0m0.99s, Wall time 0m56.28s).
Exiting spawned Singular process.
```

So let's add a doctest and get this ticket closed unless there already is such a doctest. (which I believe there is).

malb?

Cheers,

Michael



---

archive/issue_comments_013981.json:
```json
{
    "body": "The bug is fixed and #3321 re-enables doctests for this function. I vote for closing this ticket.",
    "created_at": "2009-01-22T07:47:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2136",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2136#issuecomment-13981",
    "user": "https://github.com/malb"
}
```

The bug is fixed and #3321 re-enables doctests for this function. I vote for closing this ticket.



---

archive/issue_comments_013982.json:
```json
{
    "body": "Replying to [comment:4 malb]:\n> The bug is fixed and #3321 re-enables doctests for this function. I vote for closing this ticket.\n\nI concur. Fixed via #3321.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-22T10:49:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2136",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2136#issuecomment-13982",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Replying to [comment:4 malb]:
> The bug is fixed and #3321 re-enables doctests for this function. I vote for closing this ticket.

I concur. Fixed via #3321.

Cheers,

Michael



---

archive/issue_events_002298.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2009-01-22T10:49:00Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2136",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2136#event-2298"
}
```



---

archive/issue_comments_013983.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-22T10:49:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2136",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2136#issuecomment-13983",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
