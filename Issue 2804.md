# Issue 2804: ssmod.py failure

archive/issues_002804.json:
```json
{
    "body": "Assignee: @williamstein\n\n\n```\nsage -t  devel/sage/sage/modular/ssmod/ssmod.py             **********************************************************************\nFile \"/home/x/build/sage-3.0.alpha1/tmp/ssmod.py\", line 14:\n    sage: D[:3]\nExpected:\n    [\n    (Vector space of degree 33 and dimension 1 over Finite Field of size 97\n    Basis matrix:\n    [ 0  0  0  1 96 96  1 96 96  0  2 96 96  0  1  0  1  2 95  0  1  1  0  1  0 95  0 96 95  1 96  0  2], True),\n    (Vector space of degree 33 and dimension 1 over Finite Field of size 97\n    Basis matrix:\n    [ 0  1 96 75 16 81 22 17 17  0  0 80 80  1 16 40 74  0  0 96 81 23 57 74  0  0  0 24  0 23 73  0  0], True),\n    (Vector space of degree 33 and dimension 1 over Finite Field of size 97\n    Basis matrix:\n    [ 0  1 96 90 90  7  7  6 91  0  0 91  6 13  7  0 91  0  0 84 90  6  0  6  0  0  0 90  0 91  7  0  0], True)\n    ]\nGot:\n    [\n    (Vector space of degree 33 and dimension 0 over Finite Field of size 97\n    Basis matrix:\n    [], True),\n    (Sparse vector space of degree 33 and dimension 6 over Finite Field of size 97\n    Basis matrix:\n    [ 1  0  0  0  0  0 42 22 77 61  8 76 27 95 75 81 24 22 61 78  3 95 44 26 63 31 47 61 67 24 26 49 91]\n    [ 0  1  0  0  0  0 63 79 96 61 54 21 37 39 70 51  3 68 91 54 33 20 61 96 72 23 62 45 87 24 66 31 88]\n    [ 0  0  1  0  0  0  0 19 95 33 67 91 19  0 29 78 70 37 48 72 37 62 45 72 40 57 46 95 29 50 30  6 17]\n    [ 0  0  0  1  0  0 20 57 50 17 95 67  2 88 67 57  1 41 84 44 90 96 31 34  3 46 13 52 96 94 62 77 94]\n    [ 0  0  0  0  1  0 50  6 38 38 50 31 23 32 68 45 26  9 66  6 51 31 50 53 17 29 89 53 70 24 44 27 30]\n    [ 0  0  0  0  0  1 20  8 77 51 41 25  7 63 75  2 86 20 23  0 29 77 13 26 45 10 38 41 66 68 40 49 15], True),\n    (Sparse vector space of degree 33 and dimension 8 over Finite Field of size 97\n    Basis matrix:\n    [ 1  0  0  0  0  0  0  0 23 48 44 88  8 82 60 13 35 15 74 59 18 78 42 16 12 91 13  8 19 28 41 48 31]\n    [ 0  1  0  0  0  0  0  0 83 78 55 39 17 91 90 29 85 89  3 53 15 47  8 25 79 40 82 79 24 33 45 29 70]\n    [ 0  0  1  0  0  0  0  0 69 74 21 95 41  9 80 89  6 33 17 23 94 73 65 65 61 91 77 48 32 42  4 23 46]\n    [ 0  0  0  1  0  0  0  0 43 36  6 41  4 80 73 63 38 94 33 94 71 62 93 41 83 90 21 58 57 94 79  4 88]\n    [ 0  0  0  0  1  0  0  0 87 26 91 28 67 79 78 79 62 75 25 73 24 92  5 69 17  5 67 41 65  5  0 87 57]\n    [ 0  0  0  0  0  1  0  0 37  8 88  0 56 62 67 80 82  5 62 38 64  5 14 52 64 77 77 51 79 57 34 67  6]\n    [ 0  0  0  0  0  0  1  0 46  1 43 61 76 30 91 96 77 15 43 37 90 84 70 68 24 84 34 85 46 13 10 65  9]\n    [ 0  0  0  0  0  0  0  1 78 41 40 60 52 57 13 88 90 96 29 78 95 77 16 69 72 13 85  8  3 40 19 20 53], True)\n    ]\n**********************************************************************\nFile \"/home/x/build/sage-3.0.alpha1/tmp/ssmod.py\", line 26:\n    sage: len(D)\nExpected:\n    9\nGot:\n    4\n```\n\nThis is a heisenbug.  It works some of the time.  It also sometimes spits out \n\"itere dependant intercale\" at random.\nTest machine is a 64 bit gentoo install with 4.2.3 gcc\n\nIssue created by migration from https://trac.sagemath.org/ticket/2804\n\n",
    "created_at": "2008-04-05T02:57:39Z",
    "labels": [
        "component: modular forms",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "ssmod.py failure",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2804",
    "user": "https://github.com/garyfurnish"
}
```
Assignee: @williamstein


```
sage -t  devel/sage/sage/modular/ssmod/ssmod.py             **********************************************************************
File "/home/x/build/sage-3.0.alpha1/tmp/ssmod.py", line 14:
    sage: D[:3]
