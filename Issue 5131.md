# Issue 5131: regression in free modules -- who broke my __mul__

archive/issues_005131.json:
```json
{
    "body": "Assignee: @williamstein\n\nIf A is a free module and r a ring element then r*A and A*r used to work fine. But somebody broke them.\n\nIn the good ol days:\n\n```\nwstein@sage:/disk/scratch/mabshoff-sage-releases/sage-0.10.0$ ./sage\n[...]\nsage: A = ZZ^3\nsage: A\n _5 = Ambient free module of rank 3 over the principal ideal domain Integer Ring\nsage: 2*A\n _6 = \nFree module of degree 3 and rank 3 over Integer Ring\nEchelon basis matrix:\n[2 0 0]\n[0 2 0]\n[0 0 2]\n```\n\n\nNow:\n\n```\nsage: A = ZZ^3\nsage: 2*A\nTraceback (most recent call last):\n...\nTypeError: unsupported operand parent(s) for '*': 'Integer Ring' and '<class 'sage.modules.free_module.FreeModule_ambient_pid'>'\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5131\n\n",
    "created_at": "2009-01-29T23:05:17Z",
    "labels": [
        "component: linear algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.3",
    "title": "regression in free modules -- who broke my __mul__",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5131",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

If A is a free module and r a ring element then r*A and A*r used to work fine. But somebody broke them.

In the good ol days:

```
wstein@sage:/disk/scratch/mabshoff-sage-releases/sage-0.10.0$ ./sage
[...]
sage: A = ZZ^3
sage: A
 _5 = Ambient free module of rank 3 over the principal ideal domain Integer Ring
sage: 2*A
 _6 = 
Free module of degree 3 and rank 3 over Integer Ring
Echelon basis matrix:
[2 0 0]
[0 2 0]
[0 0 2]
```


Now:

```
sage: A = ZZ^3
sage: 2*A
Traceback (most recent call last):
...
TypeError: unsupported operand parent(s) for '*': 'Integer Ring' and '<class 'sage.modules.free_module.FreeModule_ambient_pid'>'
```


Issue created by migration from https://trac.sagemath.org/ticket/5131





---

archive/issue_comments_039159.json:
```json
{
    "body": "Now also works for matrices:\n\n```\nsage: A = ZZ^3\nsage: m = matrix(3, range(9))\nsage: A * m\nFree module of degree 3 and rank 2 over Integer Ring\nEchelon basis matrix:\n[1 1 1]\n[0 3 6]\nsage: m * A\nFree module of degree 3 and rank 2 over Integer Ring\nEchelon basis matrix:\n[ 3  0 -3]\n[ 0  1  2]\n```\n\n----\nNew commits:",
    "created_at": "2014-07-18T02:17:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5131",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5131#issuecomment-39159",
    "user": "https://github.com/tscrim"
}
```

Now also works for matrices:

```
sage: A = ZZ^3
sage: m = matrix(3, range(9))
sage: A * m
Free module of degree 3 and rank 2 over Integer Ring
Echelon basis matrix:
[1 1 1]
[0 3 6]
sage: m * A
Free module of degree 3 and rank 2 over Integer Ring
Echelon basis matrix:
[ 3  0 -3]
[ 0  1  2]
```

----
New commits:



---

archive/issue_comments_039160.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2014-07-18T02:17:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5131",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5131#issuecomment-39160",
    "user": "https://github.com/tscrim"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_039161.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-07-20T17:00:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5131",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5131#issuecomment-39161",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_039162.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-07-20T17:49:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5131",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5131#issuecomment-39162",
    "user": "https://trac.sagemath.org/admin/accounts/users/jkeitel"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_039163.json:
```json
{
    "body": "Hi Travis, the patch looks good to me.",
    "created_at": "2014-07-20T17:49:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5131",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5131#issuecomment-39163",
    "user": "https://trac.sagemath.org/admin/accounts/users/jkeitel"
}
```

Hi Travis, the patch looks good to me.



---

archive/issue_events_005378.json:
```json
{
    "actor": "https://github.com/vbraun",
    "created_at": "2014-07-21T17:38:08Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5131",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5131#event-5378"
}
```



---

archive/issue_comments_039164.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2014-07-21T17:38:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5131",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5131#issuecomment-39164",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed
