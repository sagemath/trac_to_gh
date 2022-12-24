# Issue 2501: [with patch, needs review] SBox class for Sage

archive/issues_002501.json:
```json
{
    "body": "Assignee: malb\n\nThe attached patch adds a class SBox to the module `sage.crypto.mq` which offers basic functionality to work with cryptographic substitution boxes like:\n* substitution (obviously)\n* difference distribution and linear approximation matrices\n* multivariate polynomial system generation\n* univariate polynomial interpolation\n\nIt might be a bit controversial if this functionality should go in (it is not math but applied math), so here are some points in favour:\n* Sage has a `sage.crypto` module with LFSRs and such.\n* `SBox` supports (algebraic) cryptanalysis by simplifying experiments with ciphers and algebraic aspects of cryptography is an application of Sage (Sage was advertised for this application in the past)\n* Some people have expressed (some) interest in such a class.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2501\n\n",
    "created_at": "2008-03-12T18:05:16Z",
    "labels": [
        "commutative algebra",
        "major",
        "enhancement"
    ],
    "title": "[with patch, needs review] SBox class for Sage",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2501",
    "user": "malb"
}
```
Assignee: malb

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

archive/issue_comments_016950.json:
```json
{
    "body": "Attachment [sbox.patch](tarball://root/attachments/some-uuid/ticket2501/sbox.patch) by malb created at 2008-03-12 18:05:29",
    "created_at": "2008-03-12T18:05:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2501",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2501#issuecomment-16950",
    "user": "malb"
}
```

Attachment [sbox.patch](tarball://root/attachments/some-uuid/ticket2501/sbox.patch) by malb created at 2008-03-12 18:05:29



---

archive/issue_comments_016951.json:
```json
{
    "body": "> It might be a bit controversial if this functionality  should go in (it is not math but applied math)\n\nIt's not controversial at all, in my opinion -- this should *definitely* go in.\n\n\"Applied math\" belongs squarely within the mission of Sage, and S-Box's most certainly do.",
    "created_at": "2008-03-12T18:10:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2501",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2501#issuecomment-16951",
    "user": "was"
}
```

> It might be a bit controversial if this functionality  should go in (it is not math but applied math)

It's not controversial at all, in my opinion -- this should *definitely* go in.

"Applied math" belongs squarely within the mission of Sage, and S-Box's most certainly do.



---

archive/issue_comments_016952.json:
```json
{
    "body": "Applies to 2.10.4.alpha0 and passes tests after #2444 is applied.",
    "created_at": "2008-03-15T21:35:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2501",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2501#issuecomment-16952",
    "user": "mhansen"
}
```

Applies to 2.10.4.alpha0 and passes tests after #2444 is applied.



---

archive/issue_comments_016953.json:
```json
{
    "body": "Merged in Sage 2.10.4.rc0",
    "created_at": "2008-03-15T22:58:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2501",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2501#issuecomment-16953",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.4.rc0



---

archive/issue_comments_016954.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-15T22:58:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2501",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2501#issuecomment-16954",
    "user": "mabshoff"
}
```

Resolution: fixed
