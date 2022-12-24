# Issue 2206: Factorizations

archive/issues_002206.json:
```json
{
    "body": "Assignee: somebody\n\nA few miscellaneous improvements/fixes to Factorizations from mhansen's patches at 2028.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2206\n\n",
    "created_at": "2008-02-18T21:24:31Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.3",
    "title": "Factorizations",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2206",
    "user": "@jasongrout"
}
```
Assignee: somebody

A few miscellaneous improvements/fixes to Factorizations from mhansen's patches at 2028.

Issue created by migration from https://trac.sagemath.org/ticket/2206





---

archive/issue_comments_014559.json:
```json
{
    "body": "Attachment [factorization.patch](tarball://root/attachments/some-uuid/ticket2206/factorization.patch) by @jasongrout created at 2008-02-18 21:27:19",
    "created_at": "2008-02-18T21:27:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2206",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2206#issuecomment-14559",
    "user": "@jasongrout"
}
```

Attachment [factorization.patch](tarball://root/attachments/some-uuid/ticket2206/factorization.patch) by @jasongrout created at 2008-02-18 21:27:19



---

archive/issue_comments_014560.json:
```json
{
    "body": "Looks good to me.  I assume a factorization with powers > maximum integer is not supported?  Because we're converting via int(...).\n\nApply.",
    "created_at": "2008-02-19T00:30:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2206",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2206#issuecomment-14560",
    "user": "@ncalexan"
}
```

Looks good to me.  I assume a factorization with powers > maximum integer is not supported?  Because we're converting via int(...).

Apply.



---

archive/issue_comments_014561.json:
```json
{
    "body": "> I assume a factorization with powers > maximum integer is \n> not supported? Because we're converting via int(...).\n\nWhat is \"maximum integer\"?   In pure python code int(...)\nis arbitrary precision. \n\nWilliam",
    "created_at": "2008-02-19T00:35:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2206",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2206#issuecomment-14561",
    "user": "@williamstein"
}
```

> I assume a factorization with powers > maximum integer is 
> not supported? Because we're converting via int(...).

What is "maximum integer"?   In pure python code int(...)
is arbitrary precision. 

William



---

archive/issue_comments_014562.json:
```json
{
    "body": "\n```\nsage$ patch -p1 --dry-run < trac_2206_factorization.patch\npatching file sage/structure/factorization.py\nHunk #3 FAILED at 261.\nHunk #4 FAILED at 280.\nHunk #5 FAILED at 291.\n3 out of 5 hunks FAILED -- saving rejects to file sage/structure/factorization.py.rej\n```\n\n\nPlease rebase and resubmit the patch. It would also be good to change the subject line to something more descriptive.\n\nCheers,\n\nMichael",
    "created_at": "2008-02-19T15:05:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2206",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2206#issuecomment-14562",
    "user": "mabshoff"
}
```


```
sage$ patch -p1 --dry-run < trac_2206_factorization.patch
patching file sage/structure/factorization.py
Hunk #3 FAILED at 261.
Hunk #4 FAILED at 280.
Hunk #5 FAILED at 291.
3 out of 5 hunks FAILED -- saving rejects to file sage/structure/factorization.py.rej
```


Please rebase and resubmit the patch. It would also be good to change the subject line to something more descriptive.

Cheers,

Michael



---

archive/issue_comments_014563.json:
```json
{
    "body": "Attachment [factorization.2.patch](tarball://root/attachments/some-uuid/ticket2206/factorization.2.patch) by @aghitza created at 2008-02-25 04:10:56\n\nRebased against 2.10.2.",
    "created_at": "2008-02-25T04:10:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2206",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2206#issuecomment-14563",
    "user": "@aghitza"
}
```

Attachment [factorization.2.patch](tarball://root/attachments/some-uuid/ticket2206/factorization.2.patch) by @aghitza created at 2008-02-25 04:10:56

Rebased against 2.10.2.



---

archive/issue_comments_014564.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-25T04:17:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2206",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2206#issuecomment-14564",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_014565.json:
```json
{
    "body": "Merged factorization.2.patch in Sage 2.10.3.alpha0",
    "created_at": "2008-02-25T04:17:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2206",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2206#issuecomment-14565",
    "user": "mabshoff"
}
```

Merged factorization.2.patch in Sage 2.10.3.alpha0
