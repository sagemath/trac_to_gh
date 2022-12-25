# Issue 2128: bug in random_prime (trivial to fix!)

archive/issues_002128.json:
```json
{
    "body": "Assignee: @williamstein\n\n\n```\nThe function\n\n random_prime(n)\n\nreturns differing types of objects. When n is 2, it returns a Sage\ninteger. When n is > 2, it returns a Python integer. A look at the\nsource code gives the impression that it should return a Sage\ninteger.\n\nPerhaps devel/sage-main/sage/rings/arith.py line 907 should be\nchanged from\n   return p\nto\n   return integer_ring.ZZ(p)\n\n -- Kate Minola\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2128\n\n",
    "created_at": "2008-02-09T19:26:29Z",
    "labels": [
        "component: number theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.2",
    "title": "bug in random_prime (trivial to fix!)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2128",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein


```
The function

 random_prime(n)

returns differing types of objects. When n is 2, it returns a Sage
integer. When n is > 2, it returns a Python integer. A look at the
source code gives the impression that it should return a Sage
integer.

Perhaps devel/sage-main/sage/rings/arith.py line 907 should be
changed from
   return p
to
   return integer_ring.ZZ(p)

 -- Kate Minola
```


Issue created by migration from https://trac.sagemath.org/ticket/2128





---

archive/issue_comments_013931.json:
```json
{
    "body": "Implemented the change in the patch.",
    "created_at": "2008-02-17T01:51:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2128#issuecomment-13931",
    "user": "https://github.com/aghitza"
}
```

Implemented the change in the patch.



---

archive/issue_comments_013932.json:
```json
{
    "body": "The patch looks good, but I would suggest a doctest that checks the type of the return value for n=2 and some n>2.\n\nCheers,\n\nMichael",
    "created_at": "2008-02-17T17:26:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2128#issuecomment-13932",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The patch looks good, but I would suggest a doctest that checks the type of the return value for n=2 and some n>2.

Cheers,

Michael



---

archive/issue_comments_013933.json:
```json
{
    "body": "Attachment [2128-random_prime.patch](tarball://root/attachments/some-uuid/ticket2128/2128-random_prime.patch) by @aghitza created at 2008-02-17 18:49:30\n\nI've added the doctests and replaced the patch.",
    "created_at": "2008-02-17T18:49:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2128#issuecomment-13933",
    "user": "https://github.com/aghitza"
}
```

Attachment [2128-random_prime.patch](tarball://root/attachments/some-uuid/ticket2128/2128-random_prime.patch) by @aghitza created at 2008-02-17 18:49:30

I've added the doctests and replaced the patch.



---

archive/issue_comments_013934.json:
```json
{
    "body": "Updated patch looks good.\n\nCheers,\n\nMichael",
    "created_at": "2008-02-17T23:36:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2128#issuecomment-13934",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Updated patch looks good.

Cheers,

Michael



---

archive/issue_events_005097.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-02-17T23:36:25Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2128",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2128#event-5097"
}
```



---

archive/issue_comments_013935.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-17T23:36:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2128#issuecomment-13935",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_013936.json:
```json
{
    "body": "Merged in Sage 2.10.2.alpha1",
    "created_at": "2008-02-17T23:36:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2128#issuecomment-13936",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.2.alpha1