Expected:
    [
    (Vector space of degree 33 and dimension 1 over Finite Field of size 97
    Basis matrix:
    [ 0  0  0  1 96 96  1 96 96  0  2 96 96  0  1  0  1  2 95  0  1  1  0  1  0 95  0 96 95  1 96  0  2], True),
    (Vector space of degree 33 and dimension 1 over Finite Field of size 97
    Basis matrix:
    [ 0  1 96 75 16 81 22 17 17  0  0 80 80  1 16 40 74  0  0 96 81 23 57 74  0  0  0 24  0 23 73  0  0], True),
    (Vector space of degree 33 and dimension 1 over Finite Field of size 97
    Basis matrix:
    [ 0  1 96 90 90  7  7  6 91  0  0 91  6 13  7  0 91  0  0 84 90  6  0  6  0  0  0 90  0 91  7  0  0], True)
    ]
Got:
    [
    (Vector space of degree 33 and dimension 0 over Finite Field of size 97
    Basis matrix:
    [], True),
    (Sparse vector space of degree 33 and dimension 6 over Finite Field of size 97
    Basis matrix:
    [ 1  0  0  0  0  0 42 22 77 61  8 76 27 95 75 81 24 22 61 78  3 95 44 26 63 31 47 61 67 24 26 49 91]
    [ 0  1  0  0  0  0 63 79 96 61 54 21 37 39 70 51  3 68 91 54 33 20 61 96 72 23 62 45 87 24 66 31 88]
    [ 0  0  1  0  0  0  0 19 95 33 67 91 19  0 29 78 70 37 48 72 37 62 45 72 40 57 46 95 29 50 30  6 17]
    [ 0  0  0  1  0  0 20 57 50 17 95 67  2 88 67 57  1 41 84 44 90 96 31 34  3 46 13 52 96 94 62 77 94]
    [ 0  0  0  0  1  0 50  6 38 38 50 31 23 32 68 45 26  9 66  6 51 31 50 53 17 29 89 53 70 24 44 27 30]
    [ 0  0  0  0  0  1 20  8 77 51 41 25  7 63 75  2 86 20 23  0 29 77 13 26 45 10 38 41 66 68 40 49 15], True),
    (Sparse vector space of degree 33 and dimension 8 over Finite Field of size 97
    Basis matrix:
    [ 1  0  0  0  0  0  0  0 23 48 44 88  8 82 60 13 35 15 74 59 18 78 42 16 12 91 13  8 19 28 41 48 31]
    [ 0  1  0  0  0  0  0  0 83 78 55 39 17 91 90 29 85 89  3 53 15 47  8 25 79 40 82 79 24 33 45 29 70]
    [ 0  0  1  0  0  0  0  0 69 74 21 95 41  9 80 89  6 33 17 23 94 73 65 65 61 91 77 48 32 42  4 23 46]
    [ 0  0  0  1  0  0  0  0 43 36  6 41  4 80 73 63 38 94 33 94 71 62 93 41 83 90 21 58 57 94 79  4 88]
    [ 0  0  0  0  1  0  0  0 87 26 91 28 67 79 78 79 62 75 25 73 24 92  5 69 17  5 67 41 65  5  0 87 57]
    [ 0  0  0  0  0  1  0  0 37  8 88  0 56 62 67 80 82  5 62 38 64  5 14 52 64 77 77 51 79 57 34 67  6]
    [ 0  0  0  0  0  0  1  0 46  1 43 61 76 30 91 96 77 15 43 37 90 84 70 68 24 84 34 85 46 13 10 65  9]
    [ 0  0  0  0  0  0  0  1 78 41 40 60 52 57 13 88 90 96 29 78 95 77 16 69 72 13 85  8  3 40 19 20 53], True)
    ]
**********************************************************************
File "/home/x/build/sage-3.0.alpha1/tmp/ssmod.py", line 26:
    sage: len(D)
Expected:
    9
Got:
    4
