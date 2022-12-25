# Issue 499: n() is undefined for rational numbers

archive/issues_000499.json:
```json
{
    "body": "Assignee: somebody\n\nReported by Ted Kosan in sage-support - see http://groups.google.com/group/sage-support/t/2a46ced7d28116eb\n\n\n```\nx = 1/2\nx.n()\n\nException (click to the left for traceback):\n...\nAttributeError: 'sage.rings.rational.Rational' object has no attribute 'n' \n```\n\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/499\n\n",
    "created_at": "2007-08-28T17:45:59Z",
    "labels": [
        "component: basic arithmetic",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.4",
    "title": "n() is undefined for rational numbers",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/499",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: somebody

Reported by Ted Kosan in sage-support - see http://groups.google.com/group/sage-support/t/2a46ced7d28116eb


```
x = 1/2
x.n()

Exception (click to the left for traceback):
...
AttributeError: 'sage.rings.rational.Rational' object has no attribute 'n' 
```


Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/499





---

archive/issue_comments_002486.json:
```json
{
    "body": "This is done, but it's capital N:\n\n```\nsage: x = 1/2\nsage: x.N()\n0.500000000000000\n```\n",
    "created_at": "2007-08-31T21:06:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/499",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/499#issuecomment-2486",
    "user": "https://github.com/williamstein"
}
```

This is done, but it's capital N:

```
sage: x = 1/2
sage: x.N()
0.500000000000000
```




---

archive/issue_comments_002487.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-08-31T21:06:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/499",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/499#issuecomment-2487",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed
