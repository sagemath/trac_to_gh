# Issue 5683: Inverse operation for matrices over non integral domain

archive/issues_005683.json:
```json
{
    "body": "Assignee: somebody\n\nKeywords: inverse\n\nWe get this: \n\n\n```\nsage: R=IntegerModRing(8)\nsage: m=matrix(R,2,[2,1,3,3]);\nsage: m.inverse()\nTraceback (most recent call last):\n...\nTypeError: self must be an integral domain.\n```\n\n\nThe inverse operation for matrices over non integral domain, in particular for over integer mod rings, is a missing feature. Somebody should *definitely* implement this.  A\nfirst reasonable thing would be \"lift to ZZ, invert, reduce\".\n\nIssue created by migration from https://trac.sagemath.org/ticket/5683\n\n",
    "created_at": "2009-04-04T20:33:09Z",
    "labels": [
        "component: linear algebra",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.1",
    "title": "Inverse operation for matrices over non integral domain",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5683",
    "user": "https://github.com/kwankyu"
}
```
Assignee: somebody

Keywords: inverse

We get this: 


```
sage: R=IntegerModRing(8)
sage: m=matrix(R,2,[2,1,3,3]);
sage: m.inverse()
Traceback (most recent call last):
...
TypeError: self must be an integral domain.
```


The inverse operation for matrices over non integral domain, in particular for over integer mod rings, is a missing feature. Somebody should *definitely* implement this.  A
first reasonable thing would be "lift to ZZ, invert, reduce".

Issue created by migration from https://trac.sagemath.org/ticket/5683





---

archive/issue_comments_044356.json:
```json
{
    "body": "Attachment [trac_5683.patch](tarball://root/attachments/some-uuid/ticket5683/trac_5683.patch) by @williamstein created at 2009-04-05 06:00:41",
    "created_at": "2009-04-05T06:00:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5683",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5683#issuecomment-44356",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_5683.patch](tarball://root/attachments/some-uuid/ticket5683/trac_5683.patch) by @williamstein created at 2009-04-05 06:00:41



---

archive/issue_comments_044357.json:
```json
{
    "body": "Positive review: applies fine to 3.4.1.apha0 and tests in the file changed pass.\n\nI was disappointed that the similar thing does not work for residue rings of number field rings of integers, since I thought I had fixed it so that the reduction maps worked ok, but unfortunately that only works for residue fields, not residue rings.  (Even then, you have to say OK.residue_field(P) and not OK.quotient(P) for it to work properly).\n\nNever mind, this patch is still good!",
    "created_at": "2009-04-05T15:52:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5683",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5683#issuecomment-44357",
    "user": "https://github.com/JohnCremona"
}
```

Positive review: applies fine to 3.4.1.apha0 and tests in the file changed pass.

I was disappointed that the similar thing does not work for residue rings of number field rings of integers, since I thought I had fixed it so that the reduction maps worked ok, but unfortunately that only works for residue fields, not residue rings.  (Even then, you have to say OK.residue_field(P) and not OK.quotient(P) for it to work properly).

Never mind, this patch is still good!



---

archive/issue_comments_044358.json:
```json
{
    "body": "apply on top of the other patch",
    "created_at": "2009-04-05T16:46:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5683",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5683#issuecomment-44358",
    "user": "https://github.com/jhpalmieri"
}
```

apply on top of the other patch



---

archive/issue_comments_044359.json:
```json
{
    "body": "Attachment [5683-doc.patch](tarball://root/attachments/some-uuid/ticket5683/5683-doc.patch) by @jhpalmieri created at 2009-04-05 16:50:48\n\nYou have a slightly misformatted docstring which the second patch fixes.\n\n(This is another use of the patches at #5653: you can view the Sphinx version of an individual docstring to see if it's formatted correctly.  This even works for docstrings which don't appear in the reference manual, such as for functions like `__invert__` which start with an underscore.)",
    "created_at": "2009-04-05T16:50:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5683",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5683#issuecomment-44359",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [5683-doc.patch](tarball://root/attachments/some-uuid/ticket5683/5683-doc.patch) by @jhpalmieri created at 2009-04-05 16:50:48

You have a slightly misformatted docstring which the second patch fixes.

(This is another use of the patches at #5653: you can view the Sphinx version of an individual docstring to see if it's formatted correctly.  This even works for docstrings which don't appear in the reference manual, such as for functions like `__invert__` which start with an underscore.)



---

archive/issue_comments_044360.json:
```json
{
    "body": "Replying to [comment:3 jhpalmieri]:\n> You have a slightly misformatted docstring which the second patch fixes.\n> \n> (This is another use of the patches at #5653: you can view the Sphinx version of an individual docstring to see if it's formatted correctly.  This even works for docstrings which don't appear in the reference manual, such as for functions like `__invert__` which start with an underscore.)\n\nThat sounds very useful.  normally I never use the notebook interface, but with this I can see myself using it to test docstring formats if nothing else!",
    "created_at": "2009-04-05T17:08:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5683",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5683#issuecomment-44360",
    "user": "https://github.com/JohnCremona"
}
```

Replying to [comment:3 jhpalmieri]:
> You have a slightly misformatted docstring which the second patch fixes.
> 
> (This is another use of the patches at #5653: you can view the Sphinx version of an individual docstring to see if it's formatted correctly.  This even works for docstrings which don't appear in the reference manual, such as for functions like `__invert__` which start with an underscore.)

That sounds very useful.  normally I never use the notebook interface, but with this I can see myself using it to test docstring formats if nothing else!



---

archive/issue_comments_044361.json:
```json
{
    "body": "Merged both patches in Sage 3.4.1.rc1.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-06T00:46:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5683",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5683#issuecomment-44361",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged both patches in Sage 3.4.1.rc1.

Cheers,

Michael



---

archive/issue_comments_044362.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-06T00:46:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5683",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5683#issuecomment-44362",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_013365.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-04-06T00:46:39Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5683",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5683#event-13365"
}
```
