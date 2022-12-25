# Issue 1834: General linear group over ZZ hangs in __call__

archive/issues_001834.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  alexghitza\n\nsage: G = GL(3,GF(101))\nsage: G([[1,0,1],[0,1,0],[0,0,1]])\n\n[1 0 1]\n[0 1 0]\n[0 0 1]\n\nworks fine, but\n\nsage: G = GL(3,ZZ)\nsage: G([[1,0,1],[0,1,0],[0,0,1]])\n\nThis should not try to find a solution to the word problem.\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1834\n\n",
    "created_at": "2008-01-18T16:42:33Z",
    "labels": [
        "component: algebraic geometry",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.2",
    "title": "General linear group over ZZ hangs in __call__",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1834",
    "user": "https://trac.sagemath.org/admin/accounts/users/kohel"
}
```
Assignee: @williamstein

CC:  alexghitza

sage: G = GL(3,GF(101))
sage: G([[1,0,1],[0,1,0],[0,0,1]])

[1 0 1]
[0 1 0]
[0 0 1]

works fine, but

sage: G = GL(3,ZZ)
sage: G([[1,0,1],[0,1,0],[0,0,1]])

This should not try to find a solution to the word problem.



Issue created by migration from https://trac.sagemath.org/ticket/1834





---

archive/issue_events_004452.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-01-23T09:29:01Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1834",
    "milestone": "sage-2.10.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1834#event-4452"
}
```



---

archive/issue_comments_011578.json:
```json
{
    "body": "This has been around for a while, and it's been bugging me.  I fixed it by writing methods !__call!__ and !__contains!__ for the class GeneralLinearGroup_generic, so that the GAP ones (which hang over ZZ) don't get used.  A pleasant side effect is that things are now faster for the cases that were working before (i.e. over finite fields):\n\nbefore:\n\n```\nsage: G = GL(5, GF(next_prime(6*10^4)))                                    \nsage: m = [[1,0,1,0,2],[0,1,0,1,1],[0,0,1,0,0],[0,0,0,1,1],[0,0,0,0,1]]                              \nsage: timeit(\"G(m)\")                                                                                     \n25 loops, best of 3: 9.56 ms per loop\n```\n\n\nafter:\n\n```\nsage: G = GL(5, GF(next_prime(6*10^4)))                                    \nsage: m = [[1,0,1,0,2], [0,1,0,1,1], [0,0,1,0,0], [0,0,0,1,1], [0,0,0,0,1]]                              \nsage: timeit(\"G(m)\")                                                                                     \n625 loops, best of 3: 459 \u00b5s per loop\n```\n\n\nThe same issue comes up for all the matrix groups.  For the moment, I have only dealt with the really easy cases of GL and SL.  If this gets approved and merged, I will open a new ticket for the other classes of groups and deal with them in a similar way.",
    "created_at": "2008-08-29T13:37:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1834",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1834#issuecomment-11578",
    "user": "https://github.com/aghitza"
}
```

This has been around for a while, and it's been bugging me.  I fixed it by writing methods !__call!__ and !__contains!__ for the class GeneralLinearGroup_generic, so that the GAP ones (which hang over ZZ) don't get used.  A pleasant side effect is that things are now faster for the cases that were working before (i.e. over finite fields):

before:

```
sage: G = GL(5, GF(next_prime(6*10^4)))                                    
sage: m = [[1,0,1,0,2],[0,1,0,1,1],[0,0,1,0,0],[0,0,0,1,1],[0,0,0,0,1]]                              
sage: timeit("G(m)")                                                                                     
25 loops, best of 3: 9.56 ms per loop
```


after:

```
sage: G = GL(5, GF(next_prime(6*10^4)))                                    
sage: m = [[1,0,1,0,2], [0,1,0,1,1], [0,0,1,0,0], [0,0,0,1,1], [0,0,0,0,1]]                              
sage: timeit("G(m)")                                                                                     
625 loops, best of 3: 459 µs per loop
```


The same issue comes up for all the matrix groups.  For the moment, I have only dealt with the really easy cases of GL and SL.  If this gets approved and merged, I will open a new ticket for the other classes of groups and deal with them in a similar way.



---

archive/issue_comments_011579.json:
```json
{
    "body": "Changing assignee from @williamstein to @aghitza.",
    "created_at": "2008-09-01T09:15:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1834",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1834#issuecomment-11579",
    "user": "https://github.com/aghitza"
}
```

Changing assignee from @williamstein to @aghitza.



---

archive/issue_comments_011580.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-09-01T10:03:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1834",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1834#issuecomment-11580",
    "user": "https://github.com/aghitza"
}
```

