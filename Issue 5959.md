# Issue 5959: Better doctest for __cmp__ in primes.py

archive/issues_005959.json:
```json
{
    "body": "Assignee: mabshoff\n\nFrom sage-devel, regarding whether \n\n```\nPrimes()>x^2+x\n```\n\nor not\n\n\n\n> You should change the doctest to\n> \n> sage: P != x^2 + x\n> True\n> \n> The comparison is completely arbitrary and will be machine specific.\n> However equality or not is not arbitrary.\n\n> \n> > sage: cmp(SR(3), x) in [-1,1]\n> > True\n> \n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5959\n\n",
    "created_at": "2009-05-01T15:14:17Z",
    "labels": [
        "doctest coverage",
        "minor",
        "bug"
    ],
    "title": "Better doctest for __cmp__ in primes.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5959",
    "user": "kcrisman"
}
```
Assignee: mabshoff

From sage-devel, regarding whether 

```
Primes()>x^2+x
```

or not



> You should change the doctest to
> 
> sage: P != x^2 + x
> True
> 
> The comparison is completely arbitrary and will be machine specific.
> However equality or not is not arbitrary.

> 
> > sage: cmp(SR(3), x) in [-1,1]
> > True
> 



Issue created by migration from https://trac.sagemath.org/ticket/5959





---

archive/issue_comments_047198.json:
```json
{
    "body": "Based on 3.4.2.rc0",
    "created_at": "2009-05-01T15:15:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5959",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5959#issuecomment-47198",
    "user": "kcrisman"
}
```

Based on 3.4.2.rc0



---

archive/issue_comments_047199.json:
```json
{
    "body": "Attachment [trac_5959.patch](tarball://root/attachments/some-uuid/ticket5959/trac_5959.patch) by mabshoff created at 2009-05-03 01:47:22\n\nThis is superseded by #5966.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-03T01:47:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5959",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5959#issuecomment-47199",
    "user": "mabshoff"
}
```

Attachment [trac_5959.patch](tarball://root/attachments/some-uuid/ticket5959/trac_5959.patch) by mabshoff created at 2009-05-03 01:47:22

This is superseded by #5966.

Cheers,

Michael



---

archive/issue_comments_047200.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2009-05-03T01:47:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5959",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5959#issuecomment-47200",
    "user": "mabshoff"
}
```

Resolution: duplicate
