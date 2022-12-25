# Issue 1030: [with patch] MPolynomial_libsingular mutates with call to factor

archive/issues_001030.json:
```json
{
    "body": "Assignee: somebody\n\nHere's an exhibition of the bug:\n\n\n```\nsage: R.<x,w,v,u> = QQ['x','w','v','u']\nsage: f=(1-x)*(1-w)*(2-2*v)\nsage: f\n-2*x*w*v + 2*x*w + 2*x*v + 2*w*v - 2*x - 2*w - 2*v + 2\nsage: f.factor()\n(-2) * (x - 1) * (w - 1) * (v - 1)\nsage: f\nx*w*v - x*w - x*v - w*v + x + w + v - 1\n```\n\n\nThe fix is attached.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1030\n\n",
    "created_at": "2007-10-29T16:21:37Z",
    "labels": [
        "component: basic arithmetic",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.11",
    "title": "[with patch] MPolynomial_libsingular mutates with call to factor",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1030",
    "user": "https://trac.sagemath.org/admin/accounts/users/jbmohler"
}
```
Assignee: somebody

Here's an exhibition of the bug:


```
sage: R.<x,w,v,u> = QQ['x','w','v','u']
sage: f=(1-x)*(1-w)*(2-2*v)
sage: f
-2*x*w*v + 2*x*w + 2*x*v + 2*w*v - 2*x - 2*w - 2*v + 2
sage: f.factor()
(-2) * (x - 1) * (w - 1) * (v - 1)
sage: f
x*w*v - x*w - x*v - w*v + x + w + v - 1
```


The fix is attached.

Issue created by migration from https://trac.sagemath.org/ticket/1030





---

archive/issue_comments_006274.json:
```json
{
    "body": "the fix",
    "created_at": "2007-10-29T16:21:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1030",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1030#issuecomment-6274",
    "user": "https://trac.sagemath.org/admin/accounts/users/jbmohler"
}
```

the fix



---

archive/issue_comments_006275.json:
```json
{
    "body": "Attachment [singclap_factorise_immut.hg](tarball://root/attachments/some-uuid/ticket1030/singclap_factorise_immut.hg) by mabshoff created at 2007-10-29 20:36:04",
    "created_at": "2007-10-29T20:36:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1030",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1030#issuecomment-6275",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [singclap_factorise_immut.hg](tarball://root/attachments/some-uuid/ticket1030/singclap_factorise_immut.hg) by mabshoff created at 2007-10-29 20:36:04



---

archive/issue_comments_006276.json:
```json
{
    "body": "Changing priority from critical to blocker.",
    "created_at": "2007-10-29T20:36:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1030",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1030#issuecomment-6276",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing priority from critical to blocker.



---

archive/issue_comments_006277.json:
```json
{
    "body": "I can confirm that `singclap_factorize` mutates the parameter. Also, the patch looks good and should be accepted for 2.8.11",
    "created_at": "2007-10-31T11:54:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1030",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1030#issuecomment-6277",
    "user": "https://github.com/malb"
}
```

I can confirm that `singclap_factorize` mutates the parameter. Also, the patch looks good and should be accepted for 2.8.11



---

archive/issue_events_002810.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-11-01T10:10:51Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1030",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1030#event-2810"
}
```



---

archive/issue_comments_006278.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-11-01T10:10:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1030",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1030#issuecomment-6278",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_006279.json:
```json
{
    "body": "applied to 2.8.11.alpha0",
    "created_at": "2007-11-01T10:10:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1030",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1030#issuecomment-6279",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

applied to 2.8.11.alpha0