```

This is a heisenbug.  It works some of the time.  It also sometimes spits out 
"itere dependant intercale" at random.
Test machine is a 64 bit gentoo install with 4.2.3 gcc

Issue created by migration from https://trac.sagemath.org/ticket/2804





---

archive/issue_comments_019208.json:
```json
{
    "body": "Changing component from modular forms to doctest.",
    "created_at": "2008-04-05T02:59:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2804",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2804#issuecomment-19208",
    "user": "https://github.com/garyfurnish"
}
```

Changing component from modular forms to doctest.



---

archive/issue_comments_019209.json:
```json
{
    "body": "Changing assignee from @williamstein to failure.",
    "created_at": "2008-04-05T02:59:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2804",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2804#issuecomment-19209",
    "user": "https://github.com/garyfurnish"
}
```

Changing assignee from @williamstein to failure.



---

archive/issue_comments_019210.json:
```json
{
    "body": "Attachment [2804.patch](tarball://root/attachments/some-uuid/ticket2804/2804.patch) by @ClementPernet created at 2008-04-05 03:20:08\n\ntrivial patch to revert to LUK charpoly method",
    "created_at": "2008-04-05T03:20:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2804",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2804#issuecomment-19210",
    "user": "https://github.com/ClementPernet"
}
```

Attachment [2804.patch](tarball://root/attachments/some-uuid/ticket2804/2804.patch) by @ClementPernet created at 2008-04-05 03:20:08

trivial patch to revert to LUK charpoly method



---

archive/issue_comments_019211.json:
```json
{
    "body": "Changing assignee from failure to @ClementPernet.",
    "created_at": "2008-04-05T03:24:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2804",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2804#issuecomment-19211",
    "user": "https://github.com/ClementPernet"
}
```

Changing assignee from failure to @ClementPernet.



---

archive/issue_comments_019212.json:
```json
{
    "body": "I reverted the default LinBox method to LUK which is a slower on large matrices but much safer. This fix is temporary waiting, for me to investigate the real bug in the ArithProg method.\nI put an updated spkg at \n[http://sage.math.washington.edu/home/tabbott/linbox-1.1.5p1.spkg](http://sage.math.washington.edu/home/tabbott/linbox-1.1.5p1.spkg)",
    "created_at": "2008-04-05T03:24:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2804",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2804#issuecomment-19212",
    "user": "https://github.com/ClementPernet"
}
```

I reverted the default LinBox method to LUK which is a slower on large matrices but much safer. This fix is temporary waiting, for me to investigate the real bug in the ArithProg method.
I put an updated spkg at 
[http://sage.math.washington.edu/home/tabbott/linbox-1.1.5p1.spkg](http://sage.math.washington.edu/home/tabbott/linbox-1.1.5p1.spkg)



---

archive/issue_comments_019213.json:
```json
{
    "body": "Sorry I messed up the address:\n[http://sage.math.washington.edu/home/pernet/linbox-1.1.5p1.spkg](http://sage.math.washington.edu/home/pernet/linbox-1.1.5p1.spkg)",
    "created_at": "2008-04-05T03:25:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2804",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2804#issuecomment-19213",
    "user": "https://github.com/ClementPernet"
}
```

Sorry I messed up the address:
[http://sage.math.washington.edu/home/pernet/linbox-1.1.5p1.spkg](http://sage.math.washington.edu/home/pernet/linbox-1.1.5p1.spkg)



---

archive/issue_comments_019214.json:
```json
{
    "body": "Changing the method to LUK does indeed fix the failure, although  it is important to note that 2804.patch is messed up and doesn't do this at all.",
    "created_at": "2008-04-05T04:13:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2804",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2804#issuecomment-19214",
    "user": "https://github.com/garyfurnish"
}
```

Changing the method to LUK does indeed fix the failure, although  it is important to note that 2804.patch is messed up and doesn't do this at all.



---

archive/issue_comments_019215.json:
```json
{
    "body": "Replying to [comment:4 gfurnish]:\n> Changing the method to LUK does indeed fix the failure, although  it is important to note that 2804.patch is messed up and doesn't do this at all.\n\nI will check out the updated LinBox.spkg and make sure it has the right fix in it. Otherwise I will apply the patch manually.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-05T04:18:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2804",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2804#issuecomment-19215",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Replying to [comment:4 gfurnish]:
> Changing the method to LUK does indeed fix the failure, although  it is important to note that 2804.patch is messed up and doesn't do this at all.

I will check out the updated LinBox.spkg and make sure it has the right fix in it. Otherwise I will apply the patch manually.

Cheers,

Michael



---

archive/issue_comments_019216.json:
```json
{
    "body": "Positive review to the change to LUK",
    "created_at": "2008-04-06T02:23:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2804",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2804#issuecomment-19216",
    "user": "https://github.com/garyfurnish"
}
```

Positive review to the change to LUK



---

archive/issue_comments_019217.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-06T04:07:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2804",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2804#issuecomment-19217",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_019218.json:
```json
{
    "body": "Merged in Sage 3.0.alpha2",
    "created_at": "2008-04-06T04:07:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2804",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2804#issuecomment-19218",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.alpha2
