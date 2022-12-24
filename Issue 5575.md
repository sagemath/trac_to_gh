# Issue 5575: bug in span

archive/issues_005575.json:
```json
{
    "body": "Assignee: @williamstein\n\n\n```\nsage: V = QQ^4\nsage: a = [V.random_element() for _ in range(4)]\nsage: span(a)\n---------------------------------------------------------------------------\nNameError                                 Traceback (most recent call last)\n\n/Users/wstein/.sage/temp/teragon.local/19499/_Users_wstein__sage_init_sage_0.py in <module>()\n\n/Users/wstein/build/sage-3.4/local/lib/python2.5/site-packages/sage/modules/free_module.pyc in span(gens, base_ring, check, already_echelonized)\n    456         base_ring, gens = gens, base_ring\n    457         \n--> 458     R = self.base_ring() if base_ring is None else base_ring\n    459 \n    460     if not isinstance(R, principal_ideal_domain.PrincipalIdealDomain):\n\nNameError: global name 'self' is not defined\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5575\n\n",
    "created_at": "2009-03-20T11:03:00Z",
    "labels": [
        "linear algebra",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.1",
    "title": "bug in span",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5575",
    "user": "@williamstein"
}
```
Assignee: @williamstein


```
sage: V = QQ^4
sage: a = [V.random_element() for _ in range(4)]
sage: span(a)
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)

/Users/wstein/.sage/temp/teragon.local/19499/_Users_wstein__sage_init_sage_0.py in <module>()

/Users/wstein/build/sage-3.4/local/lib/python2.5/site-packages/sage/modules/free_module.pyc in span(gens, base_ring, check, already_echelonized)
    456         base_ring, gens = gens, base_ring
    457         
--> 458     R = self.base_ring() if base_ring is None else base_ring
    459 
    460     if not isinstance(R, principal_ideal_domain.PrincipalIdealDomain):

NameError: global name 'self' is not defined
```


Issue created by migration from https://trac.sagemath.org/ticket/5575





---

archive/issue_comments_043473.json:
```json
{
    "body": "Attachment [trac_5575.patch](tarball://root/attachments/some-uuid/ticket5575/trac_5575.patch) by @williamstein created at 2009-03-20 11:05:33",
    "created_at": "2009-03-20T11:05:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5575",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5575#issuecomment-43473",
    "user": "@williamstein"
}
```

Attachment [trac_5575.patch](tarball://root/attachments/some-uuid/ticket5575/trac_5575.patch) by @williamstein created at 2009-03-20 11:05:33



---

archive/issue_comments_043474.json:
```json
{
    "body": "Review:  patch looks fine and applies ok to 3.4.   There is an appropriate doctest and all tests in sage/modules pass.   Good!",
    "created_at": "2009-03-21T19:12:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5575",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5575#issuecomment-43474",
    "user": "@JohnCremona"
}
```

Review:  patch looks fine and applies ok to 3.4.   There is an appropriate doctest and all tests in sage/modules pass.   Good!



---

archive/issue_comments_043475.json:
```json
{
    "body": "Merged in Sage 3.4.1.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-23T19:36:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5575",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5575#issuecomment-43475",
    "user": "mabshoff"
}
```

Merged in Sage 3.4.1.alpha0.

Cheers,

Michael



---

archive/issue_comments_043476.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-03-23T19:36:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5575",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5575#issuecomment-43476",
    "user": "mabshoff"
}
```

Resolution: fixed
