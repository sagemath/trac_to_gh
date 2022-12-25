# Issue 2501: [with patch, needs review] SBox class for Sage

archive/issues_002501.json:
```json
{
    "body": "Assignee: @malb\n\nThe attached patch adds a class SBox to the module `sage.crypto.mq` which offers basic functionality to work with cryptographic substitution boxes like:\n* substitution (obviously)\n* difference distribution and linear approximation matrices\n* multivariate polynomial system generation\n* univariate polynomial interpolation\n\nIt might be a bit controversial if this functionality should go in (it is not math but applied math), so here are some points in favour:\n* Sage has a `sage.crypto` module with LFSRs and such.\n* `SBox` supports (algebraic) cryptanalysis by simplifying experiments with ciphers and algebraic aspects of cryptography is an application of Sage (Sage was advertised for this application in the past)\n* Some people have expressed (some) interest in such a class.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2501\n\n",
    "created_at": "2008-03-12T18:05:16Z",
    "labels": [
        "component: commutative algebra"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.4",
    "title": "[with patch, needs review] SBox class for Sage",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2501",
    "user": "https://github.com/malb"
}
```
Assignee: @malb

The attached patch adds a class SBox to the module `sage.crypto.mq` which offers basic functionality to work with cryptographic substitution boxes like:
* substitution (obviously)
* difference distribution and linear approximation matrices
* multivariate polynomial system generation
* univariate polynomial interpolation

It might be a bit controversial if this functionality should go in (it is not math but applied math), so here are some points in favour:
* Sage has a `sage.crypto` module with LFSRs and such.
* `SBox` supports (algebraic) cryptanalysis by simplifying experiments with ciphers and algebraic aspects of cryptography is an application of Sage (Sage was advertised for this application in the past)
* Some people have expressed (some) interest in such a class.

Issue created by migration from https://trac.sagemath.org/ticket/2501





---

archive/issue_comments_016914.json:
```json
{
    "body": "Attachment [sbox.patch](tarball://root/attachments/some-uuid/ticket2501/sbox.patch) by @malb created at 2008-03-12 18:05:29",
    "created_at": "2008-03-12T18:05:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2501",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2501#issuecomment-16914",
    "user": "https://github.com/malb"
}
```

Attachment [sbox.patch](tarball://root/attachments/some-uuid/ticket2501/sbox.patch) by @malb created at 2008-03-12 18:05:29



---

archive/issue_comments_016915.json:
```json
{
    "body": "> It might be a bit controversial if this functionality  should go in (it is not math but applied math)\n\nIt's not controversial at all, in my opinion -- this should *definitely* go in.\n\n\"Applied math\" belongs squarely within the mission of Sage, and S-Box's most certainly do.",
    "created_at": "2008-03-12T18:10:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2501",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2501#issuecomment-16915",
    "user": "https://github.com/williamstein"
}
```

> It might be a bit controversial if this functionality  should go in (it is not math but applied math)

It's not controversial at all, in my opinion -- this should *definitely* go in.

"Applied math" belongs squarely within the mission of Sage, and S-Box's most certainly do.



---

archive/issue_comments_016916.json:
```json
{
    "body": "Applies to 2.10.4.alpha0 and passes tests after #2444 is applied.",
    "created_at": "2008-03-15T21:35:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2501",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2501#issuecomment-16916",
    "user": "https://github.com/mwhansen"
}
```

Applies to 2.10.4.alpha0 and passes tests after #2444 is applied.



---

archive/issue_comments_016917.json:
```json
{
    "body": "Merged in Sage 2.10.4.rc0",
    "created_at": "2008-03-15T22:58:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2501",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2501#issuecomment-16917",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.4.rc0



---

archive/issue_events_005883.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-03-15T22:58:48Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2501",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2501#event-5883"
}
```



---

archive/issue_comments_016918.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-15T22:58:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2501",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2501#issuecomment-16918",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
