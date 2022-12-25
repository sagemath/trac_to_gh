# Issue 4136: [with patch, needs review] enable tail reduction when reducing multivariate polynomials

archive/issues_004136.json:
```json
{
    "body": "Assignee: @malb\n\nThis was reported on **[sage-support]**:\n\n```\nhi there,\n\nthis is going to be even worse than my recent bug report in terms of\nreproducing the error. I guess i'll start with describing what\nhappens, and then if someone tells me that it's a bug and not a\nfeature, then i'll try to get a minimal example.\n\nSo I've got a polynomial ring with a few dozens variables, over a\ncyclotomic field, and i've got an ideal J with hundreds of generators.\nJ contains at least y9 + y12. Then i got something like:\n\nsage: J.reduce(y9 - y12)\n2*y9   #which is fine\n\nsage: J.reduce(y13*y15)\ny13*y15 #why not\n\nsage: J.reduce(y13*y15 + y9 - y12)\ny13*y15 + y9 - y12\n\nNow what's up with that ? shouldn't it be y13*y15 + 2*y9 ? that's what\ni expect from the term 'reduction' anyway. Is this normal or is it a\nbug ? if it's a bug, could it influence the equivalence x in J iff\nJ.reduce(x) == 0 ?\n\nSo if this is a bug i'll give you more details.\n\nthanks!\nPierre\n```\n\nhttp://groups.google.com/group/sage-support/browse_thread/thread/138e473f31c2f2b5\n\n```\n\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4136\n\n",
    "created_at": "2008-09-16T17:53:33Z",
    "labels": [
        "component: commutative algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2",
    "title": "[with patch, needs review] enable tail reduction when reducing multivariate polynomials",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4136",
    "user": "https://github.com/malb"
}
```
Assignee: @malb

This was reported on **[sage-support]**:

```
hi there,

this is going to be even worse than my recent bug report in terms of
reproducing the error. I guess i'll start with describing what
happens, and then if someone tells me that it's a bug and not a
feature, then i'll try to get a minimal example.

So I've got a polynomial ring with a few dozens variables, over a
cyclotomic field, and i've got an ideal J with hundreds of generators.
J contains at least y9 + y12. Then i got something like:

sage: J.reduce(y9 - y12)
2*y9   #which is fine

sage: J.reduce(y13*y15)
y13*y15 #why not

sage: J.reduce(y13*y15 + y9 - y12)
y13*y15 + y9 - y12

Now what's up with that ? shouldn't it be y13*y15 + 2*y9 ? that's what
i expect from the term 'reduction' anyway. Is this normal or is it a
bug ? if it's a bug, could it influence the equivalence x in J iff
J.reduce(x) == 0 ?

So if this is a bug i'll give you more details.

thanks!
Pierre
```

http://groups.google.com/group/sage-support/browse_thread/thread/138e473f31c2f2b5

```

```


Issue created by migration from https://trac.sagemath.org/ticket/4136





---

archive/issue_comments_029968.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-09-20T15:49:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4136",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4136#issuecomment-29968",
    "user": "https://github.com/malb"
}
```

Changing status from new to assigned.



---

archive/issue_comments_029969.json:
```json
{
    "body": "it's ok.",
    "created_at": "2008-10-17T06:24:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4136",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4136#issuecomment-29969",
    "user": "https://trac.sagemath.org/admin/accounts/users/PolyBoRi"
}
```

it's ok.



---

archive/issue_comments_029970.json:
```json
{
    "body": "Mhhh, what are the patch dependencies here?\n\n```\nmabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.2.alpha0/devel/sage$ patch -p1  < trac_4136_tail_reduce.patch \npatching file sage/rings/polynomial/multi_polynomial_element.py\nHunk #1 FAILED at 1485.\nHunk #2 FAILED at 1511.\n2 out of 2 hunks FAILED -- saving rejects to file sage/rings/polynomial/multi_polynomial_element.py.rej\n```\n\nCheers,\n\nMichael",
    "created_at": "2008-10-20T11:53:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4136",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4136#issuecomment-29970",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Mhhh, what are the patch dependencies here?

```
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.2.alpha0/devel/sage$ patch -p1  < trac_4136_tail_reduce.patch 
patching file sage/rings/polynomial/multi_polynomial_element.py
Hunk #1 FAILED at 1485.
Hunk #2 FAILED at 1511.
2 out of 2 hunks FAILED -- saving rejects to file sage/rings/polynomial/multi_polynomial_element.py.rej
```

Cheers,

Michael



---

archive/issue_comments_029971.json:
```json
{
    "body": "Attachment [tail_reduce.patch](tarball://root/attachments/some-uuid/ticket4136/tail_reduce.patch) by @malb created at 2008-10-20 13:20:34",
    "created_at": "2008-10-20T13:20:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4136",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4136#issuecomment-29971",
    "user": "https://github.com/malb"
}
```

Attachment [tail_reduce.patch](tarball://root/attachments/some-uuid/ticket4136/tail_reduce.patch) by @malb created at 2008-10-20 13:20:34



---

archive/issue_comments_029972.json:
```json
{
    "body": "I rebased the patch to 3.1.3",
    "created_at": "2008-10-20T13:21:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4136",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4136#issuecomment-29972",
    "user": "https://github.com/malb"
}
```

I rebased the patch to 3.1.3



---

archive/issue_comments_029973.json:
```json
{
    "body": "Merged in Sage 3.2.alpha0",
    "created_at": "2008-10-20T14:32:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4136",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4136#issuecomment-29973",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.2.alpha0



---

archive/issue_comments_029974.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-10-20T14:32:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4136",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4136#issuecomment-29974",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_009419.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-10-20T14:32:34Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4136",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4136#event-9419"
}
```
