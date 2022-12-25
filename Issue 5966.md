# Issue 5966: sage/sets/primes.py: change doctest so that we check for Primes being != to x^2+x

archive/issues_005966.json:
```json
{
    "body": "Assignee: mabshoff\n\nThis was reported by Kiran in https://groups.google.com/group/sage-devel/browse_thread/thread/776d8e0a25735dca\n\n```\nsage -t  \"devel/sage/sage/sets/primes.py\"\n**********************************************************************\nFile \"/opt/sage/sage-3.4.2.rc0/devel/sage/sage/sets/primes.py\", line\n80:\n    sage: P>x^2+x\nExpected:\n    True\nGot:\n    False\n********************************************************************** \n```\n\nDon't test for `>`, but use `!=` since anything else is pointless. We should also compare to an MV polynomial ring ro avoid stating Maxima needlessly. \n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/5966\n\n",
    "created_at": "2009-05-03T00:44:51Z",
    "labels": [
        "component: doctest coverage",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.2",
    "title": "sage/sets/primes.py: change doctest so that we check for Primes being != to x^2+x",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5966",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

This was reported by Kiran in https://groups.google.com/group/sage-devel/browse_thread/thread/776d8e0a25735dca

```
sage -t  "devel/sage/sage/sets/primes.py"
**********************************************************************
File "/opt/sage/sage-3.4.2.rc0/devel/sage/sage/sets/primes.py", line
80:
    sage: P>x^2+x
Expected:
    True
Got:
    False
********************************************************************** 
```

Don't test for `>`, but use `!=` since anything else is pointless. We should also compare to an MV polynomial ring ro avoid stating Maxima needlessly. 

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/5966





---

archive/issue_comments_047184.json:
```json
{
    "body": "Attachment [trac_5966.patch](tarball://root/attachments/some-uuid/ticket5966/trac_5966.patch) by mabshoff created at 2009-05-04 06:40:24",
    "created_at": "2009-05-04T06:40:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5966",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5966#issuecomment-47184",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [trac_5966.patch](tarball://root/attachments/some-uuid/ticket5966/trac_5966.patch) by mabshoff created at 2009-05-04 06:40:24



---

archive/issue_comments_047185.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-05-04T06:41:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5966",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5966#issuecomment-47185",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_047186.json:
```json
{
    "body": "Merged in Sage 3.4.2.final.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-04T09:31:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5966",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5966#issuecomment-47186",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.4.2.final.

Cheers,

Michael



---

archive/issue_comments_047187.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-05-04T09:31:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5966",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5966#issuecomment-47187",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