Changing status from new to assigned.



---

archive/issue_comments_011581.json:
```json
{
    "body": "Changing component from algebraic geometry to linear algebra.",
    "created_at": "2008-09-01T19:38:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1834",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1834#issuecomment-11581",
    "user": "https://github.com/JohnCremona"
}
```

Changing component from algebraic geometry to linear algebra.



---

archive/issue_comments_011582.json:
```json
{
    "body": "Basically ok, but I would make the following changes to both cases (GL and SL):\n\nUse a try: except: block to catch when coercion in the matrix space fails, with the error message \"Cannot coerce ... to a matrix\".  Then catch the non-invertible matrices in the GL case with the error message \"... is not an invertible matrix\", and similarly in the SL case with \"... does not have determinant 1\".\n\nI think this alternative error handling will produce better output.\n\nPS As this is not \"algebraic geometry\" I changed the Component to Linear Algebra",
    "created_at": "2008-09-01T19:38:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1834",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1834#issuecomment-11582",
    "user": "https://github.com/JohnCremona"
}
```

Basically ok, but I would make the following changes to both cases (GL and SL):

Use a try: except: block to catch when coercion in the matrix space fails, with the error message "Cannot coerce ... to a matrix".  Then catch the non-invertible matrices in the GL case with the error message "... is not an invertible matrix", and similarly in the SL case with "... does not have determinant 1".

I think this alternative error handling will produce better output.

PS As this is not "algebraic geometry" I changed the Component to Linear Algebra



---

archive/issue_comments_011583.json:
```json
{
    "body": "Attachment [1834-gl_z_call.patch](tarball://root/attachments/some-uuid/ticket1834/1834-gl_z_call.patch) by @aghitza created at 2008-09-01 23:09:28\n\nGood idea.  I have made the changes and replaced the patch with a new one.",
    "created_at": "2008-09-01T23:09:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1834",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1834#issuecomment-11583",
    "user": "https://github.com/aghitza"
}
```

Attachment [1834-gl_z_call.patch](tarball://root/attachments/some-uuid/ticket1834/1834-gl_z_call.patch) by @aghitza created at 2008-09-01 23:09:28

Good idea.  I have made the changes and replaced the patch with a new one.



---

archive/issue_comments_011584.json:
```json
{
    "body": "Excellent.  These are much more helpful messages.\n\nThe new patch applies ok to 3.1.2.alpha3 (there was a little fuzz:\n\n```\napplying /home/john/1834-gl_z_call.patch\npatching file sage/groups/matrix_gps/matrix_group.py\nHunk #1 succeeded at 13 with fuzz 1 (offset 3 lines).\n```\n\nbut nothing serious).   All doctests in sage.groups.matrix_groups pass.  Publish!",
    "created_at": "2008-09-02T08:37:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1834",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1834#issuecomment-11584",
    "user": "https://github.com/JohnCremona"
}
```

Excellent.  These are much more helpful messages.

The new patch applies ok to 3.1.2.alpha3 (there was a little fuzz:

```
applying /home/john/1834-gl_z_call.patch
patching file sage/groups/matrix_gps/matrix_group.py
Hunk #1 succeeded at 13 with fuzz 1 (offset 3 lines).
```

but nothing serious).   All doctests in sage.groups.matrix_groups pass.  Publish!



---

archive/issue_comments_011585.json:
```json
{
    "body": "Merged in Sage 3.1.2.alpha4",
    "created_at": "2008-09-02T11:02:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1834",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1834#issuecomment-11585",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.1.2.alpha4



---

archive/issue_comments_011586.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-02T11:02:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1834",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1834#issuecomment-11586",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_004453.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-09-02T11:02:34Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1834",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1834#event-4453"
}
```
