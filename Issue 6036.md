# Issue 6036: a bug in polynomial()

archive/issues_006036.json:
```json
{
    "body": "Assignee: Somebody\n\nThis works:\n\n\n```\nsage: R.<x,y>=PolynomialRing(QQ,2)\nsage: a=x^2+x*y+y\nsage: a.polynomial(x)\nx^2 + y*x + y\n```\n\n\nBut this does not work:\n\n\n```\nsage: R.<x,y>=PolynomialRing(GF(5),2)\nsage: a=x^2+x*y+y\nsage: a.polynomial(x)\nTraceback (most recent call last):\n...\nTypeError: 'tuple' object cannot be interpreted as an index \n```\n\n\nThe bug is essentially in:\n\n```\nsage: B=QQ[x]\nsage: print B({0:1,1:2})\n2*x + 1\nsage: print B({(0,):1,(1,):2})\n2*x + 1\nsage: B=GF(5)[x]\nsage: print B({0:1,1:2})\n2*x + 1\nsage: print B({(0,):1,(1,):2})\nTraceback (most recent call last):\n...\nTypeError: 'tuple' object cannot be interpreted as an index\n}}\n\nI think the second form is not acceptable. Then the function\nremove_from_tuple() in sage.rings.polynomial.multi_polynomial.pyx\nshould be revised as it output (1,) from (1,2) for example\n\nIssue created by migration from https://trac.sagemath.org/ticket/6036\n\n",
    "created_at": "2009-05-14T02:16:55Z",
    "labels": [
        "component: algebra",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0",
    "title": "a bug in polynomial()",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6036",
    "user": "https://github.com/kwankyu"
}
```
Assignee: Somebody

This works:


```
sage: R.<x,y>=PolynomialRing(QQ,2)
sage: a=x^2+x*y+y
sage: a.polynomial(x)
x^2 + y*x + y
```


But this does not work:


```
sage: R.<x,y>=PolynomialRing(GF(5),2)
sage: a=x^2+x*y+y
sage: a.polynomial(x)
Traceback (most recent call last):
...
TypeError: 'tuple' object cannot be interpreted as an index 
```


The bug is essentially in:

```
sage: B=QQ[x]
sage: print B({0:1,1:2})
2*x + 1
sage: print B({(0,):1,(1,):2})
2*x + 1
sage: B=GF(5)[x]
sage: print B({0:1,1:2})
2*x + 1
sage: print B({(0,):1,(1,):2})
Traceback (most recent call last):
...
TypeError: 'tuple' object cannot be interpreted as an index
}}

I think the second form is not acceptable. Then the function
remove_from_tuple() in sage.rings.polynomial.multi_polynomial.pyx
should be revised as it output (1,) from (1,2) for example

Issue created by migration from https://trac.sagemath.org/ticket/6036





---

archive/issue_comments_047979.json:
```json
{
    "body": "Changing component from algebra to basic arithmetic.",
    "created_at": "2009-05-14T05:27:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6036",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6036#issuecomment-47979",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing component from algebra to basic arithmetic.



---

archive/issue_comments_047980.json:
```json
{
    "body": "Attachment [12159.patch](tarball://root/attachments/some-uuid/ticket6036/12159.patch) by @kwankyu created at 2009-05-14 06:38:55",
    "created_at": "2009-05-14T06:38:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6036",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6036#issuecomment-47980",
    "user": "https://github.com/kwankyu"
}
```

Attachment [12159.patch](tarball://root/attachments/some-uuid/ticket6036/12159.patch) by @kwankyu created at 2009-05-14 06:38:55



---

archive/issue_comments_047981.json:
```json
{
    "body": "Attachment [12160.patch](tarball://root/attachments/some-uuid/ticket6036/12160.patch) by @kwankyu created at 2009-05-14 06:39:07",
    "created_at": "2009-05-14T06:39:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6036",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6036#issuecomment-47981",
    "user": "https://github.com/kwankyu"
}
```

Attachment [12160.patch](tarball://root/attachments/some-uuid/ticket6036/12160.patch) by @kwankyu created at 2009-05-14 06:39:07



---

archive/issue_comments_047982.json:
```json
{
    "body": "Attachment [trac_6036.patch](tarball://root/attachments/some-uuid/ticket6036/trac_6036.patch) by @mwhansen created at 2009-05-19 05:13:19\n\nI attached a folded patch -- it should be applied instead of the other two.\n\nLooks good to me.",
    "created_at": "2009-05-19T05:13:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6036",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6036#issuecomment-47982",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_6036.patch](tarball://root/attachments/some-uuid/ticket6036/trac_6036.patch) by @mwhansen created at 2009-05-19 05:13:19

I attached a folded patch -- it should be applied instead of the other two.

Looks good to me.



---

archive/issue_comments_047983.json:
```json
{
    "body": "Merged trac_6036.patch in Sage 4.0.rc0.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-19T18:51:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6036",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6036#issuecomment-47983",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged trac_6036.patch in Sage 4.0.rc0.

Cheers,

Michael



---

archive/issue_events_006291.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2009-05-19T18:51:35Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6036",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6036#event-6291"
}
```



---

archive/issue_comments_047984.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-05-19T18:51:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6036",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6036#issuecomment-47984",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
